# Stability (Stb)

**The maturity dimension.** A workflow that produces great results once but fails unpredictably on re-runs cannot be trusted for production.

Stb answers: **Are results reproducible across runs, sessions, and model versions?**

---

## What Stb Measures

| Metric | What it captures | How to test |
|--------|-----------------|-------------|
| **Run-to-run** | Same prompt + same model → consistent results? | Run 5+ times, measure Qc variance |
| **Session-to-session** | Same task in different conversation contexts → same quality? | New session each time, compare Qc |
| **Cross-model** | Same task across GPT, Claude, DeepSeek, Gemini → score divergence? | Benchmark across models |
| **Version drift** | Same task on model v1 vs. v2 → regression? | Re-run after model updates |

---

## Scoring

```
Stb = 1 - CV(Qc_scores)
```

where CV = coefficient of variation (standard deviation / mean) across repeated runs.

| Stb Score | Interpretation |
|-----------|---------------|
| ≥ 0.9 | Highly stable — safe for production workflows |
| 0.7–0.9 | Moderately stable — acceptable with monitoring |
| < 0.7 | Unstable — not reliable for production use |

---

## How to Measure Stb

**Minimal protocol (run-to-run):**

1. Define a task with clear expected output
2. Run the same prompt against the same model 5 times
3. Compute Qc for each run
4. Calculate: `Stb = 1 - (std(Qc_scores) / mean(Qc_scores))`

**Extended protocol (cross-model):**

1. Run the same task across 3+ models
2. Compute Qc for each
3. Report the range and CV across models
4. Flag any model where Qc drops below the threshold

**Longitudinal protocol (version drift):**

1. Maintain a benchmark task set
2. Re-run after each model version update
3. Track Qc trends over time
4. Alert when Qc drops more than 10% from the previous version

---

## Why Stb Matters

Stb is the industrial counterpart to Qc. Quality measured once is anecdotal; quality measured repeatedly is evidence.

- **CI/CD integration** — Unstable workflows break pipelines unpredictably
- **Compliance** — Regulated industries require demonstrable reproducibility
- **Model migration** — When switching models or versions, Stb tells you if quality holds
- **Trust** — Teams will not adopt AI workflows they cannot rely on

**Stb + Qc = the industrial foundation.** A workflow with high Qc but low Stb is a lucky run, not a reliable process.

---

## Worked Example: Run-to-Run Stability

A developer runs the same prompt ("Build a binary search in Python with edge case handling") five times with Claude Sonnet 4:

```
Run 1: Qc = 0.82  (all tests pass, minor lint issues)
Run 2: Qc = 0.85  (all tests pass, clean lint)
Run 3: Qc = 0.79  (1 edge case fails, otherwise clean)
Run 4: Qc = 0.83  (all tests pass, minor lint issues)
Run 5: Qc = 0.81  (all tests pass, minor security note)

mean = 0.82,  std = 0.020,  CV = 0.024
Stb = 1 - 0.024 = 0.976
```

**Interpretation:** Stb = 0.976 is excellent — the workflow is highly reproducible. The minor variance comes from the non-deterministic nature of LLM generation (temperature > 0), but quality stays consistently above the Pass threshold.

Now compare with an unstable workflow (poorly designed prompt, high temperature):

```
Run 1: Qc = 0.91
Run 2: Qc = 0.42
Run 3: Qc = 0.78
Run 4: Qc = 0.55
Run 5: Qc = 0.88

mean = 0.708,  std = 0.192,  CV = 0.271
Stb = 1 - 0.271 = 0.729
```

**Interpretation:** Stb = 0.729 is a warning — this workflow is unreliable. You might get great results or terrible results depending on the run. Not suitable for production.

---

## Status

!!! warning "Under Construction"
    Stb protocols are defined but not yet validated at scale.
    Active research directions include:

    - Establishing baseline Stb ranges for common AI coding tasks
    - Temperature and sampling parameter effects on Stb
    - Prompt engineering strategies that improve Stb
    - Longitudinal Stb tracking tooling

Contributions and experimental results welcome.
