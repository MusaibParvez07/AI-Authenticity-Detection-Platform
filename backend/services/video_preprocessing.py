from pathlib import Path

import cv2


def extract_frames(
    video_path: str,
    output_directory: str,
    frame_interval: int = 10
):
    """
    Extract one frame every N frames.

    Returns a list of saved frame paths.
    """

    output_directory = Path(output_directory)
    output_directory.mkdir(
        parents=True,
        exist_ok=True
    )

    capture = cv2.VideoCapture(video_path)

    saved_frames = []

    frame_index = 0

    while True:

        success, frame = capture.read()

        if not success:
            break

        if frame_index % frame_interval == 0:

            frame_path = output_directory / f"frame_{frame_index}.jpg"

            cv2.imwrite(
                str(frame_path),
                frame
            )

            saved_frames.append(
                str(frame_path)
            )

        frame_index += 1

    capture.release()

    return saved_frames