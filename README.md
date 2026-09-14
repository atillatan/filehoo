# filehoo.com

Free software, direct downloads - running since 2007. Jekyll site served by
GitHub Pages from the `gh-pages` branch (CNAME: www.filehoo.com).

## Architecture

- **Jekyll** (github-pages gem). Collections: `_downloads` (app pages),
  `_categories`, `_letters`, `_tags` (listing pages), archive in
  `download_archive/` (published: false).
- **Design**: single custom stylesheet `assets/css/filehoo.css` (no frameworks),
  vanilla JS `assets/js/filehoo.js` (theme toggle, instant search, favorites).
  Light/dark theme, system fonts, PWA manifest.
- **Search**: `search.json` is generated at build; client-side instant search,
  "/" shortcut, `/search/?q=` deep links.
- **SEO**: jekyll-seo-tag + JSON-LD (SoftwareApplication, BreadcrumbList,
  WebSite/SearchAction), sitemap.xml with lastmod, Atom feed of updates.
- **Ads**: AdSense responsive units via `_includes/ad-unit.html`.
  GA4: set `ga4_id` in `_config.yml`.

## Local development

```sh
# needs ruby@3.3 (brew install ruby@3.3)
bundle install
bundle exec jekyll serve
```

## Maintenance

- `scripts/check_links.py <dir> <out.tsv>` - link-checks every `downloadurl`.
  Archive dead pages by moving them to `download_archive/` with
  `published: false`.
- Dates in front matter are quoted ISO strings: `"YYYY-MM-DD"`.
- Add a new app: copy any file in `_downloads/`, keep the front-matter schema.
