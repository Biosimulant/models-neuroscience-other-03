# Space Plan - neuroscience-general-combo-0061

## Scientific Scope
- Domain: neuroscience
- Theme: general
- Base models: neuroscience-other-anoxic-depolarization-recovery-osb187213-model, neuroscience-other-aob-mitral-cell-osb185332-model, neuroscience-other-aob-mitral-cell-persistent-activity-without-feed-185332-model, neuroscience-other-ap-back-prop-explains-threshold-variability-and-135839-model

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
