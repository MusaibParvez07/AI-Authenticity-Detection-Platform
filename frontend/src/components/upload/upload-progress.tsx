"use client";

import {
  Loader2,
  CheckCircle2,
} from "lucide-react";

interface UploadProgressProps {
  loading: boolean;
  progress: number;
}

export default function UploadProgress({
  loading,
  progress,
}: UploadProgressProps) {

  return (

    <div className="space-y-5 rounded-3xl border border-white/10 bg-zinc-900/60 p-6">

      <div className="flex items-center justify-between">

        <div className="flex items-center gap-3">

          {loading ? (

            <Loader2
              size={22}
              className="animate-spin text-violet-400"
            />

          ) : (

            <CheckCircle2
              size={22}
              className="text-green-400"
            />

          )}

          <div>

            <h3 className="font-semibold text-white">

              {loading
                ? "Uploading & Analyzing..."
                : "Analysis Complete"}

            </h3>

            <p className="text-sm text-zinc-400">

              {loading
                ? "Your file is being uploaded and processed by the AI engine."
                : "Detection finished successfully."}

            </p>

          </div>

        </div>

        <span className="text-lg font-bold text-violet-400">

          {progress}%

        </span>

      </div>

      <div className="h-3 overflow-hidden rounded-full bg-zinc-800">

        <div
          className="h-full rounded-full bg-gradient-to-r from-violet-600 via-blue-500 to-cyan-500 transition-all duration-300"
          style={{
            width: `${progress}%`,
          }}
        />

      </div>

    </div>

  );

}