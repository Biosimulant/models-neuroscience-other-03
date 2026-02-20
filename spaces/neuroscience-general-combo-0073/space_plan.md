# Space Plan - neuroscience-general-combo-0073

## Scientific Scope
- Domain: neuroscience
- Theme: general
- Base models: neuroscience-other-biochemical-systems-theory-model-of-sars-cov-2-i-267736-model, neuroscience-other-biochemical-systems-theory-model-of-tnfa-related-267735-model, neuroscience-other-biologically-constrained-basal-ganglia-model-bcb-150206-model, neuroscience-other-biologically-constrained-basal-ganglia-osb150206-model

## Wiring Plan
- Comparative mode with monitor-only routing.
- Each base model state-like output connects to monitor ports `state_a..state_d`.
- No direct causal links among base models unless explicitly upgraded later.

## Visualization Plan
- Include `StateComparisonMonitor` and `StateMetricsMonitor`.
- Require at least:
  - one timeseries visual,
  - one summary table visual.

## Validation Gates
- space schema validity
- wiring endpoint validity
- smoke run success
- repo manifest/entrypoint validators pass
