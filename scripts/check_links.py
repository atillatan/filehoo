#!/usr/bin/env python3
"""Check downloadurl of every markdown file in given dirs.
Writes results to a TSV: path, url, status, final_url, content_type, size.
Status: HTTP code, or ERR:<reason>. Uses HEAD with GET fallback, 15s timeout.
"""
import concurrent.futures as cf
import os, re, sys, urllib.request, urllib.error, ssl, socket

DIRS = sys.argv[1:-1] or ["_downloads"]
OUT = sys.argv[-1] if len(sys.argv) > 1 else "linkcheck.tsv"
CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36"

def frontmatter_url(path):
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            text = f.read(8192)
        m = re.search(r"^downloadurl:\s*(\S+)\s*$", text, re.M)
        return m.group(1) if m else None
    except OSError:
        return None

def probe(url, method):
    req = urllib.request.Request(url, method=method, headers={"User-Agent": UA, "Accept": "*/*"})
    return urllib.request.urlopen(req, timeout=15, context=CTX)

def check(item):
    path, url = item
    if not url or not url.startswith("http"):
        return (path, url or "", "ERR:nourl", "", "", "")
    for method in ("HEAD", "GET"):
        try:
            r = probe(url, method)
            ct = r.headers.get("Content-Type", "")
            size = r.headers.get("Content-Length", "")
            final = r.geturl()
            if method == "GET":
                r.close()
            return (path, url, str(r.status), final, ct, size)
        except urllib.error.HTTPError as e:
            if method == "GET" or e.code not in (403, 405, 501):
                return (path, url, str(e.code), "", "", "")
        except (urllib.error.URLError, socket.timeout, ConnectionError, OSError, ValueError) as e:
            if method == "GET":
                reason = getattr(e, "reason", e)
                return (path, url, f"ERR:{type(e).__name__}:{str(reason)[:60]}", "", "", "")
    return (path, url, "ERR:unknown", "", "", "")

items = []
for d in DIRS:
    for fn in sorted(os.listdir(d)):
        if fn.endswith(".md"):
            p = os.path.join(d, fn)
            items.append((p, frontmatter_url(p)))

print(f"checking {len(items)} files from {DIRS}", flush=True)
done = 0
with open(OUT, "w", encoding="utf-8") as out:
    with cf.ThreadPoolExecutor(max_workers=24) as ex:
        for row in ex.map(check, items):
            out.write("\t".join(row) + "\n")
            out.flush()
            done += 1
            if done % 25 == 0:
                print(f"{done}/{len(items)}", flush=True)
print("DONE", flush=True)
