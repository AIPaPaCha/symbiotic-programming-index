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

| Stb Score | Grade | Meaning |
|-----------|-------|---------|
| ≥ 0.9 | **Pass** | Highly stable — safe for production workflows |
| 0.7–0.9 | **Conditional** | Moderately stable — acceptable with monitoring |
| < 0.7 | **Fail** | Unstable — not reliable for production use |

**Why CV?** The coefficient of variation normalises variance by the mean, making Stb comparable across workflows with different average quality levels. A workflow with mean Qc = 0.9 and std = 0.05 is more stable than one with mean Qc = 0.5 and std = 0.05, and CV captures this correctly.

---

## How to Measure Stb

### Minimal Protocol (Run-to-Run)

The simplest and most important Stb measurement. If a workflow is not stable run-to-run, nothing else matters.

1. Define a task with clear expected output and an automated Qc evaluation
2. Run the same prompt against the same model 5+ times (10 is preferable for statistical confidence)
3. Compute Qc for each run using the [Qc protocol](../qc/index.md)
4. Calculate: `Stb = 1 - (std(Qc_scores) / mean(Qc_scores))`

```python
import statistics

qc_scores = [0.82, 0.85, 0.79, 0.83, 0.81]
mean_qc = statistics.mean(qc_scores)
std_qc = statistics.stdev(qc_scores)
cv = std_qc / mean_qc
stb = 1 - cv

print(f"mean={mean_qc:.3f}, std={std_qc:.3f}, CV={cv:.3f}, Stb={stb:.3f}")
# mean=0.820, std=0.022, CV=0.027, Stb=0.973
```

### Extended Protocol (Cross-Model)

Measures how portable a workflow is across different LLMs. Essential when evaluating vendor-agnostic orchestration pipelines.

1. Select 3+ models (e.g., GPT-4o, Claude Sonnet 4, DeepSeek V3, Gemini 2.5 Pro)
2. Run the same task with each model (same prompt, same evaluation criteria)
3. Compute Qc for each model's output
4. Report: range, CV, and per-model scores
5. Flag any model where Qc drops below the Pass threshold (0.8)

```python
model_scores = {
    "GPT-4o": 0.84,
    "Claude Sonnet 4": 0.87,
    "DeepSeek V3": 0.79,
    "Gemini 2.5 Pro": 0.82,
}

values = list(model_scores.values())
mean_qc = statistics.mean(values)
std_qc = statistics.stdev(values)
cv = std_qc / mean_qc
stb_cross = 1 - cv

print(f"Cross-model Stb = {stb_cross:.3f}")
# Identifies DeepSeek V3 as the outlier — investigate prompt sensitivity
```

### Longitudinal Protocol (Version Drift)

Tracks quality stability over time as models are updated. This is the most operationally important protocol for production systems.

1. Maintain a benchmark task set (3–5 representative tasks with automated Qc evaluation)
2. Run the benchmark after each model version update
3. Track Qc trends over time — store results in a time-series database or CSV
4. Alert when Qc drops more than 10% from the previous version
5. Re-evaluate the workflow's prompt design if Stb degrades across versions

```bash
# Example: scheduled benchmark run (cron or CI/CD)
python run_stb_benchmark.py --model claude-sonnet-4 --tasks benchmark_set.json
# Outputs: stb_results/2026-04-06_claude-sonnet-4.json
```

### Session-to-Session Protocol

Measures whether conversation context affects output quality. Important for interactive (chat-based) workflows where prior context may influence results.

1. Start a fresh session (no prior context) for each run
2. Issue the same prompt in each session
3. Compute Qc for each output
4. Compare against run-to-run Stb — session-to-session Stb is typically lower due to the absence of prior context refinement

---

## Factors That Affect Stb

Understanding what causes instability helps you improve it:

| Factor | Effect on Stb | Mitigation |
|--------|--------------|------------|
| **Temperature** | Higher temperature → lower Stb | Use temperature 0 or near-0 for production workflows |
| **Prompt specificity** | Vague prompts → variable interpretation → lower Stb | Be precise: specify language, framework, patterns, constraints |
| **Task complexity** | Complex tasks have more degrees of freedom → lower Stb | Decompose into smaller, well-constrained sub-tasks |
| **Model version** | Major version changes can shift behaviour | Pin model versions; re-run benchmarks after updates |
| **Context window usage** | Different context → different outputs | Standardise system prompts and context |
| **Seed parameter** | If available, fixes the random seed | Use when reproducibility is critical (not all APIs support this) |

---

## Tool Ecosystem

SPI does not mandate specific tools. Here are common choices for Stb measurement (as of 2026):

| Purpose | Tools | Notes |
|---------|-------|-------|
| **Batch API calls** | OpenAI Batch API, Anthropic Message Batches, custom scripts | Run same prompt N times programmatically |
| **Qc evaluation** | pytest, Bandit, Flake8, interrogate (see [Qc tools](../qc/index.md#tool-ecosystem)) | Automate the Qc pipeline for each run |
| **Statistical analysis** | Python `statistics` module, NumPy, pandas | Compute CV, confidence intervals, trend analysis |
| **CI/CD integration** | GitHub Actions, GitLab CI, Jenkins | Schedule benchmark runs, alert on regression |
| **Time-series tracking** | CSV files, InfluxDB, Prometheus + Grafana | Store longitudinal results, visualise trends |
| **Experiment tracking** | MLflow, Weights & Biases, custom dashboards | Log parameters (model, temperature, prompt version) alongside Stb scores |

---

## Improving Stb

If Stb scores are low, these interventions typically help (in order of impact):

1. **Lower temperature.** The single most effective lever. Temperature 0 eliminates sampling randomness (though some APIs still show minor variation).
2. **Increase prompt specificity.** Constrain the degrees of freedom: specify function signatures, variable names, error handling patterns, and output format.
3. **Decompose the task.** Break large tasks into smaller, well-defined steps. Each step has fewer valid outputs, reducing variance.
4. **Pin model versions.** Use exact model identifiers (e.g., `claude-sonnet-4-20260514`) rather than aliases that auto-upgrade.
5. **Standardise context.** Use identical system prompts, few-shot examples, and conversation setup across runs.
6. **Add validators.** Post-generation checks (linters, type checkers, test suites) catch outlier outputs before they reach scoring — this does not improve generation stability but reduces the impact of instability.

---

## Why Stb Matters

Stb is the industrial counterpart to Qc. Quality measured once is anecdotal; quality measured repeatedly is evidence.

- **CI/CD integration** — Unstable workflows break pipelines unpredictably
- **Compliance** — Regulated industries require demonstrable reproducibility
- **Model migration** — When switching models or versions, Stb tells you if quality holds
- **Trust** — Teams will not adopt AI workflows they cannot rely on
- **Cost management** — Unstable workflows waste compute on re-runs and human review of failed outputs

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

**Interpretation:** Stb = 0.729 is a warning — this workflow is unreliable. You might get great results or terrible results depending on the run. Not suitable for production without significant prompt redesign and temperature reduction.

---

## Open Questions

- **Sample size guidance:** How many runs are needed for a statistically reliable Stb estimate? Preliminary analysis suggests 10+ for run-to-run, 3+ models for cross-model. Formal power analysis is pending.
- **Temperature–Stb curve:** What is the relationship between temperature settings and Stb across different models? Is there a "sweet spot" that balances creativity and stability?
- **Prompt engineering for Stb:** Which prompt design patterns most reliably improve Stb? Structured output formats, few-shot examples, and constraint specification are candidates.
- **Stb across task types:** Is Stb inherently lower for creative tasks (e.g., architecture design) than mechanical tasks (e.g., unit test generation)? How should scoring thresholds adapt?
- **Multi-agent Stb:** In pipelines with multiple AI agents, how does instability compound? Is the system Stb bounded by the least stable agent?

Contributions and experimental results welcome.
