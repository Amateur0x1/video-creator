# 视频创作生成器 · Agent 使用指南

视频创作全流程工具箱：从封面制作到动画视频渲染，产出统一放在 `output/` 目录。

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

## 项目结构

```
video-creator/
├── videos/                         ← 视频项目源码（入 git）
│   ├── odyssey-my-era/             ← 个人奥德赛时期叙事
│   ├── xhs-plugin-intro/          ← 小红书插件介绍
│   ├── xhs-overlay/               ← 透明字幕叠加层
│   └── <new-project>/             ← 你的新项目
│
├── output/                         ← 所有产出（不入 git）
│   ├── videos/                     ← 最终交付的视频 MP4
│   └── covers/                     ← 导出的封面 PNG
│
├── skills/
│   ├── text-to-landscape-video/    ← 视频制作 Skill
│   └── html-cover-card/           ← 封面制作 Skill
│
├── agent.md
└── README.md
```

---

## 如何激活 Skills

### 动画视频

> "帮我把这篇文章做成横屏视频"
> "用 HyperFrames 做一个产品介绍视频"
> "新建一个视频项目，主题是 XXX"

Agent 会读取 `skills/text-to-landscape-video/SKILL.md`，按工作流自动完成。最终视频输出到 `output/videos/`。

### 视频封面

> "帮我做一个视频封面"
> "做一张课程封面，标题是 XXX"
> "给我的小红书视频做个竖版封面"

Agent 会读取 `skills/html-cover-card/SKILL.md`，生成封面并导出 PNG 到 `output/covers/`。

---

## 视频制作工作流

### Step 1: 初始化项目

```bash
cd videos/<project-name>
npx hyperframes init
```

### Step 2: 设计系统

生成 `frame.md`，定义色彩、字体、动画规范。默认使用 editorial-forest 预设。

### Step 3: 规划 STORYBOARD

将文章内容拆解为 8-12 帧叙事，每帧定义场景描述、时长、转场方式、视觉布局、核心信息。

### Step 4: 逐帧编写 HTML 动画

每帧独立的 HTML 文件，包含 CSS 布局 + GSAP timeline 动画。

### Step 5: 组装 + Lint

将所有帧组装到 `index.html`，注入转场效果，运行 `npm run check` 验证。

### Step 6: 渲染

```bash
npm run render
# 渲染完成后将 MP4 拷贝到 output/videos/
cp renders/<latest>.mp4 ../../output/videos/<project-name>.mp4
```

---

## 封面制作流程

1. 复制模板 `skills/html-cover-card/templates/cover.html`
2. 修改标题、副标题、标签、插图
3. 浏览器打开预览
4. 点右上角按钮导出 PNG → 保存到 `output/covers/`

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
# 视频项目（在 videos/<project>/ 下执行）
npm run dev          # 启动预览（后台运行）
npm run check        # lint 验证
npm run render       # 渲染 MP4

# 封面（在项目根目录执行）
python3 skills/html-cover-card/gen-images-b64.py   # 换图后重新生成 base64
open skills/html-cover-card/templates/cover.html   # 预览封面
```

---

## 关于开发者

这个工具由 **dreamer piggy** 制作。

👉 [github.com/dreamer-piggy](https://github.com/dreamer-piggy)
