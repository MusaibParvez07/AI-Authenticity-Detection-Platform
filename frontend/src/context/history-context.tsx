"use client";

import {
  createContext,
  ReactNode,
  useContext,
  useEffect,
  useState,
} from "react";

import HistoryService from "@/services/history.service";

import { HistoryItem } from "@/types/history";

interface HistoryContextType {

  history: HistoryItem[];

  loading: boolean;

  error: string;

  refreshHistory: () => Promise<void>;

}

const HistoryContext =
  createContext<HistoryContextType | null>(null);

interface Props {

  children: ReactNode;

}

export function HistoryProvider({

  children,

}: Props) {

  const [history, setHistory] =
    useState<HistoryItem[]>([]);

  const [loading, setLoading] =
    useState(true);

  const [error, setError] =
    useState("");

  const refreshHistory = async () => {

    try {

      setLoading(true);

      setError("");

      const data =
        await HistoryService.getHistory();

      setHistory(data);

    } catch (err) {

      console.error(err);

      setError(
        "Failed to load history."
      );

    } finally {

      setLoading(false);

    }

  };

  useEffect(() => {

    refreshHistory();

  }, []);

  return (

    <HistoryContext.Provider

      value={{

        history,

        loading,

        error,

        refreshHistory,

      }}

    >

      {children}

    </HistoryContext.Provider>

  );

}

export function useHistoryContext() {

  const context =
    useContext(HistoryContext);

  if (!context) {

    throw new Error(

      "useHistoryContext must be used within a HistoryProvider"

    );

  }

  return context;

}