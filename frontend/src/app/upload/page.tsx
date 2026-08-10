"use client";

import UploadLayout from "@/components/upload/upload-layout";
import UploadCard from "@/components/upload/upload-card";

export default function UploadPage() {
  return (
    <UploadLayout
      title="AI File Upload"
      description="Upload an image, video, audio or text file for AI authenticity analysis."
    >
      <UploadCard />
    </UploadLayout>
  );
}