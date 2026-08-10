"use client";

import UploadLayout from "@/components/upload/upload-layout";
import UploadCard from "@/components/upload/upload-card";

export default function VideoUploadPage() {
  return (
    <UploadLayout
      title="Video Detection"
      description="Upload a video file for AI authenticity analysis."
    >
      <UploadCard />
    </UploadLayout>
  );
}