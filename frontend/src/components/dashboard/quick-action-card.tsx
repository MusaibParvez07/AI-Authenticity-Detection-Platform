"use client";

import Link from "next/link";
import { ArrowRight, LucideIcon } from "lucide-react";

import Card from "@/components/ui/card";

interface Props {
  title: string;
  description: string;
  href: string;
  icon: LucideIcon;
  color: string;
  formats: string;
}

export default function QuickActionCard({
  title,
  description,
  href,
  icon: Icon,
  color,
  formats,
}: Props) {
  return (
    <Link href={href} className="block">
      <Card
        hover
        glow
        className="group h-[230px] cursor-pointer"
      >
        {/* Decorative Glow */}

        <div className="absolute -right-12 -top-12 h-36 w-36 rounded-full bg-violet-500/10 blur-3xl transition-all duration-300 group-hover:scale-125" />

        <div className="flex h-full flex-col">

          {/* Top */}

          <div className="flex items-start justify-between">

            <div
              className={`flex h-16 w-16 items-center justify-center rounded-2xl bg-gradient-to-br ${color}`}
            >
              <Icon
                size={30}
                className="text-white"
              />
            </div>

            <ArrowRight
              className="text-zinc-500 transition-all duration-300 group-hover:translate-x-2 group-hover:text-violet-400"
              size={22}
            />

          </div>

          {/* Content */}

          <div className="mt-6">

            <h3 className="text-2xl font-bold text-white">
              {title}
            </h3>

            <p className="mt-3 text-sm leading-7 text-zinc-400">
              {description}
            </p>

          </div>

          {/* Bottom */}

          <div className="mt-auto">

            <p className="text-xs uppercase tracking-[0.28em] text-zinc-500">
              Supported Formats
            </p>

            <p className="mt-2 font-medium text-violet-400">
              {formats}
            </p>

          </div>

        </div>

      </Card>
    </Link>
  );
}