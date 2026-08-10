"use client";

import Card from "@/components/ui/card";

import {
  FileAudio,
  FileImage,
  FileText,
  FileVideo,
  ShieldAlert,
  ShieldCheck,
} from "lucide-react";

interface Detection {

  filename: string;

  file_type: string;

  media_type?: string;

  prediction: string;

  confidence: number;

  model_name: string;

  created_at: string;

}

interface Props {

  detections: Detection[];

}

function getMediaType(item: Detection): string {

  if (item.media_type) {

    return item.media_type;

  }

  const type = item.file_type.toLowerCase();

  if (type.startsWith("image")) {

    return "image";

  }

  if (type.startsWith("video")) {

    return "video";

  }

  if (type.startsWith("audio")) {

    return "audio";

  }

  return "text";

}

function getIcon(type: string) {

  switch (type.toLowerCase()) {

    case "image":

      return <FileImage size={18} />;

    case "video":

      return <FileVideo size={18} />;

    case "audio":

      return <FileAudio size={18} />;

    default:

      return <FileText size={18} />;

  }

}

export default function DetectionTable({
  detections,
}: Props) {

  if (!detections.length) {

    return (

      <Card
        hover={false}
        className="py-16"
      >

        <div className="text-center">

          <ShieldCheck
            size={64}
            className="mx-auto text-violet-500"
          />

          <h3 className="mt-6 text-2xl font-bold text-white">

            No Detections Yet

          </h3>

          <p className="mx-auto mt-3 max-w-md text-zinc-400">

            Upload an image, video, audio or text file to begin AI authenticity analysis.

          </p>

        </div>

      </Card>

    );

  }

  return (

    <Card
      hover={false}
      padding="none"
      className="overflow-hidden"
    >

      <table className="w-full">

        <thead className="border-b border-white/10 bg-zinc-900/70">

          <tr>

            <th className="px-6 py-5 text-left text-sm font-semibold text-zinc-400">
              File
            </th>

            <th className="px-6 py-5 text-left text-sm font-semibold text-zinc-400">
              Media
            </th>

            <th className="px-6 py-5 text-left text-sm font-semibold text-zinc-400">
              Prediction
            </th>

            <th className="px-6 py-5 text-left text-sm font-semibold text-zinc-400">
              Confidence
            </th>

            <th className="px-6 py-5 text-left text-sm font-semibold text-zinc-400">
              Model
            </th>

            <th className="px-6 py-5 text-left text-sm font-semibold text-zinc-400">
              Date
            </th>

          </tr>

        </thead>

        <tbody>

          {detections.map((item, index) => {

            const mediaType = getMediaType(item);

            return (

              <tr
                key={index}
                className="border-b border-white/5 transition hover:bg-white/5"
              >

                <td className="px-6 py-5 font-medium text-white">

                  {item.filename}

                </td>

                <td className="px-6 py-5">

                  <div className="flex items-center gap-3 text-white">

                    {getIcon(mediaType)}

                    <span className="capitalize">

                      {mediaType}

                    </span>

                  </div>

                </td>

                <td className="px-6 py-5">

                  {item.prediction.toLowerCase() === "fake" ? (

                    <span className="inline-flex items-center gap-2 rounded-full bg-red-500/15 px-4 py-2 text-sm font-medium text-red-400">

                      <ShieldAlert size={16} />

                      Fake

                    </span>

                  ) : (

                    <span className="inline-flex items-center gap-2 rounded-full bg-green-500/15 px-4 py-2 text-sm font-medium text-green-400">

                      <ShieldCheck size={16} />

                      Authentic

                    </span>

                  )}

                </td>

                <td className="px-6 py-5 font-semibold text-cyan-400">

                  {(item.confidence * 100).toFixed(2)}%

                </td>

                <td className="px-6 py-5 text-violet-400">

                  {item.model_name}

                </td>

                <td className="px-6 py-5 text-zinc-400">

                  {new Date(item.created_at).toLocaleString()}

                </td>

              </tr>

            );

          })}

        </tbody>

      </table>

    </Card>

  );

}