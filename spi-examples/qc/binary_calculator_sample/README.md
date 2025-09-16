# Binary Calculator QC Sample Project

This project demonstrates the **Symbiotic Programming Index - Code Quality (SPI-QC)** framework by evaluating AI-generated binary calculator implementations across four quality dimensions.

## Quick Start

Run the complete demo:
```bash
python run_demo.py
```

Or run individual components:
```bash
# Basic QC evaluation
python qc_framework/evaluate.py

# Detailed analysis report
python qc_framework/report.py

# Compare different versions
python compare_versions.py
```

## Project Structure

- `ai_generated/` - Simulated AI-generated binary calculators
  - `binary_calculator.py` - Original version (realistic AI output)
  - `binary_calculator_flawed.py` - Flawed version (for comparison)
- `qc_framework/` - QC evaluation system implementation
- `tests/` - Comprehensive test suite for correctness evaluation
- `results/` - QC evaluation results and reports
- `SAMPLE_EXPLANATION.md` - Detailed project documentation

## QC Dimensions Evaluated

1. **Correctness** (25%) - Functional tests with comprehensive edge cases
2. **Efficiency** (25%) - Runtime and memory profiling
3. **Security** (25%) - Static analysis for vulnerability patterns
4. **Conformance** (25%) - Code style, documentation, and engineering standards

## Sample Results

The framework successfully differentiates between code quality levels:

| Version | Correctness | Efficiency | Security | Conformance | Overall | Status |
|---------|-------------|------------|----------|-------------|---------|--------|
| Original | 1.000 | 0.993 | 0.800 | 0.667 | **0.841** | ✅ PASS |
| Flawed | 0.000 | 0.500 | 0.400 | 0.626 | **0.000** | ❌ FAIL |

## Key Features

- **Meta-benchmark approach**: Integrates existing evaluation methods
- **Weighted harmonic mean**: Ensures no quality dimension can be ignored
- **Industrial realism**: Reflects real-world engineering standards
- **Actionable insights**: Provides specific recommendations for improvement