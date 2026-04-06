# AI Explainability (Exp)

**The trust dimension.** As humans step back (high HoR), the AI must be able to explain itself — not just produce code, but articulate *why* it made specific design choices.

Exp bridges engineering and pedagogy: a well-explained AI output builds trust and teaches the developer something new.

---

## What Exp Measures

| Metric | Question | Rating |
|--------|----------|--------|
| **Design rationale** | Did the AI explain *why* it chose this approach, not just *what* it produced? | 0–1 |
| **Clarity** | Is the explanation understandable to the target audience? | 0–1 |
| **Accuracy** | Does the explanation match what the code actually does? | 0–1 |
| **Pedagogical value** | Could someone learn from this explanation? Does it teach, not just describe? | 0–1 |

---

## Scoring

```
Exp = (design_rationale + clarity + accuracy + pedagogical_value) / 4
```

| Exp Score | Grade | Meaning |
|-----------|-------|---------|
| ≥ 0.8 | **Pass** | Explanations are trustworthy and educational |
| 0.6–0.8 | **Conditional** | Explanations exist but lack depth or precision |
| < 0.6 | **Fail** | Explanations are missing, misleading, or superficial |

The simple average (rather than harmonic mean) is deliberate: unlike Qc's gates, the four Exp metrics are complementary rather than prerequisite. An explanation can be highly accurate but only moderately pedagogical and still be useful.

---

## How to Assess Exp

**Step 1: Collect AI explanations.** During a coding session, note every instance where the AI explains its decisions. This includes inline comments, conversation responses that justify design choices, docstrings, commit messages, and documentation it generates. If the AI produces code without explanation, record that too — silence counts as a zero.

**Step 2: Apply the rubric.**

For each explanation, score four questions:

- *Rationale:* Did it say **why**, not just **what**? (e.g., "I used a hash map for O(1) lookup because this function is called in a hot loop" vs. "here is the code")
- *Clarity:* Would the target audience understand it? Calibrate to context — a junior developer tutorial should be simpler than a senior architect design doc.
- *Accuracy:* Does the explanation match the actual code behaviour? Check for hallucinated justifications — the AI may produce a plausible-sounding rationale that does not correspond to what the code does.
- *Pedagogy:* Could someone learn a transferable principle from this? The best explanations teach patterns, not just describe instances.

**Step 3: Average across explanations in the session.**

If a session has \(n\) explanations, each scored on the four metrics:

$$
Exp = \frac{1}{n}\sum_{i=1}^{n}\frac{R_i + C_i + A_i + P_i}{4}
$$

where \(R\) = rationale, \(C\) = clarity, \(A\) = accuracy, \(P\) = pedagogical value for each explanation \(i\).

---

## Assessment Methods

Exp can be assessed through three complementary approaches, from most rigorous to most practical:

### 1. Expert Reviewer Rubric

A human reviewer (ideally not the developer who ran the session) scores each AI explanation against the four metrics. This is the gold standard but expensive.

**Protocol:**

1. Collect all AI explanations from a session (conversation logs, inline comments, generated docs)
2. For each explanation, the reviewer reads the code and the explanation independently
3. Score each metric 0–1 using the rubric above
4. Report inter-rater reliability if using multiple reviewers (target: Cohen's κ ≥ 0.7)

### 2. LLM-as-Judge

Use a separate LLM to evaluate explanation quality. This scales better than human review but requires careful calibration.

**Protocol:**

1. Extract AI explanations and their corresponding code
2. Prompt a judge model (ideally a different model or different temperature than the one being evaluated) with the code, the explanation, and the rubric
3. Ask the judge to score each metric and justify each score
4. Validate against human reviewers on a calibration set (minimum 20 examples)

**Example judge prompt:**

```
You are evaluating the quality of an AI's code explanation.

Code: [insert code]
AI's explanation: [insert explanation]

Score each metric 0.0–1.0:
1. Design rationale: Does the explanation say WHY, not just WHAT?
2. Clarity: Is it understandable to a mid-level developer?
3. Accuracy: Does the explanation match the code's actual behaviour?
4. Pedagogical value: Could someone learn a transferable principle?

For each score, provide a one-sentence justification.
```

### 3. Automated Proxy

Use structural signals as a fast, cheap approximation of Exp. Less accurate than rubric or judge methods, but useful for CI/CD integration and large-scale screening.

**Signals to check:**

| Signal | Proxy for | How to measure |
|--------|-----------|----------------|
| Design comments present | Rationale | Regex: `# Why:`, `# Rationale:`, `# Design choice:` |
| Docstring coverage | Clarity | `interrogate` (Python), TypeDoc coverage |
| Reasoning traces in conversation | Rationale + Pedagogy | Count sentences containing "because", "since", "in order to", "trade-off" |
| Explanation–code alignment | Accuracy | LLM check: does the docstring match the function signature and body? |
| Alternative approaches mentioned | Pedagogy | Check for "alternatively", "another approach", "I considered" |

**Proxy formula:**

```
Exp_proxy = 0.3 × has_rationale + 0.2 × docstring_coverage
          + 0.2 × reasoning_density + 0.2 × alignment_score
          + 0.1 × alternatives_mentioned
```

This proxy correlates with human rubric scores at approximately r = 0.6–0.7 based on preliminary testing. Use it for screening, not for final scoring.

---

## Tool Ecosystem

SPI does not mandate specific tools. Here are common choices for Exp assessment (as of 2026):

| Method | Tools | Strengths | Limitations |
|--------|-------|-----------|-------------|
| **Expert rubric** | Spreadsheet, annotation tools (Prodigy, Label Studio) | Gold standard accuracy | Expensive, slow, subjective |
| **LLM-as-judge** | OpenAI API, Anthropic API, local models via Ollama | Scalable, consistent | Requires calibration, may miss subtle errors |
| **Docstring coverage** | `interrogate` (Python), TypeDoc, Javadoc coverage | Fast, automated, CI-friendly | Measures quantity, not quality |
| **Comment analysis** | Custom regex, AST parsers | Language-agnostic, fast | Brittle, high false-positive rate |
| **Conversation logging** | Session recorders, API logs, IDE plugins | Captures full explanation context | Privacy concerns, large data volume |

---

## Improving Exp

If Exp scores are low, these interventions typically help:

**Prompt-level:**

- Ask the AI to "explain your design choices" or "justify your approach" explicitly
- Use chain-of-thought prompting: "Think step by step and explain each decision"
- Request comparisons: "What alternatives did you consider and why did you reject them?"

**Workflow-level:**

- Add a mandatory explanation step to your orchestration pipeline
- Use a two-pass approach: generate code first, then generate explanations in a separate pass (avoids explanation quality degrading code quality)
- Configure AI tools to produce design rationale comments by default (many IDEs and agents support this)

**Assessment-level:**

- Provide the rubric to the AI upfront — models produce better explanations when they know the evaluation criteria
- Include example explanations (high-scoring and low-scoring) in your system prompt

---

## Why Exp Matters

Without explainability, human–AI collaboration degrades to "magic box" reliance. The developer accepts output without understanding, and when things break, they cannot debug or adapt.

Exp is particularly important for:

- **Education** — AI as tutor, not just coder. High Exp means the developer grows with every interaction
- **Code review** — Reviewers need to understand AI-generated code before approving it
- **Auditability** — In regulated domains, "the AI did it" is not sufficient explanation for design decisions
- **Knowledge transfer** — Explanations compound over time; they help developers build mental models that outlast any single session
- **Debugging** — When code fails, good explanations tell you *what the AI intended*, which is the first step to finding the bug

**Exp + HoR = the philosophical core.** A workflow with high HoR but low Exp is dangerous: the human has stepped back but cannot understand what the AI is doing. This is the "illusion of autonomy" — the system appears autonomous but is actually opaque.

---

## Worked Example: Rating an AI Explanation

An AI generates a caching layer and explains:

> *"I used an LRU cache with a 5-minute TTL because the /users endpoint is read-heavy (estimated 100:1 read/write ratio based on the route handlers). An LRU policy evicts least-recently-used entries, which suits this pattern better than FIFO since popular user profiles will stay cached. The TTL prevents stale data after profile updates."*

**Rubric assessment:**

| Metric | Score | Reasoning |
|--------|-------|-----------|
| Design rationale | 0.9 | Explains *why* LRU over FIFO, *why* 5 min TTL — grounded in the read/write ratio |
| Clarity | 0.8 | Clear to a mid-level developer; jargon is appropriate for the audience |
| Accuracy | 1.0 | The explanation matches the code behaviour (verified by reading the implementation) |
| Pedagogical value | 0.8 | Teaches the LRU vs FIFO trade-off; could improve by mentioning cache invalidation risks |

**Exp = (0.9 + 0.8 + 1.0 + 0.8) / 4 = 0.875 → Pass**

Compare with a weak explanation: *"I added caching to make it faster."* This scores approximately 0.2 — it describes the *what* but not the *why*, teaches nothing, and does not help a developer maintain or extend the code.

---

## Open Questions

Exp is the SPI dimension most closely connected to ongoing AI research. Key open questions include:

- **Calibration across audiences:** How should Exp scoring adjust when the target audience changes (student vs. senior engineer)? A rubric that penalises jargon for students might penalise precision for experts.
- **Explanation modality:** Do inline comments, conversation responses, and generated documentation score differently on the same rubric? Preliminary evidence suggests conversation explanations score higher on rationale but lower on accuracy.
- **Automated scoring reliability:** LLM-as-judge methods show promise but tend to overrate clarity. What calibration protocols produce reliable automated Exp scores?
- **Correlation with learning outcomes:** Does higher Exp actually produce measurable learning? Longitudinal studies are needed.
- **Explanation cost:** Generating high-quality explanations takes tokens and latency. What is the optimal explanation depth for a given workflow?

Contributions and experimental results welcome.
