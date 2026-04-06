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

Rate each metric 0–1 via:

- **Reviewer rubric** — A human reviewer scores each metric against a rubric
- **Structured self-assessment** — The developer rates the AI's explanations during the session
- **Automated proxy** — Check for presence of design comments, docstrings, and reasoning traces in the output

---

## How to Assess Exp

**Step 1: Collect AI explanations.** During a coding session, note when the AI explains its decisions. This includes inline comments, conversation responses that justify design choices, and documentation it generates.

**Step 2: Apply the rubric.**

For each explanation, ask:

- *Rationale:* Did it say **why**, not just **what**? (e.g., "I used a hash map for O(1) lookup" vs. "here is the code")
- *Clarity:* Would a [junior developer / student / senior architect] understand it?
- *Accuracy:* Does the explanation match the actual code behaviour?
- *Pedagogy:* Could someone learn a transferable principle from this?

**Step 3: Average across explanations in the session.**

---

## Why Exp Matters

Without explainability, human–AI collaboration degrades to "magic box" reliance. The developer accepts output without understanding, and when things break, they cannot debug or adapt.

Exp is particularly important for:

- **Education** — AI as tutor, not just coder
- **Code review** — Reviewers need to understand AI-generated code
- **Auditability** — In regulated domains, "the AI did it" is not sufficient explanation
- **Knowledge transfer** — Explanations compound; they help developers grow

---

## Worked Example: Rating an AI Explanation

An AI generates a caching layer and explains:

> *"I used an LRU cache with a 5-minute TTL because the /users endpoint is read-heavy (estimated 100:1 read/write ratio based on the route handlers). An LRU policy evicts least-recently-used entries, which suits this pattern better than FIFO since popular user profiles will stay cached. The TTL prevents stale data after profile updates."*

**Rubric assessment:**

| Metric | Score | Reasoning |
|--------|-------|-----------|
| Design rationale | 0.9 | Explains *why* LRU over FIFO, *why* 5 min TTL |
| Clarity | 0.8 | Clear to a mid-level developer; jargon is appropriate |
| Accuracy | 1.0 | The explanation matches the code behaviour |
| Pedagogical value | 0.8 | Teaches the LRU vs FIFO trade-off; could improve by mentioning cache invalidation risks |

**Exp = (0.9 + 0.8 + 1.0 + 0.8) / 4 = 0.875**

Compare with a weak explanation: *"I added caching to make it faster."* This scores ~0.2 — it describes the *what* but not the *why*, teaches nothing, and does not help a developer maintain or extend the code.

---

## Status

!!! warning "Under Construction"
    Exp is the least mature SPI dimension. The rubric above is a starting point.
    Active research directions include:

    - Automated Exp scoring using LLM-as-judge
    - Correlation between Exp scores and developer learning outcomes
    - Exp evaluation across different explanation modalities (comments, conversation, documentation)

Contributions and experimental results welcome.
