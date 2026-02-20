# COMBO_0070 - Neuroscience General

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
- `neuroscience-other-axonal-spheroids-and-conduction-defects-in-alzhe-185864-model`: Neuroscience: AxonalSpheroidsAndConductionDefectsInAlzhe185864Model
- `neuroscience-other-axonal-spheroids-conduction-defects-alzheimer-s-disease-osb185864-model`: Neuroscience: Model185864185864Model
- `neuroscience-other-axonal-subthreshold-voltage-signaling-along-hipp-267512-model`: Neuroscience: AxonalSubthresholdVoltageSignalingAlongHipp267512Model
- `neuroscience-other-balance-excitation-inhibition-osb125689-model`: Neuroscience: Model125689125689Model

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
- neuroscience-other-axonal-spheroids-and-conduction-defects-in-alzhe-185864-model :: modeldb:185864 :: https://modeldb.science/185864
- neuroscience-other-axonal-spheroids-conduction-defects-alzheimer-s-disease-osb185864-model :: opensourcebrain:185864 :: https://github.com/OpenSourceBrain/185864
- neuroscience-other-axonal-subthreshold-voltage-signaling-along-hipp-267512-model :: modeldb:267512 :: https://modeldb.science/267512
- neuroscience-other-balance-excitation-inhibition-osb125689-model :: opensourcebrain:125689 :: https://github.com/OpenSourceBrain/125689

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
