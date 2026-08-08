# Visual production

Use this workflow only when the user asks for rendered images, shareable cards, covers, a finished visual post, or image files. Copywriting requests can end with visual direction.

## Keep the integration boundary clear

Solo Creator is the editorial orchestrator. The visual engines remain independent projects and are not bundled:

| Engine | Best use | Integration form | License boundary |
| --- | --- | --- | --- |
| `guizang-social-card-skill` | Xiaohongshu carousels, coordinated WeChat 21:9 + 1:1 covers, screenshot-led tutorials | External Agent Skill | AGPL-3.0; do not copy templates, scripts, or adapted code into this MIT skill |
| `Kami` | WeChat visual summaries, one-pagers, process diagrams, research or product explainers | External Agent Skill/plugin | MIT code; fonts can have separate terms |
| `weizwz/cover` | One lightweight cover when a full card system is unnecessary | External web app or local Next.js app; it is not an Agent Skill | MIT code; external fonts and images retain their own terms |

Link to the original projects in user-facing installation notes. Never imply that Solo Creator owns or redistributes their code.

## Select one primary engine

Respect an engine explicitly requested by the user. Otherwise choose by deliverable:

1. Use Guizang for a Xiaohongshu carousel, a reusable visual series, screenshot-led tutorials, or coordinated Xiaohongshu and WeChat assets.
2. Use Kami for an editorial one-pager, structured article summary, product brief, process diagram, or information-dense explanatory image.
3. Use Cover for one simple cover that needs fast visual configuration but not a multi-card system.
4. Do not mix engines within one carousel. Combining engines is acceptable only across clearly different roles, such as Guizang cards plus a Kami one-page appendix.

For the default creator profile, prefer Swiss/IKB-like structured layouts for AI tools, product design, methods, and comparisons. Prefer restrained editorial layouts for personal observations, build stories, and reflective essays. Treat these as defaults, not invented personal preferences.

## Preflight the environment

1. If shell access exists, run `python3 scripts/visual_preflight.py --json` from this skill directory.
2. If the chosen engine is exposed through the host's skill/plugin system, use that installed capability even when the script cannot see its filesystem path.
3. Before invoking an external Skill, read its current `SKILL.md` completely and follow its required workflow. Do not reconstruct a stale copy of its instructions from this reference.
4. For Cover, use a local checkout or its hosted UI only when the host can control a browser or the user will complete the UI step. Do not invent a CLI or API.
5. If the chosen engine is unavailable, try another engine only when it genuinely fits the deliverable. Otherwise return the visual manifest and the exact installation or capability blocker.

Do not silently install external dependencies during an ordinary content request. Installation is allowed only when the user requests it or the host has an approved installation flow.

## Freeze copy before layout

Complete truth review and platform editing before rendering. Shorten text to fit the visual hierarchy; never shrink type until dense copy barely fits.

For every image, define:

- stable ID and posting order;
- platform and dimensions;
- page role such as cover, context, conflict, evidence, method, takeaway, or CTA;
- exact visible copy;
- visual source: user asset, verified screenshot, generated illustration, sourced image, diagram, table, or text-led layout;
- source path or URL where relevant;
- accessibility alt text;
- privacy or attribution note.

Save this as `visual-manifest.json` in the task output directory when files are being created. Use the following minimum shape:

```json
{
  "project": "short-slug",
  "platform": "xiaohongshu",
  "engine": "guizang-social-card-skill",
  "style": "swiss",
  "theme": "ikb",
  "items": [
    {
      "id": "01-cover",
      "order": 1,
      "width": 1080,
      "height": 1440,
      "role": "cover",
      "copy": {"title": "...", "body": "..."},
      "visual_source": {"type": "text-led", "path": null},
      "alt": "...",
      "notes": []
    }
  ]
}
```

## Invoke Guizang

Hand the approved platform copy and manifest to the installed `guizang-social-card-skill`.

- Xiaohongshu default: 1080×1440, 3:4, cards in final posting order.
- WeChat cover pair: 21:9 header plus 1:1 share card with the same visual identity.
- User assets take priority. Use generated or sourced imagery only when allowed and document every external source.
- Request a single-file HTML working artifact and rendered PNG outputs when supported by the current Guizang version.
- Preserve the engine's own style, theme, layout, validation, source-recording, and delivery rules.
- Do not copy Guizang templates or renderer code into Solo Creator outputs unless the user is working inside a separately licensed Guizang project.

## Invoke Kami

Hand Kami the approved content, intended audience, format, and output role.

- Use one-pager or long-document structures for WeChat summaries and downloadable explainers.
- Use its diagram system only when a diagram materially improves understanding.
- Request PNG for shareable images; PDF or HTML can be secondary artifacts.
- Keep Kami's fixed visual constraints unless the current installed version explicitly supports an override.
- Check the license of any bundled or downloaded font before commercial publication.

Kami is not the default carousel renderer. Do not force a report page into nine Xiaohongshu cards when Guizang is available.

## Invoke Cover

Cover is a configurable cover web application, not a callable Agent Skill.

- Use it for one cover, not for a multi-page narrative.
- Produce a cover brief containing title, subtitle, author/series label, ratio, layout, background mode, icon or image source, and export format.
- If a browser-capable host is available and the user's request authorizes creating the cover, configure the hosted or local app and export the image.
- If browser control is unavailable, return `cover-brief.json` and direct the user to the local or hosted app. Do not say the cover was generated.
- Unsplash search requires the app's configured access key. User-uploaded backgrounds and non-search themes may not.

## Render and inspect

1. Render into a task-specific output directory, never into the Skill directory.
2. Open or render every final image and inspect it visually.
3. Produce a contact sheet for multi-image sets when the engine does not already provide one.
4. Apply the visual checklist in `quality-control.md`.
5. Fix clipping, unreadable type, dense cards, inconsistent margins, repeated layouts, or title-content mismatch, then render again.
6. Return clickable files in posting order, followed by the contact sheet and source record.

An HTML template, design prompt, manifest, or cover brief is not a completed image deliverable. State exactly what exists.
