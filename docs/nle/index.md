# Natural Language Engagement (NLE)

**The societal dimension.** True symbiosis must not privilege English-only workflows. NLE measures whether human–AI coding collaboration remains effective across languages and cultures.

---

## What NLE Measures

| Metric | What it captures | How to test |
|--------|-----------------|-------------|
| **Cross-lingual Qc** | Does code quality hold when prompting in different languages? | Run same task in English, Chinese, Spanish, etc. → compare Qc |
| **Semantic drift** | Does translating the prompt change the output quality? | Compare outputs from semantically equivalent prompts in different languages |
| **Cultural idiom** | Does the AI handle locale-specific conventions? | Date formats, naming conventions, documentation language, local frameworks |

---

## Scoring

```
NLE = min(Qc_lang_i) / max(Qc_lang_i)   across tested languages
```

| NLE Score | Interpretation |
|-----------|---------------|
| ≥ 0.9 | Excellent — near-parity across languages |
| 0.7–0.9 | Acceptable — some language-dependent quality gaps |
| < 0.7 | English-biased — significant quality loss in non-English workflows |

---

## How to Measure NLE

**Minimal protocol:**

1. Select a coding task with clear expected output
2. Write semantically equivalent prompts in 3+ languages (e.g., English, Chinese, Spanish)
3. Run each prompt through the same AI workflow
4. Compute Qc for each language's output
5. Calculate: `NLE = min(Qc) / max(Qc)`

**Extended protocol:**

1. Include languages from different families (Indo-European, Sino-Tibetan, Semitic, etc.)
2. Test with both native speakers and machine-translated prompts
3. Measure not just Qc but also HoR — does the AI require more prompting in some languages?
4. Check conformance to locale-specific standards (e.g., documentation in the user's language)

---

## Why NLE Matters

AI coding tools are rapidly adopted worldwide, but most benchmarks and training data are English-dominated. This creates a systemic risk:

- **Educational equity** — Students in non-English-speaking countries deserve equally effective AI tutors
- **Global workforce** — Development teams are multilingual; workflows must not degrade for non-English speakers
- **Regulatory fairness** — Some jurisdictions may require AI tools to perform equitably across official languages

NLE is the societal horizon of SPI: it ensures that the benefits of symbiotic programming are not gatekept by language.

---

## Worked Example: Cross-Lingual Qc Comparison

A researcher tests the same task ("Build a function to validate email addresses with unit tests") in three languages:

```
English prompt → Qc = 0.85
Chinese prompt (中文) → Qc = 0.78
Spanish prompt (Español) → Qc = 0.72

NLE = min(0.85, 0.78, 0.72) / max(0.85, 0.78, 0.72)
    = 0.72 / 0.85
    = 0.847
```

**Interpretation:** NLE = 0.847 is acceptable but shows a gap — the Spanish prompt produced noticeably lower quality. Investigating further: the AI misinterpreted a locale-specific email convention in the Spanish prompt, producing a validator that rejected valid `.es` domain patterns.

This is exactly the kind of bias NLE is designed to detect: a workflow that appears robust in English but silently degrades for non-English-speaking developers.

---

## Status

!!! warning "Under Construction"
    NLE is the most ambitious SPI dimension and the least developed.
    Active research directions include:

    - Baseline NLE measurements across major AI coding models
    - The effect of code-switching (mixing languages in prompts) on quality
    - Cross-lingual prompt engineering strategies
    - Collaboration with multilingual developer communities for evaluation

Contributions, especially from non-English-speaking researchers and developers, are warmly welcome.
