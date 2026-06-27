"""Bootstrap the Archie application."""

from __future__ import annotations

from pathlib import Path

from archie.app.application import Archie
from archie.app.runtime import Runtime
from archie.app.service_manager import ServiceManager
from archie.brain import OllamaBrain
from archie.config import ConfigurationManager
from archie.container.application import ApplicationContainer


def bootstrap() -> Archie:
    """Create and configure the Archie application."""

    configuration = ConfigurationManager(
        Path("config"),
    ).load()

    runtime = Runtime()

    services = ServiceManager()

    brain = OllamaBrain(
        host=configuration.llm.host,
        model=configuration.llm.model,
        timeout=configuration.llm.timeout,
    )

    container = ApplicationContainer(
        configuration=configuration,
        runtime=runtime,
        services=services,
        brain=brain,
    )

    return Archie(
        container=container,
    )