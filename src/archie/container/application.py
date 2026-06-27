"""Application container."""

from __future__ import annotations

from dataclasses import dataclass

from archie.app.runtime import Runtime
from archie.app.service_manager import ServiceManager
from archie.brain import Brain
from archie.config import Configuration
from archie.personality import PersonalityManager


@dataclass(slots=True, frozen=True)
class ApplicationContainer:
    """Container for shared application services."""

    configuration: Configuration
    runtime: Runtime
    services: ServiceManager
    brain: Brain
    personality: PersonalityManager