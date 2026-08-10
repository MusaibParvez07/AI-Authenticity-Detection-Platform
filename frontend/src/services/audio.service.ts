import api from "@/lib/api";
import { PredictionResponse } from "./image.service";

class AudioService {
  async detect(file: File): Promise<PredictionResponse> {
    const formData = new FormData();

    formData.append("file", file);

    const response = await api.post(
      "/detect/audio",
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

const audioService = new AudioService();

export default audioService;