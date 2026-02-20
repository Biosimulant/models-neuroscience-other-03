# COMBO_0068 - Neuroscience General

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
- `neuroscience-other-axon-growth-osb187687-model`: Neuroscience: Model187687187687Model
- `neuroscience-other-axon-somatic-back-propagation-detailed-cat-spinal-motoneuron-osb180370-model`: Neuroscience: Model180370180370Model
- `neuroscience-other-axon-somatic-back-propagation-in-a-detailed-mode-180370-model`: Neuroscience: AxonSomaticBackPropagationInADetailedMode180370Model
- `neuroscience-other-axonal-gap-junctions-produce-fast-oscillations-cerebellar-purkinje-cells-osb114654-model`: Neuroscience: Model114654114654Model

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
- neuroscience-other-axon-growth-osb187687-model :: opensourcebrain:187687 :: https://github.com/OpenSourceBrain/187687
- neuroscience-other-axon-somatic-back-propagation-detailed-cat-spinal-motoneuron-osb180370-model :: opensourcebrain:180370 :: https://github.com/OpenSourceBrain/180370
- neuroscience-other-axon-somatic-back-propagation-in-a-detailed-mode-180370-model :: modeldb:180370 :: https://modeldb.science/180370
- neuroscience-other-axonal-gap-junctions-produce-fast-oscillations-cerebellar-purkinje-cells-osb114654-model :: opensourcebrain:114654 :: https://github.com/OpenSourceBrain/114654

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
