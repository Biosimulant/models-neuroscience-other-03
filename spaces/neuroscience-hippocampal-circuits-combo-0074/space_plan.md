# Space Plan - neuroscience-hippocampal-circuits-combo-0074

## Scientific Scope
- Domain: neuroscience
- Theme: hippocampal_circuits
- Base models: neuroscience-other-age-dependent-excitability-ca1-pyramidal-neurons-appps1-alzheimer-s-osb266848-model, neuroscience-other-age-dependent-excitability-of-ca1-pyramidal-neur-266848-model, neuroscience-other-amyloid-beta-effects-release-probability-integration-at-ca3-ca1-synapses-osb147757-model, neuroscience-other-amyloid-beta-ia-block-effects-on-a-model-ca1-pyr-87284-model

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
