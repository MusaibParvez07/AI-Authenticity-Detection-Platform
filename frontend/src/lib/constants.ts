// --------------------------------------------------
// Backend API
// --------------------------------------------------

export const API_BASE_URL =
  process.env.NEXT_PUBLIC_API_URL ??
  "http://127.0.0.1:8000";

// --------------------------------------------------
// API Endpoints
// --------------------------------------------------

export const API_ENDPOINTS = {

  // --------------------------------------------
  // Authentication
  // --------------------------------------------

  AUTH: {

    LOGIN: "/auth/login",

    REGISTER: "/auth/register",

    ME: "/auth/me",

  },

  // --------------------------------------------
  // Detection
  // --------------------------------------------

  DETECTION: {

    IMAGE: "/detect/image",

    VIDEO: "/detect/video",

    AUDIO: "/detect/audio",

    TEXT: "/detect/text",

  },

  // --------------------------------------------
  // Dashboard
  // --------------------------------------------

  DASHBOARD: "/dashboard",

  // --------------------------------------------
  // History
  // --------------------------------------------

  HISTORY: "/history",

  // --------------------------------------------
  // Models
  // --------------------------------------------

  MODELS: "/models",

  // --------------------------------------------
  // Health
  // --------------------------------------------

  HEALTH: "/health",

};

// --------------------------------------------------
// Upload Configuration
// --------------------------------------------------

export const MAX_UPLOAD_SIZE =
  100 * 1024 * 1024;

// 100 MB

export const SUPPORTED_FILE_TYPES = {

  image: [

    "image/jpeg",

    "image/png",

    "image/webp",

  ],

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

// --------------------------------------------------
// File Picker Accept String
// --------------------------------------------------

export const ACCEPT_STRING =
  "image/*,video/*,audio/*,.txt";