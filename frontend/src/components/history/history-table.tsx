"use client";

import { HistoryItem } from "@/types/history";

interface HistoryTableProps {
  history: HistoryItem[];
}

function getPredictionColor(prediction: string) {
  const value = prediction.toLowerCase();

  if (value === "real") {
    return "bg-green-500/20 text-green-400 border-green-500/30";
  }

  return "bg-red-500/20 text-red-400 border-red-500/30";
}

function getMediaColor(type: string) {
  switch (type.toLowerCase()) {
    case "image":
      return "text-cyan-400";

    case "video":
      return "text-violet-400";

    case "audio":
      return "text-orange-400";

    case "text":
      return "text-yellow-400";

    default:
      return "text-zinc-400";
  }
}

export default function HistoryTable({
  history,
}: HistoryTableProps) {

  if (history.length === 0) {

    return (

      <div className="rounded-3xl border border-zinc-800 bg-[#0b1220] p-12 text-center">

        <h2 className="text-2xl font-semibold text-white">
          No Detection History
        </h2>

        <p className="mt-3 text-zinc-400">
          Upload an image, video, audio or text file to begin.
        </p>

      </div>

    );

  }

  return (

    <div className="overflow-hidden rounded-3xl border border-zinc-800 bg-[#0b1220]">

      <div className="overflow-x-auto">

        <table className="min-w-full">

          <thead className="border-b border-zinc-800 bg-[#111827]">

            <tr>

              <th className="px-6 py-4 text-left text-sm font-semibold text-zinc-300">
                File
              </th>

              <th className="px-6 py-4 text-left text-sm font-semibold text-zinc-300">
                Media
              </th>

              <th className="px-6 py-4 text-left text-sm font-semibold text-zinc-300">
                Prediction
              </th>

              <th className="px-6 py-4 text-left text-sm font-semibold text-zinc-300">
                Confidence
              </th>

              <th className="px-6 py-4 text-left text-sm font-semibold text-zinc-300">
                Model
              </th>

              <th className="px-6 py-4 text-left text-sm font-semibold text-zinc-300">
                Date
              </th>

            </tr>

          </thead>

          <tbody>

            {history.map((item) => (

              <tr
                key={item.detection_id}
                className="border-b border-zinc-800 transition hover:bg-[#131d2f]"
              >

                <td className="px-6 py-5">

                  <div className="font-medium text-white">
                    {item.filename}
                  </div>

                </td>

                <td
                  className={`px-6 py-5 font-semibold capitalize ${getMediaColor(
                    item.media_type
                  )}`}
                >
                  {item.media_type}
                </td>

                <td className="px-6 py-5">

                  <span
                    className={`rounded-full border px-4 py-1 text-sm font-semibold ${getPredictionColor(
                      item.prediction
                    )}`}
                  >
                    {item.prediction}
                  </span>

                </td>

                <td className="px-6 py-5">

                  <div className="flex items-center gap-3">

                    <div className="h-2 w-36 rounded-full bg-zinc-700">

                      <div
                        className="h-2 rounded-full bg-violet-500"
                        style={{
                          width: `${item.confidence * 100}%`,
                        }}
                      />

                    </div>

                    <span className="text-sm text-white">

                      {(item.confidence * 100).toFixed(1)}%

                    </span>

                  </div>

                </td>

                <td className="px-6 py-5 text-sm text-zinc-300">

                  {item.model_name}

                </td>

                <td className="px-6 py-5 text-sm text-zinc-400">

                  {new Date(item.created_at).toLocaleString()}

                </td>

              </tr>

            ))}

          </tbody>

        </table>

      </div>

    </div>

  );

}