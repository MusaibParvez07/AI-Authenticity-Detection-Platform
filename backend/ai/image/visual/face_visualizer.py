"""
Professional Face Visualizer

Draws

- Bounding Boxes
- Face IDs
- Detection Confidence
- 5 Facial Landmarks

Saves a forensic visualization image.
"""

from pathlib import Path

import cv2

from backend.ai.image.face.detector import (
    face_detector,
)


class FaceVisualizer:

    def visualize(
        self,
        image_path: str | Path,
        output_path: str | Path,
    ):

        image_path = Path(image_path)
        output_path = Path(output_path)

        image = cv2.imread(str(image_path))

        if image is None:
            raise FileNotFoundError(image_path)

        faces = face_detector.detect(image_path)

        for i, face in enumerate(faces):

            # ----------------------------------------
            # Bounding Box
            # ----------------------------------------

            x1, y1, x2, y2 = map(
                int,
                face.bbox,
            )

            confidence = float(
                face.det_score
            )

            cv2.rectangle(
                image,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2,
            )

            label = (
                f"Face {i + 1} | {confidence:.2f}"
            )

            cv2.putText(
                image,
                label,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2,
            )

            # ----------------------------------------
            # 5 Facial Landmarks
            # ----------------------------------------

            if hasattr(face, "kps") and face.kps is not None:

                for point in face.kps:

                    px = int(point[0])
                    py = int(point[1])

                    cv2.circle(
                        image,
                        (px, py),
                        3,
                        (0, 0, 255),
                        -1,
                    )

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        cv2.imwrite(
            str(output_path),
            image,
        )

        return {

            "faces": len(faces),

            "saved_to": str(output_path),

        }


face_visualizer = FaceVisualizer()