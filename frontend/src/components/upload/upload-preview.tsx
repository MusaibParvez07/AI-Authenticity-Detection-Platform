"use client";

import { useMemo } from "react";

import {
  FileAudio,
  FileText,
  ImageIcon,
} from "lucide-react";

interface UploadPreviewProps {
  file: File;
}

export default function UploadPreview({
  file,
}: UploadPreviewProps) {

  const preview = useMemo(() => {

    if (
      file.type.startsWith("image/") ||
      file.type.startsWith("video/") ||
      file.type.startsWith("audio/")
    ) {

      return URL.createObjectURL(file);

    }

    return null;

  }, [file]);

  // ----------------------------
  // IMAGE
  // ----------------------------

  if (file.type.startsWith("image/")) {

    return (

      <div className="overflow-hidden rounded-3xl border border-white/10">

        <img
          src={preview ?? ""}
          alt={file.name}
          className="max-h-[420px] w-full object-contain bg-zinc-950"
        />

      </div>

    );

  }

  // ----------------------------
  // VIDEO
  // ----------------------------

  if (file.type.startsWith("video/")) {

    return (

      <div className="overflow-hidden rounded-3xl border border-white/10 bg-black">

        <video
          controls
          className="max-h-[420px] w-full"
        >

          <source
            src={preview ?? ""}
            type={file.type}
          />

        </video>

      </div>

    );

  }

  // ----------------------------
  // AUDIO
  // ----------------------------

  if (file.type.startsWith("audio/")) {

    return (

      <div className="flex flex-col items-center gap-6 rounded-3xl border border-white/10 bg-zinc-900 p-10">

        <FileAudio
          size={72}
          className="text-violet-400"
        />

        <audio
          controls
          className="w-full"
        >

          <source
            src={preview ?? ""}
            type={file.type}
          />

        </audio>

      </div>

    );

  }

  // ----------------------------
  // TEXT
  // ----------------------------

  if (
    file.type.startsWith("text/") ||
    file.name.endsWith(".txt")
  ) {

    return (

      <div className="flex min-h-[260px] items-center justify-center rounded-3xl border border-white/10 bg-zinc-900">

        <div className="text-center">

          <FileText
            size={72}
            className="mx-auto text-violet-400"
          />

          <h3 className="mt-5 text-xl font-semibold text-white">
            Text File Selected
          </h3>

          <p className="mt-2 text-zinc-400">
            {file.name}
          </p>

        </div>

      </div>

    );

  }

  // ----------------------------
  // UNKNOWN
  // ----------------------------

  return (

    <div className="flex min-h-[260px] items-center justify-center rounded-3xl border border-white/10 bg-zinc-900">

      <div className="text-center">

        <ImageIcon
          size={72}
          className="mx-auto text-violet-400"
        />

        <p className="mt-5 text-zinc-400">
          Preview not available.
        </p>

      </div>

    </div>

  );

}