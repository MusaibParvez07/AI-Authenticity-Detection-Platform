"use client";

import { useCallback, useState } from "react";
import { useDropzone } from "react-dropzone";
import {
  Upload,
  Link2,
  File,
  ImageIcon,
  FileVideo,
  FileAudio,
  FileText,
  CheckCircle2,
} from "lucide-react";

import { Button } from "@/components/ui/button";

export default function UploadCard() {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);

  const onDrop = useCallback((acceptedFiles: File[]) => {
    if (acceptedFiles.length > 0) {
      setSelectedFile(acceptedFiles[0]);
    }
  }, []);

  const { getRootProps, getInputProps, isDragActive, open } = useDropzone({
    onDrop,
    multiple: false,
    noClick: true,
    maxSize: 100 * 1024 * 1024,
    accept: {
      "image/*": [".jpg", ".jpeg", ".png"],
      "video/*": [".mp4"],
      "audio/*": [".mp3", ".wav"],
      "text/plain": [".txt"],
    },
  });

  const getFileIcon = () => {
    if (!selectedFile) return <File className="h-7 w-7 text-blue-500" />;

    if (selectedFile.type.startsWith("image"))
      return <ImageIcon className="h-7 w-7 text-green-400" />;

    if (selectedFile.type.startsWith("video"))
      return <FileVideo className="h-7 w-7 text-purple-400" />;

    if (selectedFile.type.startsWith("audio"))
      return <FileAudio className="h-7 w-7 text-orange-400" />;

    if (selectedFile.type.startsWith("text"))
      return <FileText className="h-7 w-7 text-cyan-400" />;

    return <File className="h-7 w-7 text-blue-400" />;
  };

  return (
    <div className="rounded-3xl border border-white/10 bg-zinc-900 p-8">

      {/* Header */}

      <div className="flex flex-col gap-6 lg:flex-row lg:items-center lg:justify-between">

        <div>

          <h2 className="text-2xl font-bold text-white">
            Quick Upload
          </h2>

          <p className="mt-2 text-zinc-400">
            Upload an image, video, audio or text file for AI analysis.
          </p>

        </div>

        <div className="flex flex-wrap gap-2">

          {["JPG", "PNG", "MP4", "MP3", "WAV", "TXT"].map((item) => (
            <span
              key={item}
              className="rounded-full bg-zinc-800 px-3 py-1 text-xs text-zinc-400"
            >
              {item}
            </span>
          ))}

        </div>

      </div>

      {/* Upload Box */}

      <div
        {...getRootProps()}
        className={`mt-8 rounded-2xl border-2 border-dashed p-12 transition-all duration-300 cursor-pointer

        ${
          isDragActive
            ? "border-blue-500 bg-blue-500/10"
            : "border-zinc-700 bg-zinc-950 hover:border-blue-500 hover:bg-zinc-900"
        }`}
      >
        <input {...getInputProps()} />

        <div className="flex flex-col items-center text-center">

          <div className="mb-6 flex h-20 w-20 items-center justify-center rounded-full bg-blue-500/10">

            {selectedFile ? (
              getFileIcon()
            ) : (
              <Upload className="h-10 w-10 text-blue-500" />
            )}

          </div>

          {selectedFile ? (
            <>
              <CheckCircle2 className="mb-4 h-10 w-10 text-green-500" />

              <h3 className="text-2xl font-bold text-white">
                File Selected
              </h3>

              <p className="mt-4 text-lg text-zinc-300">
                {selectedFile.name}
              </p>

              <p className="mt-2 text-sm text-zinc-500">
                {(selectedFile.size / 1024 / 1024).toFixed(2)} MB
              </p>
            </>
          ) : (
            <>
              <h3 className="text-3xl font-bold text-white">
                Drag & Drop Files
              </h3>

              <p className="mt-3 text-zinc-400">
                Images • Videos • Audio • Text
              </p>
            </>
          )}

          <div className="mt-8 flex flex-wrap justify-center gap-4">

            <Button
              size="lg"
              onClick={(e) => {
                e.stopPropagation();
                open();
              }}
            >
              Browse Files
            </Button>

            <Button
              size="lg"
              variant="outline"
            >
              <Link2 className="mr-2 h-4 w-4" />
              Paste URL
            </Button>

          </div>

          <p className="mt-8 text-sm text-zinc-500">
            Maximum file size: 100 MB
          </p>

        </div>

      </div>

    </div>
  );
}