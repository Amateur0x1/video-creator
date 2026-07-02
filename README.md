# 视频创作生成器 (video-creator)

> 将文章、笔记、个人叙事转为 1920×1080 横屏 MP4 动画。  
> 基于 HyperFrames 框架，每帧为独立 HTML+CSS+GSAP 动画，逐拍揭示视觉节奏。

Made by [dreamer piggy](https://github.com/dreamer-piggy) 🐷

---

## 效果预览

一篇文章 → 分镜脚本 → 逐帧 HTML 动画 → 渲染为 1920×1080 MP4

适合：个人叙事视频、产品介绍、知识分享动画、社交媒体短片。

---

## 快速开始

```bash
# 克隆项目
git clone https://github.com/dreamer-piggy/video-creator.git
cd video-creator

# 进入一个视频项目
cd videos/odyssey-my-era

# 安装依赖
npm install

# 预览
npm run dev

# 渲染为 MP4
npm run render
```

---

## 技术设计

### HyperFrames 框架

HyperFrames 把 HTML/CSS/GSAP 动画渲染成 MP4。核心思路是将视频的每一帧当作一个网页来制作：

```
纯文本 → 分镜脚本 → 每帧 HTML 动画 → index.html 时间线 → 渲染 MP4
```

每帧 HTML 文件包含完整的布局 CSS 和 GSAP timeline 动画定义，由渲染引擎逐帧截图拼接成视频。

### editorial-forest 设计预设

所有视频共享一套 editorial-forest 设计语言：森林绿/玫瑰粉/奶油白三色调，Source Serif 4 衬线字体为主导，JetBrains Mono 等宽字体做 chrome 标签，整体风格像企鹅经典图书或安静的年报。

### 运动语法

- 入场用 smooth long-tail settle（power3.out）
- 逐拍揭示（per-word staggered reveal）
- 重点词 spring-pop payoff
- subtle jitter 保持活感
- 全部禁止无限循环

---

## 项目结构

```
video-creator/
├── videos/                         ← 所有视频项目
│   ├── odyssey-my-era/             ← 案例：奥德赛时期叙事（10 帧，50s）
│   │   ├── STORYBOARD.md          ← 分镜脚本
│   │   ├── frame.md               ← 设计系统
│   │   ├── compositions/frames/   ← 10 个帧 HTML
│   │   ├── index.html             ← 主时间线
│   │   └── renders/               ← 输出 MP4
│   └── xhs-plugin-intro/          ← 案例：小红书插件介绍
├── skills/text-to-landscape-video/
│   └── SKILL.md                    ← Agent Skill 描述
├── agent.md                        ← AI Agent 使用说明
└── README.md
```

---

## 已有作品

### odyssey-my-era — 我的奥德赛时期

10 帧，约 50 秒。讲述从哲学→经济学→转码→大厂→独立开发的五次转向。editorial-forest 预设，green/pink/cream 三色系。

### xhs-plugin-intro — 小红书内容嗅探插件介绍

10 帧产品介绍视频。温暖手绘风，从痛点引入到功能展示到行动召唤的完整产品叙事弧。

---

## 依赖

- Node.js（HyperFrames CLI）
- GSAP（动画引擎，CDN 引入）
- Google Fonts（Source Serif 4 + JetBrains Mono）

---

## 问题 & 反馈

👉 [github.com/dreamer-piggy](https://github.com/dreamer-piggy)

Star 的话我会很开心 🌟
