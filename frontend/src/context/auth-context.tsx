"use client";

import {
  createContext,
  useState,
  useEffect,
  ReactNode,
} from "react";

import AuthService from "@/services/auth.service";

import {
  AuthContextType,
  User,
} from "@/types/auth";

export const AuthContext =
  createContext<AuthContextType | null>(null);

interface Props {
  children: ReactNode;
}

export function AuthProvider({
  children,
}: Props) {

  const [user, setUser] =
    useState<User | null>(null);

  const [token, setToken] =
    useState<string | null>(null);

  const [loading, setLoading] =
    useState(true);

  // ----------------------------
  // Restore Session
  // ----------------------------

  useEffect(() => {

    const storedToken =
      AuthService.getToken();

    if (storedToken) {

      setToken(storedToken);

      refreshUser();

    } else {

      setLoading(false);

    }

  }, []);

  // ----------------------------
  // Login
  // ----------------------------

  const login = async (
    email: string,
    password: string
  ) => {

    const response =
      await AuthService.login({
        email,
        password,
      });

    setToken(
      response.access_token
    );

    await refreshUser();

  };

  // ----------------------------
  // Register
  // ----------------------------

  const register = async (
    name: string,
    email: string,
    password: string
  ) => {

    await AuthService.register({
      name,
      email,
      password,
    });

  };

  // ----------------------------
  // Logout
  // ----------------------------

  const logout = () => {

    AuthService.logout();

    setUser(null);

    setToken(null);

  };

  // ----------------------------
  // Current User
  // ----------------------------

  const refreshUser = async () => {

    try {

      const response =
        await AuthService.me();

      setUser(
        response.logged_in_user
      );

    } catch {

      logout();

    } finally {

      setLoading(false);

    }

  };

  return (

    <AuthContext.Provider
      value={{
        user,
        token,
        loading,
        login,
        register,
        logout,
        refreshUser,
      }}
    >

      {children}

    </AuthContext.Provider>

  );

}