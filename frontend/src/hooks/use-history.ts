"use client";

import { useCallback, useEffect, useState } from "react";

import HistoryService from "@/services/history.service";

import { HistoryItem } from "@/types/history";

export function useHistory() {

  const [history, setHistory] =
    useState<HistoryItem[]>([]);

  const [loading, setLoading] =
    useState(true);

  const [error, setError] =
    useState("");

  const fetchHistory = useCallback(async () => {

    try {

      const token =
        localStorage.getItem("access_token");

      if (!token) {

        setHistory([]);

        setLoading(false);

        return;

      }

      setLoading(true);

      setError("");

      const data =
        await HistoryService.getHistory();

      setHistory(data);

    }

    catch (err) {

      console.error(err);

      setError(
        "Failed to load history."
      );

    }

    finally {

      setLoading(false);

    }

  }, []);

  useEffect(() => {

    fetchHistory();

  }, [fetchHistory]);

  return {

    history,

    loading,

    error,

    refreshHistory: fetchHistory,

  };

}