# COMBO_0052 - Neuroscience Cortical Circuits

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
- `neuroscience-other-allen-institute-scnn1a-tg3-cre-visp-layer-5-4738-184341-model`: Neuroscience: AllenInstituteScnn1aTg3CreVispLayer54738184341Model
- `neuroscience-other-allen-institute-sst-ires-cre-visp-layer-2-3-4710-184157-model`: Neuroscience: AllenInstituteSstIresCreVispLayer234710184157Model
- `neuroscience-other-allen-institute-sst-ires-cre-visp-layer-2-3-4723-184173-model`: Neuroscience: AllenInstituteSstIresCreVispLayer234723184173Model

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
- neuroscience-other-allen-institute-scnn1a-tg3-cre-visp-layer-5-4738-184341-model :: modeldb:184341 :: https://modeldb.science/184341
- neuroscience-other-allen-institute-sst-ires-cre-visp-layer-2-3-4710-184157-model :: modeldb:184157 :: https://modeldb.science/184157
- neuroscience-other-allen-institute-sst-ires-cre-visp-layer-2-3-4723-184173-model :: modeldb:184173 :: https://modeldb.science/184173

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
