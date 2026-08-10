"use client";

import {
  ShieldAlert,
  ShieldCheck,
  Target,
  Upload,
} from "lucide-react";

import { useHistory } from "@/hooks/use-history";

import StatCard from "./stat-card";

export default function DashboardStats() {
  const {
    history,
    loading,
  } = useHistory();

  if (loading) {
    return (
      <section className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">
        {[1, 2, 3, 4].map((item) => (
          <div
            key={item}
            className="h-40 animate-pulse rounded-3xl bg-zinc-900"
          />
        ))}
      </section>
    );
  }

  const totalUploads = history.length;

  const realDetections = history.filter(
    (item) => item.prediction === "real"
  ).length;

  const fakeDetections = history.filter(
    (item) => item.prediction === "fake"
  ).length;

  const averageConfidence =
    totalUploads === 0
      ? 0
      : history.reduce(
          (sum, item) => sum + item.confidence,
          0
        ) / totalUploads;

  const stats = [
    {
      title: "Total Uploads",
      value: totalUploads,
      subtitle: "Files Uploaded",
      icon: Upload,
      color: "from-sky-500 to-cyan-500",
    },

    {
      title: "Real Detections",
      value: realDetections,
      subtitle: "Verified Authentic",
      icon: ShieldCheck,
      color: "from-emerald-500 to-green-500",
    },

    {
      title: "Fake Detections",
      value: fakeDetections,
      subtitle: "AI Generated",
      icon: ShieldAlert,
      color: "from-pink-500 to-red-500",
    },

    {
      title: "Average Confidence",
      value: `${(averageConfidence * 100).toFixed(1)}%`,
      subtitle: "Detection Accuracy",
      icon: Target,
      color: "from-violet-500 to-blue-500",
    },
  ];

  return (
    <section className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">
      {stats.map((stat) => (
        <StatCard
          key={stat.title}
          title={stat.title}
          value={stat.value}
          subtitle={stat.subtitle}
          icon={stat.icon}
          color={stat.color}
        />
      ))}
    </section>
  );
}