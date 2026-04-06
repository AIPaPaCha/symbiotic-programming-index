# Methodology

This page describes the shared experimental protocol for SPI research. All dimension-specific experiments follow this framework.

---

## Framing

Turn philosophy (authorship, agency, accountability) into **operational metrics** by testing workflows under controlled conditions.

## Hypotheses

1. Productivity requires **Stb** without sacrificing **Qc** — stability is not optional
2. Human role shifts to orchestration (higher HoR) if **Qc/Stb** hold and **Exp** is intelligible
3. Hybrid QA (AI checks + human oversight) outperforms both extremes (human-only and AI-only)
4. Prompting languages evolve into orchestration DSLs when **Exp/Stb** are strong

## Three-Mode Protocol

Every SPI experiment compares the same task across three workflow modes:

| Mode | Description | What it tests |
|------|-------------|---------------|
| **Human-only** | Traditional coding, no AI assistance | Baseline quality and effort |
| **AI-only** | Single-shot generation, minimal orchestration | Raw model capability |
| **Human–AI orchestrated** | Prompts, agents, validators, human review | Workflow effectiveness |

## Logging Requirements

For each task execution, capture:

- **Prompts** — exact instructions given to the AI
- **Outputs** — raw AI-generated code
- **Diffs** — human edits to AI output
- **Tests** — pass/fail results for each test case
- **Interventions** — human decisions, corrections, and clarifications
- **Timestamps** — for effort measurement (optional)

## Validation Strategies

| Strategy | Purpose | Method |
|----------|---------|--------|
| **Convergent validity** | Does SPI correlate with established metrics? | Compare SPI scores against defect density, productivity, cycle time |
| **Test–retest reliability** | Are results stable across runs? | Same task, same model, 5+ runs → measure Stb |
| **Cross-model generalisation** | Does the evaluation work across different LLMs? | Same task across GPT, Claude, DeepSeek, Gemini |

## Getting Started

If you want to run an SPI experiment:

1. Pick 3–5 representative coding tasks of varying complexity
2. Run each in all three modes (human-only, AI-only, orchestrated)
3. Log everything (prompts, outputs, diffs, tests)
4. Score all five dimensions using the [SPI Schema](https://github.com/AIPaPaCha/symbiotic-programming-index/blob/main/SPI_SCHEMA.md)
5. Analyse and share results

We welcome experiment logs, replications, and negative results. Open an issue or pull request on the [repository](https://github.com/AIPaPaCha/symbiotic-programming-index).
