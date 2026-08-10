import api from "@/lib/api";
import { API_ENDPOINTS } from "@/lib/constants";

export interface DetectionResponse {
  status: string;
  prediction: string;
  confidence: number;
  file_path: string;
  upload_id: number;
  detection_id: number;
}

class UploadService {

  private getEndpoint(
    file: File
  ): string {

    const type = file.type.toLowerCase();
    const name = file.name.toLowerCase();

    if (type.startsWith("image/")) {

      return API_ENDPOINTS.DETECTION.IMAGE;

    }

    if (type.startsWith("video/")) {

      return API_ENDPOINTS.DETECTION.VIDEO;

    }

    if (type.startsWith("audio/")) {

      return API_ENDPOINTS.DETECTION.AUDIO;

    }

    if (
      type.startsWith("text/") ||
      name.endsWith(".txt")
    ) {

      return API_ENDPOINTS.DETECTION.TEXT;

    }

    throw new Error(
      "Unsupported file type."
    );

  }

  async upload(
    file: File,
    onProgress?: (
      progress: number
    ) => void
  ): Promise<DetectionResponse> {

    if (!file) {

      throw new Error(
        "No file selected."
      );

    }

    const endpoint =
      this.getEndpoint(file);

    const formData =
      new FormData();

    formData.append(
      "file",
      file
    );

    const response =
      await api.post<DetectionResponse>(
        endpoint,
        formData,
        {

          headers: {

            "Content-Type":
              "multipart/form-data",

          },

          onUploadProgress: (
            progressEvent
          ) => {

            if (
              !progressEvent.total
            ) {

              return;

            }

            const progress =
              Math.round(
                (
                  progressEvent.loaded /
                  progressEvent.total
                ) * 100
              );

            onProgress?.(
              progress
            );

          },

        }
      );

    return response.data;

  }

}

const uploadService =
  new UploadService();

export default uploadService;