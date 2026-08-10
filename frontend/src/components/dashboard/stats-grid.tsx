"use client";

import {
  Upload,
  BrainCircuit,
  ShieldAlert,
  ShieldCheck,
  Image,
  Video,
  Mic,
  FileText,
} from "lucide-react";

import StatCard from "./stat-card";

interface LatestDetection {
  filename: string;
  file_type: string;
  prediction: string;
  confidence: number;
  model_name: string;
  created_at: string;
}

interface DashboardStats {
  total_uploads: number;
  total_predictions: number;

  real_images: number;
  fake_images: number;

  image_count: number;
  video_count: number;
  audio_count: number;
  text_count: number;

  average_confidence: number;

  latest_detection?: LatestDetection | null;

  recent_detections?: any[];
}

interface Props {
  stats: DashboardStats;
}

export default function StatsGrid({ stats }: Props) {
  return (
    <section className="grid grid-cols-1 gap-6 md:grid-cols-2 xl:grid-cols-4">

      <StatCard
        title="Uploads"
        value={stats.total_uploads}
        subtitle="Files Uploaded"
        icon={Upload}
        color="from-sky-500 to-cyan-500"
      />

      <StatCard
        title="Detections"
        value={stats.total_predictions}
        subtitle="AI Analyses"
        icon={BrainCircuit}
        color="from-violet-500 to-fuchsia-500"
      />

      <StatCard
        title="Fake"
        value={stats.fake_images}
        subtitle="Detected Fake"
        icon={ShieldAlert}
        color="from-red-500 to-pink-500"
      />

      <StatCard
        title="Authentic"
        value={stats.real_images}
        subtitle="Verified Authentic"
        icon={ShieldCheck}
        color="from-emerald-500 to-green-500"
      />

      <StatCard
        title="Images"
        value={stats.image_count}
        subtitle="Image Uploads"
        icon={Image}
        color="from-cyan-500 to-sky-500"
      />

      <StatCard
        title="Videos"
        value={stats.video_count}
        subtitle="Video Uploads"
        icon={Video}
        color="from-pink-500 to-fuchsia-500"
      />

      <StatCard
        title="Audio"
        value={stats.audio_count}
        subtitle="Audio Uploads"
        icon={Mic}
        color="from-orange-500 to-amber-500"
      />

      <StatCard
        title="Text"
        value={stats.text_count}
        subtitle="Text Analyses"
        icon={FileText}
        color="from-indigo-500 to-blue-500"
      />

    </section>
  );
}