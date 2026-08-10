"use client";

import { LucideIcon, TrendingUp } from "lucide-react";

import Card from "@/components/ui/card";

interface StatCardProps {
  title: string;
  value: number | string;
  subtitle?: string;
  icon: LucideIcon;
  color?: string;
}

export default function StatCard({
  title,
  value,
  subtitle,
  icon: Icon,
  color = "from-violet-600 to-blue-600",
}: StatCardProps) {
  return (
    <Card
      hover
      glow
      className="group"
    >
      {/* Decorative Glow */}

      <div className="absolute -right-8 -top-8 h-28 w-28 rounded-full bg-violet-500/10 blur-3xl transition-all duration-300 group-hover:scale-125" />

      <div className="relative flex items-start justify-between">

        <div>

          <p className="text-xs uppercase tracking-[0.28em] text-zinc-500">
            {title}
          </p>

          <h2 className="mt-4 text-4xl font-bold text-white">
            {value}
          </h2>

          {subtitle && (
            <p className="mt-2 text-sm text-zinc-400">
              {subtitle}
            </p>
          )}

          <div className="mt-5 flex items-center gap-2">

            <TrendingUp
              size={15}
              className="text-emerald-400"
            />

            <span className="text-sm font-medium text-emerald-400">
              Live Statistics
            </span>

          </div>

        </div>

        <div
          className={`flex h-16 w-16 items-center justify-center rounded-2xl bg-gradient-to-br ${color}`}
        >
          <Icon
            size={28}
            className="text-white"
          />
        </div>

      </div>
    </Card>
  );
}