import api from "@/lib/api";

class DashboardService {

  async getStatistics() {

    const response = await api.get("/dashboard");

    return response.data;

  }

}

export default new DashboardService();