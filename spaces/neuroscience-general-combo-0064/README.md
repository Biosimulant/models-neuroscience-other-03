# COMBO_0064 - Neuroscience General

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
- `neuroscience-other-astrocyte-and-blood-vessel-calcium-imaging-track-266929-model`: Neuroscience: AstrocyteAndBloodVesselCalciumImagingTrack266929Model
- `neuroscience-other-asynchronous-irregular-and-up-down-states-in-exc-126466-model`: Neuroscience: AsynchronousIrregularAndUpDownStatesInExc126466Model
- `neuroscience-other-asynchronous-irregular-up-down-states-excitatory-inhibitory-nns-osb126466-model`: Neuroscience: Model126466126466Model
- `neuroscience-other-attractor-network-grid-cells-theta-nested-gamma-oscillations-osb150031-model`: Neuroscience: Model150031150031Model

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
- neuroscience-other-astrocyte-and-blood-vessel-calcium-imaging-track-266929-model :: modeldb:266929 :: https://modeldb.science/266929
- neuroscience-other-asynchronous-irregular-and-up-down-states-in-exc-126466-model :: modeldb:126466 :: https://modeldb.science/126466
- neuroscience-other-asynchronous-irregular-up-down-states-excitatory-inhibitory-nns-osb126466-model :: opensourcebrain:126466 :: https://github.com/OpenSourceBrain/126466
- neuroscience-other-attractor-network-grid-cells-theta-nested-gamma-oscillations-osb150031-model :: opensourcebrain:150031 :: https://github.com/OpenSourceBrain/150031

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
