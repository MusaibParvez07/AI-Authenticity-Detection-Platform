import re
import unicodedata

from transformers import AutoTokenizer

from backend.ai.config import (
    TEXT_MODEL_NAME,
    TEXT_MAX_LENGTH,
)


class TextPreprocessor:

    def __init__(self):

        self.tokenizer = AutoTokenizer.from_pretrained(
            TEXT_MODEL_NAME
        )

    # ---------------------------------------
    # Clean Text
    # ---------------------------------------

    def clean_text(
        self,
        text: str,
    ) -> str:

        if not text:

            return ""

        # Normalize Unicode

        text = unicodedata.normalize(
            "NFKC",
            text,
        )

        # Remove control characters

        text = "".join(

            character

            for character in text

            if unicodedata.category(character)[0] != "C"

        )

        # Normalize line breaks

        text = text.replace(
            "\r\n",
            "\n",
        ).replace(
            "\r",
            "\n",
        )

        # Remove extra spaces

        text = re.sub(
            r"[ \t]+",
            " ",
            text,
        )

        # Remove excessive blank lines

        text = re.sub(
            r"\n{3,}",
            "\n\n",
            text,
        )

        return text.strip()

    # ---------------------------------------
    # Preprocess
    # ---------------------------------------

    def preprocess(
        self,
        text: str,
    ):

        text = self.clean_text(
            text
        )

        encoding = self.tokenizer(

            text,

            truncation=True,

            padding="max_length",

            max_length=TEXT_MAX_LENGTH,

            return_tensors="pt",

        )

        return encoding


text_preprocessor = TextPreprocessor()