# Space Plan - neuroscience-general-combo-0064

## Scientific Scope
- Domain: neuroscience
- Theme: general
- Base models: neuroscience-other-astrocyte-and-blood-vessel-calcium-imaging-track-266929-model, neuroscience-other-asynchronous-irregular-and-up-down-states-in-exc-126466-model, neuroscience-other-asynchronous-irregular-up-down-states-excitatory-inhibitory-nns-osb126466-model, neuroscience-other-attractor-network-grid-cells-theta-nested-gamma-oscillations-osb150031-model

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
