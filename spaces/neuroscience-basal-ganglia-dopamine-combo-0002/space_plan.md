# Space Plan - neuroscience-basal-ganglia-dopamine-combo-0002

## Scientific Scope
- Domain: neuroscience
- Theme: basal_ganglia_dopamine
- Base models: neuroscience-other-alternative-time-representation-in-dopamine-mode-124329-model, neuroscience-other-basal-ganglia-and-levodopa-pharmacodynamics-mode-261624-model

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
