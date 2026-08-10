"use client";

import UploadLayout from "@/components/upload/upload-layout";
import UploadCard from "@/components/upload/upload-card";

export default function AudioUploadPage() {
  return (
    <UploadLayout
      title="Audio Detection"
      description="Upload an audio recording to detect AI-generated or manipulated speech."
    >
      <UploadCard />
    </UploadLayout>
  );
}