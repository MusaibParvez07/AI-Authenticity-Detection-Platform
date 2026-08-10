"""
Video Frame Sampler

Extracts a fixed number of evenly distributed
frames from a video.
"""

from typing import List

import cv2
import numpy as np

from backend.ai.config import (
    VIDEO_SAMPLE_FRAMES,
)


class FrameSampler:

    def __init__(self):

        self.num_frames = VIDEO_SAMPLE_FRAMES

    # ----------------------------------------
    # Sample Frames
    # ----------------------------------------

    def sample_frames(
        self,
        video_path: str,
    ) -> List[np.ndarray]:

        capture = cv2.VideoCapture(
            video_path
        )

        if not capture.isOpened():

            raise ValueError(
                f"Cannot open video: {video_path}"
            )

        total_frames = int(
            capture.get(
                cv2.CAP_PROP_FRAME_COUNT
            )
        )

        if total_frames <= 0:

            capture.release()

            raise ValueError(
                "Video contains no frames."
            )

        frame_indices = np.linspace(

            0,

            total_frames - 1,

            self.num_frames,

            dtype=int,

        )

        frames = []

        for index in frame_indices:

            capture.set(
                cv2.CAP_PROP_POS_FRAMES,
                int(index)
            )

            success, frame = capture.read()

            if not success:

                continue

            frame = cv2.cvtColor(
                frame,
                cv2.COLOR_BGR2RGB
            )

            frames.append(frame)

        capture.release()

        return frames


frame_sampler = FrameSampler()