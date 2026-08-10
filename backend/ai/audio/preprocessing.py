import librosa
import numpy as np

from transformers import AutoFeatureExtractor

from backend.ai.config import (
    AUDIO_MODEL_NAME,
    AUDIO_SAMPLE_RATE,
    AUDIO_MAX_DURATION,
)


class AudioPreprocessor:

    def __init__(self):

        self.processor = AutoFeatureExtractor.from_pretrained(
            AUDIO_MODEL_NAME
        )

    # ---------------------------------------
    # Load & Normalize Audio
    # ---------------------------------------

    def _load_audio(
        self,
        audio_path: str,
    ):

        waveform, sample_rate = librosa.load(

            audio_path,

            sr=AUDIO_SAMPLE_RATE,

            mono=True,

        )

        # Remove DC offset

        waveform = waveform - np.mean(waveform)

        # Normalize amplitude

        maximum = np.max(np.abs(waveform))

        if maximum > 0:

            waveform = waveform / maximum

        # ---------------------------------------
        # Trim / Pad to fixed duration
        # ---------------------------------------

        target_length = (
            AUDIO_SAMPLE_RATE *
            AUDIO_MAX_DURATION
        )

        if len(waveform) > target_length:

            waveform = waveform[:target_length]

        elif len(waveform) < target_length:

            padding = target_length - len(waveform)

            waveform = np.pad(

                waveform,

                (0, padding),

                mode="constant",

            )

        return waveform, sample_rate

    # ---------------------------------------
    # Preprocess
    # ---------------------------------------

    def preprocess(
        self,
        audio_path: str,
    ):

        waveform, sample_rate = self._load_audio(
            audio_path
        )

        encoding = self.processor(

            waveform,

            sampling_rate=sample_rate,

            return_tensors="pt",

            padding=True,

        )

        return encoding


audio_preprocessor = AudioPreprocessor()