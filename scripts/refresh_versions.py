#!/usr/bin/env python3
"""Refresh version/size/downloadurl for GitHub-released apps in _downloads.

Only touches the whitelisted apps below. For each: query the latest release,
match the installer asset, verify it responds, then update front matter.
Run from repo root: python3 scripts/refresh_versions.py [--dry-run]
"""
import json, re, sys, urllib.request, datetime

APPS = {
    "notepad-plus-plus": ("notepad-plus-plus/notepad-plus-plus", r"npp\.[\d.]+\.Installer\.x64\.exe$", r"^v"),
    "obs-studio":        ("obsproject/obs-studio",               r"OBS-Studio-[\d.]+-Windows-x64-Installer\.exe$", r""),
    "audacity":          ("audacity/audacity",                   r"audacity-win-[\d.]+-x86_64\.msi$", r"^Audacity-"),
    "sharex":            ("ShareX/ShareX",                       r"ShareX-[\d.]+-setup-x64\.exe$", r"^v"),
    "rufus":             ("pbatard/rufus",                       r"rufus-[\d.]+\.exe$", r"^v"),
    "powertoys":         ("microsoft/PowerToys",                 r"PowerToysUserSetup-[\d.]+-x64\.exe$", r"^v"),
    "handbrake":         ("HandBrake/HandBrake",                 r"HandBrake-[\d.]+-x86_64-Win_GUI\.exe$", r""),
    "mpc-hc":            ("clsid2/mpc-hc",                       r"MPC-HC\.[\d.]+\.x64\.exe$", r""),
    "bitwarden":         ("bitwarden/clients",                   r"Bitwarden-Installer-[\d.]+\.exe$", r"^desktop-v"),
}

DRY = "--dry-run" in sys.argv
TODAY = datetime.date.today().isoformat()
UA = {"User-Agent": "filehoo-refresh", "Accept": "application/vnd.github+json"}

def gh(url):
    return json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30))

def latest(repo, slug):
    # bitwarden/clients mixes desktop/browser/cli releases; find the right one
    if slug == "bitwarden":
        for r in gh(f"https://api.github.com/repos/{repo}/releases"):
            if r["tag_name"].startswith("desktop-v"):
                return r
        raise RuntimeError("no desktop release")
    return gh(f"https://api.github.com/repos/{repo}/releases/latest")

def head_ok(url):
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "filehoo-refresh"})
    try:
        return urllib.request.urlopen(req, timeout=30).status in (200, 302)
    except Exception:
        return False

def set_field(text, key, value):
    return re.sub(rf"^{key}:.*$", f"{key}: {value}", text, count=1, flags=re.M)

changed = 0
for slug, (repo, asset_re, tag_strip) in APPS.items():
    path = f"_downloads/{slug}.md"
    try:
        rel = latest(repo, slug)
        version = re.sub(tag_strip, "", rel["tag_name"]) if tag_strip else rel["tag_name"]
        asset = next(a for a in rel["assets"] if re.search(asset_re, a["name"]))
    except Exception as e:
        print(f"{slug}: SKIP ({e})"); continue
    text = open(path).read()
    cur = re.search(r"^version: (.*)$", text, re.M).group(1).strip()
    if cur == version:
        print(f"{slug}: up to date ({version})"); continue
    url = asset["browser_download_url"]
    if not head_ok(url):
        print(f"{slug}: NEW {version} but URL not reachable, skipping"); continue
    size = f"{asset['size']/1048576:.1f} MB"
    text = set_field(text, "version", version)
    text = set_field(text, "size", size)
    text = set_field(text, "downloadurl", url)
    text = set_field(text, "modified_date", f'"{TODAY}"')
    print(f"{slug}: {cur} -> {version}")
    if not DRY:
        open(path, "w").write(text)
    changed += 1
print(f"{'DRY RUN, ' if DRY else ''}{changed} app(s) updated")
