"""
Global AI Model Registry

Stores loaded AI models and their metadata.
Provides helper methods for retrieval,
inspection, and management.
"""

from typing import Any

from backend.ai.common.metadata import ModelMetadata


class ModelRegistry:

    def __init__(self):

        self._models: dict[str, Any] = {}

        self._metadata: dict[str, ModelMetadata] = {}

    # =====================================================
    # Register Model
    # =====================================================

    def register(
        self,
        name: str,
        model: Any,
        metadata: ModelMetadata,
    ) -> None:

        self._models[name] = model
        self._metadata[name] = metadata

    # =====================================================
    # Get Model
    # =====================================================

    def get(
        self,
        name: str,
    ) -> Any:

        if name not in self._models:

            raise ValueError(
                f"Model '{name}' is not registered."
            )

        return self._models[name]

    # =====================================================
    # Get Metadata
    # =====================================================

    def get_metadata(
        self,
        name: str,
    ) -> ModelMetadata:

        if name not in self._metadata:

            raise ValueError(
                f"Metadata for '{name}' not found."
            )

        return self._metadata[name]

    # =====================================================
    # Get All Metadata
    # =====================================================

    def get_all_metadata(
        self,
    ) -> dict[str, ModelMetadata]:

        return self._metadata

    # =====================================================
    # Get All Models
    # =====================================================

    def get_all_models(
        self,
    ) -> dict[str, Any]:

        return self._models

    # =====================================================
    # Total Loaded Models
    # =====================================================

    def total_models(
        self,
    ) -> int:

        return len(self._models)

    # =====================================================
    # Check Loaded
    # =====================================================

    def is_loaded(
        self,
        name: str,
    ) -> bool:

        return name in self._models

    # =====================================================
    # List Registered Models
    # =====================================================

    def list_models(
        self,
    ) -> list[str]:

        return list(self._models.keys())

    # =====================================================
    # Remove Model
    # =====================================================

    def unregister(
        self,
        name: str,
    ) -> None:

        self._models.pop(name, None)
        self._metadata.pop(name, None)

    # =====================================================
    # Clear Registry
    # =====================================================

    def clear(
        self,
    ) -> None:

        self._models.clear()
        self._metadata.clear()


# ==========================================================
# Global Registry Singleton
# ==========================================================

registry = ModelRegistry()