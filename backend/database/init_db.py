from backend.database.base import Base
from backend.database.session import engine

from backend.models.upload import Upload
from backend.models.detection_result import DetectionResult
from backend.models.user import User


def init_db():
    print("Tables in metadata:")
    print(Base.metadata.tables.keys())

    for table in Base.metadata.sorted_tables:
        print(f"Creating/checking table: {table.name}")

    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
    print("Database tables created successfully.")