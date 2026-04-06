# Code Quality (Qc)

**The foundational dimension.** Without quality, nothing else in SPI matters.

Qc answers one question: **Does this workflow produce industrial-grade software?**

---

## The Four Gates

Qc evaluates code across four gates. Every gate must pass — a single failure drags the entire score down.

### 1. Correctness — Does it work?

| What to check | Tools & signals |
|----------------|-----------------|
| Unit test pass rate | pytest, Jest, JUnit |
| Integration / E2E tests | Playwright, Cypress, Selenium |
| Build success | CI/CD pipeline status, compilation@k |
| Benchmark correctness | HumanEval+, LiveCodeBench, SWE-bench |

### 2. Efficiency — Is it fast enough?

| What to check | Tools & signals |
|----------------|-----------------|
| Runtime latency | Profiling, `time` command, benchmark suites |
| Throughput | Requests/second, items/second |
| Memory usage | `tracemalloc`, heap profiling, container metrics |
| Energy efficiency | Green software metrics (emerging) |

Normalise against targets: `E_metric = min(1, target / observed)` for latency/memory, `min(1, observed / target)` for throughput.

### 3. Security — Is it safe?

| What to check | Tools & signals |
|----------------|-----------------|
| Vulnerability detection | Bandit (Python), CodeQL, Semgrep |
| Dependency audit | `npm audit`, `pip-audit`, Snyk, Dependabot |
| License compliance | FOSSA, `license-checker` |
| Input validation | SAST scanners, manual review |

### 4. Conformance — Is it maintainable?

| What to check | Tools & signals |
|----------------|-----------------|
| Lint / style compliance | ESLint, Flake8, Prettier, `google-java-format` |
| Documentation coverage | Docstring coverage tools, `interrogate` (Python) |
| Framework idioms | Rule-based checks for Spring DI, React patterns, etc. |
| Architectural patterns | Caching, circuit breakers, graceful degradation |

---

## Scoring

Qc uses a **weighted harmonic mean** of the four gates:

$$
Qc \;=\; \Bigg(\sum_{j=1}^{4}\frac{\alpha_j}{Q_j+\epsilon}\Bigg)^{-1},\qquad
\sum_{j=1}^4 \alpha_j = 1,\;\alpha_j \ge 0
$$

where \(\epsilon\) is a small stability constant (e.g., \(10^{-6}\)) to avoid division by zero.

**Default weights:** 0.25 each (equal). Adjust for your domain:

- Academic prototypes → higher Correctness weight, lower Conformance
- Production systems → higher Security and Conformance
- Performance-critical → higher Efficiency

**Quality gates:**

| Score | Grade | Meaning |
|-------|-------|---------|
| ≥ 0.8 | **Pass** | Industrial-ready |
| 0.6–0.8 | **Conditional** | Needs targeted improvements |
| < 0.6 | **Fail** | Significant rework required |

**Why harmonic mean?** Because it enforces the *weakest-gate penalty*. Software that passes all tests but is riddled with CVEs scores poorly — exactly as it should. This mirrors real-world engineering acceptance: one failing gate invalidates the whole.

---

## How to Compute Qc (Minimal Protocol)

**Step 1: Set up a containerised environment.**
Use a minimal container (e.g., `python:3.12-slim`, `openjdk:21-jdk`) with pinned dependencies and fixed resource budgets (2 vCPU, 4–8 GB RAM).

**Step 2: Collect scores for each gate.**

```bash
# Correctness: run your test suite
pytest --tb=short -q  # record pass rate

# Efficiency: profile runtime
time python your_script.py  # compare against target

# Security: scan for vulnerabilities
bandit -r src/ -f json  # record finding count
pip-audit  # check dependencies

# Conformance: lint and check docs
flake8 src/  # record violation count
interrogate src/ -v  # docstring coverage
```

**Step 3: Normalise each gate to [0, 1].**

**Step 4: Compute Qc using the harmonic mean formula.**

All scores emit as structured JSON. A simple aggregator script (fewer than 50 lines of Python) can compute the final Qc.

---

## Sample Results

From the [Binary Calculator QC Sample](../../spi-examples/qc/):

| Version | Correctness | Efficiency | Security | Conformance | Qc | Grade |
|---------|-------------|------------|----------|-------------|-----|-------|
| Original | 1.000 | 0.993 | 0.800 | 0.667 | **0.841** | Pass |
| Flawed | 0.000 | 0.500 | 0.400 | 0.626 | **0.000** | Fail |

The flawed version scores 0.000 because Correctness = 0 — the harmonic mean ensures that a zero in any gate produces a zero overall.

---

## Worked Example: Scoring a Flask API

Suppose an AI-generated Flask REST API passes 8/8 tests, runs in 23ms (target 100ms), has 1 medium security finding (unsanitised input), and has 40% docstring coverage with clean lint.

```
Q_corr = 8/8                                       = 1.00
Q_eff  = min(1, 100/23)                             = 1.00
Q_sec  = 1.0 - (1 issue × 0.2 penalty)              = 0.80
Q_conf = harmonic_mean(lint=0.90, docs=0.40)         = 0.55

Qc = (0.25/1.00 + 0.25/1.00 + 0.25/0.80 + 0.25/0.55)^(-1)
   = 0.789 → Conditional Pass
```

The bottleneck is Conformance — specifically the missing docstrings. Adding them would push Q_conf above 0.8, which lifts Qc above the Pass threshold. This is exactly the kind of actionable insight Qc is designed to produce: it tells you *where* to improve, not just *whether* you passed.

---

## Tool Ecosystem

SPI does not mandate specific tools. Use whatever fits your stack. Here are common choices for each gate (as of 2026):

| Gate | Python | JavaScript/TypeScript | Java | Multi-language |
|------|--------|----------------------|------|----------------|
| **Correctness** | pytest, unittest | Jest, Vitest | JUnit 5, TestNG | SWE-bench, HumanEval+ |
| **Efficiency** | `time`, `tracemalloc`, py-spy | Lighthouse, `perf_hooks` | JMH, VisualVM | hyperfine, k6 |
| **Security** | Bandit, pip-audit, Semgrep | npm audit, ESLint-security | SpotBugs, OWASP dep-check | CodeQL, Snyk, Trivy |
| **Conformance** | Flake8, Ruff, interrogate | ESLint, Prettier, TypeDoc | Checkstyle, google-java-format | SonarQube |

---

## Studies

For the full theoretical foundations of Qc, including a deep reading of the 2025 Survey of 291 benchmarks (arXiv:2505.08903):

**[On Code Quality (Qc) as the Foundational Interface](./studies/qc_foundational_interface.md)** — Working paper (September 2025)
