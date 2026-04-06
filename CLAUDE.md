# CLAUDE.md — Project Guide for AI Assistants

## Project Identity

**Symbiotic Programming Index (SPI)** is a practical framework for measuring human–AI coding workflows. Authored by Charles Li, published at https://aipapacha.github.io/symbiotic-programming-index/ (repo: https://github.com/AIPaPaCha/symbiotic-programming-index).

SPI is a **meta-framework** that unifies existing benchmarks under a coherent, workflow-level evaluation model. The unit of analysis is the **workflow** (human–AI orchestration pipeline), not the model in isolation.

## Two Deliverables

1. **SPI_SCHEMA.md** — The agent-executable idea file. A single document any AI agent can consume to evaluate a workflow. This is the primary product.
2. **MkDocs site** — The readable guide explaining each dimension, providing depth, and hosting research studies. This supports the schema.

The schema is the tool. The site is the documentation.

## Core Thesis

Programming is shifting from **authorship** to **orchestration**. SPI provides the quantitative instrument to measure this shift.

## Five Dimensions (Priority Order)

1. **Qc (Code Quality)** — Foundation. Four industrial gates: Correctness, Efficiency, Security, Conformance. Weighted harmonic mean (weakest-gate penalty).
2. **HoR (Human-off Ratio)** — How far can the human step back? Must be read alongside Qc.
3. **Exp (AI Explainability)** — Can the AI explain its design choices? Complete.
4. **Stb (Stability)** — Reproducibility across runs, sessions, model versions. Complete.
5. **NLE (Natural Language Engagement)** — Cross-lingual robustness and global fairness. Complete.

**Groupings:** Qc+Stb = industrial foundation; HoR+Exp = academic/philosophical breakthrough; NLE = societal horizon.

## SPI Formula

```
SPI = w_Qc * Qc + w_HoR * HoR + w_Exp * Exp + w_Stb * Stb + w_NLE * NLE
where sum(w_i) = 1, w_i >= 0
```

Weights adapt by context (industry, education, research, equity) and by AI system scale (function → pipeline → multi-agent → AI tutor).

## Project Structure

```
/
  SPI_SCHEMA.md          — Agent-executable idea file (the primary product)
  CLAUDE.md              — This file (AI assistant guide)
  README.md              — Project overview and citation
  mkdocs.yml             — MkDocs Material configuration
  docs/
    index.md             — Practical guide (how to use SPI)
    qc/index.md          — Qc: four gates, scoring, tools, protocols
    qc/studies/          — Research papers (Qc foundational interface)
    hor/index.md         — HoR: metrics, scoring, interpretation
    exp/index.md         — Exp: rubric, assessment methods
    stb/index.md         — Stb: protocols, scoring
    nle/index.md         — NLE: cross-lingual testing, scoring
    methodology.md       — Shared experimental protocol (three-mode, logging, validation)
    licenses.md          — Dual license page
    images/              — SVG/PNG assets
    javascripts/         — MathJax configuration
  spi-examples/
    qc/                  — Binary Calculator QC sample implementation
  .github/workflows/
    pages.yml            — GitHub Actions: deploy to GitHub Pages
```

## Tech Stack

- **Documentation:** MkDocs with Material theme, GitHub Pages via Actions
- **Math rendering:** MathJax 3 (LaTeX via pymdownx.arithmatex)
- **Python:** 3.11 (CI), 3.12 (container examples)

## Development Status

- **Available:** SPI Schema (agent-executable evaluation framework)
- **Mature:** Qc dimension (framework, formulas, working paper, sample implementation)
- **Outlined:** HoR dimension (metrics, scoring, interpretation, open questions)
- **Complete:** Exp, Stb, NLE (rubrics, protocols, tool ecosystems, worked examples)
- **Planned:** Experiments, datasets, venue submissions

## Writing & Style Conventions

- **Operational first, theoretical second.** Lead with what to do and how; explain why afterwards.
- Academically rigorous but accessible — audience spans researchers, engineers, educators
- British-influenced academic English (e.g., "emphasise", "organisation")
- LaTeX via MathJax: `$$...$$` for display math, `\(...\)` for inline
- Dimension names always use their acronym: Qc, HoR, Exp, Stb, NLE
- The MkDocs dimension pages are the "guide"; theoretical papers live under Studies

## Key Commitments

- SPI evaluates **workflows**, not models in isolation
- The harmonic mean enforces the weakest-gate penalty: one failing gate invalidates quality
- HoR without Qc is the "illusion of autonomy" — always report them together
- The schema is the product; the site is the documentation
- In the agent era, share ideas (not code): the schema is an "idea file" any agent can execute

## Dual License

- **Code** (including examples): Apache-2.0
- **Documentation & research materials** (`/docs`): CC BY-NC 4.0

## Working with This Project

1. **Operational focus** — Everything should be practically implementable, not just theoretically elegant
2. **Maintain philosophical depth** — Theory supports practice; it lives in Studies, not in the way
3. **Coherence** — The five dimensions must be internally consistent and mutually reinforcing
4. **Respect the staircase** — Qc first; do not develop higher dimensions in ways that bypass foundational ones
5. **Reproducibility** — Prefer concrete protocols and measurable definitions over vague aspirations
6. **MkDocs compatibility** — All docs must render correctly with MkDocs Material
