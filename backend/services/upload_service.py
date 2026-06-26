from sqlalchemy.orm import Session

from backend.models.upload import Upload


def create_upload_record(
    db: Session,
    user_id: int,
    filename: str,
    file_type: str,
    file_path: str
) -> Upload:

    upload = Upload(
        user_id=user_id,
        filename=filename,
        file_type=file_type,
        file_path=file_path
    )

    db.add(upload)

    db.commit()

    db.refresh(upload)

    return upload