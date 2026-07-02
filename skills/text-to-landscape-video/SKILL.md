---
name: text-to-landscape-video
description: |
  视频创作生成器 — 将文章、笔记、个人叙事转为 1920×1080 横屏 MP4 动画，
  每帧为独立 HTML+CSS+GSAP 动画文件，基于 HyperFrames 框架渲染。
  当用户要求把文章做成视频、制作横屏动画、用 HyperFrames 做视频时使用此 skill。
triggers:
  - "做成视频"
  - "横屏视频"
  - "动画视频"
  - "HyperFrames"
  - "文字转视频"
  - "text to video"
  - "视频创作"
  - "制作视频"
---

# text-to-landscape-video

将文章、笔记、个人叙事转为 **1920×1080 横屏 MP4 动画**，每帧为左右分区布局，配 GSAP 逐拍动画，无配音静默版。

## HyperFrames 是什么

**HyperFrames** 是一个把 HTML/CSS/GSAP 动画渲染成 MP4 的视频制作框架。原理：

```
纯文本 → 每帧 HTML 动画文件 → index.html 组装时间线 → npx hyperframes render → MP4
```

- **每一帧 = 一个 HTML 文件**，包含布局 CSS + GSAP timeline
- **背景必须是独立 clip div**，不能直接设在 `#root` 上
- **每个 clip 需要唯一 `data-track-index`**，同帧内不能重复
- **GSAP timeline 必须注册**到 `window.__timelines['composition-id']`

## 工作流

| 步骤 | 动作 | 产物 |
|------|------|------|
| 1 | 初始化 HyperFrames 项目 | `videos/<project>/hyperframes.json` |
| 2 | 生成设计系统 | `frame.md`（editorial-forest 预设） |
| 3 | 规划 STORYBOARD | `STORYBOARD.md`（每帧叙事） |
| 4 | 逐帧写 HTML 动画 | `compositions/frames/0N-*.html` |
| 5 | 组装 + 注入转场 + lint | `index.html` |
| 6 | 渲染 | `renders/*.mp4` |

## 如何使用

直接告诉 Agent：

> "把这篇文章做成横屏视频"
> "用 HyperFrames 把文章转为 1920x1080 视频"
> "帮我做一个产品介绍视频"

## 设计预设：editorial-forest

- **调色板**：green `#2e4a2a` / pink `#e89cb1` / cream `#efe7d4`
- **字体**：Source Serif 4 500（标题）+ JetBrains Mono 500（标签）
- **动画风格**：power3.out 缓动，逐拍揭示，无 bounce
- **格式**：1920×1080（16:9 横屏），静音

## 输出规范

- **视频目录**：`videos/<project-name>/`
- **renders/ 不入 git**：MP4 文件太大，建议只 commit 源文件
- **每帧独立**：`compositions/frames/0N-*.html`

## 关键规则

1. 每个 timed element 需要 `data-start`、`data-duration`、`data-track-index`
2. 带 timing 的元素**必须**有 `class="clip"`
3. Timeline 必须 paused 并注册到 `window.__timelines`
4. 只用确定性逻辑——禁止 `Date.now()`、`Math.random()`、网络请求
5. 修改后必须运行 `npm run check` lint

## 命令

```bash
npm run dev          # 启动预览服务（后台运行）
npm run check        # lint + validate
npm run render       # 渲染为 MP4
```

## 运动规范（静音视频）

- 入场：smooth long-tail settle（power3），绝不使用 bounce/back.out
- 显示节奏：每帧按 beat 分段逐步揭示
- 持续感：subtle jitter（sine-wave-loop 低振幅）
- 运动数量：2–4 种 move per 帧
- 无限循环：全部禁止

## 参考实现

```
videos/odyssey-my-era/   ← 完整案例（10 帧，50 秒）
├── STORYBOARD.md        ← 叙事规划
├── frame.md             ← 设计系统
├── compositions/frames/ ← 10 个横版帧 HTML
├── index.html           ← 组装后时间线
└── renders/             ← 输出 MP4

videos/xhs-plugin-intro/ ← 产品介绍视频（10 帧）
├── STORYBOARD.md        ← 产品叙事规划
├── compositions/frames/ ← 10 个帧 HTML
└── renders/             ← 输出 MP4
```
