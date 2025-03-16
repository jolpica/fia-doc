# -*- coding: utf-8 -*-
from typing import Optional

from pydantic import (
    BaseModel,
    ConfigDict,
    NonNegativeFloat,
    NonNegativeInt,
    PositiveInt,
    field_validator
)

from .foreign_key import SessionEntry
    
class Classification(BaseModel):
    position: PositiveInt
    is_classified: bool
    status: NonNegativeInt
    detail: str | None = None
    points: NonNegativeFloat
    is_eligible_for_points: bool | None = None
    grid: PositiveInt | None = None
    time: dict[str, str | int] | None
    fastest_lap_rank: PositiveInt | None
    laps_completed: NonNegativeInt  # TODO: or positive int? What if retire in lap 1?

    model_config = ConfigDict(extra='forbid')


class ClassificationData(BaseModel):
    object_type: str = 'SessionEntry'
    foreign_keys: SessionEntry
    objects: list[Classification]

    model_config = ConfigDict(extra='forbid')


class QualiClassification(BaseModel):
    position: PositiveInt


class QualiClassificationData(BaseModel):
    object_type: str = 'SessionEntry'
    foreign_keys: SessionEntry
    objects: list[QualiClassification]

    model_config = ConfigDict(extra='forbid')
