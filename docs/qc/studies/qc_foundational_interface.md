# SPI Working Paper Study: On Code Quality (Qc) as the Foundational Interface
*Author: Charles Li*  
*Date: September 2025*  
*License: CC-BY-SA 4.0*

## Changelog

**Version 1.1 (September 16, 2025)**
- Updated Appendix A to reference the working Binary Calculator QC Sample implementation
- Added concrete examples and live demonstration links
- Replaced theoretical "Lab Manual (coming soon)" with actual working code
- Aligned with the practical QC framework implementation in SPI examples

**Version 1.0 (September 2025)**
- Initial publication of the foundational QC interface study
- Established four-dimensional QC framework (Correctness, Efficiency, Security, Conformance)
- Defined harmonic mean scoring system and theoretical foundations  

## 1. Introduction

The evaluation of large language models (LLMs) for software engineering tasks has undergone **explosive expansion in recent years**. In *Assessing and Advancing Benchmarks for Evaluating Large Language Models in Software Engineering Tasks* (2025, arXiv:2505.08903v3, henceforth the **2025 Survey**), a total of **291 distinct benchmarks** have been systematically catalogued by June 2025, spanning requirements, design, coding assistants, testing, maintenance, AIOps, and quality management. As the authors emphasize:

> “**Benchmarks with real-world data… lead to more practical evaluations**” and “**future benchmarks must be designed to scale efficiently**” (2025 Survey).

The 2025 Survey further documents the acceleration of benchmark creation: “**Since 2022, the number of benchmarks has grown rapidly: 30 in 2022, 69 in 2023, 81 in 2024, and 42 already in the first half of 2025**.” This trajectory suggests that the field is not stabilizing but rather fragmenting further, with increasingly domain-specific benchmarks.

The authors also highlight both the **promise and the challenge** of this growth. On the one hand, new benchmarks “**help reduce the risk of data leakage and cover more diverse capabilities of LLMs**” (2025 Survey). On the other hand, the lack of unified standards is especially acute in requirements engineering, where “**challenges in creating a unified benchmark**” stem from varied templates, domain terminologies, and industrial confidentiality barriers.

Thus, while the 2025 Survey offers an invaluable **map of the current terrain**, it also implicitly raises a pressing question: with 291 benchmarks today, 2,910 tomorrow, and 20,000 in the foreseeable future, how can we extract a coherent measure that reflects **human–AI co-production workflows** rather than isolated task performance?

It is in response to this question—barely three months after the survey’s publication—that we revisit the **Symbiotic Programming Index (SPI)** framework. In SPI, **Code Quality (Qc)** is deliberately placed as the **first dimension**. This article explains why. Qc is not merely one metric among many; it is an **interface**—an abstraction through which thousands of fragmented benchmarks can be unified into a single, reproducible measure of whether a workflow is producing trustworthy, industrial-grade software.


---

## 2. Deep Reading of the 2025 Survey

### 2.1 Coding Assistant Benchmarks

Among the 291 benchmarks catalogued in the 2025 Survey, the **coding assistant** domain is by far the most densely populated, comprising **124 benchmarks**. The distribution itself is revealing: **102 benchmarks focus on code generation**, while smaller clusters target recommendation (11), summarization (11), translation (13), and reasoning (3). The authors stress that “**benchmarks in coding assistants are essential… enabling researchers to assess LLMs… in real-world scenarios**” (2025 Survey).

The coding assistant benchmarks are distinguished by their **metrics**, which align closely with software execution and usability:

* **Execution-based metrics** such as *pass\@k*, execution accuracy, and robust-pass (exemplified by HumanEval (Chen et al., 2021), MBPP (Austin et al., 2021), and APPS (Hendrycks et al., 2021), as well as newer datasets like EvalPlus and ReCode). The survey notes that “**execution-based metrics… assess practical usability and robustness**,” underscoring their centrality.
* **Compilation-based metrics**, including *compilation\@k* and build success rates (e.g., JavaBench (Cao et al., 2024)), which shift the evaluation beyond correctness of single functions toward engineering feasibility.
* **Repository-level metrics**, as in RepoExec (RepoExec, 2024), which measure functional correctness and dependency utilization. These metrics bring evaluation closer to the real-world scenario of integrating AI-generated code into existing systems.

In addition, the survey highlights the **evolution of granularity**: early benchmarks like HumanEval tested isolated functions, whereas recent ones such as SWE-bench (Jimenez et al., 2023), RepoBench, and JavaBench (Cao et al., 2024) extend evaluations to multi-file, repository-level, or even project-level correctness. This progression makes it clear that Qc must account not only for correctness in the small, but for **sustained quality across integrated systems**.

---

### 2.2 Requirements & Design Benchmarks

While smaller in number (**25 benchmarks**), the **requirements and design** category presents unique challenges. The 2025 Survey divides these into requirements acquisition, classification, ambiguity detection, and specification/verification tasks.

Representative examples include:

* **PROMISE NFR (2007)**: 625 requirement sentences categorized into functional vs. non-functional and NFR subcategories.
* **NFR-Review (2018)**: 1,278 user reviews (from iBooks, WhatsApp) annotated according to ISO/IEC 25010.
* **ReqEval (2020) and DAMIR (2022)**: targeting ambiguity and reference resolution in industrial requirements.
* **Jdoctor (2018) and DocTer (2022)**: focusing on extraction and generation of executable specifications, especially for JavaDoc and deep learning framework APIs.
* **SpecGenBench (2024) and SV-Benchmarks (SV-Benchmarks, ongoing)**: designed for formal specification generation and verification in Java and C.

The metrics in this domain are heterogeneous:

* **Classification tasks** rely on precision, recall, F1, and AUC.
* **Recommendation tasks** use MAP, MRR, and Precision\@k.
* **Generation and verification tasks** measure success rates, verifier calls, and formal specification validity.

The 2025 Survey cautions that “**challenges in creating a unified benchmark**” are particularly acute here, as requirements are highly context-dependent, with variations across industries and domains. Unlike code correctness, which admits a relatively objective measure (tests pass or fail), requirement interpretation inherently involves **semantic nuance** and **organizational conventions**.

This fragmentation directly motivates SPI’s abstraction strategy. Rather than attempting to resolve differences in terminology or templates, we treat all requirements-side benchmarks as evidence feeding into a higher-level dimension: **Can an AI coder, agent, multi-component pipeline (MCP), or any AI-orchestrated workflow reliably capture, disambiguate, and formalize human requirements into *verifiable specifications*?** Within the SPI framework, this foundational challenge is subsumed under **Code Quality (Qc)**.

---

### 2.3 Other Domains

The 2025 Survey also documents benchmarks for **software testing (25), maintenance (13), AIOps (6), and quality management (111)**. Although these are important, their methodological contribution overlaps significantly with those already discussed. Testing benchmarks extend execution-based metrics to mutation testing and fault detection. Maintenance benchmarks focus on bug localization and repair. AIOps benchmarks are still scarce but signal the growing need to measure operational quality in AI-driven environments. Quality management benchmarks often intersect with coding assistant metrics, emphasizing defect detection and software reliability.

From the SPI perspective, these domains are **supporting evidence**: they reinforce that regardless of task, the final question is always *does the software produced or modified meet quality standards?* In other words, they too collapse into Qc.

---

### 2.4 Key Insights from the 2025 Survey

Three insights emerge from a close reading:

1. **Execution is paramount**: The repeated emphasis that “execution-based metrics assess practical usability and robustness”(2025 Survey) demonstrates that correctness-in-use, not just correctness-in-theory, is what matters.
2. **Benchmarks will fragment endlessly**: With dozens of new benchmarks added each year, the proliferation will not slow down. The 2025 Survey shows the slope is steepening rather than flattening.
3. **A unifying abstraction is absent**: Especially in requirements and design, but also across coding and testing, there is no consensus framework to integrate disparate metrics.

Together, these insights reveal both the richness and the instability of the current evaluation landscape. If benchmarks continue to proliferate without abstraction, comparisons across tasks, languages, or workflows will remain incommensurable. This motivates the **Symbiotic Programming Index (SPI)** to treat **Code Quality (Qc)** as the first and foundational dimension—an *interface* through which thousands of fragmented metrics can be consistently translated into workflow-level assessment.

In the next section, we examine why Qc must come first in SPI, and how it functions as the ground truth upon which the other dimensions—Human-off Ratio, Explainability, and Stability—depend.

---

## 3. Why Qc Must Come First in SPI

Within the **Symbiotic Programming Index (SPI)**, we define five dimensions: **Code Quality (Qc), Human-off Ratio (HoR), Explainability (Exp), Stability (Stb), and Natural Language Engagement (NLE)**. Among these, **Qc** is deliberately positioned as the first and foundational dimension.

Qc is not a catch-all, but an **interface**. It condenses the vast proliferation of benchmarks—291 today, and potentially thousands more—into a set of coherent, workflow-level quality commitments. To function as such an interface, Qc must be carefully scoped: broad enough to capture industrial-grade software requirements, but precise enough not to absorb the mandates of the other four dimensions.

We argue that Qc is best represented by **four core sub-coefficients**: **Correctness, Efficiency, Security**, and **Conformance**. Together, they answer the practical engineering question: *can the code run, run fast, run safely, and run according to accepted practices?*

---

### 3.1 Correctness

Correctness is the most classical and non-negotiable component of Qc. It covers:

* **Execution accuracy** (*pass\@k, execution-based metrics, robust-pass*).
* **Compilation and build success** (compilation\@k, CI/CD pipeline reliability).
* **Repository-level correctness** (functional correctness and dependency utilization across multi-file projects).

The **2025 Survey** emphasizes that “**execution-based metrics… assess practical usability and robustness**,” directly aligning with this component. Correctness is therefore the *baseline contract* without which no workflow can be trusted.

---

### 3.2 Efficiency

Efficiency extends quality beyond mere correctness to the **resource profile of execution**. It includes:

* Runtime performance (latency, throughput).
* Resource consumption (memory, CPU).
* Emerging measures such as energy efficiency (green software).

The **2025 Survey** points to new benchmarks such as LiveCodeBench (LiveCodeBench, 2024), Mercury (Mercury, 2024), and EffiBench (EffiBench, 2024), which incorporate runtime and efficiency considerations. As systems scale, efficiency becomes not optional but integral to judging industrial-grade workflows.

---

### 3.3 Security

Security ensures that generated software is not only correct and efficient, but also resilient against known threats and compliant with dependency policies. Sub-factors include:

* Vulnerability detection (e.g., buffer overflows, injection attacks).
* Bug repair success rates.
* Dependency and version security.
* License and compliance checks.

Benchmarks like SecurityEval(SecurityEval, 2022) begin this work, but coverage remains uneven. SPI-Qc integrates security as a necessary coefficient, since software that passes tests but exposes vulnerabilities cannot be deemed of acceptable quality.

Related datasets such as Vul4J (Bui et al., 2022) extend this evaluation by providing reproducible Java vulnerabilities for program repair.

---

### 3.4 Conformance

Conformance addresses alignment with **software engineering norms and frameworks**. Unlike correctness or efficiency, it is not about whether the code runs, but *how* it is structured:

* **Lint and style adherence** (naming, formatting, static analysis).
* **Framework idioms** (e.g., Spring dependency injection, React component design, microservice layering).
* **Architectural compliance** (whether modules implement standard resilience mechanisms such as caching, circuit breakers, and graceful degradation).

This dimension is underrepresented in current benchmarks, but essential for bridging AI-generated code with industrial maintainability. As the 2025 Survey notes, “**human-in-the-loop evaluations are needed to assess alignment with good practices and user requirements**.” Qc must therefore incorporate conformance explicitly.

---

### 3.5 Evolutionary Adaptability (Extension Point)

A potential future extension of Qc is **evolutionary adaptability**—the capacity of generated code to sustain quality across iterations and requirement changes. This includes defect trend reduction, ease of extension, and maintainability under evolution.

However, evolutionary adaptability overlaps strongly with **Stability (Stb)** and possibly **Explainability (Exp)**. For now, we treat it not as a core Qc coefficient but as an **interface extension point**, to be refined in future research.

---


### 3.6 Synthesis

By defining Qc as the weighted harmonic mean of **Correctness, Efficiency, Security**, and **Conformance**, SPI provides a rigorous but bounded abstraction. Qc thereby remains **broad enough** to capture what “industrial-grade software” requires, yet **narrow enough** to avoid absorbing the mandates of Stability, Explainability, or NLE.

In essence, these four sub-coefficients represent the **four industrial gates of software quality**:

* **Correctness — the software must run.**
* **Efficiency — the software must run fast.**
* **Security — the software must run safely.**
* **Conformance — the software must run according to established engineering norms.**

Together, they form the uncompromising contract at the heart of SPI: *all workflows, no matter how varied in task or benchmark, are first judged by the test of quality*.

---

## 4. Towards a Formula for Qc

The overall Symbiotic Programming Index is a convex combination of five dimensions:

$$
\text{SPI}=\; w_{Qc}\,Qc + w_{HoR}\,HoR + w_{Exp}\,Exp + w_{Stb}\,Stb + w_{NLE}\,NLE,\quad
\text{s.t. } \sum_i w_i = 1,\; w_i \ge 0.
$$

Within SPI, **Qc** is the ground truth. We define Qc as a **weighted harmonic mean** of four sub-coefficients corresponding to the **four industrial gates of software quality** (Correctness, Efficiency, Security, Conformance). The harmonic mean enforces a “weakest-gate penalty” appropriate for engineering acceptance:

$$
Qc \;=\; \Bigg(\sum_{j=1}^{4}\frac{\alpha_j}{Q_j+\epsilon}\Bigg)^{-1},\qquad
\sum_{j=1}^4 \alpha_j = 1,\;\alpha_j \ge 0,
$$

where $\epsilon>0$ avoids division by zero.
**Note.** The exponent ${}^{-1}$ denotes “take the reciprocal” (i.e., a harmonic mean), ensuring that a low score in any single gate substantially lowers the overall $Qc$. This reflects industrial reality: software that fails to run, runs too slowly, is insecure, or violates engineering norms is not high-quality.

We instantiate the four gates as follows:

### 4.1 Sub-coefficients (measurable definitions)

#### (A) Correctness $\;Q_{\text{Corr}}$

Composite of execution, compilation/build, and repository-level functional criteria:

$$
Q_{\text{Corr}} \;=\; \Big(\tfrac{\beta_1}{\textsf{ExecPass}+\epsilon}+\tfrac{\beta_2}{\textsf{Compile}+\epsilon}+\tfrac{\beta_3}{\textsf{RepoExec}+\epsilon}\Big)^{-1},\;\sum\beta_i=1.
$$

* **ExecPass**: pass\@k / execution accuracy / robust-pass on standard tasks (e.g., HumanEval/MBPP/APPS/EvalPlus/ReCode). The survey classifies **execution-based metrics** (Pass\@k, Execution Accuracy, Robust Pass) as directly measuring **practical usability and robustness**.
* **Compile**: compilation\@k / build success (e.g., JavaBench (Cao et al., 2024) offers Completion@k, Compilation@k, Pass@k at repo level).
* **RepoExec**: repository/project-level functional correctness and **dependency utilization** (e.g., **RepoExec (RepoExec, 2024)**).

#### (B) Efficiency $\;Q_{\text{Eff}}$

Normalize runtime/footprint against targets; combine by harmonic mean:

$$
Q_{\text{Eff}} \;=\; \Big(\tfrac{\gamma_1}{E_{\text{lat}}+\epsilon}+\tfrac{\gamma_2}{E_{\text{thr}}+\epsilon}+\tfrac{\gamma_3}{E_{\text{mem}}+\epsilon}\Big)^{-1},\;\sum\gamma_i=1,
$$

with typical normalizations $E_{\text{lat}}=\min(1, T_{\text{target}}/T_{\text{obs}})$, $E_{\text{thr}}=\min(1, \text{Thr}_{\text{obs}}/\text{Thr}_{\text{target}})$, $E_{\text{mem}}=\min(1, M_{\text{target}}/M_{\text{obs}})$. The survey documents **LiveCode-Bench**, **Mercury**, and **EffiBench** (“Beyond Pass”, efficiency/time & memory units), and **PAREval** (speedup/efficiency\@k), evidencing feasible, performance-aware evaluation.

#### (C) Security $\;Q_{\text{Sec}}$

Fuse detection, repair, and dependency compliance:

$$
Q_{\text{Sec}} \;=\; \Big(\tfrac{\delta_1}{S_{\text{detect}}+\epsilon}+\tfrac{\delta_2}{S_{\text{repair}}+\epsilon}+\tfrac{\delta_3}{S_{\text{deps}}+\epsilon}\Big)^{-1},\;\sum\delta_i=1.
$$

* **Detection**: F1/Accuracy/MAP/MRR on vulnerability detection/localization (survey overviews Juliet/BigVul/VulEval/etc.).
* **Repair**: correctly-fixed/compilation-rate/plausibly-fixed (e.g., **Vul4J**, **VJBench**); **SecurityEval** targets prompt-based repair and secure completions.
* **Deps**: proportion of dependencies passing security/license checks (the survey’s limitations/opportunities sections call for going **beyond accuracy** to include **maintainability, performance, and security**).

#### (D) Conformance $\;Q_{\text{Conf}}$

Capture adherence to engineering norms and framework idioms:

$$
Q_{\text{Conf}} \;=\; \Big(\tfrac{\zeta_1}{C_{\text{lint}}+\epsilon}+\tfrac{\zeta_2}{C_{\text{idiom}}+\epsilon}+\tfrac{\zeta_3}{C_{\text{arch}}+\epsilon}\Big)^{-1},\;\sum\zeta_i=1,
$$

where $C_{\text{lint}}$ is lint/style pass rate; $C_{\text{idiom}}$ is framework-idiom coverage (e.g., Spring DI patterns, React component structure); $C_{\text{arch}}$ is architectural compliance (e.g., microservice **caching**, **circuit breakers**, **graceful degradation**). While underrepresented in current benchmarks, the survey explicitly advocates **human-in-the-loop** evaluations to judge alignment with **good practices and user requirements**, supporting the inclusion of conformance.

Finally, aggregate the four gates:

$$
Qc \;=\; \Big(\tfrac{\alpha_{\text{Corr}}}{Q_{\text{Corr}}+\epsilon}+\tfrac{\alpha_{\text{Eff}}}{Q_{\text{Eff}}+\epsilon}+\tfrac{\alpha_{\text{Sec}}}{Q_{\text{Sec}}+\epsilon}+\tfrac{\alpha_{\text{Conf}}}{Q_{\text{Conf}}+\epsilon}\Big)^{-1},\quad \sum\alpha_\bullet=1.
$$

**Interpretation.** These four sub-coefficients realize the **four industrial gates**:
**Correctness — the software must run.** **Efficiency — it must run fast.** **Security — it must run safely.** **Conformance — it must run according to established engineering norms.**

---

### 4.2 Practical Measurement Pathway (experimentable with limited resources)

* **Correctness**:

  - *ExecPass*: pass\@k / execution accuracy on HumanEval-family tasks (function/contest level) and newer robustness variants.
  - *Compile*: compilation\@k / build success via **JavaBench** harness.
  - *RepoExec*: run **REPOEXEC** tasks (functional correctness + dependency utilization).

* **Efficiency**:

  - Use **LiveCode-Bench / Mercury / EffiBench** “beyond pass” logs to extract runtime and memory; normalize as in $Q_{\text{Eff}}$.
  - Where applicable, include **PAREval** speedup/efficiency\@k for compute-bound tasks.

* **Security**:

  - Detection: evaluate F1/Accuracy on **BigVul / VulEval / SecVulEval** families.
  - Repair: correctly-fixed / plausibly-fixed / compilation rate on **Vul4J / VJBench / SecurityEval**.
  - Deps: audit dependencies for CVEs & licenses; report fraction compliant (the survey argues for **multi-metric evaluation beyond accuracy**, including **security**).

* **Conformance**:

  * Lint/style score (ESLint/PSR/Google-Java-Format etc.).
  * Idioms: rule-based checks for framework conventions (e.g., Spring layered DI, React component props/state hygiene).
  * Architecture: presence/coverage of resilience mechanisms (caching, circuit breakers, rate limiting, graceful degradation). The survey’s **human-in-the-loop** guidance justifies evaluating these practice-level criteria.

**No extra chapter is required** to justify the math: the harmonic mean is chosen precisely because it encodes the engineering doctrine that **a single failing gate invalidates quality**. The survey’s own taxonomy—**NLP-based, code-specific, execution-based, diversity/consistency**—and its calls to go **beyond accuracy** to include **maintainability, performance,** and **security** provide the empirical footing for these four gates and their measurability.

---

## 5. Feasibility & Minimal Protocols

A formula is only useful if it can be **experimented with and reproduced**. The value of Qc lies not in its abstraction but in its operationalization. This section therefore outlines how one might compute Qc on modest hardware, without requiring industrial-scale resources.

### 5.1 Environment and Assumptions

* **Containerized runs.** Each candidate workflow is executed inside a minimal container (e.g., `python:3.12-slim`, `openjdk:21-jdk`).
* **Isolation.** Dependencies are pinned, and CPU/memory budgets fixed (e.g., 2 vCPU, 4–8 GB RAM).
* **Common runner.** All evaluations produce normalized scores in $[0,1]$ and emit them as structured JSON, which the aggregator consumes to compute $Q_{\text{Corr}}, Q_{\text{Eff}}, Q_{\text{Sec}}, Q_{\text{Conf}}$, and ultimately $Qc$.

### 5.2 Sources of Reference (the “oracle”)

Two types of oracles exist:

1. **Benchmark mode.** Public datasets already provide hidden tests or vulnerability corpora (e.g., HumanEval, MBPP, SWE-bench, SecurityEval). These can be used directly to instantiate Correctness, Efficiency, and Security metrics.
2. **Real-project mode.** For bespoke tasks (e.g., “generate a Spring Boot CRUD service”), the oracle is derived from:

   * **Contractual requirements** (OpenAPI, acceptance tests, smoke tests).
   * **Performance baselines** (latency, memory, throughput targets).
   * **Security scans** (SAST tools, dependency audits).
   * **Conformance rules** (lint/style checkers, framework idioms, architectural checks).

In both cases, the output is measurable data, not subjective opinion.

### 5.3 Minimal Protocol

For each gate, one collects a small but representative set of signals:

* **Correctness.** Fraction of tests passed, build success rate, and end-to-end smoke tests.
* **Efficiency.** Normalized runtime latency, throughput, and memory usage against published targets.
* **Security.** Detection of planted vulnerabilities, repair success rate, dependency compliance.
* **Conformance.** Pass rate on lint/style rules, framework idiom coverage, architectural safeguards (e.g., caching, circuit breakers).

These are combined via the harmonic-mean aggregation in §4.

### 5.4 Practical Constraints

The protocols above are intentionally minimal. They can be run on laptops or modest cloud VMs, reuse the same artifacts across gates, and rely on open-source tools (pytest, Bandit, Flake8, ESLint, etc.).

### 5.5 Hand-off to a Lab Manual

This section serves only as a **conceptual introduction**. The detailed glue scripts, container manifests, and worked examples are provided separately in a **Lab Manual** accompanying this notebook. That manual shows how each adapter can be implemented in fewer than fifty lines of Python or Bash, with reproducible results.

---

## 6. Discussion

The proposed formulation of Qc as the harmonic mean of **Correctness, Efficiency, Security,** and **Conformance** is deliberately strict. It embodies the engineering principle that *a single failure invalidates quality*. This makes Qc less forgiving than arithmetic averages, but more aligned with the acceptance criteria of industrial software.

### 6.1 Flexibility vs. Rigour

While strictness enforces reliability, flexibility is introduced through weightings $\alpha_j$. Different domains can adjust priorities:

* Academic prototypes may assign higher weight to Correctness and lower weight to Conformance.
* Industrial contexts may emphasize Security and Conformance more heavily.
  This balance allows Qc to be both **context-aware** and **principled**.

### 6.2 Risks of Bias

Several risks must be acknowledged:

* **Dataset Bias.** Current benchmarks are dominated by Python/Java. Languages such as Rust, Go, or domain-specific DSLs remain underrepresented.
* **Benchmark Fragmentation.** Execution-focused datasets may inflate Correctness while ignoring maintainability.
* **Tooling Bias.** Static analyzers and lint tools vary in coverage; relying on a single tool risks underreporting vulnerabilities or style violations.

Addressing these requires continuous integration of new datasets and tools into the Qc adapters, while maintaining a stable scoring contract.

### 6.3 Relation to Other SPI Dimensions

The placement of Qc as the first dimension is not arbitrary. It acts as the **ground truth**:

* **HoR (Human-off Ratio)** is only meaningful when the software is demonstrably correct, efficient, secure, and conformant.
* **Exp (Explainability)** has value only when explanations correspond to genuinely correct artifacts.
* **Stb (Stability)** is validated by replicating *good* outcomes, not failures.
* **NLE (Natural Language Engagement)** is persuasive only when the resulting artifacts meet quality thresholds.

Thus, Qc is the **root contract** upon which the remaining four dimensions rest.

### 6.4 Future Directions

* **Evolutionary Quality.** Section 3 suggested evolutionary adaptability as an extension point. Incorporating longitudinal benchmarks to track defect trends or maintainability across versions remains an open challenge.
* **Cross-cultural Benchmarks.** Extending Conformance beyond frameworks (Spring, React) to include regional coding standards and industry regulations (e.g., GDPR compliance in Europe, secure coding standards in aerospace).
* **Beyond Code.** While this paper centers on software artifacts, Qc may in the future extend to **data pipelines** or **model-serving systems**, broadening SPI beyond source code.


---

## 7. Conclusion

This working paper argued for **Code Quality (Qc)** as the **foundational dimension of the Symbiotic Programming Index (SPI)**. Building on the *2025 Survey* of 291 benchmarks, we observed:

1. Correctness remains the non-negotiable baseline.
2. Efficiency, Security, and Conformance are necessary complements to ensure industrial-grade viability.
3. A harmonic mean formalization ensures that failures in any gate significantly penalize the overall Qc, mirroring real-world engineering acceptance.

The **four industrial gates of software quality** — *the software must run, must run fast, must run safely, and must run according to established norms* — provide a practical abstraction that unifies the otherwise fragmented landscape of benchmarks.

We emphasize that this formulation is not final. It is a **proposal and invitation**: with limited resources, we cannot yet conduct large-scale experiments. But the adapters and minimal protocols outlined here demonstrate that Qc is measurable today, not only in theory but in practice.

Future collaborators are encouraged to expand these adapters, refine the formulas, and validate Qc across broader languages, domains, and industries. In doing so, we can transform Qc from a working note into a reproducible standard, anchoring the larger SPI framework in measurable, actionable ground truth.

**Notebook reflection.** This entry (September 2025) captures my first attempt to operationalize Qc beyond abstract formulas. The emphasis on minimal but runnable protocols reflects both my enthusiasm and my constraints. What matters is that the ideas are now concrete enough for others to test, extend, and challenge — exactly the spirit in which SPI is meant to grow.


---


## References

* Hu, X., Niu, F., Chen, J., Zhou, X., Zhang, J., He, J., Xia, X., & Lo, D. (2025). *Assessing and advancing benchmarks for evaluating large language models in software engineering tasks*. arXiv:2505.08903. [https://arxiv.org/abs/2505.08903](https://arxiv.org/abs/2505.08903)

* Li, C. M. (2025). *Symbiotic Programming Index (SPI)*. Unpublished document. [https://aipapacha.github.io/symbiotic-programming-index/](https://aipapacha.github.io/symbiotic-programming-index/)

* Austin, J., Odena, A., Nye, M., Bosma, M., Michalewski, H., Dohan, D., … & Sutton, C. (2021). *Program synthesis with large language models*. arXiv:2108.07732.

* Bui, Q.-C., Scandariato, R., & Díaz Ferreyra, N. (2022). *Vul4J: A dataset of reproducible Java vulnerabilities geared towards program repair*. In *Proceedings of the 19th International Conference on Mining Software Repositories (MSR 2022)* (pp. 464–468).

* Cao, J., Chen, Z., Wu, J., Cheung, S.-C., & Xu, C. (2024). *JavaBench: A benchmark of object-oriented code generation for evaluating large language models*. In *Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering (ASE 2024)* (pp. 870–882).

* Chen, M., Tworek, J., Jun, H., Yuan, Q., de Oliveira Pinto, H. P., Kaplan, J., … & Zaremba, W. (2021). *Evaluating large language models trained on code*. arXiv:2107.03374.

* EffiBench. (2024). *Benchmark & leaderboard (time/memory units)*. Hugging Face. [https://huggingface.co/spaces/EffiBench/effibench-leaderboard](https://huggingface.co/spaces/EffiBench/effibench-leaderboard)

* Hendrycks, D., Basart, S., Kadavath, S., Arora, A., Guo, E., Burns, C., … & Steinhardt, J. (2021). *Measuring coding challenge competence with APPS*. In *Advances in Neural Information Processing Systems (NeurIPS 2021)*.

* Jimenez, C., Jain, P., Zhou, S., Sutton, C., Neubig, G., & Vasilescu, B. (2023). *SWE-bench: Can language models resolve real-world GitHub issues?* arXiv:2310.06770.

* LiveCodeBench. (2024). *Benchmark & leaderboard*.

* Mercury. (2024). *Benchmark (runtime profiling beyond pass)*. GitHub. [https://github.com/Elfsong/Mercury](https://github.com/Elfsong/Mercury)

* RepoExec. (2024). *Benchmark repository*. GitHub. [https://github.com/FSoft-AI4Code/RepoExec](https://github.com/FSoft-AI4Code/RepoExec)

* SecurityEval. (2022). *Benchmark & tools for security-oriented code evaluation*. GitHub. [https://github.com/s2e-lab/SecurityEval](https://github.com/s2e-lab/SecurityEval)

* SV-Benchmarks. (Ongoing). *Software verification benchmarks*. GitLab. [https://gitlab.com/sosy-lab/benchmarking/sv-benchmarks](https://gitlab.com/sosy-lab/benchmarking/sv-benchmarks)


---

## Appendix A. Working Implementation: Binary Calculator QC Sample

This paper has deliberately focused on the **conceptual definition** of Qc and its role within the Symbiotic Programming Index (SPI). While Section 5 outlined minimal protocols and sources of reference, we now provide a **complete working implementation** that demonstrates the four-dimensional QC framework in practice.

### A.1 Live Demonstration

The **[Binary Calculator QC Sample](../../../spi-examples/spi-qc/binary_calculator_sample/)** provides a fully operational implementation of the QC evaluation system described in this paper. This sample demonstrates:

- **Real AI-generated code evaluation** across all four QC dimensions
- **Concrete scoring implementation** using the weighted harmonic mean formula
- **Practical measurement protocols** that can be run on modest hardware
- **Actionable quality reports** with specific improvement recommendations

### A.2 Running the Sample

```bash
cd spi-examples/spi-qc/binary_calculator_sample/
python run_demo.py
```

**Expected Output:**
```
SPI-QC Results (Binary Calculator):
Overall QC Score: 0.841 ✅ PASS
Correctness: 1.000 (All tests pass)
Efficiency: 0.993 (Fast execution, low memory)
Security: 0.800 (Minor input validation issues)
Conformance: 0.667 (Missing documentation)

Recommendations:
• Add docstrings to classes and methods
• Implement input sanitization for user data
```

### A.3 Implementation Architecture

The sample includes:

- **`qc_framework/qc_evaluator.py`**: Core QC evaluation engine implementing the harmonic mean formula
- **`qc_framework/report.py`**: Quality reporting and recommendation system
- **`tests/test_binary_calculator.py`**: Comprehensive test suite for correctness evaluation
- **`ai_generated/`**: Sample AI-generated code (both working and flawed versions)

### A.4 Extending the Framework

The binary calculator sample serves as a **template for custom QC implementations**:

1. **Add new algorithms**: Extend the `AlgorithmBase` class for different domains
2. **Customize quality rules**: Modify the evaluation criteria in `qc_evaluator.py`
3. **Integrate new benchmarks**: Add adapters for additional correctness/security benchmarks
4. **Deploy in CI/CD**: Use the framework for automated quality gates

This working implementation transforms the theoretical QC framework into **immediately usable, reproducible evaluation tools** that can be deployed today.
---
