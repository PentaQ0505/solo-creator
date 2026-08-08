# Solo Creator

English | [中文](README.md)

An open-source AI content creation skill for Xiaohongshu and WeChat Official Accounts. It turns an AI agent into a content strategist, managing editor, researcher, writer, and reviewer for solo creators.

Solo Creator does not promise virality or fabricate experience, revenue, users, or metrics. Its goal is to amplify truthful source material when it exists and produce credible, useful, positioning-aligned content when recent material is limited.

## Capabilities

- Extract reusable content atoms from notes, screenshots, decisions, failed attempts, and product progress
- Generate, score, and rank distinct content angles
- Produce complete Xiaohongshu carousel packages and, with an installed visual engine, continue to rendered PNG/JPG assets
- Produce complete WeChat articles and optionally render coordinated 21:9 header and 1:1 share covers
- Adapt an idea between platforms instead of mechanically expanding or shortening it
- Create honest content during low-material periods using audience questions, methods, public cases, viewpoint proposals, and evergreen guides
- Maintain a content bank with evidence, usage history, and remaining derivatives
- Review performance from supplied metrics and propose the next experiments
- Separate personal facts, verified public facts, inferences, and opinions awaiting confirmation

## Production modes

| Mode | Use when | Approach |
| --- | --- | --- |
| Source-rich | You have experiences, notes, screenshots, metrics, or a draft | Extract tension, evidence, and insight; create a flagship piece and distinct derivatives |
| Source-light | You have fragments, older material, or content-bank entries | Reframe them as a new question, method, decision framework, or retrospective without presenting them as new events |
| Positioning-driven | No usable personal source exists | Build from audience problems, public cases, evergreen tutorials, or proposed viewpoints |

## Repository structure

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

`SKILL.md` is the entry point. `references/creator-profile.md` is a de-personalized default profile template that you can customize.

## Installation

### Codex

Install globally for all projects:

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/PentaQ0505/solo-creator.git ~/.agents/skills/solo-creator
```

Install for the current repository only:

```bash
mkdir -p .agents/skills
git clone https://github.com/PentaQ0505/solo-creator.git .agents/skills/solo-creator
```

Codex discovers skills in `~/.agents/skills` and repository-level `.agents/skills` directories. Invoke it explicitly with `$solo-creator`. See the [official OpenAI skill documentation](https://learn.chatgpt.com/docs/build-skills).

### Claude Code

Install globally:

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/PentaQ0505/solo-creator.git ~/.claude/skills/solo-creator
```

Install for the current project only:

```bash
mkdir -p .claude/skills
git clone https://github.com/PentaQ0505/solo-creator.git .claude/skills/solo-creator
```

Invoke it in Claude Code with `/solo-creator`. See the [official Claude Code skill documentation](https://code.claude.com/docs/en/skills).

### Cursor and other Agent Skills-compatible tools

This repository follows the Agent Skills structure with `SKILL.md` as its entry point. Clone or copy the entire repository into the personal or project skill directory supported by your tool, keeping the directory name `solo-creator`. Cursor users can consult the [Cursor Agent Skills documentation](https://cursor.com/docs/skills) for the location supported by their current version.

## Optional visual engines

Solo Creator orchestrates editorial and visual production without bundling or redistributing third-party templates. Install independent engines when you need actual image files:

| Project | Best for | Integration | License note |
| --- | --- | --- | --- |
| [guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) | Xiaohongshu carousels, coordinated WeChat cover pairs, screenshot tutorials | External Agent Skill | AGPL-3.0; its code and templates are not copied into this MIT repository |
| [Kami](https://github.com/tw93/Kami) | WeChat visual summaries, one-pagers, product explainers, process diagrams | External Skill/plugin | MIT; fonts can carry separate terms |
| [weizwz/cover](https://github.com/weizwz/cover) | A single lightweight cover | External hosted or local Next.js app | MIT; it is a web app, not an Agent Skill or documented CLI/API |

Install Guizang for a generic Agent Skills host:

```bash
npx skills add https://github.com/op7418/guizang-social-card-skill --skill guizang-social-card-skill
```

Install Kami for a generic Agent Skills host:

```bash
npx skills add tw93/kami/plugins/kami -a universal -g -y
```

Use the [hosted Cover app](https://cover.weizwz.com) or run its repository locally. Its image search requires an Unsplash access key configured according to that project.

Check filesystem-visible engines:

```bash
python3 scripts/visual_preflight.py --json
```

Host-managed plugins may be callable without exposing a filesystem path; prefer the host's actual Skill/plugin registry in that case.

## Personalization

After installation, edit `references/creator-profile.md` first:

1. Add your identity and long-term objective.
2. Choose two to four connected content pillars.
3. Define your audience, voice, and private boundaries.
4. Set a publishing cadence you can sustain.

You can also leave the file unchanged and provide a newer profile in the conversation. New user instructions override the defaults.

## Usage examples

### 1. Turn real source material into a Xiaohongshu carousel

```text
Use $solo-creator. Here are my raw notes from building a product this week. Find the strongest defensible tension, create a seven-card Xiaohongshu package, and list the facts I need to confirm.
```

### 2. Keep publishing without recent progress

```text
Use $solo-creator. I made no meaningful progress this week. Do not invent a build log. Generate ten credible ideas from my positioning, score them, and finish the top-ranked Xiaohongshu draft.
```

### 3. Adapt one source for two platforms

```text
Use $solo-creator. Turn this product-validation record into a Xiaohongshu carousel and a WeChat article. Keep one shared thesis, but rebuild the structure for each platform.
```

### 4. Review published content

```text
Use $solo-creator. Review my last six posts from the reach, saves, comments, and follower data I provide. Label inferred conclusions and propose three measurable experiments.
```

### 5. Build a content bank

```text
Use $solo-creator. Convert these fragments into content-bank entries with evidence, safe-to-share limits, candidate angles, used outputs, and remaining derivatives.
```

### 6. Render shareable images

```text
Use $solo-creator. Turn this article into seven publishable Xiaohongshu images.
Check the claims and card copy first, then use Guizang to render 1080×1440 PNGs.
Return the final images, a contact sheet, and asset-source records; do not stop at visual direction.
```

## Design principles

- Truth before drama
- Evidence before generic opinion
- One primary reader problem per piece
- Never turn a public case into “my experience”
- Automation remains draft-only unless publication is explicitly approved
- When image files are requested, deliver real renders or state the exact missing engine; never present prompts or HTML as completed images
- Build a sustainable system before optimizing for occasional spikes

## License

[MIT License](LICENSE)
