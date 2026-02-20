# COMBO_0077 - Neuroscience Hippocampal Circuits

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
- `neuroscience-other-bartosetal2002-bartosetal2002-model`: Neuroscience: Bartosetal2002Bartosetal2002Model
- `neuroscience-other-behavioral-time-scale-synaptic-plasticity-underlies-ca1-place-fields-osb232074-model`: Neuroscience: Model232074232074Model
- `neuroscience-other-biologically-plausible-models-for-spatial-naviga-64242-model`: Neuroscience: BiologicallyPlausibleModelsForSpatialNaviga64242Model
- `neuroscience-other-ca1-activity-during-working-memory-task-osb223962-model`: Neuroscience: Model223962223962Model

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
- neuroscience-other-bartosetal2002-bartosetal2002-model :: opensourcebrain:BartosEtAl2002 :: https://github.com/OpenSourceBrain/BartosEtAl2002
- neuroscience-other-behavioral-time-scale-synaptic-plasticity-underlies-ca1-place-fields-osb232074-model :: opensourcebrain:232074 :: https://github.com/OpenSourceBrain/232074
- neuroscience-other-biologically-plausible-models-for-spatial-naviga-64242-model :: modeldb:64242 :: https://modeldb.science/64242
- neuroscience-other-ca1-activity-during-working-memory-task-osb223962-model :: opensourcebrain:223962 :: https://github.com/OpenSourceBrain/223962

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
