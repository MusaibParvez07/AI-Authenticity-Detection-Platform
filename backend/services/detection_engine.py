from pathlib import Path

from fastapi import HTTPException
from fastapi import UploadFile
from sqlalchemy.orm import Session

from backend.services.file_service import save_file
from backend.services.upload_service import create_upload_record
from backend.services.detection_result_service import (
    save_detection_result,
)


class DetectionEngine:

    def __init__(
        self,
        inference,
        metadata_loader,
        pipeline=None,
    ):

        self.inference = inference
        self.metadata_loader = metadata_loader
        self.pipeline = pipeline

    async def detect(
        self,
        *,
        db: Session,
        file: UploadFile,
        current_user,
        destination,
        media_type: str,
    ):

        # ---------------------------------------
        # Save Uploaded File
        # ---------------------------------------

        path = await save_file(
            file=file,
            destination=destination,
        )

        # ---------------------------------------
        # Create Upload Record
        # ---------------------------------------

        upload = create_upload_record(
            db=db,
            user_id=current_user.id,
            filename=file.filename,
            file_type=media_type,
            file_path=path,
        )

        # ---------------------------------------
        # Prepare Input
        # ---------------------------------------

        inference_input = path

        # Text models need actual file contents
        if media_type == "text":

            inference_input = Path(path).read_text(
                encoding="utf-8",
                errors="ignore",
            )

        # ---------------------------------------
        # Run Detection
        # ---------------------------------------

        try:

            # Image uses the forensic pipeline
            if self.pipeline is not None:

                result = self.pipeline.analyze(
                    inference_input
                )

                prediction = result["decision"]["prediction"]

                confidence = result["ai_detector"]["confidence"]

            # Audio / Video / Text
            else:

                result = self.inference.predict(
                    inference_input
                )

                prediction = result["prediction"]

                confidence = result["confidence"]

        except Exception as e:

            raise HTTPException(
                status_code=500,
                detail=str(e),
            )

        # ---------------------------------------
        # Model Metadata
        # ---------------------------------------

        if callable(self.metadata_loader):

            metadata = self.metadata_loader()

        else:

            metadata = self.metadata_loader.get_metadata()

        # ---------------------------------------
        # Save Detection Result
        # ---------------------------------------

        detection = save_detection_result(
            db=db,
            upload_id=upload.id,
            prediction=prediction,
            confidence=confidence,
            model_name=metadata.name,
            media_type=media_type,
        )

        # ---------------------------------------
        # API Response
        # ---------------------------------------

        response = {

            "status": "success",

            "prediction": prediction,

            "confidence": confidence,

            "confidence_percent": result.get(
                "confidence_percent",
                round(confidence * 100, 2),
            ),

            "confidence_label": result.get(
                "confidence_label",
                "Unknown",
            ),

            "file_path": path,

            "upload_id": upload.id,

            "detection_id": detection.id,

            "model_name": metadata.name,

            "media_type": media_type,

        }

        # ---------------------------------------
        # Image Forensic Report
        # ---------------------------------------

        if self.pipeline is not None:

            response["report"] = result

            response["professional_report"] = result.get(
                "professional_report"
            )

        return response