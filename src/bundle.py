"""Make single-file copies of the deck and the labs (all CSS and JS inlined)
for sharing as standalone pages. Output goes to dist/ (not committed).
Usage: python3 src/bundle.py [base_url]
  base_url (optional): where the labs are hosted, e.g. https://<user>.github.io/<repo>/
  so the embedded labs and lab links in the standalone deck point there.
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

deck = inline(root / 'slides' / 'epidemiological-thinking.html')
deck = deck.replace('<style>\n  /* per-deck', '<style>\n  html, body { background: #ffffff; }\n  /* per-deck', 1)
deck = deck.replace('../widgets/', (base_url + 'widgets/') if base_url else '')
(dist / 'epidemiological-thinking.html').write_text(deck)
for w in ('two-by-two', 'test-lab', 'confounding-lab'):
    (dist / f'{w}.html').write_text(inline(root / 'widgets' / f'{w}.html').replace('../index.html', base_url or '#'))
for f in sorted(dist.iterdir()): print(f.name, f.stat().st_size // 1024, 'KB')
