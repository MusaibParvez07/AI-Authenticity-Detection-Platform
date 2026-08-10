import api from "@/lib/api";

export interface PredictionResponse {
  status: string;
  prediction: string;
  confidence: number;
  file_path: string;
  upload_id: number;
  detection_id: number;
}

class ImageService {
  async detect(file: File): Promise<PredictionResponse> {
    const formData = new FormData();

    formData.append("file", file);

    const response = await api.post(
      "/detect/image",
      formData,
      {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      }
    );

    return response.data;
  }
}

const imageService = new ImageService();

export default imageService;