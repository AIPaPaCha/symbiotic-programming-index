# Symbiotic Programming Index (SPI)

**From Coding to Symbiosis: Redefining Software Engineering in the Age of AI**

---

## 🔍 What is SPI?

The **Symbiotic Programming Index (SPI)** is a research framework to **measure human–AI co-production in software engineering**.
Unlike benchmarks that test models in isolation, SPI evaluates **workflows** — pipelines where humans and AI collaborate to design, implement, and validate software.

SPI integrates **five measurable dimensions**:

* **Code Quality (Qc)** – Can AI-orchestrated workflows produce industrial-grade software?
* **Human-off Ratio (HoR)** – To what extent can humans “let go” while still ensuring accountability?
* **AI Explainability (Exp)** – Can AI coders explain their reasoning in trustworthy, pedagogical ways?
* **Stability (Stb)** – Are workflows reproducible across prompts, sessions, and model versions?
* **Natural Language Engagement (NLE)** – Does orchestration remain effective and fair across languages, cultures, and variations in wording?

Together, these dimensions provide a **quantitative lens** for the shift from programming as authorship to programming as **orchestration**.

---

## 🧭 Why SPI (and why now)?

With modern LLMs producing entire modules and pipelines, the developer’s role is moving from line-by-line authorship to **orchestrating** prompts, agents, and validators.
SPI turns that shift into **reproducible measurement** — so teams, educators, and researchers can **test, teach, and trust** AI-assisted programming.

For a deeper narrative and methods: see **[`/docs/en/index.md`](./docs/en/index.md)**.

---

## ⛰️ Priority & Progression

The five dimensions form a **research staircase** — from practical foundations to deep societal impact:

1. **Qc (Code Quality)** → the entry point; without quality, nothing else matters.
2. **HoR (Human-off Ratio)** → once quality is under control, measure how far humans can step back.
3. **Exp (Explainability)** → with reduced intervention, require AI to explain itself for trust and pedagogy.
4. **Stb (Stability)** → the maturity test: reproducibility across runs, contexts, and versions.
5. **NLE (Natural Language Engagement)** → the societal horizon: make symbiosis work across languages and cultures.

Rule of thumb:

* **Qc + Stb** = industrial foundation
* **HoR + Exp** = academic & pedagogical breakthrough
* **NLE** = global fairness & access

---

## 📐 SPI Formula (with NLE)

A weighted combination of the five dimensions:

$$
SPI = w_{Qc}\,Qc + w_{HoR}\,HoR + w_{Exp}\,Exp + w_{Stb}\,Stb + w_{NLE}\,NLE,
\quad \text{s.t. } \sum w_i = 1,\; w_i \ge 0
$$

**Contextual weighting examples**

* **Industry:** emphasize $Qc, Stb$
* **Education:** emphasize $Exp, HoR$
* **Global access:** emphasize $NLE$

---

## 🎯 Research Goals

1. Establish SPI as a **reproducible benchmark** for AI-assisted coding workflows.
2. Build datasets, taxonomies, and logging tools to capture orchestration traces.
3. Pilot SPI in **academic**, **industrial**, and **educational** contexts.
4. Ground the shift in a **philosophical foundation** for authorship, agency, and pedagogy.

---

**Quick links**

* Start here → [`/docs/en/index.md`](./docs/en/index.md)
* Draft snapshot → [`/docs/en/v0_1.md`](./docs/en/v0_1.md)
* Experiments → [`/docs/en/experiments/`](./docs/en/experiments/)
* Datasets → [`/docs/en/datasets/`](./docs/en/datasets/)

---

## 🌍 Why Public?

This repo is an **open lab notebook**. By documenting experiments and negative results alongside successes, we aim to accelerate collective learning across academia, industry, and open-source communities.

---

## 🤝 Contributing

SPI is an **open research project** — a living notebook that grows through shared ideas and experiments.

**Ways to contribute**

* 📖 Add references or related work (PRs welcome)
* 🧪 Propose or replicate experiments; share logs/results
* 🛠️ Improve methodology, metrics, or dataset design
* 💡 Open an Issue to discuss new dimensions or applications

Please keep contributions respectful, well-documented, and aligned with SPI’s **scientific and educational** goals.
Commercial forks are **not** allowed under our docs license.

---

## ✍️ Citation

If you use SPI ideas, metrics, or datasets, please cite as:

> **Charles Li and the SPI Project Contributors**,
> *Symbiotic Programming Index (SPI): Measuring Human–AI Co-Production in Software Engineering*, 2025.
> Available at: **[https://github.com/AIPaPaCha/symbiotic-programming-index](https://github.com/AIPaPaCha/symbiotic-programming-index)**

**BibTeX**

```bibtex
@misc{spi2025,
  author       = {Charles Li and SPI Project Contributors},
  title        = {Symbiotic Programming Index (SPI): Measuring Human--AI Co-Production in Software Engineering},
  year         = {2025},
  howpublished = {\url{https://github.com/AIPaPaCha/symbiotic-programming-index}},
  note         = {Version 0.1, Open Research Project}
}
```

---

## 📜 License

* **Code**: Apache-2.0 — see [`LICENSE`](./LICENSE)
* **Docs & research materials** (e.g., statements, methodology in `/docs`): **CC BY-NC 4.0** — see [`LICENSE-docs.md`](./LICENSE-docs.md)

This dual license lets **code be freely reused**, while keeping **research documents non-commercial**.

---

## 📬 Contact

For collaboration or inquiries:

* **Author**: Charles Li Mingqian
* **Email**: [charles\_lmq@outlook.com](mailto:charles_lmq@outlook.com)

---
