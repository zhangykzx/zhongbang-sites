#!/usr/bin/env python
"""
Re-insert 积道山 SLIDE 15 into deployed index.html with all latest updates:
- Resource row removed
- Right column 3 segments (last: location text)
- Data: 7000万 / 50000 (no 万)
- Eyebrow: 积 道 山 康 养 小 镇
- Renumber downstream slides 15-19 → 16-20
- Update nav map
"""
import re
import os
import shutil

WORK = r'D:\admin\Desktop\品牌\zhongbang-sites\index.html'

NEW_SLIDE = '''<!-- ============================================================
     SLIDE 15 · 战略旗舰项目 积道山康养小镇
     ============================================================ -->
<section class="slide slide--ink" id="slide-15">
  <div class="bg-glow bg-glow--tl"></div>

  <div class="container">
    <!-- 1. HERO BANNER -->
    <div class="reveal" style="position: relative; aspect-ratio: 16 / 7; overflow: hidden; border-radius: 4px; box-shadow: 0 25px 70px rgba(0, 0, 0, 0.5);">
      <img src="assets/jidaoshan.png" alt="积道山康养小镇效果图" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: center 45%; filter: brightness(0.5) contrast(1.05);">
      <div style="position: absolute; inset: 0; background: linear-gradient(180deg, rgba(10, 9, 8, 0.25) 0%, rgba(10, 9, 8, 0.55) 70%, rgba(10, 9, 8, 0.7) 100%);"></div>
      <div style="position: absolute; inset: 0; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: 1.5rem 2rem;">
        <p style="color: var(--gold); font-size: 0.75rem; letter-spacing: 0.35em; font-weight: 500; opacity: 0.95;">战 略 旗 舰 项 目 &nbsp;·&nbsp; 积 道 山 康 养 小 镇</p>
        <h2 class="h1" style="line-height: 1.2; color: var(--ivory); margin-top: 0.85rem; text-shadow: 0 2px 12px rgba(0, 0, 0, 0.6); font-weight: 500;">
          浙 中 地 区 <em style="font-style: normal; color: var(--gold); font-weight: 500;">首 个</em><br>
          山 水 康 养 休 闲 度 假 小 镇
        </h2>
        <p style="color: var(--gold-soft); margin-top: 0.75rem; letter-spacing: 0.35em; font-size: 0.8125rem; font-weight: 500;">
          JIDAOSHAN &nbsp;·&nbsp; WELLNESS TOWN
        </p>
      </div>
    </div>

    <!-- 2. Pull Quote -->
    <div class="reveal reveal--delay-1" style="margin-top: 1.25rem; text-align: center;">
      <p style="font-family: var(--font-serif); font-size: 1rem; line-height: 1.4; color: var(--gold-soft); font-style: italic; font-weight: 400; letter-spacing: 0.05em;">
        "都市繁华和青山绿水之间，给身心一处悠然切换的栖息地。"
      </p>
    </div>

    <!-- 3. LEFT-RIGHT SPLIT -->
    <div class="reveal reveal--delay-2" style="margin-top: 1.5rem; display: grid; grid-template-columns: 1fr 1.5fr; gap: 2.5rem; align-items: stretch;">
      <!-- Left: 3 chip rows -->
      <div style="display: flex; flex-direction: column; gap: 0.55rem;">
        <div style="display: flex; align-items: center; gap: 0.75rem; padding: 0.55rem 0.9rem; border-left: 2px solid var(--gold); background: rgba(20, 17, 15, 0.5);">
          <span style="color: var(--gold); font-size: 0.7rem; letter-spacing: 0.2em; font-weight: 500; min-width: 38px;">理 念</span>
          <span style="color: var(--ivory); font-size: 0.875rem; letter-spacing: 0.05em; line-height: 1.4;">旅居康养<span style="color: var(--gold-soft);"> · 核心</span> &nbsp; 文化<span style="color: var(--gold-soft);"> · 驱动</span> &nbsp; 业态创新<span style="color: var(--gold-soft);"> · 导向</span></span>
        </div>
        <div style="display: flex; align-items: center; gap: 0.75rem; padding: 0.55rem 0.9rem; border-left: 2px solid var(--gold); background: rgba(20, 17, 15, 0.5);">
          <span style="color: var(--gold); font-size: 0.7rem; letter-spacing: 0.2em; font-weight: 500; min-width: 38px;">模 式</span>
          <span style="color: var(--gold); font-family: var(--font-display); font-size: 1.0625rem; letter-spacing: 0.4em; font-weight: 500;">养 游 居</span>
        </div>
        <div style="display: flex; align-items: center; gap: 0.75rem; padding: 0.55rem 0.9rem; border-left: 2px solid var(--gold); background: rgba(20, 17, 15, 0.5);">
          <span style="color: var(--gold); font-size: 0.7rem; letter-spacing: 0.2em; font-weight: 500; min-width: 38px;">功 能</span>
          <span style="color: var(--ivory); font-size: 0.8125rem; letter-spacing: 0.05em; line-height: 1.4;">养老养生 &nbsp; 文化体验 &nbsp; 田园度假 &nbsp; 旅游集散</span>
        </div>
      </div>

      <!-- Right: 3 segments -->
      <div style="display: flex; flex-direction: column; gap: 0.55rem; justify-content: space-between;">
        <p style="color: rgba(245, 240, 232, 0.85); line-height: 1.4; font-size: 0.875rem; margin: 0;">
          积道山康养小镇位于<strong style="color: var(--gold); font-weight: 500;">省级景区积道山旅游度假区</strong>，地处浙中核心金华，紧邻金义东公路和金义东连接线。
        </p>
        <p style="color: rgba(245, 240, 232, 0.85); line-height: 1.4; font-size: 0.875rem; margin: 0;">
          通过<strong style="color: var(--gold-soft); font-weight: 500;">导入人文资源 → 带动主题度假 → 植入全龄康养概念</strong>，打造<strong style="color: var(--gold); font-weight: 500;">「养、游、居」</strong>为核心的开发模式。
        </p>
        <p style="color: rgba(245, 240, 232, 0.85); line-height: 1.4; font-size: 0.875rem; margin: 0;">
          集<span style="color: var(--gold-soft);">养老养生、文化体验、田园度假、旅游集散</span>等<strong style="color: var(--gold); font-weight: 500;">全龄旅居康养小镇</strong>。
        </p>
      </div>
    </div>

    <!-- 4. Data Callouts -->
    <div class="reveal reveal--delay-3" style="margin-top: 1.5rem; padding-top: 1rem; border-top: 1px solid rgba(201, 169, 97, 0.2);">
      <div style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 0.5rem; text-align: center;">
        <div><span style="font-family: var(--font-display); font-size: 1.625rem; color: var(--gold); font-weight: 500;">240<sup style="font-size: 0.875rem; font-weight: 400; margin-left: 0.1rem;">+</sup></span><p style="font-size: 0.6875rem; color: rgba(245, 240, 232, 0.6); margin-top: 0.2rem; letter-spacing: 0.1em;">亩 · 总规划</p></div>
        <div><span style="font-family: var(--font-display); font-size: 1.625rem; color: var(--gold); font-weight: 500;">7000<sup style="font-size: 0.875rem; font-weight: 400; margin-left: 0.1rem;">万</sup></span><p style="font-size: 0.6875rem; color: rgba(245, 240, 232, 0.6); margin-top: 0.2rem; letter-spacing: 0.1em;">元 · 总投资</p></div>
        <div><span style="font-family: var(--font-display); font-size: 1.625rem; color: var(--gold); font-weight: 500;">50000</span><p style="font-size: 0.6875rem; color: rgba(245, 240, 232, 0.6); margin-top: 0.2rem; letter-spacing: 0.1em;">㎡ · 一期建面</p></div>
        <div><span style="font-family: var(--font-display); font-size: 1.625rem; color: var(--gold); font-weight: 500;">806</span><p style="font-size: 0.6875rem; color: rgba(245, 240, 232, 0.6); margin-top: 0.2rem; letter-spacing: 0.1em;">张 · 设计床位</p></div>
        <div><span style="font-family: var(--font-display); font-size: 1.625rem; color: var(--gold); font-weight: 500;">2<sup style="font-size: 0.875rem; font-weight: 400; margin-left: 0.1rem;">h</sup></span><p style="font-size: 0.6875rem; color: rgba(245, 240, 232, 0.6); margin-top: 0.2rem; letter-spacing: 0.1em;">长三角核心圈</p></div>
      </div>
    </div>
  </div>

  <img class="corner-logo" src="assets/logo.png" alt="众邦康养">
  <div class="page-marker">
    <span class="page-marker__num">15</span> &nbsp;/&nbsp; 20
  </div>
</section>

'''


def main():
    with open(WORK, 'r', encoding='utf-8') as f:
        content = f.read()

    changes = []

    # Step 1: Renumber slide-15..19 → 16..20 (decreasing)
    for old, new in [('slide-19', 'slide-20'),
                     ('slide-18', 'slide-19'),
                     ('slide-17', 'slide-18'),
                     ('slide-16', 'slide-17'),
                     ('slide-15', 'slide-16')]:
        before = content.count(f'id="{old}"')
        content = content.replace(f'id="{old}"', f'id="{new}"')
        if before > 0:
            changes.append(f'Renumbered: id="{old}" → id="{new}" ({before}x)')

    # Step 2: Renumber page-marker numerators 15..19 → 16..20 (decreasing)
    for old, new in [(19, 20), (18, 19), (17, 18), (16, 17), (15, 16)]:
        before = content.count(f'>{old}</span>')
        content = content.replace(f'>{old}</span>', f'>{new}</span>')
        if before > 0:
            changes.append(f'Renumbered: page-marker {old} → {new}')

    # Step 3: Update denominator / 19 → / 20
    before = content.count('&nbsp;/&nbsp; 19')
    content = content.replace('&nbsp;/&nbsp; 19', '&nbsp;/&nbsp; 20')
    if before > 0:
        changes.append(f'Updated: / 19 → / 20 ({before}x)')

    # Step 4: Renumber nav map entries
    for old, new in [('slide-19', 'slide-20'),
                     ('slide-18', 'slide-19'),
                     ('slide-17', 'slide-18'),
                     ('slide-16', 'slide-17'),
                     ('slide-15', 'slide-16')]:
        before = content.count(f"id: '{old}'")
        if before > 0:
            content = content.replace(f"id: '{old}'", f"id: '{new}'")
            changes.append(f'Renumbered nav: {old} → {new}')

    # Step 5: Insert new SLIDE 15 before SLIDE 16 comment
    target = '<!-- ============================================================\n     SLIDE 16 · CHAPTER'
    if target in content:
        content = content.replace(target, NEW_SLIDE + target, 1)
        changes.append('Inserted new SLIDE 15 · 积道山康养小镇')
    else:
        # Try alternative
        target2 = '<!-- SLIDE 16'
        if target2 in content:
            idx = content.find(target2)
            content = content[:idx] + NEW_SLIDE + content[idx:]
            changes.append('Inserted new SLIDE 15 · 积道山康养小镇 (alt)')

    # Step 6: Add new nav map entry
    nav_anchor = "{ id: 'slide-16'"
    if nav_anchor in content:
        # Find a good insertion point - right after the slide-14 line
        nav_14 = "{ id: 'slide-14', label: '五年规划' }"
        if nav_14 in content:
            new_nav = nav_14 + ",\n    { id: 'slide-15', label: '积道山旗舰' },"
            content = content.replace(nav_14, new_nav, 1)
            changes.append('Added nav map entry: slide-15 积道山旗舰')

    with open(WORK, 'w', encoding='utf-8') as f:
        f.write(content)

    print('=== CHANGES ===')
    for c in changes:
        print(f'  - {c}')


if __name__ == '__main__':
    main()