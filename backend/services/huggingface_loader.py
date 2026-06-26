from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification


MODEL_NAME = "Hello-SimpleAI/chatgpt-detector-roberta"


def load_huggingface_model():

    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_NAME
    )

    model = AutoModelForSequenceClassification.from_pretrained(
        MODEL_NAME
    )

    model.eval()

    return tokenizer, model