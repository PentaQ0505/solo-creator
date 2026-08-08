# Solo Creator

[English](README_EN.md) | 中文

一个面向小红书与微信公众号的开源 AI 内容创作 Skill。它把 AI 变成内容策略师、主编、研究员、写作者与复盘助手，帮助个人创作者从真实素材出发，完成选题、写作、跨平台改编、内容库维护与复盘。

它不会承诺“爆款”，不会虚构经历、收入、用户或数据。核心目标是：在素材充足时放大真实价值，在缺少新素材时仍能稳定产出可信、有用、符合账号定位的内容。

## 能力

- 从笔记、截图、决策、失败记录和产品进展中提取可复用的内容原子
- 生成并评分选题，规划可持续的内容节奏
- 生成完整的小红书图文包：标题、封面、逐页文案、正文、标签与评论引导；在安装视觉引擎后可继续渲染 PNG/JPG
- 生成微信公众号文章：标题、摘要、结构、Markdown 正文、配图位置与封面方案；按需生成 21:9 头图与 1:1 分享封面
- 在小红书和公众号之间进行真正的内容改编，而不是机械扩写或压缩
- 在没有近期素材时，用受众问题、方法、公开案例、观点提案和常青内容持续创作
- 维护内容库，记录素材证据、使用历史和剩余衍生方向
- 根据真实数据复盘内容表现并提出下一轮实验
- 对个人事实、公开事实、推断和待确认观点进行分层，避免把 AI 生成内容伪装成亲身经历

## 工作模式

| 模式 | 适用情况 | 处理方式 |
| --- | --- | --- |
| 素材充足 | 有经历、笔记、截图、数据或草稿 | 提取冲突、证据和洞察，生成主内容与差异化衍生方向 |
| 素材较少 | 只有碎片，或有历史素材/内容库 | 重组为新问题、方法、决策框架或复盘，不伪装成新事件 |
| 定位驱动 | 没有可用个人素材 | 围绕受众问题、公开案例、常青教程或待确认观点创作 |

## 文件结构

```text
solo-creator/
├── SKILL.md
├── agents/openai.yaml
├── assets/icon.svg
├── scripts/visual_preflight.py
└── references/
    ├── automation.md
    ├── content-engine.md
    ├── creator-profile.md
    ├── output-contracts.md
    ├── quality-control.md
    ├── visual-production.md
    ├── wechat.md
    └── xiaohongshu.md
```

`SKILL.md` 是入口；`references/creator-profile.md` 是无个人信息的默认画像模板，可以直接修改为你的账号定位。

## 安装

### Codex

全局安装，适用于所有项目：

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/PentaQ0505/solo-creator.git ~/.agents/skills/solo-creator
```

仅安装到当前项目：

```bash
mkdir -p .agents/skills
git clone https://github.com/PentaQ0505/solo-creator.git .agents/skills/solo-creator
```

Codex 会从 `~/.agents/skills` 和项目内的 `.agents/skills` 发现 Skill。可输入 `$solo-creator` 显式调用。参见 [OpenAI 官方 Skill 文档](https://learn.chatgpt.com/docs/build-skills)。

### Claude Code

全局安装：

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/PentaQ0505/solo-creator.git ~/.claude/skills/solo-creator
```

仅安装到当前项目：

```bash
mkdir -p .claude/skills
git clone https://github.com/PentaQ0505/solo-creator.git .claude/skills/solo-creator
```

在 Claude Code 中使用 `/solo-creator` 调用。参见 [Claude Code 官方 Skill 文档](https://code.claude.com/docs/en/skills)。

### Cursor 与其他 Agent Skills 兼容工具

本仓库采用以 `SKILL.md` 为入口的 Agent Skills 结构。将整个仓库克隆或复制到工具支持的个人级或项目级 Skill 目录中；目录名保持为 `solo-creator`。Cursor 用户可参考 [Cursor Agent Skills 文档](https://cursor.com/docs/skills) 选择当前版本支持的安装位置。

## 可选视觉引擎

Solo Creator 负责编排内容和视觉生产，不内置或重新分发第三方模板。需要输出真实图片文件时，可以按任务调用以下独立项目：

| 项目 | 用途 | 集成方式 | 许可证说明 |
| --- | --- | --- | --- |
| [guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) | 小红书多页卡片、公众号 21:9 + 1:1 封面对、截图教程 | 外部 Agent Skill | AGPL-3.0；代码和模板不会复制进本 MIT 仓库 |
| [Kami](https://github.com/tw93/Kami) | 公众号视觉摘要、一页纸、产品说明、流程图 | 外部 Skill / Plugin | MIT；字体可能有独立条款 |
| [weizwz/cover](https://github.com/weizwz/cover) | 单张轻量封面 | 外部网页或本地 Next.js 应用 | MIT；它是封面应用，不是 Agent Skill，也没有文档化的 CLI/API |

通用 Agent 安装 Guizang：

```bash
npx skills add https://github.com/op7418/guizang-social-card-skill --skill guizang-social-card-skill
```

通用 Agent 安装 Kami：

```bash
npx skills add tw93/kami/plugins/kami -a universal -g -y
```

Cover 可以使用[在线版本](https://cover.weizwz.com)，也可以克隆原仓库本地运行。使用在线图片搜索时需按其说明配置 Unsplash access key。

检查当前机器能否发现视觉引擎：

```bash
python3 scripts/visual_preflight.py --json
```

宿主工具通过插件系统安装的引擎可能不会暴露文件路径；此时以宿主实际可调用的 Skill/Plugin 为准。

## 个性化

安装后，优先编辑 `references/creator-profile.md`：

1. 填写你的身份与长期目标。
2. 选择 2–4 个相互关联的内容支柱。
3. 描述目标读者、语气和不愿分享的边界。
4. 设置你能长期坚持的发布节奏。

也可以不改文件，直接在对话中告诉 Agent 新的定位；新指令会覆盖默认画像。

## 使用示例

### 1. 从真实素材生成小红书图文

```text
使用 $solo-creator。下面是我这周开发产品时的原始笔记，请提取最值得讲的冲突，生成一套 7 张小红书图文，并列出需要我确认的事实。
```

### 2. 没有新素材时保持输出

```text
使用 $solo-creator。我这周没有实质性进展。请不要编造开发日志，按照账号定位生成 10 个可信选题，评分后完成排名第一的小红书稿件。
```

### 3. 同一素材适配两个平台

```text
使用 $solo-creator。把这份产品验证记录分别做成小红书图文和微信公众号文章。两边共享同一个观点，但要按平台重新组织内容。
```

### 4. 复盘已发布内容

```text
使用 $solo-creator。根据我提供的曝光、收藏、评论和关注数据复盘最近 6 篇内容，标明哪些结论只是推断，并给出下一轮 3 个实验。
```

### 5. 建立内容库

```text
使用 $solo-creator。把这些零散笔记整理成内容库条目，标记证据、可公开边界、候选角度、已使用方向和剩余衍生内容。
```

### 6. 直接生成可分享图片

```text
使用 $solo-creator。把这篇内容做成 7 张可以直接发布的小红书图片。
先检查事实和卡片文案，再调用 Guizang 生成 1080×1440 PNG，
提供成图、总览图和素材来源记录；不要只给视觉建议。
```

## 设计原则

- 真实优先于戏剧性
- 证据优先于空泛观点
- 一个内容只解决一个核心读者问题
- 不把公开案例写成“我的经历”
- 自动化默认只生成草稿，未经确认不自动发布
- 请求图片时必须交付真实成图；如果外部引擎不可用，要明确说明，不能把提示词或 HTML 当成成图
- 先建立可持续系统，再追求偶发流量

## 许可证

[MIT License](LICENSE)
