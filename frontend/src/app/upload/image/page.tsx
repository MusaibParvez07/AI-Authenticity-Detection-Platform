"use client";

import UploadLayout from "@/components/upload/upload-layout";
import UploadCard from "@/components/upload/upload-card";

export default function ImageUploadPage() {
  return (
    <UploadLayout
      title="Image Detection"
      description="Upload an image and let our AI determine whether it is authentic or AI-generated."
    >
      <UploadCard />
    </UploadLayout>
  );
}