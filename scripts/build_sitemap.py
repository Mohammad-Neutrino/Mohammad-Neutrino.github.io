from pathlib import Path
from html import escape

base = "https://mohammad-neutrino.github.io"
root = Path("_site")
urls = []

for p in root.rglob("*.html"):
    rel = p.relative_to(root).as_posix()
    if rel == "404.html" or rel.startswith("site_libs/"):
        continue
    if rel == "index.html":
        url = base + "/"
    elif rel.endswith("/index.html"):
        url = base + "/" + rel[:-10]
    else:
        url = base + "/" + rel
    urls.append(url)

urls = sorted(set(urls))
xml = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
xml += [f"  <url><loc>{escape(url)}</loc></url>" for url in urls]
xml.append("</urlset>")
(root / "sitemap.xml").write_text("\n".join(xml) + "\n")
print(f"Generated sitemap with {len(urls)} URLs")
