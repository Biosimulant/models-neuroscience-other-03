# Space Plan - neuroscience-general-combo-0060

## Scientific Scope
- Domain: neuroscience
- Theme: general
- Base models: neuroscience-other-analyzing-neural-time-series-data-theory-and-pra-154927-model, neuroscience-other-analyzing-neural-time-series-data-theory-practice-osb154927-model, neuroscience-other-angii-signaling-membrane-electrophysiology-osb156830-model, neuroscience-other-anoxic-depolarization-recovery-effect-of-brain-r-187213-model

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
