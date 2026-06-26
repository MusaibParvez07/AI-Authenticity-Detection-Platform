// Backend API

export const API_BASE_URL =
  process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8000";

// API Endpoints

export const API_ENDPOINTS = {
  IMAGE: "/predict/image",
  VIDEO: "/predict/video",
  AUDIO: "/predict/audio",
  TEXT: "/predict/text",

  HISTORY: "/history",
  HEALTH: "/health",
};

// Upload Limits

export const MAX_UPLOAD_SIZE = 100 * 1024 * 1024; //100MB

// Supported File Types

export const SUPPORTED_FILE_TYPES = {
  image: ["image/jpeg", "image/png", "image/webp"],

  video: [
    "video/mp4",
    "video/quicktime",
    "video/x-msvideo",
  ],

  audio: [
    "audio/mpeg",
    "audio/wav",
    "audio/x-wav",
  ],

  text: [
    "text/plain",
  ],
};