# Code Quality (Qc)

## Current Landscape

Among the five SPI dimensions, **Code Quality (Qc)** is the most widely studied.  
Existing benchmarks for LLMs in programming — such as **HumanEval**, **MBPP**, and **CodeXGLUE** — almost all rely on variations of Qc.  
These measures answer a narrow question: *Does the generated code work as intended?*  

## Common Measures of Code Quality

Below are the most frequently used evaluation metrics and their purpose:

- **Unit Test Pass Rate** — Percentage of pre-defined unit tests passed. Directly measures functional correctness.  
- **Integration Test Pass Rate** — Ensures that generated components interact correctly in larger systems.  
- **Static Analysis Score** — Linting, style checks, and cyclomatic complexity for maintainability and readability.  
- **Runtime Reliability** — Frequency of crashes, exceptions, or resource leaks during execution.  
- **Performance Benchmarks** — Time complexity, memory usage, efficiency compared to human baselines.  
- **Defect Density** — Number of bugs per thousand lines of generated code.  
- **Security Vulnerability Scan** — Detection of unsafe patterns (e.g., injection risks, buffer overflows).  
- **Cross-Platform Consistency** — Whether code runs identically across OS, frameworks, or hardware targets.  
- **Reusability & Modularity** — Whether functions, classes, or APIs are structured for reuse.  
- **Documentation & Comments** — Availability of meaningful explanations alongside code.  

## Missing Dimension: Industrial Usefulness

Good code is not always *useful* code. Current benchmarks rarely capture **industry applicability**:  

- **Architectural Fit** — Does the code adhere to widely used paradigms like **MVC**, **OOP**, or in frontend contexts, **MVVM**?  
- **Maintainability in Teams** — Is the code structured in a way that future engineers can easily modify or extend?  
- **Compatibility with Toolchains** — Does the output integrate smoothly into CI/CD pipelines, build systems, or frameworks?  
- **Value Alignment** — Does the code solve the actual user or business problem, or is it just syntactically correct?  

## Our Position

SPI treats Qc not just as a matter of “passing tests,” but as a broader measure of **real-world viability**.  
Future work must bridge the gap between **benchmark correctness** and **industry readiness**:  
from functional snippets → to modular, maintainable, and contextually *useful* software systems.  
