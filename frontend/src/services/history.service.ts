import api from "@/lib/api";
import { API_ENDPOINTS } from "@/lib/constants";
import { HistoryItem } from "@/types/history";

class HistoryService {

  async getHistory(): Promise<HistoryItem[]> {

    if (typeof window !== "undefined") {

      const token = localStorage.getItem("access_token");

      if (!token) {
        return [];
      }

    }

    try {

      const response =
        await api.get<HistoryItem[]>(
          API_ENDPOINTS.HISTORY
        );

      return response.data;

    }

    catch (error) {

      console.error(
        "Failed to fetch history:",
        error
      );

      return [];

    }

  }

}

export default new HistoryService();