from pathlib import Path

from fastapi import HTTPException, UploadFile


ALLOWED_IMAGE_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".webp"
}

ALLOWED_AUDIO_EXTENSIONS = {
    ".wav",
    ".mp3",
    ".m4a",
    ".flac"
}

ALLOWED_VIDEO_EXTENSIONS = {
    ".mp4",
    ".mov",
    ".avi",
    ".mkv"
}

ALLOWED_TEXT_EXTENSIONS = {
    ".txt"
}


MAX_IMAGE_SIZE = 10 * 1024 * 1024      # 10 MB
MAX_AUDIO_SIZE = 50 * 1024 * 1024      # 50 MB
MAX_VIDEO_SIZE = 500 * 1024 * 1024     # 500 MB
MAX_TEXT_SIZE = 5 * 1024 * 1024        # 5 MB


def validate_extension(
    file: UploadFile,
    allowed_extensions: set
) -> None:

    extension = Path(file.filename).suffix.lower()

    if extension not in allowed_extensions:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file type: {extension}"
        )


async def validate_file_size(
    file: UploadFile,
    max_size: int
) -> None:

    content = await file.read()

    file_size = len(content)

    await file.seek(0)

    if file_size > max_size:
        raise HTTPException(
            status_code=400,
            detail=f"File size exceeds limit of {max_size // (1024 * 1024)} MB"
        )