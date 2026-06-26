from pathlib import Path
from uuid import uuid4
from fastapi import UploadFile


def generate_filename(filename: str) -> str:
    """
    Generate unique filename.
    Example:
    image.jpg
    ->
    8f2c1a34d6f14c8ab2f9c7f4f3a1.jpg
    """

    extension = Path(filename).suffix

    return f"{uuid4().hex}{extension}"


async def save_file(
    file: UploadFile,
    destination: Path
) -> str:

    filename = generate_filename(file.filename)

    filepath = destination / filename

    contents = await file.read()

    with open(filepath, "wb") as buffer:
        buffer.write(contents)

    return str(filepath)