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

| NLE Score | Grade | Meaning |
|-----------|-------|---------|
| ≥ 0.9 | **Pass** | Near-parity across languages — workflow is globally equitable |
| 0.7–0.9 | **Conditional** | Some language-dependent quality gaps — acceptable with awareness |
| < 0.7 | **Fail** | Significant quality loss in non-English workflows — English-biased |

**Why min/max ratio?** This metric directly captures the worst-case gap. A workflow that scores 0.95 in English but 0.60 in Arabic has NLE = 0.63 — the ratio immediately surfaces the disparity. Alternative metrics (e.g., mean Qc across languages) would mask this gap.

---

## How to Measure NLE

### Minimal Protocol (Cross-Lingual Qc)

The simplest NLE measurement: does the same task produce the same quality in different languages?

1. Select a coding task with clear expected output and an automated Qc evaluation
2. Write semantically equivalent prompts in 3+ languages (e.g., English, Chinese, Spanish)
3. Have native speakers verify that the prompts are semantically equivalent (not just machine-translated)
4. Run each prompt through the same AI workflow (same model, same temperature, same system prompt)
5. Compute Qc for each language's output using the [Qc protocol](../qc/index.md)
6. Calculate: `NLE = min(Qc) / max(Qc)`

```python
import statistics

qc_by_lang = {
    "English": 0.85,
    "Chinese (中文)": 0.78,
    "Spanish (Español)": 0.72,
}

nle = min(qc_by_lang.values()) / max(qc_by_lang.values())
print(f"NLE = {nle:.3f}")  # NLE = 0.847
```

### Extended Protocol (Multi-Family)

For rigorous assessment, test across language families to detect systematic biases:

1. Include languages from different families: Indo-European (English, Spanish, Hindi), Sino-Tibetan (Chinese), Semitic (Arabic), Japonic (Japanese), Koreanic (Korean), Turkic (Turkish)
2. Test with both native-speaker prompts and machine-translated prompts — report both NLE scores
3. Measure not just Qc but also HoR: does the AI require more prompting rounds in some languages to achieve the same quality?
4. Check conformance to locale-specific standards: variable naming in the user's preferred style, documentation in the prompt language, date/number formatting conventions

```python
qc_extended = {
    "English": 0.87,
    "Chinese (中文)": 0.82,
    "Spanish (Español)": 0.80,
    "Arabic (العربية)": 0.71,
    "Japanese (日本語)": 0.79,
    "Hindi (हिन्दी)": 0.68,
}

nle = min(qc_extended.values()) / max(qc_extended.values())
print(f"NLE = {nle:.3f}")  # NLE = 0.782

# Per-language gap analysis
max_qc = max(qc_extended.values())
for lang, qc in sorted(qc_extended.items(), key=lambda x: x[1]):
    gap = max_qc - qc
    print(f"  {lang}: Qc={qc:.2f}, gap={gap:.2f}")
```

### Semantic Drift Protocol

Measures whether *translation itself* introduces quality degradation, separate from the model's language capability:

1. Write a prompt in the primary language (e.g., English)
2. Have native speakers translate the prompt into each target language
3. Also machine-translate the English prompt into each target language
4. Run all versions (native + machine-translated) through the same workflow
5. Compare: if native-speaker prompts score higher than machine-translated prompts, semantic drift is the bottleneck — not the model's language capability

### Cultural Idiom Protocol

Tests whether the AI respects locale-specific conventions:

1. Define tasks that involve locale-sensitive elements: date formatting, currency, naming conventions, regulatory references, framework preferences
2. Prompt in the local language with implicit cultural context (e.g., "format the date" should produce DD/MM/YYYY in Europe, MM/DD/YYYY in the US, YYYY-MM-DD in ISO/East Asian contexts)
3. Score: does the AI output respect the cultural context, or does it default to US/English conventions?

---

## Factors That Affect NLE

| Factor | Effect on NLE | Mitigation |
|--------|--------------|------------|
| **Training data distribution** | Models trained predominantly on English data → lower quality for underrepresented languages | Choose models with strong multilingual training; test before committing |
| **Prompt complexity** | Complex, nuanced prompts degrade more in translation | Use simpler, more structured prompts for multilingual workflows |
| **Code-switching** | Mixing languages in a single prompt can confuse models | Keep prompts in a single language; if mixing is necessary, test the specific pattern |
| **Technical vocabulary** | Some languages lack established terms for programming concepts | Allow English technical terms within non-English prompts; test both approaches |
| **Model version** | Multilingual performance can shift between versions | Include NLE in version-drift benchmarks (see [Stb](../stb/index.md)) |
| **System prompt language** | System prompts in English + user prompts in other languages can create tension | Test with system prompts in both English and the target language |

---

## Tool Ecosystem

SPI does not mandate specific tools. Here are common choices for NLE measurement (as of 2026):

| Purpose | Tools | Notes |
|---------|-------|-------|
| **Prompt translation** | Native speakers (gold standard), DeepL, Google Translate | Machine translation is a useful baseline but not sufficient for rigorous NLE |
| **Semantic equivalence** | Back-translation check, bilingual reviewer | Verify translated prompts preserve meaning |
| **Qc evaluation** | Same as [Qc tools](../qc/index.md#tool-ecosystem) — applied per-language | Automate the Qc pipeline so it can run N times efficiently |
| **Batch execution** | OpenAI Batch API, Anthropic Message Batches, custom scripts | Run the same task across languages programmatically |
| **Statistical analysis** | Python `statistics`, NumPy, pandas | Compute NLE ratio, per-language gap analysis, confidence intervals |
| **Locale testing** | `locale` module (Python), ICU libraries, `Intl` (JavaScript) | Verify locale-specific formatting in AI outputs |
| **Multilingual benchmarks** | MultiPL-E, HumanEval-X, MBPP multilingual variants | Established benchmarks for cross-lingual code generation |

---

## Improving NLE

If NLE scores are low, these interventions typically help:

**Prompt-level:**

- Use structured, unambiguous prompt formats that translate well (numbered steps, explicit constraints, example inputs/outputs)
- Include code examples in the prompt — code is a universal language and anchors the AI's interpretation regardless of the natural language wrapper
- Allow English technical terms within non-English prompts rather than forcing translation of programming concepts

**Workflow-level:**

- Test your workflow in your target languages *before* deployment, not after
- Use a two-stage approach for multilingual teams: prompt in the developer's preferred language, then validate the output using the same automated Qc pipeline used for English
- Maintain a multilingual prompt library — pre-validated prompt templates in each target language

**Model selection:**

- Evaluate NLE across candidate models before choosing — multilingual performance varies significantly between models
- Consider models specifically trained for multilingual tasks (e.g., models with strong Chinese, Japanese, or Arabic benchmarks)
- Test with the specific languages your team uses, not just the common benchmark languages

---

## Why NLE Matters

AI coding tools are rapidly adopted worldwide, but most benchmarks and training data are English-dominated. This creates a systemic risk:

- **Educational equity** — Students in non-English-speaking countries deserve equally effective AI tutors. A 20% Qc gap between English and Hindi prompts means Indian CS students get a measurably worse learning experience.
- **Global workforce** — Development teams are multilingual; workflows must not degrade for non-English speakers. A Chinese developer prompting in Mandarin should not need to switch to English to get quality results.
- **Regulatory fairness** — Some jurisdictions may require AI tools to perform equitably across official languages. NLE provides the measurement framework for compliance.
- **Competitive advantage** — Organisations that optimise for NLE access a wider talent pool and serve diverse markets more effectively.

NLE is the societal horizon of SPI: it ensures that the benefits of symbiotic programming are not gatekept by language.

---

## Worked Example: Cross-Lingual Qc Comparison

A researcher tests the same task ("Build a function to validate email addresses with unit tests") in three languages:

```
English prompt → Qc = 0.85
  Correctness: 1.00 (all tests pass)
  Efficiency: 0.95 (fast regex-based validation)
  Security: 0.80 (handles injection, but no rate limiting)
  Conformance: 0.70 (good lint, partial docstrings)

Chinese prompt (中文) → Qc = 0.78
  Correctness: 0.90 (missed one edge case: punycode domains)
  Efficiency: 0.90 (similar approach)
  Security: 0.75 (same as English but variable names less clear)
  Conformance: 0.60 (docstrings in mixed Chinese/English)

Spanish prompt (Español) → Qc = 0.72
  Correctness: 0.80 (misinterpreted locale-specific email convention)
  Efficiency: 0.85 (slightly different approach, acceptable)
  Security: 0.70 (missed input validation edge case)
  Conformance: 0.55 (inconsistent naming, sparse documentation)

NLE = min(0.85, 0.78, 0.72) / max(0.85, 0.78, 0.72)
    = 0.72 / 0.85
    = 0.847
```

**Interpretation:** NLE = 0.847 is acceptable but shows a gap — the Spanish prompt produced noticeably lower quality. Investigating further: the AI misinterpreted a locale-specific email convention in the Spanish prompt, producing a validator that rejected valid `.es` domain patterns. The Chinese prompt lost quality mainly in conformance (mixed-language documentation).

This is exactly the kind of bias NLE is designed to detect: a workflow that appears robust in English but silently degrades for non-English-speaking developers.

---

## Open Questions

- **Language coverage:** How many languages must be tested for a representative NLE score? Testing every language is impractical. A minimum viable set might include one language from each major family (Indo-European, Sino-Tibetan, Semitic, Japonic, Koreanic, Dravidian).
- **Code-switching effects:** Many multilingual developers naturally mix languages (e.g., English technical terms in a Chinese prompt). Does this help or hurt Qc? Preliminary evidence is mixed.
- **Prompt design vs. model capability:** When NLE is low, how do you distinguish between "the prompt translates poorly" and "the model is weaker in this language"? The semantic drift protocol helps, but more systematic methods are needed.
- **NLE for non-Latin scripts:** Languages with non-Latin scripts (Arabic, Chinese, Korean, Hindi) may face additional challenges with code generation tools that expect Latin-based identifiers. How should NLE account for this?
- **Longitudinal NLE:** Are models becoming more or less equitable across languages over time? Tracking NLE alongside Stb's version-drift protocol could answer this.

Contributions, especially from non-English-speaking researchers and developers, are warmly welcome.
