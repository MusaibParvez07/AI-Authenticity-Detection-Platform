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
  private getEndpoint(file: File): string {
    const type = file.type;

    if (type.startsWith("image/")) {
      return API_ENDPOINTS.IMAGE;
    }

    if (type.startsWith("video/")) {
      return API_ENDPOINTS.VIDEO;
    }

    if (type.startsWith("audio/")) {
      return API_ENDPOINTS.AUDIO;
    }

    if (type.startsWith("text/")) {
      return API_ENDPOINTS.TEXT;
    }

    throw new Error("Unsupported file type.");
  }

  async upload(file: File): Promise<DetectionResponse> {
    const endpoint = this.getEndpoint(file);

    const formData = new FormData();

    formData.append("file", file);

    const response = await api.post<DetectionResponse>(
      endpoint,
      formData
    );

    return response.data;
  }
}

export default new UploadService();