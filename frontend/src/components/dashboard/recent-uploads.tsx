"use client";

import { useHistory } from "@/hooks/use-history";

export default function RecentUploads() {

  const {
    history,
    loading,
    error,
  } = useHistory();

  return (

    <div className="rounded-3xl border border-white/10 bg-zinc-900 p-8">

      <h2 className="text-2xl font-bold text-white">
        Recent Uploads
      </h2>

      <p className="mt-2 text-zinc-400">
        Complete history of your AI detections.
      </p>

      {loading && (

        <div className="mt-8 rounded-2xl border border-zinc-700 p-8 text-center">

          <p className="text-zinc-400">
            Loading uploads...
          </p>

        </div>

      )}

      {error && (

        <div className="mt-8 rounded-2xl border border-red-500/20 bg-red-500/5 p-8 text-center">

          <p className="text-red-400">

            {error}

          </p>

        </div>

      )}

      {!loading && !error && history.length === 0 && (

        <div className="mt-8 rounded-2xl border border-dashed border-zinc-700 py-16 text-center">

          <p className="text-lg text-zinc-300">
            No uploads yet
          </p>

          <p className="mt-2 text-zinc-500">
            Upload a file to start AI detection.
          </p>

        </div>

      )}

      {!loading && !error && history.length > 0 && (

        <div className="mt-8 overflow-x-auto">

          <table className="w-full">

            <thead>

              <tr className="border-b border-zinc-800 text-left">

                <th className="pb-4 text-sm font-semibold text-zinc-400">
                  File
                </th>

                <th className="pb-4 text-sm font-semibold text-zinc-400">
                  Type
                </th>

                <th className="pb-4 text-sm font-semibold text-zinc-400">
                  Prediction
                </th>

                <th className="pb-4 text-sm font-semibold text-zinc-400">
                  Confidence
                </th>

                <th className="pb-4 text-sm font-semibold text-zinc-400">
                  Model
                </th>

                <th className="pb-4 text-sm font-semibold text-zinc-400">
                  Date
                </th>

              </tr>

            </thead>

            <tbody>

              {history.map((item) => (

                <tr
                  key={item.detection_id}
                  className="border-b border-zinc-800 hover:bg-zinc-800/40 transition-colors"
                >

                  <td className="py-4 text-white">

                    {item.filename}

                  </td>

                  <td className="py-4">

                    <span className="rounded-full bg-zinc-800 px-3 py-1 text-xs text-zinc-300">

                      {item.file_type.toUpperCase()}

                    </span>

                  </td>

                  <td className="py-4">

                    <span
                      className={`rounded-full px-3 py-1 text-xs font-semibold ${
                        item.prediction === "real"
                          ? "bg-green-500/20 text-green-400"
                          : "bg-red-500/20 text-red-400"
                      }`}
                    >

                      {item.prediction.toUpperCase()}

                    </span>

                  </td>

                  <td className="py-4 text-white">

                    {(item.confidence * 100).toFixed(2)}%

                  </td>

                  <td className="py-4 text-zinc-300">

                    {item.model_name}

                  </td>

                  <td className="py-4 text-zinc-400">

                    {new Date(
                      item.created_at
                    ).toLocaleString()}

                  </td>

                </tr>

              ))}

            </tbody>

          </table>

        </div>

      )}

    </div>

  );

}