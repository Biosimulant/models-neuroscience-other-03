# Space Plan - neuroscience-cortical-circuits-combo-0052

## Scientific Scope
- Domain: neuroscience
- Theme: cortical_circuits
- Base models: neuroscience-other-allen-institute-scnn1a-tg3-cre-visp-layer-5-4738-184341-model, neuroscience-other-allen-institute-sst-ires-cre-visp-layer-2-3-4710-184157-model, neuroscience-other-allen-institute-sst-ires-cre-visp-layer-2-3-4723-184173-model

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
