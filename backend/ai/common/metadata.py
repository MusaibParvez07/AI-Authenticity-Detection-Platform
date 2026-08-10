from dataclasses import dataclass
from typing import List
from typing import Optional


@dataclass
class ModelMetadata:

    name: str

    version: str

    media_type: str

    architecture: str

    framework: str

    task: str

    dataset: str

    input_size: Optional[str]

    classes: List[str]

    confidence_threshold: float

    weights_path: str

    device: str

    description: str

    author: str

    status: str = "loaded"