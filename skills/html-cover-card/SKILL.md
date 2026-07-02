---
name: html-cover-card
description: |
  视频封面制作 — 生成 1055×1491 竖屏封面图，包含插图、标题、标签、作者信息，
  一键导出高清 PNG 到 output/covers/ 目录。适合视频封面、播客封面、课程封面等。
  当用户要求制作视频封面、频道封面图、课程封面、播客封面、竖版海报时使用此 skill。
triggers:
  - "视频封面"
  - "封面图"
  - "频道封面"
  - "播客封面"
  - "课程封面"
  - "竖版海报"
  - "cover image"
  - "thumbnail"
  - "做个封面"
---

# html-cover-card

生成 **1055×1491** 竖屏封面图，包含插图、标题、标签、作者信息，一键导出高清 PNG。

## 项目结构

```
video-creator/
├── output/
│   └── covers/                   ← 导出的封面 PNG 放这里
├── skills/html-cover-card/
│   ├── SKILL.md
│   ├── gen-images-b64.py         ← 图片 base64 生成脚本
│   ├── assets/
│   │   ├── fonts/lxgw-wenkai-v1.522/ ← 霞鹜文楷字体
│   │   ├── bg.png                ← 封面背景图（1055×1491）
│   │   ├── piggy_transparent.png ← 封面插图示例（透明 PNG，900×900）
│   │   └── images-b64.js         ← 图片 base64 缓存
│   └── templates/
│       └── cover.html            ← 封面模板
```

## 使用方式

1. **复制模板**：将 `skills/html-cover-card/templates/cover.html` 复制到工作位置
2. **修改内容**：
   - 替换 `<img class="cover-illustration" src="...">` 的图片路径
   - 修改 `.cover-tag` 标签文字
   - 修改 `.p-title` 标题内容（可用 `<span class="hl">` 高亮关键词）
   - 修改 `.p-subtitle` 副标题/导语
   - 修改 `.cover-author` 作者和年份
3. **打开预览**：用浏览器直接打开 HTML 即可预览
4. **导出 PNG**：点击右上角下载按钮，将 PNG 保存到 `output/covers/`

## 关键参数

| 参数 | 值 |
|------|----|
| 封面尺寸 | 1055 × 1491 px |
| 标题字号 | 80px / Noto Serif SC 500 |
| 副标题字号 | 52px / LXGWWenKai |
| 标签字号 | 26px / LXGWWenKai |
| 高亮颜色 | #f5b0c0（粉色下划线） |
| 插图建议尺寸 | 900 × 900 px（透明 PNG） |

## 替换图片后

```bash
# 更换插图或背景后必须重跑
python3 skills/html-cover-card/gen-images-b64.py
```

## 封面元素说明

| 元素 | CSS 类名 | 说明 |
|------|----------|------|
| 插图 | `.cover-illustration` | 顶部大图，透明 PNG 最佳 |
| 标签 | `.cover-tag` | 左侧小标签，如「产品介绍 · 开源」 |
| 主标题 | `.p-title` | 大字标题，支持高亮 |
| 副标题 | `.p-subtitle` | 一句话导语 |
| 分割线 | `.cover-divider` | 渐变水平线 |
| 作者行 | `.cover-author` | 作者名 · 年份 |

## 输出规范

- 导出的封面 PNG 统一放到 `output/covers/` 目录
- 文件名建议：`<视频项目名>-cover.png`，如 `xhs-plugin-intro-cover.png`
