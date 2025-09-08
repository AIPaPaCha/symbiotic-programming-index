---
title: Symbiotic Programming Index (SPI) — Documentation
version: 0.1
lang: en
---

# Symbiotic Programming Index (SPI)

## Why this project exists

The rise of large language models (LLMs) has unsettled one of the core assumptions of computer science:  
that programming is the act of human authorship, line by line, where logic and intention are painstakingly encoded into formal syntax.

Today, AI systems can generate entire modules, pipelines, even complete products.  
The human role is shifting: from writing code to orchestrating workflows, validating outputs, and safeguarding intent.

This transformation demands more than anecdotes or personal workflows.  
It requires a **reproducible, measurable framework** to capture the maturity and reliability of human–AI programming.  

This is why we created the **Symbiotic Programming Index (SPI)**.

---

## From Vibe Coding to SPI

The concept of **“vibe coding”** emerged as practitioners began to use AI not just as a snippet generator,  
but as a co-developer capable of sustaining multi-step orchestration.

- Humans act at the architectural and judgment level.  
- AI executes the majority of code generation, explanations, and validation.  
- The workflow becomes a rhythm: cache prompts, orchestrate multiple agents, validate results, and replay reliably.

But anecdotes are not enough. To move beyond intuition, vibe coding must be formalised.  
The next step is **measurement**: defining indices that make human–AI programming visible, testable, and comparable.

SPI is that framework.

---

## Why these five dimensions?

SPI initially defined **four core dimensions** to capture the paradigm shift:

1. **Code Quality (Qc)** — Accuracy and completeness of outputs across tests, CI/CD, and architecture.  
2. **Human-off Ratio (HoR)** — To what extent can humans “let go” while workflows remain accountable?  
3. **AI Explainability (Exp)** — Can AI coders explain their design choices intelligibly and pedagogically?  
4. **Stability (Stb)** — Do workflows reproduce across prompts, sessions, and model versions?  
5. **Natural Language Engagement (NLE)** — Ensuring orchestration works across languages and cultures, not just English.  
   Without this, AI programming risks creating new divides in global education and industry.

Together, these five dimensions offer both **technical depth** and **social breadth**:  
from unit tests and reproducibility, to pedagogy, professional identity, and global fairness.

---

## Priority and progression

The five dimensions are not flat; they form a **research staircase** — from practical foundations to deep societal impact:

1. **Qc (Code Quality)** → the entry point. Without quality, nothing else matters.  
2. **HoR (Human-off Ratio)** → once quality is stable, measure how far humans can step back.  
3. **Exp (AI Explainability)** → with reduced intervention, demand that AI explains itself in ways humans can trust and learn from.  
4. **Stb (Stability)** → the maturity test. Workflows must remain reproducible across runs, contexts, and model versions.  
5. **NLE (Natural Language Engagement)** → the highest peak. True symbiosis must work across languages and cultures, avoiding an English-only bottleneck.

In short:

- **Qc + Stb** are the **industrial foundation** — making workflows reliable and trustworthy.  
- **HoR + Exp** are the **academic and philosophical breakthrough** — redefining the engineer’s role and AI’s epistemic value.  
- **NLE** is the **societal horizon** — ensuring global fairness and inclusivity in AI programming.  

This priority structure also reflects **analysis difficulty and depth**:  
from QC (low difficulty, mid depth) → HoR (moderate) → Exp (higher) → Stb (very high) → NLE (extreme).  
The first three are “visible mountains,” while Stb and NLE are “peaks in the clouds.”


---

## 📐 SPI Formula (with NLE)

We define the **Symbiotic Programming Index (SPI)** as a weighted combination of five dimensions:

$$
SPI = w_{Qc}\,Qc \;+\; w_{HoR}\,HoR \;+\; w_{Exp}\,Exp \;+\; w_{Stb}\,Stb \;+\; w_{NLE}\,NLE,
\quad \text{s.t. } \sum w_i = 1,\; w_i \ge 0
$$

Where:

- **$Qc$** — *Code Quality*: accuracy, completeness, maintainability  
- **$HoR$** — *Human-off Ratio*: extent to which humans can “let go” while workflows remain accountable  
- **$Exp$** — *Explainability*: clarity and pedagogical value of AI’s self-explanations  
- **$Stb$** — *Stability*: reproducibility across runs, sessions, and model versions  
- **$NLE$** — *Natural Language Engagement*: the effect of language, wording, or cross-lingual variation on quality and explainability  

The **weights ($w_i$)** are adjustable depending on context:  
- **Industrial settings** may emphasise $Qc$ and $Stb$  
- **Education** may emphasise $Exp$ and $HoR$  
- **Global fairness** highlights $NLE$  

---


## What this documentation provides

This repository is structured to provide both **narrative** and **methodology**:

- **Drafts and Licenses**
  - [v0.1 Draft](./v_01.md) — snapshot of the original proposal
  - [License](./license.md) — sharing and citation rules

- **Dimensions**
  - [Code Quality (Qc)](./qc/index.md)
  - [Human-off Ratio (HoR)](./hor/index.md)
  - [AI Explainability (Exp)](./exp/index.md)
  - [Stability (Stb)](./stb/index.md)
  - [Natural Language Engagement (NLE)](./nle/index.md)


---

## Quick navigation

- **Getting started** → Begin with the [v0.1 Draft](./v_01.md)  
- **Research details** → Dive into [Methodology](./qc/methodology.md) and other dimension folders  
- **Community use** → Cite SPI, contribute references, or use datasets under the [License](./license.md)

---

## Enduring aim

SPI is not about faster coding.  
It is about **rethinking the nature of programming itself**:  

- From authorship to orchestration  
- From snippets to workflows  
- From isolated benchmarks to reproducible indices  

Our aim is to build a **visible, teachable, and reproducible foundation** for software engineering in the era of AI —  
a framework that can be tested, taught, and trusted.
