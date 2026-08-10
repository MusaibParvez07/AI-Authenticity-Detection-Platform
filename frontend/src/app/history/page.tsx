"use client";

import { useEffect, useState } from "react";

import AppShell from "@/components/layout/app-shell";
import HistoryTable from "@/components/history/history-table";

import HistoryService from "@/services/history.service";

import { HistoryItem } from "@/types/history";

export default function HistoryPage() {

  const [history, setHistory] = useState<HistoryItem[]>([]);

  const [loading, setLoading] = useState(true);

  const [error, setError] = useState("");

  useEffect(() => {

    loadHistory();

  }, []);

  async function loadHistory() {

    try {

      const response =
        await HistoryService.getHistory();

      setHistory(response);

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

  }

  if (loading) {

    return (

      <div className="flex h-screen items-center justify-center bg-[#050816]">

        <div className="flex flex-col items-center gap-4">

          <div className="h-14 w-14 animate-spin rounded-full border-4 border-violet-500 border-t-transparent" />

          <p className="text-zinc-400 text-lg">

            Loading Detection History...

          </p>

        </div>

      </div>

    );

  }

  if (error) {

    return (

      <div className="flex h-screen items-center justify-center bg-[#050816]">

        <div className="rounded-2xl border border-red-500/20 bg-red-500/10 px-8 py-6">

          <h2 className="text-2xl font-bold text-red-500">

            Error

          </h2>

          <p className="mt-2 text-zinc-300">

            {error}

          </p>

        </div>

      </div>

    );

  }

  return (

    <AppShell>

      <div className="space-y-8">

        {/* Header */}

        <div>

          <h1 className="text-4xl font-bold text-white">

            Detection History

          </h1>

          <p className="mt-2 text-zinc-400">

            View every AI detection performed by your account.

          </p>

        </div>

        {/* Stats */}

        <div className="grid grid-cols-1 gap-6 md:grid-cols-4">

          <div className="rounded-2xl border border-zinc-800 bg-[#0b1220] p-6">

            <p className="text-zinc-400">

              Total Detections

            </p>

            <h2 className="mt-2 text-3xl font-bold text-white">

              {history.length}

            </h2>

          </div>

          <div className="rounded-2xl border border-zinc-800 bg-[#0b1220] p-6">

            <p className="text-zinc-400">

              Real Files

            </p>

            <h2 className="mt-2 text-3xl font-bold text-green-400">

              {
                history.filter(
                  h =>
                    h.prediction.toLowerCase() ===
                    "real"
                ).length
              }

            </h2>

          </div>

          <div className="rounded-2xl border border-zinc-800 bg-[#0b1220] p-6">

            <p className="text-zinc-400">

              Fake Files

            </p>

            <h2 className="mt-2 text-3xl font-bold text-red-400">

              {
                history.filter(
                  h =>
                    h.prediction.toLowerCase() ===
                    "fake"
                ).length
              }

            </h2>

          </div>

          <div className="rounded-2xl border border-zinc-800 bg-[#0b1220] p-6">

            <p className="text-zinc-400">

              Average Confidence

            </p>

            <h2 className="mt-2 text-3xl font-bold text-violet-400">

              {history.length
                ? (
                    history.reduce(
                      (sum, item) =>
                        sum + item.confidence,
                      0
                    ) /
                    history.length *
                    100
                  ).toFixed(1)
                : "0"}
              %

            </h2>

          </div>

        </div>

        {/* Table */}

        <HistoryTable

          history={history}

        />

      </div>

    </AppShell>

  );

}