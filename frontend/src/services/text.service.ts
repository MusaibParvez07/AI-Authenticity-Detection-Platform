import api from "@/lib/api";
import { PredictionResponse } from "./image.service";

class TextService {
  async detect(file: File): Promise<PredictionResponse> {
    const formData = new FormData();

    formData.append("file", file);

    const response = await api.post(
      "/detect/text",
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

const textService = new TextService();

export default textService;