# COMBO_0080 - Neuroscience Hippocampal Circuits

## Scientific Question
How do recurrent hippocampal motifs shape network dynamics over time?

## Biological Context
Neuronal dynamics, network signaling, and emergent circuit behavior.

## Mechanistic Assumptions
- Model implementations are used as published in their curated manifests without biological reinterpretation.
- Time integration uses a shared global tick compatible with model min_dt constraints.
- Comparative (non-causal) mode is used because full deterministic IO coverage for causal coupling was not satisfied.

## Why These Models Belong Together
The combination was selected from a shared domain/theme bucket with deterministic compatibility checks.
- `neuroscience-other-ca1-pv-fast-firing-hippocampal-interneuron-osb182843-model`: Neuroscience: Model182843182843Model
- `neuroscience-other-ca1-pyr-cell-inhibitory-modulation-of-spatial-se-225080-model`: Neuroscience: Ca1PyrCellInhibitoryModulationOfSpatialSe225080Model
- `neuroscience-other-ca1-pyr-cell-osb225080-model`: Neuroscience: Model225080225080Model
- `neuroscience-other-ca1-pyr-cell-osb267680-model`: Neuroscience: Model267680267680Model

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
- neuroscience-other-ca1-pv-fast-firing-hippocampal-interneuron-osb182843-model :: opensourcebrain:182843 :: https://github.com/OpenSourceBrain/182843
- neuroscience-other-ca1-pyr-cell-inhibitory-modulation-of-spatial-se-225080-model :: modeldb:225080 :: https://modeldb.science/225080
- neuroscience-other-ca1-pyr-cell-osb225080-model :: opensourcebrain:225080 :: https://github.com/OpenSourceBrain/225080
- neuroscience-other-ca1-pyr-cell-osb267680-model :: opensourcebrain:267680 :: https://github.com/OpenSourceBrain/267680

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
