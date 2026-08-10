"use client";

import {
  AlertCircle,
  CheckCircle2,
  Info,
} from "lucide-react";

interface ValidationMessageProps {
  type?: "error" | "success" | "info";
  message: string;
}

export default function ValidationMessage({
  type = "info",
  message,
}: ValidationMessageProps) {

  const styles = {
    error: {
      border: "border-red-500/20",
      background: "bg-red-500/10",
      text: "text-red-400",
      icon: AlertCircle,
    },

    success: {
      border: "border-emerald-500/20",
      background: "bg-emerald-500/10",
      text: "text-emerald-400",
      icon: CheckCircle2,
    },

    info: {
      border: "border-blue-500/20",
      background: "bg-blue-500/10",
      text: "text-blue-400",
      icon: Info,
    },
  };

  const current = styles[type];
  const Icon = current.icon;

  return (

    <div
      className={`flex items-start gap-3 rounded-2xl border p-4 ${current.border} ${current.background}`}
    >

      <Icon
        size={22}
        className={current.text}
      />

      <p className={`text-sm ${current.text}`}>
        {message}
      </p>

    </div>

  );

}