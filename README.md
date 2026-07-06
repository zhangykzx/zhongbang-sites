# 众邦品牌站点 / Zhongbang Brand Sites

众邦康养品牌资产与对外站点的集中托管仓库。

## 站点地图

| URL | 名称 | 状态 |
|---|---|---|
| `/` | 主品牌站 v2（zhongbang_v2_2026） | ✅ 已上线 |
| `/sites/recruitment/` | 招聘站 | 🚧 规划中 |
| `/sites/investor/` | 投资人站 | 🚧 规划中 |

## 本地预览

PowerShell 在仓库根目录运行：

```powershell
python -m http.server 8000
```

浏览器打开 `http://localhost:8000/`。

## 部署

推到 `main` 分支即自动部署到 GitHub Pages。

```powershell
git add .
git commit -m "描述本次改动"
git push
```

## 目录约定

```
zhongbang-sites/
├── index.html                # 主品牌站（首页）
├── assets/                   # 共享资源（logo、字体、图片）
├── downloads/                # 提供下载的文件（PPTX/PDF）
├── sites/
│   ├── recruitment/          # 招聘站
│   └── investor/             # 投资人站
└── README.md
```

每个子站是一个独立的 `index.html`，URL 即子目录路径。

## 协作

- 主分支受保护，建议通过 PR 合并
- 推送前本地预览确认
- 推送后约 30 秒～1 分钟自动上线