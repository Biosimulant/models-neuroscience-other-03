# Space Plan - neuroscience-cortical-circuits-combo-0048

## Scientific Scope
- Domain: neuroscience
- Theme: cortical_circuits
- Base models: neuroscience-other-allen-institute-rorb-ires2-cre-d-visp-layer-5-47-184314-model, neuroscience-other-allen-institute-scnn1a-tg2-cre-visp-layer-4-4723-184166-model, neuroscience-other-allen-institute-scnn1a-tg2-cre-visp-layer-4-4724-184202-model

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
