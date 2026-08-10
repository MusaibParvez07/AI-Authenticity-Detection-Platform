"use client";

import {
  Calendar,
  File,
  HardDrive,
  Tag,
} from "lucide-react";

interface FileInfoProps {
  file: File;
}

function formatFileSize(bytes: number) {

  if (bytes < 1024) {
    return `${bytes} Bytes`;
  }

  if (bytes < 1024 * 1024) {
    return `${(bytes / 1024).toFixed(2)} KB`;
  }

  return `${(bytes / (1024 * 1024)).toFixed(2)} MB`;

}

function getMediaType(file: File) {

  if (file.type.startsWith("image/")) {
    return "Image";
  }

  if (file.type.startsWith("video/")) {
    return "Video";
  }

  if (file.type.startsWith("audio/")) {
    return "Audio";
  }

  if (file.type.startsWith("text/")) {
    return "Text";
  }

  return "Unknown";

}

export default function FileInfo({
  file,
}: FileInfoProps) {

  return (

    <div className="grid gap-4 rounded-2xl border border-white/10 bg-zinc-900/50 p-6 lg:grid-cols-4">

      {/* File Name */}

      <div className="flex items-center gap-3">

        <File
          size={22}
          className="text-violet-400"
        />

        <div>

          <p className="text-xs uppercase tracking-wide text-zinc-500">
            File Name
          </p>

          <p className="truncate font-medium text-white">
            {file.name}
          </p>

        </div>

      </div>

      {/* File Size */}

      <div className="flex items-center gap-3">

        <HardDrive
          size={22}
          className="text-blue-400"
        />

        <div>

          <p className="text-xs uppercase tracking-wide text-zinc-500">
            File Size
          </p>

          <p className="font-medium text-white">
            {formatFileSize(file.size)}
          </p>

        </div>

      </div>

      {/* Media Type */}

      <div className="flex items-center gap-3">

        <Tag
          size={22}
          className="text-amber-400"
        />

        <div>

          <p className="text-xs uppercase tracking-wide text-zinc-500">
            Media Type
          </p>

          <p className="font-medium text-white">
            {getMediaType(file)}
          </p>

        </div>

      </div>

      {/* Last Modified */}

      <div className="flex items-center gap-3">

        <Calendar
          size={22}
          className="text-emerald-400"
        />

        <div>

          <p className="text-xs uppercase tracking-wide text-zinc-500">
            Last Modified
          </p>

          <p className="font-medium text-white">
            {new Date(file.lastModified).toLocaleString()}
          </p>

        </div>

      </div>

    </div>

  );

}