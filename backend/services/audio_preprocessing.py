import torchaudio


def preprocess_audio(
    audio_path: str
):

    waveform, sample_rate = torchaudio.load(
        audio_path
    )

    # Convert stereo to mono
    if waveform.shape[0] > 1:

        waveform = waveform.mean(
            dim=0,
            keepdim=True
        )

    # Resample to 16 kHz
    target_sample_rate = 16000

    if sample_rate != target_sample_rate:

        resampler = torchaudio.transforms.Resample(
            sample_rate,
            target_sample_rate
        )

        waveform = resampler(
            waveform
        )

    return waveform