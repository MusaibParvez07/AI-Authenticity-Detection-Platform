"use client";

import {
  ShieldAlert,
  ShieldCheck,
  BrainCircuit,
  FolderOpen,
  Hash,
} from "lucide-react";

import Card from "@/components/ui/card";

import { DetectionResponse } from "@/services/upload.service";

interface UploadResultProps {
  result: DetectionResponse;
}

export default function UploadResult({
  result,
}: UploadResultProps) {

  const isFake =
    result.prediction.toLowerCase() === "fake";

  return (

    <Card
      hover={false}
      glow
      className="space-y-8"
    >

      <div className="flex items-center gap-4">

        <div
          className={`flex h-16 w-16 items-center justify-center rounded-2xl ${
            isFake
              ? "bg-red-500/15"
              : "bg-emerald-500/15"
          }`}
        >

          {isFake ? (

            <ShieldAlert
              size={34}
              className="text-red-400"
            />

          ) : (

            <ShieldCheck
              size={34}
              className="text-emerald-400"
            />

          )}

        </div>

        <div>

          <h2 className="text-3xl font-bold text-white">

            {isFake
              ? "Fake Content Detected"
              : "Authentic Content"}

          </h2>

          <p className="mt-2 text-zinc-400">

            AI analysis completed successfully.

          </p>

        </div>

      </div>

      <div className="grid gap-5 md:grid-cols-2 xl:grid-cols-4">

        <div className="rounded-2xl border border-white/10 bg-zinc-900/60 p-5">

          <p className="text-sm text-zinc-400">
            Prediction
          </p>

          <h3
            className={`mt-3 text-2xl font-bold ${
              isFake
                ? "text-red-400"
                : "text-emerald-400"
            }`}
          >
            {result.prediction}
          </h3>

        </div>

        <div className="rounded-2xl border border-white/10 bg-zinc-900/60 p-5">

          <div className="flex items-center gap-2">

            <BrainCircuit
              size={18}
              className="text-blue-400"
            />

            <span className="text-sm text-zinc-400">

              Confidence

            </span>

          </div>

          <h3 className="mt-3 text-2xl font-bold text-white">

            {(result.confidence * 100).toFixed(2)}%

          </h3>

        </div>

        <div className="rounded-2xl border border-white/10 bg-zinc-900/60 p-5">

          <div className="flex items-center gap-2">

            <Hash
              size={18}
              className="text-yellow-400"
            />

            <span className="text-sm text-zinc-400">

              Upload ID

            </span>

          </div>

          <h3 className="mt-3 text-xl font-bold text-white">

            #{result.upload_id}

          </h3>

        </div>

        <div className="rounded-2xl border border-white/10 bg-zinc-900/60 p-5">

          <div className="flex items-center gap-2">

            <FolderOpen
              size={18}
              className="text-cyan-400"
            />

            <span className="text-sm text-zinc-400">

              Detection ID

            </span>

          </div>

          <h3 className="mt-3 text-xl font-bold text-white">

            #{result.detection_id}

          </h3>

        </div>

      </div>

      <div className="rounded-2xl border border-white/10 bg-zinc-900/60 p-5">

        <p className="text-sm text-zinc-500">

          Stored File

        </p>

        <p className="mt-2 break-all text-white">

          {result.file_path}

        </p>

      </div>

    </Card>

  );

}