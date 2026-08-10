"use client";

import DetectionTable from "./detection-table";

import SectionHeader from "@/components/ui/section-header";

interface Detection {
  filename: string;
  file_type: string;
  media_type?: string;
  prediction: string;
  confidence: number;
  model_name: string;
  created_at: string;
}

interface RecentDetectionProps {
  detections: Detection[];
}

export default function RecentDetection({
  detections,
}: RecentDetectionProps) {
  return (
    <section className="space-y-6">

      <div className="flex items-end justify-between">

        <SectionHeader
          title="Recent Detections"
          description="Latest AI authenticity analyses performed by the platform."
          className="mb-0"
        />

        <button className="h-11 rounded-2xl border border-white/10 bg-zinc-900 px-5 text-sm font-semibold text-white transition hover:bg-zinc-800">
          View All
        </button>

      </div>

      <DetectionTable
        detections={detections}
      />

    </section>
  );
}