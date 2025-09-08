# Human-off Ratio (HoR)

## Concept

**Human-off Ratio (HoR)** asks a simple but powerful question:  
👉 *How far can humans “let go” while AI still produces usable, accountable results?*

In traditional programming, humans control every keystroke.  
In symbiotic programming, the human role shifts toward **orchestration and validation**,  
and the real measure is how little intervention is needed for tasks to complete reliably.

---

## Minimal Interaction Principle

At its core, HoR can be approximated in the **minimal case**:

- **Minimal Prompts** — The fewer unique instructions given, the higher the HoR.  
- **Minimal Rounds** — If an LLM can solve a task in *one or two exchanges* rather than ten, the HoR is high.  
- **Minimal Edits** — If the human only validates outputs, without rewriting logic, HoR approaches 1.0.  

In practice, *high HoR* means the LLM can execute multi-step tasks with:  
- Few prompts  
- Few clarification turns  
- Few or no post-hoc edits  

---

## Measures of HoR

Possible ways to quantify HoR include:

- **Prompt Count** — Number of human-authored instructions required.  
- **Turn Count** — Number of interaction rounds until task completion.  
- **Edit Ratio** — Percentage of human-modified lines vs. AI-generated lines.  
- **Autonomy Index** — Ratio of AI-generated commits accepted without change.  

---

## Challenges

A high HoR does **not automatically imply success**:  
- An LLM might produce runnable code in one shot, but fail quality or stability checks.  
- Minimal interaction can come at the cost of clarity or explainability.  
- Over-reliance on HoR alone risks “illusion of autonomy.”  

Therefore, **HoR must always be interpreted alongside Qc (quality) and Stb (stability)** to ensure that reduced human intervention does not erode trustworthiness.

---

## Our Position

SPI frames HoR as the **measure of human withdrawal**:  
- From full authorship → to orchestration → to validation-only.  
- The ultimate question: *When does a workflow qualify as an “AI coder” or even an “AI tutor”?*

By quantifying HoR, we move beyond anecdotes (“it worked in one prompt”)  
toward **systematic thresholds** for when orchestration can be trusted.