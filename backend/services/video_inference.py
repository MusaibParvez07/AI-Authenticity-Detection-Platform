from backend.services.video_preprocessing import extract_frames
from backend.services.inference_service import predict_image


def predict_video(video_path: str):

    frame_paths = extract_frames(
        video_path,
        "datasets/video/frames"
    )

    if len(frame_paths) == 0:
        return {
            "prediction": "unknown",
            "confidence": 0.0,
            "frames": 0
        }

    fake_frames = 0
    real_frames = 0
    total_confidence = 0

    for frame in frame_paths:

        result = predict_image(frame)

        total_confidence += result["confidence"]

        if result["prediction"] == "fake":
            fake_frames += 1
        else:
            real_frames += 1

    if fake_frames > real_frames:
        prediction = "fake"
    else:
        prediction = "real"

    confidence = round(
        total_confidence / len(frame_paths),
        4
    )

    return {
        "prediction": prediction,
        "confidence": confidence,
        "frames_processed": len(frame_paths),
        "fake_frames": fake_frames,
        "real_frames": real_frames
    }