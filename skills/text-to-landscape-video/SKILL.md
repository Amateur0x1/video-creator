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

## 项目结构

```
video-creator/
├── videos/                       ← 视频项目源码（入 git）
│   ├── odyssey-my-era/           ← 案例：奥德赛时期叙事（10 帧）
│   ├── xhs-plugin-intro/        ← 案例：插件介绍视频（10 帧）
│   └── xhs-overlay/             ← 案例：透明字幕叠加层
├── output/
│   └── videos/                   ← 最终交付视频（不入 git）
└── skills/text-to-landscape-video/
    └── SKILL.md
```

## HyperFrames 是什么

**HyperFrames** 是一个把 HTML/CSS/GSAP 动画渲染成 MP4 的视频制作框架。原理：

```
纯文本 → 每帧 HTML 动画文件 → index.html 组装时间线 → npx hyperframes render → MP4
```

## 工作流

| 步骤 | 动作 | 产物 |
|------|------|------|
| 1 | 初始化 HyperFrames 项目 | `videos/<project>/hyperframes.json` |
| 2 | 生成设计系统 | `frame.md`（editorial-forest 预设） |
| 3 | 规划 STORYBOARD | `STORYBOARD.md`（每帧叙事） |
| 4 | 逐帧写 HTML 动画 | `compositions/frames/0N-*.html` |
| 5 | 组装 + 注入转场 + lint | `index.html` |
| 6 | 渲染 | `renders/*.mp4`，最终拷贝到 `output/videos/` |

## 每个视频项目的结构

```
videos/<project-name>/
├── hyperframes.json         ← HyperFrames 配置
├── meta.json                ← 项目元数据
├── package.json             ← npm 依赖
├── frame.md                 ← 设计系统（色彩/字体/动画规范）
├── STORYBOARD.md            ← 分镜脚本（每帧叙事详细描述）
├── index.html               ← 主时间线（组装所有帧）
├── compositions/frames/     ← 每帧的 HTML 动画文件
│   ├── 01-hook.html
│   ├── 02-xxx.html
│   └── ...
├── public/                  ← 静态资源（背景图等）
└── renders/                 ← 渲染中间产物（不入 git）
```

## 设计预设：editorial-forest

- **调色板**：green `#2e4a2a` / pink `#e89cb1` / cream `#efe7d4`
- **字体**：Source Serif 4 500（标题）+ JetBrains Mono 500（标签）
- **动画风格**：power3.out 缓动，逐拍揭示，无 bounce
- **格式**：1920×1080（16:9 横屏），静音

## 输出规范

- 渲染过程中 MP4 先生成到 `videos/<project>/renders/`
- 最终交付的视频拷贝到 `output/videos/` 目录
- `output/videos/` 是给用户拿走的成品目录

## 关键规则

1. 每个 timed element 需要 `data-start`、`data-duration`、`data-track-index`
2. 带 timing 的元素**必须**有 `class="clip"`
3. Timeline 必须 paused 并注册到 `window.__timelines`
4. 只用确定性逻辑——禁止 `Date.now()`、`Math.random()`、网络请求
5. 修改后必须运行 `npm run check` lint

## 命令

```bash
cd videos/<project-name>
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
