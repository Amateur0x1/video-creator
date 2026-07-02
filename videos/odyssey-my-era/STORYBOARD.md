---
format: 1920x1080
message: "每一次转向都以为是终点，每一次都不是——这就是奥德赛时期。"
arc: Hook → 奥德赛定义 → 五次转向的故事 → 两个感悟 → 着陆
audience: 正在迷茫中、不确定方向的年轻人；独立开发者；关注个人成长的读者
silent: true
---

## Video direction

**调色板（来自 frame.md editorial-forest）**
- 背景主色：cream `#efe7d4`（内容帧）/ green `#2e4a2a`（重量/宣言帧）
- 主文字：ink `#1a1a17`（cream 底上）/ cream `#efe7d4`（green 底上）
- 强调色：pink `#e89cb1`（高亮词、分隔线、circle stamp）
- 绝不使用第四色系；绝不使用 rgba 半透明面

**字体体系（来自 frame.md）**
- 展示/标题：Source Serif 4 weight 500，opsz，负字距（display ramp）
- 正文：Source Serif 4 weight 400，line-height 1.38
- Chrome（标签/脚注/编号）：JetBrains Mono 500 大写，0.08–0.18em 字距
- 每帧顶部必须有 topbar（mono label + 帧号）

**运动语法（静音视频——以视觉 beat 代替 VO 节奏）**
- 入场：smooth long-tail settle（power3），绝不使用 bounce/back.out
- 显示节奏：每帧按「beat 分段」逐步揭示——Scene 1 只放入场；Scene 2–N 在后 ~50% 时间内逐步引入其余元素
- 持续感：仅 subtle jitter（sine-wave-loop 低振幅）——不做 lazy breathing，不做后半段 push/pan
- 运动数量：2–4 种 move per 帧，不叠加所有效果
- 无限循环：全部禁止（无 repeat/yoyo/Math.random/Date.now）

**节奏分配（breather 帧）**
- Frame 2（奥德赛定义）：titlecard-reveal，低运动量，作为开篇情绪呼吸点
- Frame 10（着陆）：titlecard-reveal，held read，低运动量，视频闭合

**绝对禁止**
- 无 slideshow（首 25% 倾倒全部内容后冻结）
- 无 screensaver（多元素各自独立浮动）
- 无 bouncy entrance；无 lazy breathing；无后半段 slow pan
- 无浮动 bokeh；无紫蓝 AI 渐变；无真实 UI chrome（地址栏/光标/滚动条）
- 无 CSS transition/@keyframes 动画——全部走 paused GSAP timeline

---

## Frame 1 — Hook · 五次转向

- scene: 极简黑底上，"哲学 → 经济学 → 转码 → 大厂 → 独立开发" 五个词逐一打入，每次都带着一个 ✕ 打叉，最后一个没有打叉，而是一个问号
- voiceover: ""
- duration: 5s
- transition_in: cut
- poster: 3s
- status: outline
- src: compositions/frames/01-hook.html
- type: hook
- persuasion: Progressive disclosure（逐步揭示每一站，制造累积张力）
- beat: 好奇 + 认同
- blueprint: kinetic-type-beats (Adapt)
- focal: 五站文字序列（哲学→经济学→转码→大厂→独立开发）
- roles: 文字序列 = foreground subject（每站逐一入场）· ✕ 标记 = supporting（跟随每站 after 1s 入场）· 深色背景 = background（green-deep `#243a21` 全出血）

Adapt：保留 kinetic-type-beats 的「in-place token cycle / hard-cut word-swap」签名动作；不使用产品 logo，改用竖向单列文字流替代横向换词。
深色 green-deep 背景营造厚重感；每一站以 pink `#e89cb1` 做 ✕ 标记，最后站以 pink 问号替代。

Scene 1 (0.0–0.8s)：green-deep 全出血背景；顶部 topbar（mono "DREAMER PIGGY · 01" cream）通过 **per-word staggered reveal** (`dynamic-content-sequencing`) 淡入。画面仅 topbar，大量留白，形成入场张力。
Scene 2 (0.8–2.8s)：五个站依次从画面中心稍偏上（y≈0.38×高）**逐一入场**——每站 per-word staggered reveal，每隔约 0.35s 一站，smooth long-tail settle（power3）；前四站入场后约 0.4s，同行右侧一枚 pink ✕ 通过 **spring-pop entrance** (`spring-pop-entrance`) 弹出（平滑，无过冲）。五站文字以 Source Serif 4 display 500 cream 色，竖向排列，行间距约 1.1。
Scene 3 (2.8–4.2s)：第五站（独立开发）入场，**无 ✕**，改为 pink **?** 通过 spring-pop entrance 在右侧弹出；整列文字此时完整可见。centered template，主视觉占 ~55% 画面高度，3 depth layers（背景 / 文字列 / 标记层）。
Scene 4 (4.2–5.0s)：hold on 完整列表，**subtle jitter** (`sine-wave-loop` 低振幅) 在 pink? 上保持活感；文字列静止不动（no breathing, no drift）。

narrativeRole: 用五次转向的序列打开认知缺口——"这人到底经历了什么？"
keyMessage: 不断转向，每次以为是终点，每次都不是。

---

## Frame 2 — 概念 · 什么是奥德赛时期

- scene: 大字 "奥德赛时期" 居中出现，下方两行小字解释：漂泊 · 探索 · 尚未定锚的人生阶段
- voiceover: ""
- duration: 4s
- transition_in: crossfade
- poster: 2s
- status: outline
- src: compositions/frames/02-odyssey-define.html
- type: product_intro
- persuasion: Concept announcement（用具名术语命名体验，让观众"终于有个词了"）
- beat: 清晰 + 共鸣（breather 帧，低运动量）
- blueprint: titlecard-reveal (Reproduce)
- focal: "奥德赛时期" Source Serif 4 display-hero
- roles: 标题 = foreground subject · 副标题（漂泊 · 探索 · 尚未定锚）= supporting · cream 背景 = background

Reproduce：保留 titlecard-reveal 「ONE restrained slide-up crossfade + still hold」签名动作。cream 底，green 字。

Scene 1 (0.0–1.0s)：cream 全出血背景；topbar（mono "奥德赛时期 · 02" green） **per-word staggered reveal** 淡入。留白大，呼吸感强（breather）。
Scene 2 (1.0–2.5s)：主标题 "奥德赛时期" Source Serif 4 display-hero（~11.5cqw equivalent）green，从画面中央偏上（y≈0.40×高）**slide-up crossfade**（一次性，smooth power3）。字体大，占 ~48% 宽。
Scene 3 (2.5–3.5s)：三个副词 "漂泊 · 探索 · 尚未定锚" 以 Source Serif 4 body 400 ink，在主标题下方约 1.5 行距处 **per-word staggered reveal**（0.2s 间隔，smooth）。centered layout，两层 depth。
Scene 4 (3.5–4.0s)：held read，所有元素静止；**no jitter, no breathing**——这是 breather 帧，静止本身是意图。

narrativeRole: 给这段漂泊的人生阶段命名，让观众感受到被命名的释然。
keyMessage: "奥德赛时期"就是在多次探索中还没找到自己轴心的阶段。

---

## Frame 3 — 起点 · 小镇做题家的困境

- scene: 两列对比文字：左侧"哲学（爱好）"右侧"经济学（谋生）"，一道粉色分隔线，底部注释"2019年，不敢把爱好当饭吃"
- voiceover: ""
- duration: 5s
- transition_in: cut
- poster: 3s
- status: outline
- src: compositions/frames/03-origin.html
- type: pain_point
- persuasion: Comparison of two options（爱好 vs 谋生的具象对立，激发认同）
- beat: 认同 + 轻微痛苦
- blueprint: comparison-split (Adapt)
- focal: 哲学 vs 经济学 split 对比
- roles: 左列（哲学/爱好）= foreground subject left · 右列（经济学/谋生）= foreground subject right · pink 竖向分隔线 = supporting · cream 背景 = background

Adapt：保留 comparison-split「mirrored book-open tilts from opposite wings」签名动作；竖版改为上下 stack（哲学在上，经济学在下，中间 pink 横向 2px 分隔线），因为竖版不适合左右 split-screen。

Scene 1 (0.0–0.8s)：cream 背景；topbar（mono "ORIGIN · 03" green）per-word staggered reveal 淡入。
Scene 2 (0.8–2.2s)：上半区：哲学（爱好）块——JetBrains Mono label "LOVE" pink 大写先入；Source Serif 4 headline-xl "哲学" green，从 y=0 **slide-up** 入场（smooth power3，带轻微 3D rotationY 入场倾斜，约 -8deg→0，Adapt 签名保留）。占上部 ~35% 高度。
Scene 3 (2.2–2.6s)：pink 2px 横向分隔线从左向右 **SVG self-draw** (`svg-path-draw`) 绘出，宽度 80%，居中。
Scene 4 (2.6–4.0s)：下半区：经济学（谋生）块——JetBrains Mono label "CAREER" ink 大写先入；Source Serif 4 headline-xl "经济学" ink，**slide-down** 入场（3D rotationY +8deg→0）。占下部 ~35% 高度。两块同时可见，视觉上对称张力。
Scene 5 (4.0–5.0s)：底部注释行 "2019年，不敢把爱好当饭吃" Source Serif 4 body 400 ink，**per-word staggered reveal**（smooth 0.15s 间隔）；held read，**subtle jitter** on pink 分隔线保持 alive（低振幅）。

narrativeRole: 建立起点的矛盾——大多数人的共同困境：不敢把爱好当主旋律。
keyMessage: 绝大部分人只能在主流叙述中开辟一点点自己的空间。

---

## Frame 4 — 转机 · 草台班子的信念

- scene: 深绿底色，屏幕中央大字引言："如果世界是个草台班子呢？" 下方小字：某个普通的夜晚，在喘息时间里积累出的力量
- voiceover: ""
- duration: 5s
- transition_in: crossfade
- poster: 3s
- status: outline
- src: compositions/frames/04-belief.html
- type: feature_showcase
- persuasion: Visceral metaphor（草台班子这个意象让抽象的"信念"变得可感知、可笑、可共鸣）
- beat: 惊喜 + 解放感
- blueprint: kinetic-type-beats (Adapt)
- focal: 引言 "如果世界是个草台班子呢？"
- roles: 引言 = foreground subject（display scale，pink）· 上下引号装饰 = supporting · green 背景 = background（green `#2e4a2a` 全出血）

Adapt：保留 kinetic-type-beats 「spring-pop payoff」签名动作，改成单句引言的逐词揭示 + 最后 spring-pop 整句落定。green 背景是 editorial-forest「重量/宣言」帧的标准配置。

Scene 1 (0.0–0.8s)：green 全出血背景；topbar（mono "BELIEF · 04" cream/pink）per-word staggered reveal 淡入。大留白。
Scene 2 (0.8–3.0s)：引言 "如果世界是个草台班子呢？" Source Serif 4 headline-xl 500 pink，分两行，居中（y≈0.38×高）；**per-word staggered reveal**（0.22s 间隔，power3 smooth）——每个词按 beat 落下，最后一个「呢」+ 问号一起 spring-pop (`spring-pop-entrance`，smooth，无过冲）落定。字块占 ~60% 宽度。
Scene 3 (3.0–4.2s)：下方注释 "某个普通的夜晚 · 喘息时间里积累的力量" JetBrains Mono label 500 cream 大写，**per-word staggered reveal**（0.15s 间隔）从引言底部 1.5 行距处浮起入场。layered-depth，3 层（背景 / 引言 / 注释）。
Scene 4 (4.2–5.0s)：held read；**subtle jitter** on 引言文字（sine-wave-loop 低振幅）；背景静止。

narrativeRole: 内心转折点——一句话成为支撑转向的信念。
keyMessage: 普通人也只能这么相信：世界也许没那么难攻克。

---

## Frame 5 — 行动 · INTP 的计算与苦学年

- scene: 一个计算公式："大学4年 ÷ 4 = 1年" 配文字"用四分之一时间备战秋招"，下方"咖啡馆 · 海德格尔 · 代码 · 一升咖啡"四个标签逐一出现
- voiceover: ""
- duration: 6s
- transition_in: push-slide RIGHT
- poster: 4s
- status: outline
- src: compositions/frames/05-action.html
- type: feature_showcase
- persuasion: Concretization（把抽象的"努力"变成一个具体的时间计算，让行动有了数学依据）
- beat: 理解 + 愉快
- blueprint: grid-card-assemble (Adapt)
- focal: 计算公式 "4年 ÷ 4 = 1年"
- roles: 公式 = foreground subject（display scale，green on cream）· 四个标签卡片 = supporting（grid staggered assemble）· cream 背景 = background

Adapt：保留 grid-card-assemble 「staggered cascade assemble」签名动作用于四个标签；公式作为 hero 先入场，标签随后 cascade assemble 在公式下方。

Scene 1 (0.0–0.8s)：cream 背景；topbar（mono "ACTION · 05" green）per-word staggered reveal 淡入。
Scene 2 (0.8–2.5s)：公式分两步入场，rule-of-thirds 偏上（y≈0.32×高）：
  (a) "大学 4 年 ÷ 4" Source Serif 4 headline 500 green，**per-word staggered reveal**（0.2s 间隔）；
  (b) 等号 + "1年" 以 display-hero pink，spring-pop entrance 落定——这是公式的 payoff 节点。公式整体宽约 70%，居中。
Scene 3 (2.5–3.5s)：公式下方 1 行距，一行注释 "用四分之一时间备战秋招" Source Serif 4 body 400 ink，**per-word staggered reveal**（0.15s 间隔）。
Scene 4 (3.5–5.5s)：注释下方四个标签 tile（按 frame.md topic-tile 样式，6px radius，rotating fills：green/pink/green-lite/cream-2+border）通过 **staggered cascade assemble**（每隔 0.4s 一张，从中心向下 expand，smooth power3）依次出现：咖啡馆 / 海德格尔 / 代码 / 一升咖啡。四张 tile 2×2 排列，各带 JetBrains Mono caption-mono 标题。整体 centered，4 depth layers。
Scene 5 (5.5–6.0s)：held read，四个 tile 全部可见；**subtle jitter** on pink "1年" 字；其余静止。

narrativeRole: 展示行动策略——并不苦，甚至是给 INTP 爽完了的状态。
keyMessage: 用一年（本科四分之一）系统备战，极限但合理。

---

## Frame 6 — 收获 · 黑客松到大厂

- scene: 时间轴：半年自学 → 黑客松 → 实习 offer → 上岸大厂，时间轴从上到下展开，每个节点依次点亮
- voiceover: ""
- duration: 5s
- transition_in: push-slide RIGHT
- poster: 3s
- status: outline
- src: compositions/frames/06-result.html
- type: social_proof
- persuasion: Causal chain（A→B→C 因果链展示：自学→黑客松→Offer）
- beat: 惊喜 + 振奋
- blueprint: spatial-pan-stations (Adapt)
- focal: 四节点时间轴（竖版）
- roles: 时间轴线 = foreground subject · 节点圆圈+标签 = supporting（逐一点亮）· cream 背景 = background

Adapt：保留 spatial-pan-stations 「camera panning through labeled stations」签名——竖版改为静态竖向时间轴（宽版横向 pan 不适合 9:16），用节点逐一点亮替代 pan；保留「依次 reveal 每个 station + 最后 held on final」结构。

Scene 1 (0.0–0.8s)：cream 背景；topbar（mono "RESULT · 06" green）per-word staggered reveal 淡入；垂直时间轴主线（2px green 竖线）从屏幕上方 **SVG self-draw** 向下延伸，占画面中心略偏左，高度约 60%。
Scene 2 (0.8–2.8s)：四个节点依次从上到下 **spring-pop entrance**（每隔 0.45s），每节点：pink 圆圈（12px）+ JetBrains Mono label 绿色大写 + Source Serif 4 body 描述文字，从时间轴右侧 slide-in：
  ① "半年自学" → ② "黑客松" → ③ "实习 Offer" → ④ "上岸大厂"
Scene 3 (2.8–4.2s)：第四节点「上岸大厂」入场后，该节点 pink 圆圈做 **ambient glow bloom**（`ambient-glow-bloom`）——扩散光晕 0.6s；同时 "上岸大厂" 标签 keyword glow (`asr-keyword-glow`) 闪亮一次落定。bottom 诚实注释 "运气太好了 · 好导师 · 缓冲期" JetBrains Mono caption-mono ink，per-word staggered reveal。
Scene 4 (4.2–5.0s)：held read；所有节点可见；**subtle jitter** on pink 圆圈（sine-wave-loop 低振幅）。

narrativeRole: 验证行动有效——但立刻加上"运气好"的诚实前缀，避免鸡汤。
keyMessage: 如果有自己想做的事情，一定不要犹豫，果断去尝试。

---

## Frame 7 — 独立开发 · 真的很难

- scene: 屏幕中央大字："独立开发是真的难" 下方四个标签同时涌现：设计 / 代码 / 营销 / 增长，每个带一个感叹号
- voiceover: ""
- duration: 5s
- transition_in: cut
- poster: 3s
- status: outline
- src: compositions/frames/07-indie-hard.html
- type: pain_point
- persuasion: Enumeration（设计·代码·营销·增长四项并列，用密度感制造真实的辛苦感）
- beat: 共鸣 + 坦诚
- blueprint: grid-card-assemble (Adapt)
- focal: "独立开发是真的难"
- roles: 主标题 = foreground subject · 四个 tile（设计/代码/营销/增长）= supporting · cream 背景 = background

Adapt：grid-card-assemble 签名（staggered cascade assemble）用于四个难点 tile；主标题先于 tile 入场。cream 底，因为是坦诚/内省帧，绿底留给宣言帧。

Scene 1 (0.0–0.8s)：cream 背景；topbar（mono "INDIE DEV · 07" green）per-word staggered reveal 淡入。
Scene 2 (0.8–2.5s)：主标题 "独立开发是真的难" Source Serif 4 headline-xl 500 green，居中（y≈0.38×高），**per-word staggered reveal**（0.2s 间隔，power3）；"真的难" 三字以 pink 色强调，spring-pop entrance 落定（签名）。宽约 80%。
Scene 3 (2.5–4.5s)：主标题下方 2 行距，四个 tile（step-tile 样式，8px radius，各一种 fill：green/pink/green-lite/cream-2+border）通过 **staggered cascade assemble** 逐一出现（0.35s 间隔）：
  ① 设计 ② 代码 ③ 营销 ④ 增长，每 tile 右上角带 JetBrains Mono "!" 标记。2×2 grid，居中，tile 宽约 38%，4 depth layers。
Scene 4 (4.5–5.0s)：held read；**subtle jitter** on pink "真的难" 三字；tile 静止。

narrativeRole: 诚实的感悟一——独立开发的全栈难度，消解"成功鸡汤"的风险。
keyMessage: 独立开发要扛所有事，不是 influencer × builder 就很难跑出来。

---

## Frame 8 — 机会 · 个人开发者仍有机会

- scene: 上下对比：上方"大厂"（复杂/迟缓），下方"个人开发者"（灵活/快），中间 pink 分隔线，底部「煮理人」app 名
- voiceover: ""
- duration: 5s
- transition_in: crossfade
- poster: 3s
- status: outline
- src: compositions/frames/08-opportunity.html
- type: benefit_highlight
- persuasion: Contrast（大厂 vs 个人开发者的对比，用结构性弱点找到机会点）
- beat: 希望 + 分析性满足
- blueprint: comparison-split (Adapt)
- focal: 下方"个人开发者 · 有机会"
- roles: 上块（大厂）= supporting（ink/dim）· 下块（个人开发者）= foreground subject（green, bright）· pink 分隔线 = accent · cream 背景 = background

Adapt：comparison-split 签名「mirrored book-open tilts」改为上下 stack（竖版），上块倾斜 -6deg→0 slide-down，下块 +6deg→0 slide-up；保留「opposing tilts + pill badge spring-pop」签名节点。

Scene 1 (0.0–0.8s)：cream 背景；topbar（mono "OPPORTUNITY · 08" green）per-word staggered reveal 淡入。
Scene 2 (0.8–2.0s)：上半区——大厂块；JetBrains Mono label "BIG TECH" ink 大写先入；"复杂 · 迟缓" Source Serif 4 headline ink，从上方 **slide-down**（3D rotationY -6deg→0，smooth power3）入场，带灰色 dim overlay（opacity 0.6），暗示"沉重"。占上部约 28% 高度。
Scene 3 (2.0–2.5s)：pink 2px 横向分隔线 **SVG self-draw** 绘出，80% 宽居中。
Scene 4 (2.5–4.0s)：下半区——个人开发者块；JetBrains Mono label "INDIE DEV" green 大写先入；"灵活 · 有机会" Source Serif 4 headline-xl 500 green，从下方 **slide-up**（3D rotationY +6deg→0）入场，full brightness；右侧 pink pill badge "有机会" **spring-pop entrance**（签名）。占下部约 30% 高度。
Scene 5 (4.0–5.0s)：底部注释 "「煮理人」— 把视频菜谱变成文字步骤" JetBrains Mono caption-mono ink，**per-word staggered reveal**；held read，**subtle jitter** on pink pill badge。

narrativeRole: 感悟二——在大厂行动迟缓的地方，个人开发者有机会。
keyMessage: 大厂在细分垂类上要么复杂要么迟缓——个人开发者依然有机会。

---

## Frame 9 — 现状 · 遍地开花的道路

- scene: 竖排标签从上到下逐一浮现：内容 · 设计 · 代码 · 增长 · 大厂工作，配底部文字"被迫走向遍地开花的道路"
- voiceover: ""
- duration: 5s
- transition_in: push-slide UP
- poster: 3s
- status: outline
- src: compositions/frames/09-now.html
- type: branding
- persuasion: Distillation（把复杂的现状压缩成一句话：遍地开花）
- beat: 真实感 + 充实
- blueprint: kinetic-type-beats (Adapt)
- focal: 底部宣言 "遍地开花的道路"
- roles: 五个标签流 = supporting（逐一下行 reveal）· 宣言句 = foreground subject（display, pink on green）· green 背景 = background（green 全出血，宣言/哲学帧）

Adapt：kinetic-type-beats 签名「spring-pop payoff」用于最后宣言句的落定；前五个标签做 per-word sequential reveal 作为 build。green 底，宣言帧。

Scene 1 (0.0–0.8s)：green 全出血背景；topbar（mono "NOW · 09" cream）per-word staggered reveal 淡入。
Scene 2 (0.8–3.5s)：五个标签从画面上方（y≈0.25×高）依次向下 **per-word staggered reveal**（每隔 0.5s 一个），居中单列，Source Serif 4 body 500 cream：
  内容 / 设计 / 代码 / 增长 / 大厂工作
  每个标签入场时左侧有 pink 圆点（4px）通过 spring-pop entrance 先弹出，再 reveal 文字。列表占约 40% 高度，centered。
Scene 3 (3.5–4.5s)：底部（y≈0.72×高）宣言句 "被迫走向遍地开花的道路" 分两行，Source Serif 4 headline 500 pink，**per-word staggered reveal** + 最后三字（遍地开花）**spring-pop entrance**（签名 payoff）。占约 25% 宽。
Scene 4 (4.5–5.0s)：held read；**subtle jitter** on "遍地开花" pink 字；其余静止。

narrativeRole: 现状的哲学定调——累但充实，漫游中找到自己的路。
keyMessage: 被迫走向遍地开花的道路，也是另一种丰盛。

---

## Frame 10 — 着陆 · 成为自己想成为的人

- scene: 深绿背景，居中大字两行："成为自己想成为的人 / 做自己想做的事" 下方署名 dreamer piggy · 2026，pink 细线分隔
- voiceover: ""
- duration: 5s
- transition_in: crossfade
- poster: 3s
- status: outline
- src: compositions/frames/10-landing.html
- type: cta
- persuasion: Callback（回调第一帧五次转向意象，给出正面答案）+ Generalization（个体经历升华为普遍原则）
- beat: 满足 + 感召（breather + 闭合帧，低运动量）
- blueprint: titlecard-reveal (Reproduce)
- focal: "成为自己想成为的人 · 做自己想做的事"
- roles: 两行宣言 = foreground subject（display, cream on green）· monogram circle = supporting（identity stamp）· green 背景 = background

Reproduce：titlecard-reveal 签名「one slide-up crossfade + still hold」；green 底是 editorial-forest「重量帧」的标准。

Scene 1 (0.0–1.0s)：green 全出血背景；topbar（mono "DREAMER PIGGY · 10" cream/pink）per-word staggered reveal 淡入；画面大留白，闭合感。
Scene 2 (1.0–2.8s)：两行宣言分两步 **slide-up crossfade**（titlecard 签名，一次性，smooth power3）：
  第一行 "成为自己想成为的人" Source Serif 4 headline-xl 500 cream，（1.0s 入场）；
  第二行 "做自己想做的事" 同体 pink，（1.6s 入场），错落感。居中（y≈0.40×高），占约 70% 宽。
Scene 3 (2.8–3.8s)：pink 2px 细线 **SVG self-draw** 在宣言下方绘出，80% 宽居中。
  署名 "dreamer piggy · 2026" JetBrains Mono caption-mono cream，**per-word staggered reveal**（0.15s 间隔）。
  右下角 monogram circle（130px，2px pink border，mono "DP"）**spring-pop entrance**。
Scene 4 (3.8–5.0s)：held read，**完全静止**——闭合帧，不加 jitter（刻意的静默感）；这是视频的最后落点。

narrativeRole: 全视频着陆——希望观众也能找到自己的轴心时期。
keyMessage: 顺利从"奥德赛时期"进入"成年期"，成为自己想成为的人。
