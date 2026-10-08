"""Make single-file copies of every lecture deck and lab (all CSS and JS inlined)
for sharing as standalone pages. Output goes to dist/ (not committed).
Usage: python3 src/bundle.py [base_url]
  base_url (optional): where the site is hosted, e.g. https://<user>.github.io/<repo>/
  so embedded labs and lab links in the standalone decks point there.
"""
import re, sys, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
dist = root / 'dist'; dist.mkdir(exist_ok=True)
base_url = sys.argv[1].rstrip('/') + '/' if len(sys.argv) > 1 else None

def inline(path):
    base = path.parent
    html = path.read_text()
    html = re.sub(r'<link rel="stylesheet" href="([^"]+)">', lambda m: '<style>\n' + (base / m.group(1)).read_text() + '\n</style>', html)
    html = re.sub(r'<script src="([^"]+)"></script>', lambda m: '<script>\n' + (base / m.group(1)).read_text().replace('</script', '<\\/script') + '\n</script>', html)
    return html

for deck in sorted(d for d in (root / 'slides').glob('*.html') if not d.name.startswith('_') and 'Reveal.initialize' in d.read_text()):
    html = inline(deck).replace('<style>\n  /* per-deck', '<style>\n  html, body { background: #ffffff; }\n  /* per-deck', 1)
    html = html.replace('../widgets/', (base_url + 'widgets/') if base_url else '')
    (dist / deck.name).write_text(html)
for lab in sorted((root / 'widgets').glob('*.html')):
    (dist / lab.name).write_text(inline(lab).replace('../index.html', base_url or '#'))
for f in sorted(dist.iterdir()): print(f.name, f.stat().st_size // 1024, 'KB')
