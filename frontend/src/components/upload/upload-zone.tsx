"use client";

import { useRef } from "react";

import { UploadCloud } from "lucide-react";

import { Button } from "@/components/ui/button";
interface UploadZoneProps {
  accept: string;
  disabled?: boolean;
  onFileSelect: (file: File) => void;
}

export default function UploadZone({
  accept,
  disabled = false,
  onFileSelect,
}: UploadZoneProps) {

  const inputRef = useRef<HTMLInputElement>(null);

  function handleBrowse() {
    inputRef.current?.click();
  }

  function handleFile(file?: File) {
    if (!file) return;

    onFileSelect(file);
  }

  function handleInputChange(
    event: React.ChangeEvent<HTMLInputElement>
  ) {
    const file = event.target.files?.[0];

    handleFile(file);
  }

  function handleDrop(
    event: React.DragEvent<HTMLDivElement>
  ) {
    event.preventDefault();

    if (disabled) return;

    const file = event.dataTransfer.files?.[0];

    handleFile(file);
  }

  function handleDragOver(
    event: React.DragEvent<HTMLDivElement>
  ) {
    event.preventDefault();
  }

  return (
    <div
      onDrop={handleDrop}
      onDragOver={handleDragOver}
      className="flex min-h-[320px] flex-col items-center justify-center rounded-3xl border-2 border-dashed border-violet-500/40 bg-zinc-900/40 p-10 text-center transition hover:border-violet-400"
    >

      <UploadCloud
        size={72}
        className="text-violet-400"
      />

      <h2 className="mt-6 text-2xl font-bold text-white">
        Drag & Drop your file
      </h2>

      <p className="mt-3 max-w-lg text-zinc-400">
        Drag your file into this area or click the button below
        to browse your computer.
      </p>

      <Button
        onClick={handleBrowse}
        disabled={disabled}
        className="mt-8"
      >
        Browse Files
      </Button>

      <input
        ref={inputRef}
        hidden
        type="file"
        accept={accept}
        onChange={handleInputChange}
      />

    </div>
  );
}