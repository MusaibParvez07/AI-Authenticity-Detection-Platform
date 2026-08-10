import api from "@/lib/api";
import { PredictionResponse } from "./image.service";

class VideoService {
  async detect(file: File): Promise<PredictionResponse> {
    const formData = new FormData();

    formData.append("file", file);

    const response = await api.post(
      "/detect/video",
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

const videoService = new VideoService();

export default videoService;