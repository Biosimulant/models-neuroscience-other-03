# Space Plan - neuroscience-hippocampal-circuits-combo-0077

## Scientific Scope
- Domain: neuroscience
- Theme: hippocampal_circuits
- Base models: neuroscience-other-bartosetal2002-bartosetal2002-model, neuroscience-other-behavioral-time-scale-synaptic-plasticity-underlies-ca1-place-fields-osb232074-model, neuroscience-other-biologically-plausible-models-for-spatial-naviga-64242-model, neuroscience-other-ca1-activity-during-working-memory-task-osb223962-model

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
