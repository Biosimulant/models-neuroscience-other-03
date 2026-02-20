# COMBO_0079 - Neuroscience Hippocampal Circuits

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
- `neuroscience-other-ca1-network-place-cell-dynamics-osb246546-model`: Neuroscience: Model246546246546Model
- `neuroscience-other-ca1-oriens-alveus-interneurons-osb87546-model`: Neuroscience: Model8754687546Model
- `neuroscience-other-ca1-oriens-alveus-interneurons-signaling-propert-87546-model`: Neuroscience: Ca1OriensAlveusInterneuronsSignalingPropert87546Model
- `neuroscience-other-ca1-pv-fast-firing-hippocampal-interneuron-fergu-182843-model`: Neuroscience: Ca1PvFastFiringHippocampalInterneuronFergu182843Model

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
- neuroscience-other-ca1-network-place-cell-dynamics-osb246546-model :: opensourcebrain:246546 :: https://github.com/OpenSourceBrain/246546
- neuroscience-other-ca1-oriens-alveus-interneurons-osb87546-model :: opensourcebrain:87546 :: https://github.com/OpenSourceBrain/87546
- neuroscience-other-ca1-oriens-alveus-interneurons-signaling-propert-87546-model :: modeldb:87546 :: https://modeldb.science/87546
- neuroscience-other-ca1-pv-fast-firing-hippocampal-interneuron-fergu-182843-model :: modeldb:182843 :: https://modeldb.science/182843

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
