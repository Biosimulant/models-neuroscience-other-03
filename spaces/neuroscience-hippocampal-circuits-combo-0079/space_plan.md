# Space Plan - neuroscience-hippocampal-circuits-combo-0079

## Scientific Scope
- Domain: neuroscience
- Theme: hippocampal_circuits
- Base models: neuroscience-other-ca1-network-place-cell-dynamics-osb246546-model, neuroscience-other-ca1-oriens-alveus-interneurons-osb87546-model, neuroscience-other-ca1-oriens-alveus-interneurons-signaling-propert-87546-model, neuroscience-other-ca1-pv-fast-firing-hippocampal-interneuron-fergu-182843-model

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
