import re
with open(r'D:\admin\Desktop\品牌\zhongbang-sites\index.html', 'r', encoding='utf-8') as fp:
    c = fp.read()

# Find context around 招 商 加 盟
for m in re.finditer(r'招[\s ]?商[\s ]?加[\s ]?盟', c):
    ctx = c[max(0,m.start()-100):m.end()+200]
    print(f"@{m.start()}: {ctx}")
    print("---")