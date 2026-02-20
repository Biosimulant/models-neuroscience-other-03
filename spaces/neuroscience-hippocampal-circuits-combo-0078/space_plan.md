# Space Plan - neuroscience-hippocampal-circuits-combo-0078

## Scientific Scope
- Domain: neuroscience
- Theme: hippocampal_circuits
- Base models: neuroscience-other-ca1-interneuron-osb20015-model, neuroscience-other-ca1-network-model-for-place-cell-dynamics-turi-e-246546-model, neuroscience-other-ca1-network-model-interneuron-contributions-to-e-256311-model, neuroscience-other-ca1-network-osb256311-model

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
