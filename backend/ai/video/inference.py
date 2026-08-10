from statistics import mean

from backend.ai.config import VIDEO_CLASSES

from backend.ai.image.inference import image_inference

from backend.ai.video.frame_sampler import frame_sampler


class VideoInference:

    def predict(
        self,
        video_path: str,
    ):

        frames = frame_sampler.sample_frames(video_path)

        if not frames:

            raise Exception("No frames extracted from video.")

        predictions = []

        confidences = []

        for frame in frames:

            result = image_inference.predict(frame)

            if result["prediction"].lower() == "fake":
                predictions.append(0)
            else:
                predictions.append(1)

            confidences.append(result["confidence"])

        avg_prediction = round(mean(predictions))
        avg_confidence = mean(confidences)

        return {

            "prediction": VIDEO_CLASSES[avg_prediction],

            "confidence": avg_confidence,

            "confidence_percent": round(avg_confidence * 100, 2),

            "confidence_label": (
                "High"
                if avg_confidence >= 0.80
                else "Medium"
                if avg_confidence >= 0.60
                else "Low"
            ),

        }


video_inference = VideoInference()