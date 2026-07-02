# 视频创作生成器 (video-creator)

> 视频创作全流程工具箱：动画视频制作 + 封面图制作，产出统一在 `output/` 目录。  
> 基于 HyperFrames 框架，每帧为独立 HTML+CSS+GSAP 动画，逐拍揭示视觉节奏。

Made by [dreamer piggy](https://github.com/dreamer-piggy) 🐷

---

## 两个能力

### 🎬 动画视频

一篇文章 → 分镜脚本 → 逐帧 HTML 动画 → 渲染为 1920×1080 MP4 → `output/videos/`

### 🖼️ 视频封面

标题 + 插图 + 标签 → 生成 1055×1491 竖屏封面 → 导出 PNG → `output/covers/`

---

## 快速开始

```bash
# 克隆项目
git clone https://github.com/Amateur0x1/video-creator.git
cd video-creator

# === 做视频 ===
cd videos/odyssey-my-era
npm install
npm run dev        # 预览
npm run render     # 渲染 MP4
# 将成品拷到 output
cp renders/<latest>.mp4 ../../output/videos/odyssey-my-era.mp4

# === 做封面 ===
open skills/html-cover-card/templates/cover.html
# 修改内容后点右上角按钮导出 PNG，保存到 output/covers/
```

---

## 项目结构

```
video-creator/
├── videos/                              ← 视频项目源码（入 git）
│   ├── odyssey-my-era/                  ← 奥德赛时期叙事（10 帧，50s）
│   │   ├── STORYBOARD.md               ← 分镜脚本
│   │   ├── frame.md                    ← 设计系统
│   │   ├── compositions/frames/        ← 10 个帧 HTML
│   │   ├── index.html                  ← 主时间线
│   │   └── renders/                    ← 渲染中间产物（不入 git）
│   ├── xhs-plugin-intro/               ← 小红书插件介绍
│   └── xhs-overlay/                    ← 透明字幕叠加层
│
├── output/                              ← 所有最终产出（不入 git）
│   ├── videos/                          ← 交付的 MP4
│   └── covers/                          ← 导出的封面 PNG
│
├── skills/
│   ├── text-to-landscape-video/
│   │   └── SKILL.md                    ← 视频制作 Skill
│   └── html-cover-card/
│       ├── SKILL.md                    ← 封面制作 Skill
│       ├── gen-images-b64.py           ← 图片 base64 生成
│       ├── assets/                     ← 字体、背景图、插图
│       └── templates/cover.html        ← 封面模板
│
├── agent.md                             ← AI Agent 使用说明
└── README.md
```

---

## 已有作品

### odyssey-my-era — 我的奥德赛时期

10 帧，约 50 秒。讲述从哲学→经济学→转码→大厂→独立开发的五次转向。

### xhs-plugin-intro — 小红书内容嗅探插件介绍

10 帧产品介绍视频。从痛点引入到功能展示到行动召唤的完整产品叙事弧。

### xhs-overlay — 透明字幕叠加层

1080×660 透明背景字幕动画，叠加到口播视频上生成最终成品。

---

## 技术设计

### HyperFrames 框架

将视频的每一帧当作网页来制作。每帧 HTML 包含布局 CSS 和 GSAP timeline 动画，由渲染引擎逐帧截图拼接成 MP4。

### editorial-forest 设计预设

森林绿/玫瑰粉/奶油白三色调，Source Serif 4 衬线字体为主导，整体风格像企鹅经典图书或安静的年报。

### 运动语法

入场用 smooth long-tail settle（power3.out），逐拍揭示，重点词 spring-pop payoff，subtle jitter 保持活感，全部禁止无限循环。

---

## 依赖

- Node.js（HyperFrames CLI）
- GSAP（动画引擎，CDN 引入）
- Google Fonts（Source Serif 4 + JetBrains Mono）
- Python 3（仅封面的 base64 脚本，标准库即可）
- html2canvas（封面导出 PNG，CDN 引入）

---

## 问题 & 反馈

👉 [github.com/dreamer-piggy](https://github.com/dreamer-piggy)

Star 的话我会很开心 🌟
