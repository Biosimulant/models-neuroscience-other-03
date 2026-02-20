# Space Plan - neuroscience-general-combo-0063

## Scientific Scope
- Domain: neuroscience
- Theme: general
- Base models: neuroscience-other-arrhythmias-cardiac-cells-network-osb150691-model, neuroscience-other-arteriolar-networks-osb3785-model, neuroscience-other-arteriolar-networks-spread-of-potential-crane-et-3785-model, neuroscience-other-artificial-neuron-osb39948-model

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
