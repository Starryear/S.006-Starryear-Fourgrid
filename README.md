<div align="center">

# 【S.006】Starryear-Fourgrid丨星年·四格

**一张照片，四次抵达。摄影证据、诗意提炼、节奏结构与抽象灵魂在同一画面中彼此生长。**

**One photograph, four arrivals—evidence, poetic distillation, rhythmic structure, and abstract soul.**

[![Codex Skill](https://img.shields.io/badge/Codex-Skill-111111?style=for-the-badge&logo=openai&logoColor=white)](./SKILL.md)
[![S.006](https://img.shields.io/badge/Starryear-S.006-D6A63B?style=for-the-badge)](https://starryear.github.io/S.006-Starryear-Fourgrid/)
[![Usage](https://img.shields.io/badge/Usage-Personal%20%26%20Non--commercial-EAE5DA?style=for-the-badge)](./LICENSE.md)
[![Language](https://img.shields.io/badge/中文-English-708C85?style=for-the-badge)](#english)

[专属网站](https://starryear.github.io/S.006-Starryear-Fourgrid/) · [安装 Skill](#作为-codex-skill-使用) · [直接使用提示词](#直接使用完整提示词)

</div>

---

> **仅限个人学习、非营利研究与非商业创作。**任何商业使用均须事先取得 Starryear年 的书面许可。分享作品时，欢迎注明来源并 **@Starryear年**。完整条款见 [LICENSE.md](./LICENSE.md)。

## 关于 S.006

Starryear-Fourgrid 是一套以单张摄影为唯一视觉证据的 2×2 转译方法。左上保留真实照片像素，右上凝缩诗意记忆，左下抽取结构节奏，右下释放抽象灵魂；一个来自原主体的中央线索穿越四格，使作品成为连续叙事，而非四种滤镜的并列。

- ✅ 原片证据被锁定，不重新生成左上格
- ✅ 色彩、形状、方向、节奏和超现实变化均可追溯至原图
- ✅ 同时提供可安装的 Codex Skill 与中英双语完整提示词
- ❌ 不生成通用水墨山水、无来源装饰、四张重复图或整图滤镜

## 两种路径，24 件作品

同一视觉命题分别通过完整提示词与 Codex Skill 运行。下方各展示 12 件经 Starryear年 认可的最终作品；它们是方法的证据，不是供模型照抄的模板。

| 完整提示词生成 · Direct Prompt | Skill 生成 · Codex Skill |
| :---: | :---: |
| ![Lotus Memory](assets/examples/prompt/s006-prompt-01-lotus-memory.webp) | ![Rain Walker](assets/examples/skill/s006-skill-01-rain-walker.webp) |
| ![Spider Lily](assets/examples/prompt/s006-prompt-02-spider-lily.webp) | ![Lotus Bloom](assets/examples/skill/s006-skill-02-lotus-bloom.webp) |
| ![Silent Stones](assets/examples/prompt/s006-prompt-03-silent-stones.webp) | ![Autumn Light](assets/examples/skill/s006-skill-03-autumn-light.webp) |
| ![White Tulips](assets/examples/prompt/s006-prompt-04-white-tulips.webp) | ![Yellow Surveillance](assets/examples/skill/s006-skill-04-yellow-surveillance.webp) |
| ![Skyward Bloom](assets/examples/prompt/s006-prompt-05-skyward-bloom.webp) | ![Pink Bloom](assets/examples/skill/s006-skill-05-pink-bloom.webp) |
| ![Waterlily Study A](assets/examples/prompt/s006-prompt-06-waterlily-study-a.webp) | ![Cockatoo](assets/examples/skill/s006-skill-06-cockatoo.webp) |
| ![Waterlily Study B](assets/examples/prompt/s006-prompt-07-waterlily-study-b.webp) | ![White Tulips](assets/examples/skill/s006-skill-07-white-tulips.webp) |
| ![Magnolia Blue](assets/examples/prompt/s006-prompt-08-magnolia-blue.webp) | ![Crows at the Waterline](assets/examples/skill/s006-skill-08-crows-at-waterline.webp) |
| ![Autumn Tower](assets/examples/prompt/s006-prompt-09-autumn-tower.webp) | ![Birds over Lake](assets/examples/skill/s006-skill-09-birds-over-lake.webp) |
| ![Pink Blossom](assets/examples/prompt/s006-prompt-10-pink-blossom.webp) | ![Red Koi](assets/examples/skill/s006-skill-10-red-koi.webp) |
| ![Ripple Through Green](assets/examples/prompt/s006-prompt-11-ripple-through-green.webp) | ![Magnolia Sky](assets/examples/skill/s006-skill-11-magnolia-sky.webp) |
| ![Birds and Distance](assets/examples/prompt/s006-prompt-12-birds-and-distance.webp) | ![Geese Ripple](assets/examples/skill/s006-skill-12-geese-ripple.webp) |

## 使用方法

### 作为 Codex Skill 使用

1. 下载本仓库，将文件夹命名为 `starryear-fourgrid`。
2. 把它放入 Codex skills 目录，例如 `~/.codex/skills/`。
3. 开启新对话，上传一张你拥有或获准使用的照片。
4. 输入：`使用 $starryear-fourgrid 把这张照片制作成星年·四格。`

Skill 将生成三个转译面板和一个中央连接母题，并把真实原片确定性拼入左上格，输出一张竖向 2:3 PNG。

### 直接使用完整提示词

| 语言 | Markdown | 纯文本 |
| :---: | :--- | :--- |
| 中文 | [完整提示词](references/starryear-fourgrid-prompt.zh-CN.md) | [复制友好版](prompts/Starryear-Fourgrid-完整提示词-中文.txt) |
| English | [Full prompt](references/starryear-fourgrid-prompt.en.md) | [Plain-text edition](prompts/Starryear-Fourgrid-Full-Prompt-English.txt) |

## 可调整参数

| 参数 | 可调整范围 |
| :--- | :--- |
| 源图适配 | 在关键证据不受损的前提下轻微裁切，或使用源图浅色补边 |
| 中央母题 | 调整方向、跨格位置和覆盖面积，通常保持总画布的 3%–8% |
| 材质强度 | 在精确墨线、干印残迹与透明彩墨之间微调 |
| 抽象程度 | 调整第二至第四格的辨识度递减速度，但保持统一视觉 DNA |
| 文字 | 默认无字；用户明确要求时再以确定性方式后期添加 |

## 不可改变的原则

1. **摄影证据锁定**：左上格只使用真实原图像素。
2. **转译可追溯**：每个重要形状、色彩与事件都来自原图事实。
3. **四态递进**：作品从可见事实逐步走向非写实表达。
4. **中央线索相连**：连接母题是材料转换的铰链，不是贴纸或第五格。

## 项目结构

```text
starryear-fourgrid/
├── README.md
├── LICENSE.md
├── SKILL.md
├── index.html
├── styles.css
├── script.js
├── agents/openai.yaml
├── assets/examples/
│   ├── prompt/            # 12 件提示词生成作品
│   └── skill/             # 12 件 Skill 生成作品
├── prompts/               # 中英文纯文本完整提示词
├── references/            # 完整规范、艺术方向与质量门槛
└── scripts/
    └── assemble_fourgrid.py
```

---

<a id="english"></a>

## English

Starryear-Fourgrid transforms one authorized photograph into a vertical 2×2 artwork. The upper-left panel preserves the source pixels; the other three panels move through poetic distillation, rhythmic structure, and abstract soul. A restrained, source-derived junction links the four states.

Use it as an installable [Codex Skill](./SKILL.md), or run the complete [English prompt](references/starryear-fourgrid-prompt.en.md) directly. The two galleries above contain twelve approved works from each route. They demonstrate the method but must never be reused as subject, palette, or composition templates.

Personal learning, non-profit research, and non-commercial creative use are permitted. Commercial use requires prior written authorization from Starryear年. See [LICENSE.md](./LICENSE.md).

<div align="center">

**S.006 is a milestone in the Starryear visual-skill archive.**

Authored by **Starryear年** · © 2026

</div>
