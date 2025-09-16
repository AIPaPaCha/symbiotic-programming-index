# SPI-QC Binary Calculator Sample Project

This project demonstrates the **Symbiotic Programming Index - Code Quality (SPI-QC)** framework by evaluating AI-generated binary calculator implementations across four quality dimensions.

## Project Overview

The sample simulates a real-world scenario where an AI assistant creates a binary calculator in response to the user request: *"Can you create a binary calculator to me by using python?"*

## Architecture

### 1. AI-Generated Code (`ai_generated/`)

**`binary_calculator.py`** - The "original" AI-generated implementation
- Functional binary calculator with basic operations
- Contains some typical AI-generated code issues (minimal documentation, potential security concerns)
- Represents realistic AI coder output

**`binary_calculator_flawed.py`** - Intentionally flawed version for comparison
- Contains multiple quality issues across all dimensions
- Demonstrates how QC framework identifies different types of problems

### 2. QC Framework (`qc_framework/`)

**`qc_evaluator.py`** - Core evaluation engine
- Implements the four-dimensional QC assessment
- Uses weighted harmonic mean for overall scoring
- Follows the SPI-QC design philosophy of integrating existing evaluation methods

**`evaluate.py`** - Main evaluation script
- Runs complete QC assessment
- Generates summary results and insights

**`report.py`** - Detailed reporting system
- Provides comprehensive analysis of each dimension
- Offers actionable recommendations
- Implements quality gate decisions

### 3. Test Suite (`tests/`)

**`test_binary_calculator.py`** - Comprehensive unit tests
- Demonstrates correctness evaluation component
- Includes edge cases and error conditions
- Shows traditional testing vs. QC evaluation

## Four-Dimensional Evaluation

### 1. Correctness (Weight: 25%)
- **Method**: Functional testing with comprehensive test cases
- **Metrics**: Pass@k rate, edge case handling
- **Implementation**: Unit tests covering basic operations, edge cases, and error conditions

### 2. Efficiency (Weight: 25%)
- **Method**: Runtime and memory profiling
- **Metrics**: Execution time, memory usage, performance ratios
- **Implementation**: Benchmarking with various input sizes

### 3. Security (Weight: 25%)
- **Method**: Static analysis for vulnerability patterns
- **Metrics**: Vulnerability density, exploit susceptibility
- **Implementation**: Pattern matching for common security issues (eval usage, division by zero, bare except clauses)

### 4. Conformance (Weight: 25%)
- **Method**: Code style and documentation analysis
- **Metrics**: Lint compliance, documentation coverage, naming conventions
- **Implementation**: AST parsing for structural analysis, PEP 8 compliance checking

## Key Features Demonstrated

### Meta-Benchmark Approach
- **Integration over Innovation**: Uses existing evaluation methods rather than creating new datasets
- **Orchestration**: Combines multiple assessment techniques into unified framework
- **Extensibility**: Easy to add new evaluation methods or adjust weights

### Weighted Harmonic Mean Scoring
```python
QC = (Σ(w_j / (s_j + ε)))^(-1)
```
- **Shortest-Plank Principle**: Poor performance in any dimension significantly impacts overall score
- **Industrial Realism**: Reflects real-world engineering where all dimensions matter

### Quality Gate System
- **Pass** (≥0.8): Code meets quality standards
- **Conditional Pass** (0.6-0.8): Code needs improvements
- **Fail** (<0.6): Code requires significant improvements

## Usage Examples

### Basic Evaluation
```bash
python qc_framework/evaluate.py
```

### Detailed Analysis
```bash
python qc_framework/report.py
```

### Version Comparison
```bash
python compare_versions.py
```

### Complete Demo
```bash
python run_demo.py
```

## Sample Results

### Original Version Results
- **Correctness**: 1.000 (All tests pass)
- **Efficiency**: 0.993 (Fast execution, low memory)
- **Security**: 0.800 (Minor input validation concerns)
- **Conformance**: 0.667 (Missing documentation)
- **Overall QC**: 0.841 ✅ **PASS**

### Flawed Version Results
- **Correctness**: 0.000 (Import errors, test failures)
- **Efficiency**: 0.500 (Inefficient algorithms)
- **Security**: 0.400 (Multiple vulnerabilities)
- **Conformance**: 0.626 (Naming violations)
- **Overall QC**: 0.000 ❌ **FAIL**

## Educational Value

This sample demonstrates:

1. **Practical QC Assessment**: How to evaluate AI-generated code systematically
2. **Multi-Dimensional Quality**: Why single metrics (like test pass rate) are insufficient
3. **Industrial Standards**: What quality means in real software engineering contexts
4. **Framework Extensibility**: How to adapt QC evaluation to different contexts

## Integration with SPI

This QC framework serves as the foundational layer of the Symbiotic Programming Index:
- **Gatekeeper Function**: Code must meet QC standards before higher-level collaboration metrics apply
- **Baseline Quality**: Establishes minimum engineering standards for human-AI workflows
- **Continuous Assessment**: Enables ongoing quality monitoring throughout development

## Future Extensions

The framework can be extended with:
- **Additional Benchmarks**: Integration with more specialized evaluation datasets
- **Domain-Specific Weights**: Customizable dimension weights for different application contexts
- **Continuous Integration**: Automated QC assessment in development pipelines
- **Comparative Analysis**: Multi-model evaluation and ranking systems