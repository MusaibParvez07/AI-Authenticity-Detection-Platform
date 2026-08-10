"use client";

import { useState } from "react";

import UploadService, {
  DetectionResponse,
} from "@/services/upload.service";

export function useUpload() {

  const [loading, setLoading] =
    useState(false);

  const [progress, setProgress] =
    useState(0);

  const [error, setError] =
    useState("");

  const [result, setResult] =
    useState<DetectionResponse | null>(null);

  // ---------------------------------------
  // Upload File
  // ---------------------------------------

  const upload = async (
    file: File
  ): Promise<DetectionResponse | null> => {

    try {

      setLoading(true);

      setProgress(0);

      setError("");

      setResult(null);

      const response =
        await UploadService.upload(
          file,
          (value) => {

            setProgress(value);

          }
        );

      setProgress(100);

      setResult(response);

      return response;

    }

    catch (err: unknown) {

      console.error(err);

      if (
        typeof err === "object" &&
        err !== null &&
        "response" in err
      ) {

        const axiosError = err as {
          response?: {
            data?: {
              detail?: string;
            };
          };
        };

        setError(
          axiosError.response?.data?.detail ??
          "Upload failed."
        );

      }

      else if (
        err instanceof Error
      ) {

        setError(err.message);

      }

      else {

        setError(
          "Upload failed."
        );

      }

      return null;

    }

    finally {

      setLoading(false);

    }

  };

  // ---------------------------------------
  // Reset
  // ---------------------------------------

  const reset = () => {

    setProgress(0);

    setResult(null);

    setError("");

  };

  return {

    upload,

    loading,

    progress,

    error,

    result,

    reset,

  };

}