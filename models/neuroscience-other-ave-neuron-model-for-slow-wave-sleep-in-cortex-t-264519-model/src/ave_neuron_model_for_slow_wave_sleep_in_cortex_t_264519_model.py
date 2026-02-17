# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Auto-generated BioModule wrapper for Ave. neuron model for slow-wave sleep in cortex Tatsuki 2016 Yoshida 2018 Rasmussen 2017 (all et al).

Source: modeldb:264519
Original: https://modeldb.science/264519
Standard: other

Note: This is a placeholder wrapper. The model uses a non-standard format
and requires manual integration with the appropriate simulator.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, Optional, Set, TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover - typing only
    from bsim import BioWorld

import bsim
from bsim.signals import BioSignal, SignalMetadata


class OtherAveNeuronModelForSlowWaveSleepInCortexTatsuki2016(bsim.BioModule):
    """Placeholder BioModule wrapper for: Ave. neuron model for slow-wave sleep in cortex Tatsuki 2016 Yoshida 2018 Rasmussen 2017 (all et al).

    This model's original format is not directly supported by the auto-generator.
    Manual integration with the appropriate simulator is needed.
    """

    def __init__(self, model_path: str = "data/264519.zip", min_dt: float = 0.01) -> None:
        self.min_dt = min_dt
        self._model_path = Path(__file__).parent.parent / model_path
        self._t = 0.0
        self._outputs: Dict[str, BioSignal] = {}

    def setup(self, config: Optional[Dict[str, Any]] = None) -> None:
        self._t = 0.0

    def reset(self) -> None:
        self._t = 0.0
        self._outputs = {}

    def inputs(self) -> Set[str]:
        return set()

    def outputs(self) -> Set[str]:
        return {"state"}

    def advance_to(self, t: float) -> None:
        self._t = t
        source_name = getattr(self, "_world_name", self.__class__.__name__)
        self._outputs = {
            "state": BioSignal(
                source=source_name,
                name="state",
                value={"t": t},
                time=t,
                metadata=SignalMetadata(
                    description="Placeholder state — manual integration needed",
                    kind="state",
                ),
            )
        }

    def get_outputs(self) -> Dict[str, BioSignal]:
        return dict(self._outputs)

# Canonical alias for stable entrypoint naming.
AveNeuronModelForSlowWaveSleepInCortexT264519Model = OtherAveNeuronModelForSlowWaveSleepInCortexTatsuki2016
