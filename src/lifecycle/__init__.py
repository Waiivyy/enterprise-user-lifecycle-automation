"""Enterprise user lifecycle automation demo package."""

from lifecycle.config_loader import LifecycleConfig, load_lifecycle_config
from lifecycle.onboarding import build_onboarding_plan
from lifecycle.offboarding import build_offboarding_plan

__all__ = [
    "LifecycleConfig",
    "build_offboarding_plan",
    "build_onboarding_plan",
    "load_lifecycle_config",
]
