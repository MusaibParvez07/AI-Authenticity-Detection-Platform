"use client";

import { cn } from "@/lib/utils";

interface SectionHeaderProps {
  title: string;
  description?: string;
  className?: string;
}

export default function SectionHeader({
  title,
  description,
  className,
}: SectionHeaderProps) {
  return (
    <div className={cn("mb-8", className)}>
      <h2 className="text-3xl font-bold tracking-tight text-white">
        {title}
      </h2>

      {description && (
        <p className="mt-2 max-w-2xl text-zinc-400 leading-7">
          {description}
        </p>
      )}
    </div>
  );
}