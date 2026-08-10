"use client";

import * as React from "react";
import { cn } from "@/lib/utils";

interface CardProps extends React.HTMLAttributes<HTMLDivElement> {
  hover?: boolean;
  glow?: boolean;
  padding?: "none" | "sm" | "md" | "lg";
}

export default function Card({
  children,
  className,
  hover = true,
  glow = false,
  padding = "md",
  ...props
}: CardProps) {
  const paddingClass = {
    none: "",
    sm: "p-4",
    md: "p-6",
    lg: "p-8",
  };

  return (
    <div
      {...props}
      className={cn(
        "relative overflow-hidden rounded-3xl",
        "border border-white/10",
        "bg-gradient-to-br from-[#111827] via-[#101827] to-[#0B1220]",
        "transition-all duration-300",

        paddingClass[padding],

        hover &&
          "hover:-translate-y-1 hover:border-violet-500/40",

        glow &&
          "hover:shadow-[0_0_45px_rgba(124,58,237,.18)]",

        className
      )}
    >
      {children}
    </div>
  );
}