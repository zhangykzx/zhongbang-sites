import re
path = r'D:\admin\Desktop\品牌\zhongbang-sites\index.html'
with open(path, 'r', encoding='utf-8') as fp:
    c = fp.read()

# 找 slide-10 section
m = re.search(r'<section[^>]*id="slide-10"[^>]*>(.*?)</section>', c, re.DOTALL)
if m:
    section = m.group(1)
    print(f'P10 section length: {len(section)} chars')
    print()
    eb = re.search(r'class="eyebrow[^"]*"[^>]*>([^<]+)<', section)
    print(f'eyebrow: {eb.group(1).strip() if eb else "?"}')
    h2 = re.search(r'<h2[^>]*>(.+?)</h2>', section, re.DOTALL)
    if h2:
        print(f'h2: {re.sub(r"<[^>]+>", " ", h2.group(1)).strip()}')
    # 找现有数据 callout
    cards = re.findall(r'class="card[^"]*"', section)
    print(f'card count: {len(cards)}')
    # 找小标题
    for h in re.finditer(r'<h3[^>]*>(.+?)</h3>|<h4[^>]*>(.+?)</h4>', section):
        t = h.group(1) or h.group(2)
        if t:
            print(f'  subhead: {re.sub(r"<[^>]+>", " ", t).strip()}')
    print()
    print('=== first 1500 chars ===')
    print(section[:1500])