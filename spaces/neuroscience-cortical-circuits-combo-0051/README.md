# COMBO_0051 - Neuroscience Cortical Circuits

## Scientific Question
How do cortical circuit motifs transform and propagate activity?

## Biological Context
Neuronal dynamics, network signaling, and emergent circuit behavior.

## Mechanistic Assumptions
- Model implementations are used as published in their curated manifests without biological reinterpretation.
- Time integration uses a shared global tick compatible with model min_dt constraints.
- Comparative (non-causal) mode is used because full deterministic IO coverage for causal coupling was not satisfied.

## Why These Models Belong Together
The combination was selected from a shared domain/theme bucket with deterministic compatibility checks.
- `neuroscience-other-allen-institute-scnn1a-tg3-cre-visp-layer-4-4738-184344-model`: Neuroscience: AllenInstituteScnn1aTg3CreVispLayer44738184344Model
- `neuroscience-other-allen-institute-scnn1a-tg3-cre-visp-layer-5-4724-184305-model`: Neuroscience: AllenInstituteScnn1aTg3CreVispLayer54724184305Model
- `neuroscience-other-allen-institute-scnn1a-tg3-cre-visp-layer-5-4738-184335-model`: Neuroscience: AllenInstituteScnn1aTg3CreVispLayer54738184335Model

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
- neuroscience-other-allen-institute-scnn1a-tg3-cre-visp-layer-4-4738-184344-model :: modeldb:184344 :: https://modeldb.science/184344
- neuroscience-other-allen-institute-scnn1a-tg3-cre-visp-layer-5-4724-184305-model :: modeldb:184305 :: https://modeldb.science/184305
- neuroscience-other-allen-institute-scnn1a-tg3-cre-visp-layer-5-4738-184335-model :: modeldb:184335 :: https://modeldb.science/184335

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
