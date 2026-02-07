"""
Canonical schema for the optimisation triage pipeline.

"""

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class CandidateInput:
    candidate_id: str
    source: src

    #Size/cost proxies
    mass_kg: Optional[float] = None
    element_count: Optional[float] = None
    node_count: Optional[float] = None

    #Optimisation levers
    design_variable_count: Optional[float] = None
    dv_type: Optional[str] = None

    #Constraint
    max_utilisation: Optional[float] = None
    min_margin: Optional[float] = None


@dataclass(frozen=True)
class CandidateOutput:
    candidate_id: str
    triage_score: float
    rank: int
    rationale: str
    