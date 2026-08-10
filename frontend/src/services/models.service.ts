import api from "@/lib/api";

import { API_ENDPOINTS } from "@/lib/constants";

import { ModelsResponse } from "@/types/model";

class ModelsService {

  async getModels(): Promise<ModelsResponse> {

    try {

      const response =
        await api.get<ModelsResponse>(
          API_ENDPOINTS.MODELS
        );

      return response.data;

    }

    catch (error) {

      console.error(
        "Failed to load models",
        error
      );

      return {

        total_models: 0,

        loaded_models: 0,

        models: [],

      };

    }

  }

}

export default new ModelsService();