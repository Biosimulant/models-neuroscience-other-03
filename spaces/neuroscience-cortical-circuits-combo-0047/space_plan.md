# Space Plan - neuroscience-cortical-circuits-combo-0047

## Scientific Scope
- Domain: neuroscience
- Theme: cortical_circuits
- Base models: neuroscience-other-allen-institute-rorb-ires2-cre-d-visp-layer-2-3-184231-model, neuroscience-other-allen-institute-rorb-ires2-cre-d-visp-layer-4-47-184333-model, neuroscience-other-allen-institute-rorb-ires2-cre-d-visp-layer-5-47-184159-model

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
