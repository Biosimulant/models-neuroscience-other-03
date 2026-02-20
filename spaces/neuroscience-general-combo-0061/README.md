# COMBO_0061 - Neuroscience General

## Scientific Question
How do general mechanisms compare across these models?

## Biological Context
Neuronal dynamics, network signaling, and emergent circuit behavior.

## Mechanistic Assumptions
- Model implementations are used as published in their curated manifests without biological reinterpretation.
- Time integration uses a shared global tick compatible with model min_dt constraints.
- Comparative (non-causal) mode is used because full deterministic IO coverage for causal coupling was not satisfied.

## Why These Models Belong Together
The combination was selected from a shared domain/theme bucket with deterministic compatibility checks.
- `neuroscience-other-anoxic-depolarization-recovery-osb187213-model`: Neuroscience: Model187213187213Model
- `neuroscience-other-aob-mitral-cell-osb185332-model`: Neuroscience: Model185332185332Model
- `neuroscience-other-aob-mitral-cell-persistent-activity-without-feed-185332-model`: Neuroscience: AobMitralCellPersistentActivityWithoutFeed185332Model
- `neuroscience-other-ap-back-prop-explains-threshold-variability-and-135839-model`: Neuroscience: ApBackPropExplainsThresholdVariabilityAnd135839Model

## Wiring Rationale
- Comparative (non-causal) mode: no direct causal links were created.

## Visualization Strategy
- Monitor-driven visualization is required for this space.
- State streams are routed into explicit monitor ports (`state_a..state_d`) to avoid signal overwrite.
- At minimum, monitor visuals include one timeseries panel and one summary table.
- Rationale: A dedicated monitor model receives all participating model state streams (`state_a..state_d`) so trajectories can be compared in one place without claiming causal coupling when IO semantics are incomplete.

## Expected Behaviors
- Model output trajectories under shared runtime settings.
- Cross-model agreement/divergence in key state or metric signals.
- Relative behavior comparison without causal linkage claims.

## Known Limitations
- No new biology is introduced beyond what upstream models encode.
- Cross-model semantic matching is rule-based and may under-connect uncertain routes.

## Source Provenance
- neuroscience-other-anoxic-depolarization-recovery-osb187213-model :: opensourcebrain:187213 :: https://github.com/OpenSourceBrain/187213
- neuroscience-other-aob-mitral-cell-osb185332-model :: opensourcebrain:185332 :: https://github.com/OpenSourceBrain/185332
- neuroscience-other-aob-mitral-cell-persistent-activity-without-feed-185332-model :: modeldb:185332 :: https://modeldb.science/185332
- neuroscience-other-ap-back-prop-explains-threshold-variability-and-135839-model :: modeldb:135839 :: https://modeldb.science/135839

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
