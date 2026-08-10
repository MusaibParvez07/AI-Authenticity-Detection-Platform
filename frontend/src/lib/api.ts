import axios from "axios";

import { API_BASE_URL } from "./constants";

const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 60000,
});

// ----------------------------------------------------
// Request Interceptor
// ----------------------------------------------------

api.interceptors.request.use(
  (config) => {

    if (typeof window !== "undefined") {

      const token = localStorage.getItem("access_token");

      console.log("====================================");
      console.log(
        "🚀 Request:",
        config.method?.toUpperCase(),
        config.url
      );
      console.log("🌐 Base URL:", config.baseURL);

      if (token) {

        config.headers = config.headers ?? {};

        config.headers.Authorization = `Bearer ${token}`;

      }

      console.log(
        "🔑 Authorization:",
        config.headers?.Authorization
      );

      console.log("====================================");

    }

    return config;

  },
  (error) => Promise.reject(error)
);

// ----------------------------------------------------
// Response Interceptor
// ----------------------------------------------------

api.interceptors.response.use(

  (response) => {

    console.log(
      "✅ Response:",
      response.status,
      response.config.url
    );

    return response;

  },

  (error) => {

    console.error("====================================");
    console.error("❌ API ERROR");
    console.error(
      "URL:",
      error.config?.url
    );
    console.error(
      "Status:",
      error.response?.status
    );
    console.error(
      "Response:",
      error.response?.data
    );
    console.error("====================================");

    if (error.response?.status === 401) {

      console.warn(
        "Authentication expired. Redirecting to login..."
      );

      localStorage.removeItem("access_token");

      if (typeof window !== "undefined") {
        window.location.href = "/login";
      }

    }

    return Promise.reject(error);

  }

);

export default api;