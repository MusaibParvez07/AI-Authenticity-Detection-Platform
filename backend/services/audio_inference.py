from backend.services.audio_preprocessing import (
    preprocess_audio
)


def predict_audio(
    audio_path: str
):

    waveform = preprocess_audio(
        audio_path=audio_path
    )

    print(
        f"Waveform Shape: {waveform.shape}"
    )

    # Placeholder until a fine-tuned audio model is integrated
    prediction = "real"
    confidence = 0.95

    return {
        "prediction": prediction,
        "confidence": confidence
    }