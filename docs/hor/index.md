# Human-off Ratio (HoR)

**The leverage dimension.** Once quality is reliable, the interesting question becomes: *how far can humans step back?*

HoR measures the shift from **authorship** to **orchestration** to **validation-only**. A high HoR means the AI handles most of the work; the human steers, reviews, and approves.

---

## What HoR Measures

| Metric | What it captures | How to collect |
|--------|-----------------|----------------|
| **Prompt count** | How many distinct instructions did the human give? | Count unique prompts in the session |
| **Turn count** | How many interaction rounds until task completion? | Count human–AI exchanges |
| **Edit ratio** | What fraction of the final code was manually edited? | `human_edited_lines / total_lines` |
| **Autonomy index** | What fraction of AI outputs were accepted without change? | `accepted_outputs / total_outputs` |

---

## Scoring

```
HoR = 1 - (human_effort / total_effort)
```

where `human_effort` is a weighted combination of the metrics above, normalised to [0, 1].

**Practical shortcut for a single session:**

```
HoR ≈ 1 - (human_edited_lines / total_generated_lines)
```

| HoR Score | Interpretation |
|-----------|---------------|
| 0.0–0.3 | Human-dominated — AI assists but human writes most code |
| 0.3–0.6 | Collaborative — meaningful AI contribution with human guidance |
| 0.6–0.8 | Orchestration — human primarily steers and reviews |
| 0.8–1.0 | Validation-only — human approves, AI produces |

---

## How to Measure HoR

**Step 1: Record your session.** Track prompts, AI outputs, and your edits. Many AI coding tools provide session logs or conversation history.

**Step 2: Count the inputs.**

- Number of prompts (distinct instructions, not follow-ups)
- Number of turns (back-and-forth exchanges)
- Lines of code you edited manually after AI generation

**Step 3: Compute.**

```python
# Simple HoR calculation
total_lines = lines_generated_by_ai + lines_written_by_human
human_effort = lines_written_by_human / total_lines
hor = 1 - human_effort
```

For more nuanced measurement, weight prompts and turns alongside edits:

```python
# Weighted HoR
prompt_weight = 0.3
turn_weight = 0.2
edit_weight = 0.5

normalised_prompts = min(1, prompt_count / expected_prompts)
normalised_turns = min(1, turn_count / expected_turns)
edit_fraction = human_edited_lines / total_lines

human_effort = (prompt_weight * normalised_prompts +
                turn_weight * normalised_turns +
                edit_weight * edit_fraction)
hor = 1 - human_effort
```

---

## The Critical Rule: HoR Without Qc Is Meaningless

A high HoR with low Qc means the AI ran free and produced garbage. This is the **illusion of autonomy**.

**Always report HoR alongside Qc.** The following table shows how to interpret the pair:

| HoR | Qc | Interpretation |
|-----|-----|---------------|
| High | High | The goal: efficient orchestration producing quality code |
| High | Low | Dangerous: AI running unchecked, poor output |
| Low | High | Acceptable: human effort produces good results (but inefficient) |
| Low | Low | Worst case: heavy effort, poor results |

---

## Use Cases

**Developer self-assessment:** "Am I getting better at orchestrating AI? Track HoR over time. If HoR rises while Qc stays above 0.8, your orchestration skills are improving."

**Team benchmarking:** "Which AI tool or workflow achieves higher HoR at the same Qc threshold? Compare across tools, prompting strategies, or team members."

**Education:** "Can students achieve HoR ≥ 0.6 while maintaining Qc ≥ 0.7? This is the operationalised definition of 'orchestration competency.'"

---

## Worked Example: Measuring a Coding Session

A developer uses Claude to build a REST API. Here is their session trace:

```
Session: Build Flask to-do API
Model: Claude Sonnet 4

Prompt 1: "Create a Flask REST API for a to-do list with CRUD endpoints"
  → AI generates 78 lines (routes, models, error handling)
  → Developer accepts without changes

Prompt 2: "Add input validation using marshmallow schemas"
  → AI generates 35 lines
  → Developer edits 8 lines (adjusts field names to match existing DB)

Prompt 3: "Write pytest tests for all endpoints"
  → AI generates 52 lines
  → Developer edits 4 lines (fixes test database URL)

Prompt 4: "Add rate limiting middleware"
  → AI generates 12 lines
  → Developer accepts without changes
```

**Measurement:**
```
Prompts:     4
Turns:       4  (one-shot per prompt, no clarification needed)
AI lines:    177
Human edits: 12 lines
Total lines: 177

HoR = 1 - (12 / 177) = 0.932
```

**Paired with Qc = 0.789 (Conditional Pass):** This is a productive orchestration session — high HoR, reasonable quality. The developer steered effectively but the output needs docstrings and input sanitisation before production use.

---

## Open Questions

- Where is the optimal HoR for a given task complexity? Very high HoR might indicate the task was too simple.
- How should HoR account for multi-agent workflows where the human orchestrates multiple AI agents?
- Should "prompt engineering effort" (time spent crafting prompts) factor into human effort?

These questions are active research directions. Contributions welcome.
