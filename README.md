# Symbiotic Programming Index (SPI)

**A practical framework for measuring human–AI coding workflows.**

[**Online Guide**](https://aipapacha.github.io/symbiotic-programming-index/) · [**SPI Schema (Idea File)**](./SPI_SCHEMA.md)

---

## What is SPI?

SPI measures how effectively humans and AI collaborate to produce software. Unlike benchmarks that test models in isolation, SPI evaluates **workflows** — the orchestration pipelines of prompts, agents, validators, and human decisions.

SPI is distributed as an **idea file** ([`SPI_SCHEMA.md`](./SPI_SCHEMA.md)): hand it to any AI agent and ask it to evaluate your workflow. The agent will know what to measure, how to score, and what to recommend.

## Five Dimensions

| Dimension | Question | Status |
|-----------|----------|--------|
| **Qc** — Code Quality | Does the workflow produce software that works, performs, is secure, and follows conventions? | Mature |
| **HoR** — Human-off Ratio | How far can the human step back while maintaining quality? | Outlined |
| **Exp** — AI Explainability | Can the AI explain its design choices for trust and learning? | Complete |
| **Stb** — Stability | Are results reproducible across runs, sessions, and model versions? | Complete |
| **NLE** — Natural Language Engagement | Does the workflow remain effective across languages and cultures? | Complete |

## Quick Start

**Option 1: Give the schema to your AI agent**

Copy [`SPI_SCHEMA.md`](./SPI_SCHEMA.md) into your project or conversation context, then ask your agent: *"Evaluate my last coding session using SPI."*

**Option 2: Manual evaluation**

```bash
# 1. Run your tests → Correctness
pytest --tb=short -q

# 2. Scan for vulnerabilities → Security
bandit -r src/ -f json

# 3. Check code style → Conformance
flake8 src/
interrogate src/ -v   # docstring coverage

# 4. Count your prompts and edits → HoR
#    (manual: how many prompts, how many lines did you edit?)

# 5. Compute Qc (harmonic mean of the four gates)
#    Then compute SPI with your weight profile
```

**Option 3: Run the sample**

```bash
cd spi-examples/qc/binary_calculator_sample/
python run_demo.py
```

## The SPI Formula

```
SPI = w_Qc × Qc + w_HoR × HoR + w_Exp × Exp + w_Stb × Stb + w_NLE × NLE
```

Weights adapt to context: industry emphasises Qc + Stb, education emphasises HoR + Exp, global equity emphasises NLE. See the [schema](./SPI_SCHEMA.md) for weight profiles.

## Project Structure

```
SPI_SCHEMA.md         — The idea file (primary product — hand this to any AI agent)
CLAUDE.md             — Project guide for AI assistants
docs/                 — MkDocs site (the readable guide)
  index.md            — How to use SPI
  qc/                 — Code Quality: four gates, scoring, tools
  hor/                — Human-off Ratio: metrics, interpretation
  exp/                — AI Explainability: rubric, assessment
  stb/                — Stability: protocols, scoring
  nle/                — Natural Language Engagement: cross-lingual testing
  qc/studies/         — Research papers (theoretical foundations)
spi-examples/qc/      — Working Binary Calculator QC sample
```

## Why SPI?

Programming is shifting from **authorship** to **orchestration**. Every vendor will claim their AI coding workflow is "the best." SPI provides the reproducible yardstick to turn "best" into something measurable — for industry, education, and governance.

Inspired by the emerging practice of sharing idea files rather than finished applications (cf. Karpathy's LLM Wiki), SPI is a **meta-framework** distributed as a schema that any agent can execute. The schema is the tool; the MkDocs site is the documentation.

## Contributing

SPI is an open research project. Ways to contribute:

- Propose or replicate experiments; share results
- Improve methodology, metrics, or sample implementations
- Open an Issue to discuss new dimensions or applications
- Add references or related work

## Citation

```bibtex
@misc{spi2026,
  author       = {Charles Li and SPI Project Contributors},
  title        = {Symbiotic Programming Index (SPI): Measuring Human--AI
                  Co-Production in Software Engineering},
  year         = {2026},
  howpublished = {\url{https://github.com/AIPaPaCha/symbiotic-programming-index}},
  note         = {Version 0.2, Open Research Project}
}
```

## License

- **Code** (including examples): Apache-2.0 — see [LICENSE](./LICENSE)
- **Docs & research materials** (`/docs`): CC BY-NC 4.0 — see [LICENSE-CC-BY-4.0](./LICENSE-CC-BY-4.0)

## Contact

- **Author**: Charles Li
- **Email**: charles_lmq@outlook.com
