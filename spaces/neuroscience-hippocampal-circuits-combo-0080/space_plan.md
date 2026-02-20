# Space Plan - neuroscience-hippocampal-circuits-combo-0080

## Scientific Scope
- Domain: neuroscience
- Theme: hippocampal_circuits
- Base models: neuroscience-other-ca1-pv-fast-firing-hippocampal-interneuron-osb182843-model, neuroscience-other-ca1-pyr-cell-inhibitory-modulation-of-spatial-se-225080-model, neuroscience-other-ca1-pyr-cell-osb225080-model, neuroscience-other-ca1-pyr-cell-osb267680-model

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
