# COMBO_0076 - Neuroscience Hippocampal Circuits

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
- `neuroscience-other-axonal-k-channel-inhibition-promotes-ectopic-bur-2015571-model`: Neuroscience: AxonalKChannelInhibitionPromotesEctopicBur2015571Model
- `neuroscience-other-axonal-k-channel-inhibition-promotes-ectopic-burst-hippocampal-mossy-fiber-osb2015571-model`: Neuroscience: Model20155712015571Model
- `neuroscience-other-axonal-nav1-osb115356-model`: Neuroscience: Model115356115356Model
- `neuroscience-other-axonal-subthreshold-voltage-signaling-along-hippocampal-mossy-fiber-osb267512-model`: Neuroscience: Model267512267512Model

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
- neuroscience-other-axonal-k-channel-inhibition-promotes-ectopic-bur-2015571-model :: modeldb:2015571 :: https://modeldb.science/2015571
- neuroscience-other-axonal-k-channel-inhibition-promotes-ectopic-burst-hippocampal-mossy-fiber-osb2015571-model :: opensourcebrain:2015571 :: https://github.com/OpenSourceBrain/2015571
- neuroscience-other-axonal-nav1-osb115356-model :: opensourcebrain:115356 :: https://github.com/OpenSourceBrain/115356
- neuroscience-other-axonal-subthreshold-voltage-signaling-along-hippocampal-mossy-fiber-osb267512-model :: opensourcebrain:267512 :: https://github.com/OpenSourceBrain/267512

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
