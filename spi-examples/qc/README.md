# SPI Quality Control (QC) Examples

This directory contains examples and guides for implementing the **Symbiotic Programming Index Quality Control (QC)** dimension. QC serves as the foundational interface between human-AI collaboration and real-world engineering acceptance, evaluating AI-generated code across four critical dimensions.

## 🎯 Philosophy: Standing on the Shoulders of Giants

**QC is not about creating yet another dataset.** Instead, QC integrates and orchestrates the best of existing benchmarks into a coherent evaluative structure. This "integration-first" approach recognizes that:

- Over 291 coding benchmarks exist, each focusing on different aspects of correctness, efficiency, or realism
- These benchmarks are highly valuable but remain fragmented
- SPI's originality lies in **reframing them under a unified contract of quality**

### Why Apply Existing Benchmarks?

1. **Methodological Soundness**: Avoids duplication and leverages community consensus
2. **Practical Implementation**: Can be deployed today using existing infrastructure
3. **Academic Positioning**: Creates a meta-benchmark framework that synthesizes rather than competes

## 🏗 Four-Dimensional Framework

The SPI-QC system evaluates code quality through four uncompromising dimensions:

- **Correctness (25%)**: The software must run as intended (HumanEval+, LiveCodeBench, SWE-bench)
- **Efficiency (25%)**: The software must run fast and use resources responsibly (Mercury, EffiBench)
- **Security (25%)**: The software must run safely without vulnerabilities (SecurityEval, CodeQL)
- **Conformance (25%)**: The software must run according to engineering norms (CodeStyleBench, linters)

## 📁 Directory Structure

```
spi-examples/qc/
├── README.md                    # This guide
└── binary-calculator-sample/   # Complete working QC demonstration
```

## 🚀 Quick Start

### Option 1: Live QC Demonstration
See the **[Binary Calculator Sample](../../../spi-examples/spi-qc/binary_calculator_sample/)** - a complete working example that demonstrates QC evaluation of AI-generated code:

```bash
cd spi-examples/spi-qc/binary_calculator_sample/
python run_demo.py
```

**Results Preview:**
| Version | Correctness | Efficiency | Security | Conformance | Overall | Status |
|---------|-------------|------------|----------|-------------|---------|--------|
| Original | 1.000 | 0.993 | 0.800 | 0.667 | **0.841** | ✅ PASS |
| Flawed | 0.000 | 0.500 | 0.400 | 0.626 | **0.000** | ❌ FAIL |

### Option 2: Understand the Theory
Read the **[QC Design Document](../../../spi-examples/spi-qc/raw_requirement.md)** to understand the complete specification and philosophy.

## 🎨 Key Concepts

### Meta-Benchmark Integration
The core innovation is **orchestrating existing benchmarks** rather than creating new ones:

```python
# Correctness: Integrate existing benchmarks
correctness_score = evaluate_with_existing_benchmarks([
    'HumanEval+',     # Function-level correctness
    'LiveCodeBench',  # Program-level solutions  
    'SWE-bench',      # Repository-level issues
])

# Security: Apply established tools
security_score = run_security_analysis([
    'SecurityEval',   # Vulnerability patterns
    'CodeQL',         # Static analysis
    'Bandit',         # Python security linter
])
```

### Weighted Harmonic Mean Scoring
QC uses the **shortest-plank principle** - poor performance in any dimension significantly impacts overall quality:

```python
QC = (Σ(w_j / (s_j + ε)))^(-1)
```

Where:
- `s_j`: normalized score per dimension (0.0-1.0)
- `w_j`: dimension weights (default: 0.25 each)
- `ε`: stability constant

### Four-Dimensional Evaluation
Each dimension measures critical aspects of industrial software quality:

1. **Correctness**: Does it work? (Existing function/program/repository benchmarks)
2. **Efficiency**: Is it fast? (Runtime/memory profiling against canonical solutions)
3. **Security**: Is it safe? (Static analysis with established vulnerability scanners)
4. **Conformance**: Is it maintainable? (Style guides, documentation, API usage patterns)

### Quality Gate System
- **Pass (≥0.8)**: Industrial-ready code
- **Conditional Pass (0.6-0.8)**: Needs improvements
- **Fail (<0.6)**: Requires significant work

## 📚 Examples by Use Case

### For AI Code Generation Evaluation
**Real-world scenario**: *"Can you create a binary calculator using Python?"*

The [Binary Calculator Sample](../../spi-examples/spi-qc/binary_calculator_sample/) demonstrates:
- Evaluating AI-generated code across all four dimensions
- Identifying quality differences between implementations
- Providing actionable improvement recommendations
- Integrating multiple existing evaluation methods

### For AI Code Generation Platforms
- Automatic quality scoring for generated code
- Feedback loops for model improvement
- User-facing quality metrics

### For Educational Platforms
- Student assignment evaluation
- Automated feedback generation
- Progress tracking and analytics

### For Development Teams
- Pull request quality gates
- Code review automation
- Team quality standards

## 🔧 Customization Examples

### Adding New Algorithm Domains

**Computer Vision:**
```python
# app/src/algorithms/cv_ops.py
class ComputerVisionOperations(AlgorithmBase):
    def detect_edges(self, image: np.ndarray) -> np.ndarray:
        # Edge detection implementation
```

**Machine Learning:**
```python
# app/src/algorithms/ml_ops.py
class MachineLearningOperations(AlgorithmBase):
    def train_classifier(self, X: np.ndarray, y: np.ndarray) -> Model:
        # Classifier training implementation
```

**Cryptography:**
```python
# app/src/algorithms/crypto_ops.py
class CryptographyOperations(AlgorithmBase):
    def encrypt_aes(self, plaintext: str, key: str) -> str:
        # AES encryption implementation
```

### Custom Quality Rules

**Domain-Specific Patterns:**
```yaml
# rules/ml_patterns.yaml
rules:
  - id: "data_validation"
    name: "ML Data Validation"
    must_exist: ["app/src/algorithms/"]
    contains_any: ["validate_features", "check_labels", "preprocess_data"]
```

**Performance Requirements:**
```yaml
# rules/performance_requirements.yaml
rules:
  - id: "complexity_limits"
    name: "Algorithm Complexity Limits"
    must_exist: ["app/src/algorithms/"]
    contains_any: ["O\\(n\\)", "O\\(log n\\)", "O\\(n log n\\)"]
```

## 📊 Quality Metrics & Benchmark Integration

The system produces normalized scores (0.0-1.0) for each dimension by integrating existing benchmarks:

### Correctness Benchmarks
- **HumanEval+**: Extended test cases for function-level correctness
- **LiveCodeBench**: Competitive programming for program-level solutions
- **SWE-bench**: GitHub issue resolution for repository-level correctness

### Efficiency Benchmarks  
- **Mercury & EffiBench**: Performance evaluation beyond pass/fail
- **Runtime profiling**: Execution time vs. canonical solutions
- **Memory analysis**: Resource usage optimization

### Security Analysis
- **SecurityEval**: Vulnerability pattern detection
- **CodeQL**: Static analysis for exploitable patterns
- **Bandit/ESLint**: Language-specific security linters

### Conformance Standards
- **PEP 8/ESLint**: Style guide compliance
- **Documentation coverage**: Docstring and comment analysis
- **API usage patterns**: Library contract adherence

### Example Output:
```
SPI-QC Results (Binary Calculator):
Overall QC Score: 0.841 ✅ PASS
Correctness: 1.000 (All HumanEval+ tests pass)
Efficiency: 0.993 (Fast execution, low memory)
Security: 0.800 (Minor input validation issues)
Conformance: 0.667 (Missing documentation)

Recommendations:
• Add docstrings to classes and methods
• Implement input sanitization for user data
```

## 🛠 Implementation Patterns

### 1. Algorithm Base Class Pattern
```python
class AlgorithmBase(ABC):
    @abstractmethod
    def get_metadata(self) -> Dict[str, AlgorithmMetadata]:
        """Return algorithm metadata including complexity info"""
        pass
    
    def execute_with_metrics(self, function_name: str, *args) -> ExecutionResult:
        """Execute with performance tracking"""
        pass
```

### 2. Registry Pattern
```python
class AlgorithmRegistry:
    def get_function(self, name: str) -> Callable:
        """Get function by name for benchmark compatibility"""
        return self._function_map[name]
```

### 3. Validation Pattern
```python
class ValidationUtils:
    @staticmethod
    def validate_input_type(value: Any, expected_type: type, param_name: str):
        """Comprehensive input validation"""
        if not isinstance(value, expected_type):
            raise InvalidInputError(f"Parameter '{param_name}' must be...")
```

## 🔗 Related Resources

- **[Binary Calculator QC Sample](../../../spi-examples/spi-qc/binary_calculator_sample/)**: Complete working demonstration
- **[SPI-QC Design Document](../../../spi-examples/spi-qc/raw_requirement.md)**: Full specification and philosophy
- **[GitHub Repository](https://github.com/symbiotic-programming/spi)**: Source code and issues

### Key Papers & Benchmarks Referenced
- **HumanEval+**: Chen et al. - Extended evaluation for code generation
- **LiveCodeBench**: Jain et al. - Contamination-free evaluation
- **SWE-bench**: Jimenez et al. - Repository-level code generation
- **SecurityEval**: Pearce et al. - Security vulnerability detection

## 🤝 Contributing

We welcome contributions! You can:

- **Submit examples**: Add new QC examples to this directory
- **Improve documentation**: Enhance existing guides and explanations
- **Bug reports**: Use GitHub issues

## 📄 License

This work is licensed under [CC BY 4.0](../../LICENSE-CC-BY-4.0). You are free to use, modify, and distribute these examples with attribution.

---

## 🎯 The QC Advantage: Integration Over Innovation

**Why QC succeeds where other approaches fall short:**

1. **Leverages Existing Excellence**: Instead of reinventing evaluation, QC orchestrates 291+ existing benchmarks
2. **Industrial Realism**: Four-dimensional evaluation mirrors real engineering standards
3. **Immediate Deployment**: Uses existing tools and infrastructure - no waiting for new datasets
4. **Community Consensus**: Builds on established benchmarks with proven validity
5. **Meta-Framework**: Creates a higher-order evaluative system that synthesizes rather than competes

**The result**: A unified quality score that reflects the uncompromising contract of software engineering - code must run, run fast, run safely, and run according to professional norms.

---

**Next Steps:**
1. 🎮 **Try the Demo**: Run the **[Binary Calculator Sample](../../../spi-examples/spi-qc/binary_calculator_sample/)** 
2. 📖 **Understand the Theory**: Read the **[QC Design Document](../../../spi-examples/spi-qc/raw_requirement.md)**
3. 🔍 **Build Your Own**: Use the binary calculator as a template for your own QC implementations