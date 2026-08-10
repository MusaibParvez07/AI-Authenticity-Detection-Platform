"use client";

import { useEffect, useState } from "react";

import AppShell from "@/components/layout/app-shell";

import DashboardService from "@/services/dashboard.service";

import WelcomeBanner from "@/components/dashboard/welcome-banner";
import StatsGrid from "@/components/dashboard/stats-grid";
import QuickActions from "@/components/dashboard/quick-actions";
import RecentDetections from "@/components/dashboard/recent-detection";
import StatusPanel from "@/components/dashboard/status-panel";

interface LatestDetection {
  filename: string;
  file_type: string;
  media_type: string;
  prediction: string;
  confidence: number;
  model_name: string;
  created_at: string;
}

interface SystemStatus {
  backend: string;
  database: string;
  models_loaded: number;
  total_models: number;
  detection_engine: string;
  last_updated: string;
}

interface DashboardData {
  total_uploads: number;
  total_predictions: number;

  real_images: number;
  fake_images: number;

  image_count: number;
  video_count: number;
  audio_count: number;
  text_count: number;

  average_confidence: number;

  latest_detection: LatestDetection | null;

  recent_detections: LatestDetection[];

  system_status: SystemStatus;
}

export default function DashboardPage() {
  const [stats, setStats] = useState<DashboardData | null>(null);

  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadDashboard();
  }, []);

  async function loadDashboard() {
    try {
      const response =
        await DashboardService.getStatistics();

      setStats(response);
    } catch (error) {
      console.error(
        "Dashboard Error:",
        error
      );
    } finally {
      setLoading(false);
    }
  }

  if (loading) {
    return (
      <div className="flex h-screen items-center justify-center bg-[#050816]">
        <div className="flex flex-col items-center gap-4">
          <div className="h-14 w-14 animate-spin rounded-full border-4 border-violet-500 border-t-transparent" />

          <p className="text-lg text-zinc-400">
            Loading Dashboard...
          </p>
        </div>
      </div>
    );
  }

  if (!stats) {
    return (
      <div className="flex h-screen items-center justify-center bg-[#050816]">
        <div className="rounded-2xl border border-red-500/20 bg-red-500/10 px-8 py-6 text-center">
          <h2 className="text-2xl font-bold text-red-500">
            Dashboard Failed to Load
          </h2>

          <p className="mt-2 text-zinc-400">
            Unable to fetch dashboard statistics.
          </p>
        </div>
      </div>
    );
  }

  return (
    <AppShell>
      <div className="mx-auto max-w-[1550px] space-y-6">

        {/* Welcome Banner */}
        <WelcomeBanner />

        {/* Statistics */}
        <StatsGrid stats={stats} />

        {/* Quick Actions */}
        <QuickActions />

        {/* Recent Detections */}
        <RecentDetections
          detections={stats.recent_detections}
        />

        {/* Platform Status */}
        <StatusPanel
          status={stats.system_status}
        />

      </div>
    </AppShell>
  );
}