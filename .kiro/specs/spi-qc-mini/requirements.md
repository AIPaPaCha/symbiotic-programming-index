# Requirements Document

## Introduction

The SPI-QC Mini project implements a minimal but complete reference implementation of the Code Quality dimension (Qc) from the Symbiotic Programming Index (SPI). This system measures software quality across four gates: Correctness, Efficiency, Security, and Conformance. The goal is to create a runnable repository that can evaluate a Flask CRUD application and function benchmarks, producing normalized quality scores, detailed reports, and visualizations.

## Requirements

### Requirement 1: Project Structure and Scaffolding

**User Story:** As a researcher or educator, I want a well-organized project structure that clearly separates concerns, so that I can easily understand and extend the QC measurement framework.

#### Acceptance Criteria

1. WHEN the project is created THEN the system SHALL create the exact directory structure: `spi-qc-min/container/{Dockerfile,entrypoint.sh}`, `qc_targets.yaml`, `rules/{flask_idioms.yaml,microservice.yaml}`, `bench/{humbene-mini.json,canonical_solutions.py,run_funcs.py,grade_funcs.py}`, `app/{src/*.py,tests/unit/*.py,tests/smoke/test_crud_roundtrip.py,openapi.yaml,requirements.txt}`, `qc/{run_build.py,run_perf.py,run_sec.py,run_conf.py,run_qc.py,utils.py}`, `scripts/{arch_checks.py,idiom_checks.py}`, `reports/.gitkeep`, `Makefile`, `README.md`
2. WHEN examining the codebase THEN each QC adapter script in `qc/` SHALL be ≤50 lines of code where feasible
3. WHEN the project is built THEN it SHALL target Python 3.11 with deterministic dependency installation

### Requirement 2: Flask CRUD Application Implementation

**User Story:** As a developer, I want a minimal but engineering-like Flask application that demonstrates real-world patterns, so that the QC system can evaluate realistic code quality scenarios.

#### Acceptance Criteria

1. WHEN the Flask app is implemented THEN it SHALL provide endpoints: `POST/GET/PUT/DELETE /todos` and `GET /healthz`
2. WHEN the app handles requests THEN it SHALL use in-memory storage for todo items with fields: `id`, `title`, `done`
3. WHEN the app processes requests THEN it SHALL include structured logging with request IDs via `logging_conf.py`
4. WHEN the app serves requests THEN it SHALL implement simple caching via `cache.py` and rate limiting via `rate_limit.py`
5. WHEN the API is documented THEN it SHALL provide `openapi.yaml` describing all endpoints and schemas
6. WHEN dependencies are managed THEN they SHALL be pinned in `app/requirements.txt`

### Requirement 3: Test Suite Implementation

**User Story:** As a quality engineer, I want comprehensive tests that validate both unit-level and integration-level functionality, so that the Correctness gate can measure test pass rates accurately.

#### Acceptance Criteria

1. WHEN unit tests are implemented THEN they SHALL include `tests/unit/test_models.py` for basic data operations
2. WHEN smoke tests are implemented THEN `tests/smoke/test_crud_roundtrip.py` SHALL start the app and perform a complete create→list→update→delete cycle
3. WHEN tests are executed THEN the smoke test success SHALL determine the `repo_exec` metric (1.0 for full success, 0.0 otherwise)
4. WHEN the build system runs THEN `pytest -q` pass rate SHALL determine the `compile` metric

### Requirement 4: Gate A - Correctness Measurement

**User Story:** As a researcher, I want to measure code correctness through both function-level benchmarks and repository-level build/test success, so that I can quantify basic functionality.

#### Acceptance Criteria

1. WHEN function benchmarks are executed THEN `bench/run_funcs.py` SHALL run 10 tasks from `humbene-mini.json` against canonical solutions in `bench/canonical_solutions.py`
2. WHEN function results are graded THEN `bench/grade_funcs.py` SHALL compute `exec_pass ∈ [0,1]` by comparing outputs to expected results
3. WHEN build quality is measured THEN the system SHALL compute `compile` as the pytest pass rate
4. WHEN repository execution is tested THEN the system SHALL compute `repo_exec` from smoke test success
5. WHEN Correctness is aggregated THEN it SHALL use harmonic mean: `Q_Corr = (β₁/exec_pass + β₂/compile + β₃/repo_exec)⁻¹` with weights from `qc_targets.yaml`

### Requirement 5: Gate B - Efficiency Measurement

**User Story:** As a performance engineer, I want to measure execution efficiency in terms of latency, memory usage, and throughput, so that I can identify performance bottlenecks.

#### Acceptance Criteria

1. WHEN efficiency is measured THEN `qc/run_perf.py` SHALL measure `lat_ms`, `mem_mb`, and `thr_ops` only on successful function tasks
2. WHEN measurements are taken THEN the system SHALL use `/usr/bin/time -v` or Python `resource` module for accurate metrics
3. WHEN throughput is calculated THEN it SHALL run N tasks in batch and compute ops/second
4. WHEN metrics are normalized THEN they SHALL use targets from `qc_targets.yaml` (50ms latency, 128MB memory, 100 QPS throughput)
5. WHEN Efficiency is aggregated THEN it SHALL use harmonic mean with gamma weights: `[0.5, 0.2, 0.3]` for latency, throughput, memory

### Requirement 6: Gate C - Security Measurement

**User Story:** As a security engineer, I want to detect security vulnerabilities and dependency issues, so that I can quantify security posture.

#### Acceptance Criteria

1. WHEN security scanning runs THEN `qc/run_sec.py` SHALL execute `bandit -q -r app/src -f json` and `pip-audit -r app/requirements.txt -f json`
2. WHEN vulnerabilities are planted THEN the system SHALL include `app/src/insecure_examples.py` with intentional issues: unsafe `eval()`, `subprocess.Popen(..., shell=True)`, and hardcoded secrets
3. WHEN detection is measured THEN `S_detect` SHALL be computed as detection rate against planted vulnerabilities
4. WHEN dependencies are audited THEN `S_deps` SHALL be the proportion of dependencies without known CVEs
5. WHEN repair is attempted THEN `S_repair` SHALL be set to 0.0 and documented as future work
6. WHEN Security is aggregated THEN it SHALL use delta weights: `[0.6, 0.2, 0.2]` for detect, repair, deps

### Requirement 7: Gate D - Conformance Measurement

**User Story:** As a code quality engineer, I want to measure adherence to coding standards, framework idioms, and architectural patterns, so that I can ensure maintainable code.

#### Acceptance Criteria

1. WHEN linting is performed THEN `qc/run_conf.py` SHALL run `flake8` and `black --check` to compute `C_lint` as average pass rate
2. WHEN idiom checking runs THEN `scripts/idiom_checks.py` SHALL validate Flask patterns from `rules/flask_idioms.yaml`
3. WHEN architecture is validated THEN `scripts/arch_checks.py` SHALL check microservice patterns from `rules/microservice.yaml`
4. WHEN idiom rules are evaluated THEN each rule SHALL pass if all `must_exist` files are present AND any `contains_any` pattern matches
5. WHEN architecture checks run THEN each check SHALL pass if any `grep_any` pattern is found in any listed path
6. WHEN Conformance is aggregated THEN it SHALL use zeta weights: `[0.5, 0.3, 0.2]` for lint, idiom, arch

### Requirement 8: Aggregation and Reporting

**User Story:** As a user, I want comprehensive reports with normalized scores, quality bands, and visual representations, so that I can quickly understand overall code quality.

#### Acceptance Criteria

1. WHEN QC runs THEN `qc/run_qc.py` SHALL orchestrate all four gates and collect raw metrics in `reports/qc_raw.json`
2. WHEN normalization occurs THEN the system SHALL apply `qc_targets.yaml` rules and output `reports/qc_norm.json`
3. WHEN final scores are computed THEN the system SHALL calculate `Q_Corr`, `Q_Eff`, `Q_Sec`, `Q_Conf` using harmonic means with epsilon=1e-6
4. WHEN overall quality is determined THEN `Qc` SHALL be computed using alpha weights: `[0.4, 0.2, 0.2, 0.2]`
5. WHEN reports are generated THEN the system SHALL produce `reports/report.md` with score tables and quality band labels
6. WHEN visualization is created THEN the system SHALL generate `reports/radar.png` using matplotlib
7. WHEN quality bands are assigned THEN scores ≥0.80 SHALL be "industrial-ready", ≥0.65 "prototype", else "research"

### Requirement 9: Build and Deployment System

**User Story:** As a user, I want simple commands to install, run QC analysis, and deploy the system, so that I can easily use the framework.

#### Acceptance Criteria

1. WHEN the Makefile is used THEN it SHALL provide targets: `install`, `qc`, `report`, `docker`, `ci`
2. WHEN `make install` runs THEN it SHALL install all required dependencies
3. WHEN `make qc` runs THEN it SHALL execute the complete QC pipeline and generate all reports
4. WHEN containerization is used THEN `container/Dockerfile` SHALL use `python:3.11-slim` base image
5. WHEN the container runs THEN `container/entrypoint.sh` SHALL install dependencies and execute QC analysis
6. WHEN resource limits are applied THEN the system SHALL document 2 vCPU, 4-8GB RAM requirements

### Requirement 10: Documentation and Usability

**User Story:** As a new user, I want clear documentation explaining how to use the system and understand the results, so that I can quickly get started and interpret outputs.

#### Acceptance Criteria

1. WHEN documentation is provided THEN `README.md` SHALL explain one-command usage with `make qc`
2. WHEN oracle sources are documented THEN the README SHALL explain benchmark tests, OpenAPI contracts, and rule files as quality oracles
3. WHEN configuration is explained THEN the README SHALL show how to modify `qc_targets.yaml` for custom targets
4. WHEN examples are provided THEN the README SHALL include expected output screenshots and score interpretations
5. WHEN the system runs successfully THEN `make install && make qc` SHALL produce all required outputs: `qc_raw.json`, `qc_norm.json`, `report.md`, `radar.png`

### Requirement 11: Non-Functional Requirements

**User Story:** As a maintainer, I need deterministic, reproducible runs on modest hardware, so that results are consistent across environments.

#### Acceptance Criteria

1. WHEN randomness is used THEN the system SHALL set `PYTHONHASHSEED=0` and explicit PRNG seeds in runner scripts
2. WHEN tasks execute THEN each function task SHALL finish within 2s and CRUD smoke test within 5s (configurable timeouts)
3. WHEN resource limits apply THEN the system SHALL succeed on 2 vCPU, 4-8GB RAM and document Docker usage with `--cpus="2" --memory="8g"`
4. WHEN network isolation is required THEN the QC pipeline SHALL NOT require outbound internet after `make install`
5. WHEN execution completes THEN `run_qc.py` SHALL exit 0 on success, non-zero on failure, with errors logged to `reports/qc_run.log`

### Requirement 12: CLI and Configuration Interface

**User Story:** As a power user, I want to customize QC execution without editing code, so that I can adapt the system to different scenarios.

#### Acceptance Criteria

1. WHEN CLI flags are used THEN `qc/run_qc.py` SHALL support `--targets`, `--solutions-dir`, `--attempt-repair`, `--report-md`, `--radar`, `--raw`, `--norm`
2. WHEN environment overrides are set THEN the system SHALL respect `QC_SEED`, `QC_CPUS`, `QC_MEM_MB` variables
3. WHEN external solutions are provided THEN `--solutions-dir external_solutions/` SHALL import functions from that directory instead of canonical solutions

### Requirement 13: Structured Output Formats

**User Story:** As an integrator, I want well-defined JSON schemas for all outputs, so that I can programmatically consume QC results.

#### Acceptance Criteria

1. WHEN raw metrics are output THEN `reports/qc_raw.json` SHALL include meta, gate_A, gate_B, gate_C, gate_D sections with timestamps and environment info
2. WHEN normalized results are output THEN `reports/qc_norm.json` SHALL include norm, Q_sub, Qc, bands, weights, targets, epsilon sections
3. WHEN precision is applied THEN all rates SHALL be rounded to 4 decimal places, milliseconds and MB to 1 decimal place
4. WHEN components are missing THEN absent metrics SHALL be set to 0.0 with notes in details sections

### Requirement 14: Report Layout and Presentation

**User Story:** As a reader, I want a compact, skimmable report that highlights key quality insights, so that I can quickly understand code quality status.

#### Acceptance Criteria

1. WHEN reports are generated THEN `report.md` SHALL include title block, summary table, raw metrics, normalization table, weights, radar chart, interpretation notes, and reproduction instructions
2. WHEN quality bands are assigned THEN Qc ≥0.80 SHALL be "Industrial-ready", ≥0.65 "Prototype", <0.65 "Research"
3. WHEN interpretation is provided THEN the report SHALL list top 3 penalties dragging Qc score
4. WHEN radar visualization is created THEN `radar.png` SHALL be embedded as local path reference

### Requirement 15: Failure and Degradation Handling

**User Story:** As a user, I want the system to gracefully handle missing tools or failed components, so that partial results are still useful.

#### Acceptance Criteria

1. WHEN pytest fails catastrophically THEN the system SHALL set `compile=0.0`, `repo_exec=0.0` and continue with other gates
2. WHEN security tools are missing THEN `S_detect`/`S_deps` SHALL default to 0.0 with error entries in `qc_run.log`
3. WHEN rule files are missing THEN `C_idiom=C_arch=0.0` SHALL be set with flags in report
4. WHEN any gate fails THEN the pipeline SHALL NOT abort unless artifacts cannot be written