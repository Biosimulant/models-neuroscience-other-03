# COMBO_0072 - Neuroscience General

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
- `neuroscience-other-basal-ganglia-thalamic-network-deep-brain-stimulation-osb141699-model`: Neuroscience: Model141699141699Model
- `neuroscience-other-beta-adrenergic-modulation-iks-guinea-pig-ventricle-osb120835-model`: Neuroscience: Model120835120835Model
- `neuroscience-other-beta-cell-hubs-maintain-ca2-oscillations-in-huma-266497-model`: Neuroscience: BetaCellHubsMaintainCa2OscillationsInHuma266497Model
- `neuroscience-other-binocular-energy-model-set-for-binocular-neurons-266560-model`: Neuroscience: BinocularEnergyModelSetForBinocularNeurons266560Model

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
- neuroscience-other-basal-ganglia-thalamic-network-deep-brain-stimulation-osb141699-model :: opensourcebrain:141699 :: https://github.com/OpenSourceBrain/141699
- neuroscience-other-beta-adrenergic-modulation-iks-guinea-pig-ventricle-osb120835-model :: opensourcebrain:120835 :: https://github.com/OpenSourceBrain/120835
- neuroscience-other-beta-cell-hubs-maintain-ca2-oscillations-in-huma-266497-model :: modeldb:266497 :: https://modeldb.science/266497
- neuroscience-other-binocular-energy-model-set-for-binocular-neurons-266560-model :: modeldb:266560 :: https://modeldb.science/266560

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
