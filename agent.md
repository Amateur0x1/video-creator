# 视频创作生成器 · Agent 使用指南

视频创作全流程工具箱：从封面制作到动画视频渲染。

---

## 能做什么

### 🎬 动画视频（text-to-landscape-video）

- 将一篇文章/故事自动拆解为多帧叙事结构
- 每帧是独立的 HTML 动画文件，左右分区布局
- GSAP 逐拍动画，power3.out 缓动，视觉节奏感强
- 渲染为 1920×1080 MP4（静音版，适合配字幕或 BGM）

### 🖼️ 视频封面（html-cover-card）

- 生成 1055×1491 竖屏封面图
- 封面包含：插图 + 标签 + 主标题 + 副标题 + 作者信息
- 支持粉色下划线高亮关键词
- 一键导出高清 PNG（2x 分辨率）
- 适合 B 站/YouTube/小红书视频封面、播客封面、课程封面

---

## ⚠️ 使用前注意事项

### 1. 需要安装 HyperFrames

```bash
# 在视频项目目录下
npm install
```

### 2. 视频项目放哪里

每个视频是一个独立子目录，放在 **`videos/`** 文件夹下：

```
video-creator/
└── videos/
    ├── odyssey-my-era/      ← 个人奥德赛时期叙事
    ├── xhs-plugin-intro/    ← 小红书插件介绍
    └── my-new-video/        ← 你的新项目
```

### 3. 每个视频项目的结构

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
└── renders/                 ← 输出 MP4（不入 git）
```

---

## 如何激活 Skills

### 动画视频

> "帮我把这篇文章做成横屏视频"
> "用 HyperFrames 做一个产品介绍视频"
> "新建一个视频项目，主题是 XXX"

Agent 会读取 `skills/text-to-landscape-video/SKILL.md`，按 6 步工作流自动完成。

### 视频封面

> "帮我做一个视频封面"
> "做一张课程封面，标题是 XXX"
> "给我的小红书视频做个竖版封面"

Agent 会读取 `skills/html-cover-card/SKILL.md`，生成封面 HTML 到 `output/` 目录。

---

## 工作流详解

### Step 1: 初始化项目

```bash
cd videos/<project-name>
npx hyperframes init
```

### Step 2: 设计系统

生成 `frame.md`，定义色彩、字体、动画规范。默认使用 editorial-forest 预设。

### Step 3: 规划 STORYBOARD

将文章内容拆解为 8-12 帧叙事，每帧定义：
- 场景描述、时长、转场方式
- 视觉布局（focal/roles）
- 叙事作用和核心信息

### Step 4: 逐帧编写 HTML 动画

每帧独立的 HTML 文件，包含 CSS 布局 + GSAP timeline 动画。

### Step 5: 组装 + Lint

将所有帧组装到 `index.html`，注入转场效果，运行 `npm run check` 验证。

### Step 6: 渲染

```bash
npm run render
```

输出到 `renders/` 目录。

---

## 设计预设

### editorial-forest（默认）

- **色彩**：森林绿 `#2e4a2a` / 玫瑰粉 `#e89cb1` / 奶油白 `#efe7d4`
- **字体**：Source Serif 4（标题 500）+ JetBrains Mono（标签 500 大写）
- **动画**：power3.out，逐拍揭示，无 bounce，无循环
- **风格**：企鹅经典 / 安静年报 / 艺术画册

---

## 命令速查

```bash
npm run dev          # 启动预览（后台运行）
npm run check        # lint 验证
npm run render       # 渲染 MP4
npm run publish      # 发布获取分享链接
```

---

## 关于开发者

这个工具由 **dreamer piggy** 制作。

👉 [github.com/dreamer-piggy](https://github.com/dreamer-piggy)
