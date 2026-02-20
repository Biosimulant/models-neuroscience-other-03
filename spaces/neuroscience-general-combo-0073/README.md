# COMBO_0073 - Neuroscience General

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
- `neuroscience-other-biochemical-systems-theory-model-of-sars-cov-2-i-267736-model`: Neuroscience: BiochemicalSystemsTheoryModelOfSarsCov2I267736Model
- `neuroscience-other-biochemical-systems-theory-model-of-tnfa-related-267735-model`: Neuroscience: BiochemicalSystemsTheoryModelOfTnfaRelated267735Model
- `neuroscience-other-biologically-constrained-basal-ganglia-model-bcb-150206-model`: Neuroscience: BiologicallyConstrainedBasalGangliaModelBcb150206Model
- `neuroscience-other-biologically-constrained-basal-ganglia-osb150206-model`: Neuroscience: Model150206150206Model

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
- neuroscience-other-biochemical-systems-theory-model-of-sars-cov-2-i-267736-model :: modeldb:267736 :: https://modeldb.science/267736
- neuroscience-other-biochemical-systems-theory-model-of-tnfa-related-267735-model :: modeldb:267735 :: https://modeldb.science/267735
- neuroscience-other-biologically-constrained-basal-ganglia-model-bcb-150206-model :: modeldb:150206 :: https://modeldb.science/150206
- neuroscience-other-biologically-constrained-basal-ganglia-osb150206-model :: opensourcebrain:150206 :: https://github.com/OpenSourceBrain/150206

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
