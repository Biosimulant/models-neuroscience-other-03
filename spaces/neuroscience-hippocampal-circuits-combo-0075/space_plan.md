# Space Plan - neuroscience-hippocampal-circuits-combo-0075

## Scientific Scope
- Domain: neuroscience
- Theme: hippocampal_circuits
- Base models: neuroscience-other-amyloid-beta-osb87284-model, neuroscience-other-app-c-terminal-domain-alters-ca1-neuron-firing-osb256388-model, neuroscience-other-astro-fig-k-dynamics-fully-reconstructed-four-ca1-astrocytes-osb2019791-model, neuroscience-other-axonal-ectopic-burst-induced-by-repetitive-stimu-2018003-model

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
