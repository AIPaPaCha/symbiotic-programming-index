# Implementation Plan

## Milestones

**M1: Foundation & Benchmarks** (Tasks 1-2)
- Project scaffolding and configuration
- Function benchmark system with canonical solutions

**M2: Sample Application** (Tasks 3-4)  
- Flask CRUD app with engineering patterns
- Comprehensive test suite

**M3: Quality Gates** (Tasks 5-8)
- All four measurement dimensions (Correctness, Efficiency, Security, Conformance)
- Rule engines and measurement adapters

**M4: Aggregation & Orchestration** (Tasks 9-10)
- Utility functions and report generation
- Main orchestrator with CLI and error handling

**M5: Deployment & Validation** (Tasks 11-14)
- Container setup and build system
- Documentation and end-to-end validation

- [ ] 1. Set up project structure and configuration files
  - Create the exact directory structure as specified in requirements
  - Implement `qc_targets.yaml` with default weights, targets, and bands
  - Create `.gitkeep` files and basic `Makefile` structure
  - _Requirements: 1.1, 1.2_

- [ ] 2. Implement benchmark system and canonical solutions
- [ ] 2.1 Create function benchmark data and canonical solutions
  - Write `bench/humbene-mini.json` with 10 algorithmic problems and test cases
  - Implement `bench/canonical_solutions.py` with reference implementations for all 10 functions
  - Ensure each function handles edge cases and matches expected outputs exactly
  - _Requirements: 4.1, 4.2_

- [ ] 2.2 Build function execution and grading system
  - Write `bench/run_funcs.py` to dynamically import and execute canonical solutions against JSON test cases
  - Implement `bench/grade_funcs.py` to compute exec_pass ratio by comparing outputs to expected results
  - Add timeout handling (2s per function) and error capture for failed executions
  - _Requirements: 4.1, 4.2, 11.2_

- [ ] 3. Create Flask CRUD application with engineering patterns
- [ ] 3.1 Implement core Flask application structure
  - Write `app/src/app.py` with Blueprint setup and route definitions for CRUD endpoints
  - Create `app/src/models.py` with TodoItem dataclass and in-memory storage operations
  - Implement all required endpoints: POST/GET/PUT/DELETE /todos and GET /healthz
  - _Requirements: 2.1, 2.2_

- [ ] 3.2 Add engineering middleware and utilities
  - Implement `app/src/logging_conf.py` with structured logging and request ID propagation
  - Create `app/src/cache.py` with simple in-memory caching using lru_cache or similar
  - Write `app/src/rate_limit.py` with basic rate limiting middleware
  - _Requirements: 2.3, 2.4_

- [ ] 3.3 Create API documentation and dependencies
  - Write `app/openapi.yaml` with complete OpenAPI 3.0 specification for all endpoints and schemas
  - Create `app/requirements.txt` with pinned dependencies for Flask and required packages
  - Ensure OpenAPI spec accurately reflects all endpoint behaviors and data models
  - _Requirements: 2.5, 2.6_

- [ ] 3.4 Plant security vulnerabilities for testing
  - Create `app/src/insecure_examples.py` with intentional security issues: eval(), subprocess with shell=True, hardcoded secrets
  - Import the insecure module in main app to ensure Bandit scans it
  - Keep vulnerabilities isolated and non-executable in normal operation
  - _Requirements: 6.2_

- [ ] 4. Implement comprehensive test suite
- [ ] 4.1 Create unit tests for core functionality
  - Write `app/tests/unit/test_models.py` with tests for TodoItem CRUD operations
  - Test edge cases, validation, and error conditions in data models
  - Ensure tests cover all business logic and data manipulation functions
  - _Requirements: 3.1_

- [ ] 4.2 Build integration smoke tests
  - Implement `app/tests/smoke/test_crud_roundtrip.py` with complete create→list→update→delete cycle
  - Use Flask test client to start app and perform full API workflow
  - Add timeout handling (5s) and clear pass/fail determination for repo_exec metric
  - _Requirements: 3.2, 3.3, 11.2_

- [ ] 5. Create stub gate adapters for early integration testing
  - Write stub versions of `qc/run_build.py`, `qc/run_perf.py`, `qc/run_sec.py`, `qc/run_conf.py` that return dummy metrics
  - Create basic `qc/run_qc.py` orchestrator that calls all stubs and produces sample JSON output
  - Implement `qc/utils.py` with normalization and aggregation functions using dummy data
  - Test end-to-end pipeline flow before implementing actual measurements
  - _Requirements: 8.1, 8.2_

- [ ] 6. Build Gate A - Correctness measurement system
  - Replace stub `qc/run_build.py` with real implementation to execute pytest and compute compile pass rate
  - Integrate with benchmark system to collect exec_pass from bench/grade_funcs.py
  - Determine repo_exec from smoke test results (1.0 for success, 0.0 for failure)
  - Implement harmonic mean aggregation for Q_Corr using beta weights
  - _Requirements: 4.3, 4.4, 4.5_

- [ ] 7. Build Gate B - Efficiency measurement system
  - Implement `qc/run_perf.py` to measure latency, memory, and throughput on successful function tasks
  - Use `/usr/bin/time -v` or Python resource module for accurate resource measurement
  - Calculate batch throughput by running N tasks and computing ops/second
  - Average metrics across all successful tasks and handle measurement failures gracefully
  - _Requirements: 5.1, 5.2, 5.3, 5.4, 5.5_

- [ ] 8. Build Gate C - Security measurement system
  - Write `qc/run_sec.py` to execute bandit and pip-audit with JSON output
  - Implement S_detect calculation based on detection rate of planted vulnerabilities
  - Calculate S_deps from pip-audit results as proportion of clean dependencies
  - Set S_repair to 0.0 with stub for future implementation and proper documentation
  - _Requirements: 6.1, 6.3, 6.4, 6.5, 6.6_

- [ ] 9. Build Gate D - Conformance measurement system
- [ ] 9.1 Create rule engine scripts
  - Write `scripts/idiom_checks.py` to validate Flask idioms from rules/flask_idioms.yaml
  - Implement `scripts/arch_checks.py` to check microservice patterns from rules/microservice.yaml
  - Each script should output pass/total ratios and handle missing files gracefully
  - _Requirements: 7.2, 7.3, 7.4, 7.5_

- [ ] 9.2 Implement conformance measurement orchestration
  - Write `qc/run_conf.py` to execute flake8, black --check, and custom rule engines
  - Calculate C_lint as average pass rate of linting tools
  - Compute C_idiom and C_arch from rule engine outputs
  - Aggregate using zeta weights for final Q_Conf score
  - _Requirements: 7.1, 7.6_

- [ ] 9.3 Create rule configuration files
  - Write `rules/flask_idioms.yaml` with 8 Flask framework pattern rules
  - Create `rules/microservice.yaml` with 7 microservice architecture checks
  - Ensure rules are realistic and achievable by the sample Flask application
  - _Requirements: 7.2, 7.3_

- [ ] 10. Enhance aggregation and utility system
- [ ] 10.1 Replace stub aggregation utilities with full implementation
  - Write `qc/utils.py` with normalization functions using targets from qc_targets.yaml
  - Implement harmonic mean calculation with epsilon handling for division by zero
  - Create quality score computation functions for all four gates
  - Add precision handling: 4 decimal places for ratios, 1 decimal for ms/MB
  - _Requirements: 8.3, 13.3_

- [ ] 10.2 Build report generation system
  - Implement markdown report generation with all required sections: summary, raw metrics, normalization, weights, interpretation
  - Create radar chart visualization using matplotlib with proper scaling and labels
  - Add quality band assignment logic and top penalty identification
  - Generate structured JSON outputs with complete metadata and environment info
  - _Requirements: 8.5, 8.6, 8.7, 14.1, 14.2, 14.3_

- [ ] 11. Enhance main orchestration system
- [ ] 11.1 Replace stub orchestrator with full CLI interface
  - Write `qc/run_qc.py` as main entry point with argument parsing for all CLI flags
  - Implement gate execution coordination with proper error handling and logging
  - Add environment variable support for QC_SEED, QC_CPUS, QC_MEM_MB
  - Create structured logging to reports/qc_run.log with timestamps and error details
  - _Requirements: 8.1, 8.2, 12.1, 12.2, 11.5_

- [ ] 11.2 Implement error handling and degradation
  - Add graceful degradation for failed gates (set metrics to 0.0, continue pipeline)
  - Handle missing tools by setting appropriate metrics to 0.0 with error logging
  - Implement timeout handling for all external tool executions
  - Ensure pipeline produces artifacts even with partial failures
  - _Requirements: 15.1, 15.2, 15.3, 15.4_

- [ ] 12. Build containerization and build system
- [ ] 12.1 Create Docker container setup
  - Write `container/Dockerfile` using python:3.11-slim with non-root user
  - Implement `container/entrypoint.sh` to install dependencies and run QC pipeline
  - Add resource limit documentation and ulimit configurations
  - Test container execution with --cpus="2" --memory="8g" constraints
  - _Requirements: 9.4, 9.5, 11.3_

- [ ] 12.2 Complete Makefile with all targets
  - Implement install, qc, report, docker targets with proper dependencies
  - Add ci target that uploads artifacts (qc_raw.json, qc_norm.json, report.md, radar.png) for GitHub Actions integration
  - Add error handling and status reporting for each target
  - Ensure make qc produces all required output artifacts
  - Test complete workflow from clean environment
  - _Requirements: 9.1, 9.2, 9.3_

- [ ] 13. Create comprehensive documentation
  - Write `README.md` with quickstart instructions, oracle explanations, and configuration guidance
  - Include example outputs, quality band explanations, and troubleshooting guide
  - Document resource requirements, Docker usage, and CI integration examples
  - Add configuration customization examples for qc_targets.yaml
  - _Requirements: 10.1, 10.2, 10.3, 10.4, 10.5_

- [ ] 14. Implement determinism and validation
  - Add PYTHONHASHSEED=0 and explicit random seeds to all execution scripts
  - Implement timeout enforcement for all external tool calls and test executions
  - Add network isolation verification (no outbound calls after install)
  - Create end-to-end validation test to ensure complete pipeline produces expected artifacts
  - _Requirements: 11.1, 11.2, 11.4_

- [ ] 15. Final integration and testing
  - Create `examples/expected_output/` folder with sample qc_raw.json, qc_norm.json, report.md for validation reference
  - Run complete pipeline from clean environment to verify all requirements
  - Compare actual outputs to expected examples to ensure correctness
  - Test error scenarios and degradation modes to ensure robust operation
  - Validate JSON schema compliance and precision requirements for all outputs
  - Verify harmonic mean penalty behavior when individual gates perform poorly
  - _Requirements: 8.4, 13.1, 13.2, 13.4_

## Future Work (Out of Scope for v1)

- **Language Extensions**: Java/Node.js support with Maven/npm integration
- **S_repair Implementation**: Automated vulnerability fixing with model-based repair
- **Advanced Visualizations**: HTML dashboards, CSV exports, Grafana integration
- **Enterprise Features**: SonarQube plugins, database storage, trend analysis
- **Performance Optimization**: Parallel gate execution, caching, incremental analysis