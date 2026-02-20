# Space Plan - neuroscience-hippocampal-circuits-combo-0076

## Scientific Scope
- Domain: neuroscience
- Theme: hippocampal_circuits
- Base models: neuroscience-other-axonal-k-channel-inhibition-promotes-ectopic-bur-2015571-model, neuroscience-other-axonal-k-channel-inhibition-promotes-ectopic-burst-hippocampal-mossy-fiber-osb2015571-model, neuroscience-other-axonal-nav1-osb115356-model, neuroscience-other-axonal-subthreshold-voltage-signaling-along-hippocampal-mossy-fiber-osb267512-model

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
