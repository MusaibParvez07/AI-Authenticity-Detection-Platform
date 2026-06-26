import api from "@/lib/api";
import {
  LoginRequest,
  RegisterRequest,
  TokenResponse,
  MeResponse,
} from "@/types/auth";

const TOKEN_KEY = "access_token";

class AuthService {
  // ----------------------------
  // Register User
  // ----------------------------
  async register(data: RegisterRequest) {
    const response = await api.post("/auth/register", data);

    return response.data;
  }

  // ----------------------------
  // Login User
  // ----------------------------
  async login(
    data: LoginRequest
  ): Promise<TokenResponse> {
    const response = await api.post<TokenResponse>(
      "/auth/login",
      data
    );

    const token = response.data.access_token;

    localStorage.setItem(TOKEN_KEY, token);

    return response.data;
  }

  // ----------------------------
  // Current User
  // ----------------------------
  async me(): Promise<MeResponse> {
    const response = await api.get<MeResponse>(
      "/auth/me"
    );

    return response.data;
  }

  // ----------------------------
  // Logout
  // ----------------------------
  logout() {
    localStorage.removeItem(TOKEN_KEY);
  }

  // ----------------------------
  // Get Stored Token
  // ----------------------------
  getToken(): string | null {
    return localStorage.getItem(TOKEN_KEY);
  }

  // ----------------------------
  // Is Logged In
  // ----------------------------
  isAuthenticated(): boolean {
    return !!this.getToken();
  }
}

export default new AuthService();