import torch

from backend.ai.common.inference_engine import InferenceEngine


class DummyModel(torch.nn.Module):

    def forward(self, x):

        return torch.tensor([[0.3, 2.5]])


def preprocess(x):

    return torch.randn(
        1,
        3,
        224,
        224
    )


engine = InferenceEngine(
    DummyModel(),
    preprocess
)

print(engine.predict(None))