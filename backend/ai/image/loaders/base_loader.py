from abc import ABC, abstractmethod


class BaseImageModel(ABC):

    @abstractmethod
    def predict(self, image_path: str) -> dict:
        """
        Returns:
        {
            "prediction": "real" | "fake",
            "confidence": 0.91
        }
        """
        pass