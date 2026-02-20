# COMBO_0062 - Neuroscience General

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
- `neuroscience-other-ap-back-prop-osb135839-model`: Neuroscience: Model135839135839Model
- `neuroscience-other-ap-initiation-and-propagation-in-type-ii-cochlea-54903-model`: Neuroscience: ApInitiationAndPropagationInTypeIiCochlea54903Model
- `neuroscience-other-ap-shape-and-parameter-constraints-in-optimizati-87473-model`: Neuroscience: ApShapeAndParameterConstraintsInOptimizati87473Model
- `neuroscience-other-ap-shape-parameter-constraints-optimization-compartment-models-osb87473-model`: Neuroscience: Model8747387473Model

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
- neuroscience-other-ap-back-prop-osb135839-model :: opensourcebrain:135839 :: https://github.com/OpenSourceBrain/135839
- neuroscience-other-ap-initiation-and-propagation-in-type-ii-cochlea-54903-model :: modeldb:54903 :: https://modeldb.science/54903
- neuroscience-other-ap-shape-and-parameter-constraints-in-optimizati-87473-model :: modeldb:87473 :: https://modeldb.science/87473
- neuroscience-other-ap-shape-parameter-constraints-optimization-compartment-models-osb87473-model :: opensourcebrain:87473 :: https://github.com/OpenSourceBrain/87473

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
