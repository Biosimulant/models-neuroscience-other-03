# COMBO_0069 - Neuroscience General

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
- `neuroscience-other-axonal-gap-junctions-produce-fast-oscillations-i-114654-model`: Neuroscience: AxonalGapJunctionsProduceFastOscillationsI114654Model
- `neuroscience-other-axonal-hh-model-for-temperature-stimulation-frib-189155-model`: Neuroscience: AxonalHhModelForTemperatureStimulationFrib189155Model
- `neuroscience-other-axonal-hh-temperature-stimulation-osb189155-model`: Neuroscience: Model189155189155Model
- `neuroscience-other-axonal-projection-interneuron-types-osb116053-model`: Neuroscience: Model116053116053Model

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
- neuroscience-other-axonal-gap-junctions-produce-fast-oscillations-i-114654-model :: modeldb:114654 :: https://modeldb.science/114654
- neuroscience-other-axonal-hh-model-for-temperature-stimulation-frib-189155-model :: modeldb:189155 :: https://modeldb.science/189155
- neuroscience-other-axonal-hh-temperature-stimulation-osb189155-model :: opensourcebrain:189155 :: https://github.com/OpenSourceBrain/189155
- neuroscience-other-axonal-projection-interneuron-types-osb116053-model :: opensourcebrain:116053 :: https://github.com/OpenSourceBrain/116053

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
