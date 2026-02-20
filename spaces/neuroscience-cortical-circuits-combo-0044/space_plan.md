# Space Plan - neuroscience-cortical-circuits-combo-0044

## Scientific Scope
- Domain: neuroscience
- Theme: cortical_circuits
- Base models: neuroscience-other-allen-institute-pvalb-ires-cre-visp-layer-5-4729-184310-model, neuroscience-other-allen-institute-pvalb-ires-cre-visp-layer-5-4734-184350-model, neuroscience-other-allen-institute-pvalb-ires-cre-visp-layer-5-4738-184325-model

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
