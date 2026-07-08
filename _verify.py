import re
path = r'D:\admin\Desktop\品牌\zhongbang-sites\index.html'
with open(path, 'r', encoding='utf-8') as fp:
    content = fp.read()
pat = re.compile(r'<section\b[^>]*id="slide-(\d+)"[^>]*>.*?</section>', re.DOTALL)
for m in pat.finditer(content):
    section = m.group(0)
    sid = m.group(1)
    eb = re.search(r'class="eyebrow[^"]*"[^>]*>([^<]+)<', section)
    eb_text = eb.group(1).strip() if eb else '?'
    mk = re.search(r'page-marker__num["\s]*[^>]*>\s*(\d+)\s*</span>', section)
    mk_text = mk.group(1) if mk else '?'
    print(f'P{mk_text} (slide-{sid}): {eb_text}')