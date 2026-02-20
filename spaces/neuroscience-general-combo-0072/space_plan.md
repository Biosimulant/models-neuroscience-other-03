# Space Plan - neuroscience-general-combo-0072

## Scientific Scope
- Domain: neuroscience
- Theme: general
- Base models: neuroscience-other-basal-ganglia-thalamic-network-deep-brain-stimulation-osb141699-model, neuroscience-other-beta-adrenergic-modulation-iks-guinea-pig-ventricle-osb120835-model, neuroscience-other-beta-cell-hubs-maintain-ca2-oscillations-in-huma-266497-model, neuroscience-other-binocular-energy-model-set-for-binocular-neurons-266560-model

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
