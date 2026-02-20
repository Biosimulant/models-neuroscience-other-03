# Space Plan - neuroscience-cortical-circuits-combo-0045

## Scientific Scope
- Domain: neuroscience
- Theme: cortical_circuits
- Base models: neuroscience-other-allen-institute-pvalb-ires-cre-visp-layer-6a-471-184145-model, neuroscience-other-allen-institute-pvalb-ires-cre-visp-layer-6a-472-184168-model, neuroscience-other-allen-institute-pvalb-ires-cre-visp-layer-6a-473-184323-model

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
