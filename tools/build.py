import re, json, pathlib, sys
SRC = pathlib.Path(sys.argv[1]); s = SRC.read_text()
vault = re.search(r'id="pc-vault">(.*?)</script>', s, re.S).group(1)
appb64 = re.search(r'id="pc-app">(.*?)</script>', s, re.S).group(1).strip()
boot = re.search(r'<script id="pc-boot">(.*?)</script>', s, re.S).group(1)
reset = re.search(r'var RESET = "(.*?)";', boot).group(1)
SC = "</script>"
html = ('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
 '<title>Next Horizon Circle</title><meta name="theme-color" content="#050913"><meta name="robots" content="noindex">'
 '<meta name="apple-mobile-web-app-capable" content="yes"><meta name="mobile-web-app-capable" content="yes"><meta name="apple-mobile-web-app-status-bar-style" content="black-translucent"><meta name="apple-mobile-web-app-title" content="Horizon Circle">'
 '<link rel="manifest" href="manifest.webmanifest"><link rel="icon" href="icon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="apple-touch-icon.png">'
 f'<style>{reset}</style></head><body>\n<script>window.__PC_STANDALONE=true{SC}\n'
 f'<script type="application/json" id="pc-vault">{vault}{SC}\n<script type="text/plain" id="pc-app">{appb64}{SC}\n<script id="pc-boot">{boot}{SC}\n</body></html>')
out = pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else ".")
(out / "index.html").write_text(html)
print("built", len(html), "entries", len(json.loads(vault.replace("\\u003c","<")).get("entries", {})))
