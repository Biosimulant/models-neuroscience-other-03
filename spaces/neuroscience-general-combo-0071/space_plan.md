# Space Plan - neuroscience-general-combo-0071

## Scientific Scope
- Domain: neuroscience
- Theme: general
- Base models: neuroscience-other-basal-ganglia-corticothalamic-bgct-network-chen-152113-model, neuroscience-other-basal-ganglia-corticothalamic-osb152113-model, neuroscience-other-basal-ganglia-motor-circuit-for-kinematic-planni-234313-model, neuroscience-other-basal-ganglia-motor-function-and-the-inverse-kin-232875-model

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
