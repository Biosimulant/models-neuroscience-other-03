# Space Plan - neuroscience-general-combo-0056

## Scientific Scope
- Domain: neuroscience
- Theme: general
- Base models: neuroscience-other-alcohol-action-in-a-detailed-purkinje-neuron-mod-180789-model, neuroscience-other-alcohol-excites-cerebellar-golgi-cells-by-inhibi-127021-model, neuroscience-other-alcohol-excites-cerebellar-golgi-cells-inhibiting-na-k-atpase-osb127021-model, neuroscience-other-alleviating-catastrophic-forgetting-context-gati-256370-model

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
