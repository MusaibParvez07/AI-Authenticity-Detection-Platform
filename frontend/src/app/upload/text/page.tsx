"use client";

import UploadLayout from "@/components/upload/upload-layout";
import UploadCard from "@/components/upload/upload-card";

export default function TextUploadPage() {
  return (
    <UploadLayout
      title="Text Detection"
      description="Upload a text document to detect AI-generated or human-written content."
    >
      <UploadCard />
    </UploadLayout>
  );
}