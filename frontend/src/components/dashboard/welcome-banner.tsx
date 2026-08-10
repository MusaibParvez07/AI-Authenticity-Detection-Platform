"use client";

import Link from "next/link";
import { motion } from "framer-motion";

import {
  ShieldCheck,
  Upload,
  History,
  ArrowRight,
  Sparkles,
} from "lucide-react";

import Card from "@/components/ui/card";

export default function WelcomeBanner() {
  return (
    <motion.div
      initial={{ opacity: 0, y: 15 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.45 }}
    >
      <Card
        glow
        hover={false}
        padding="none"
        className="relative overflow-hidden"
      >
        {/* Background Glow */}

        <div className="absolute -left-20 -top-20 h-72 w-72 rounded-full bg-blue-500/15 blur-[120px]" />

        <div className="absolute right-0 top-0 h-80 w-80 rounded-full bg-violet-600/15 blur-[140px]" />

        <div className="relative grid min-h-[320px] items-center gap-8 px-10 py-8 lg:grid-cols-[1.5fr_.8fr]">

          {/* Left */}

          <div className="max-w-xl">

            <div className="mb-5 flex items-center gap-4">

              <div className="flex h-14 w-14 items-center justify-center rounded-2xl bg-gradient-to-br from-violet-600 to-blue-600 shadow-lg">

                <ShieldCheck
                  size={30}
                  className="text-white"
                />

              </div>

              <span className="rounded-full border border-violet-500/20 bg-violet-500/10 px-4 py-1 text-sm font-medium text-violet-300">
                AI Security Platform
              </span>

            </div>

            <h1 className="text-4xl font-black leading-tight text-white xl:text-5xl">

              AI Authenticity

              <br />

              <span className="bg-gradient-to-r from-violet-400 to-blue-400 bg-clip-text text-transparent">
                Detection Platform
              </span>

            </h1>

            <p className="mt-5 text-base leading-7 text-zinc-400">

              Detect AI-generated images, videos, audio and text
              using advanced multimodal deep learning models with
              real-time authenticity verification.

            </p>

            <div className="mt-8 flex flex-wrap gap-4">

              <Link
                href="/upload"
                className="inline-flex h-12 items-center gap-2 rounded-2xl bg-gradient-to-r from-violet-600 to-blue-600 px-6 font-semibold text-white transition hover:scale-105"
              >
                <Upload size={18} />

                Upload

                <ArrowRight size={18} />

              </Link>

              <Link
                href="/history"
                className="inline-flex h-12 items-center gap-2 rounded-2xl border border-white/10 bg-zinc-900 px-6 font-semibold text-white transition hover:bg-zinc-800"
              >
                <History size={18} />

                History

              </Link>

            </div>

          </div>

          {/* Right */}

          <div className="flex justify-center">

            <div className="relative">

              <div className="absolute inset-0 rounded-full bg-violet-500/20 blur-[70px]" />

              <div className="relative flex h-52 w-52 items-center justify-center rounded-full border border-violet-500/20 bg-gradient-to-br from-violet-500/15 to-blue-500/15">

                <Sparkles
                  size={78}
                  className="text-violet-400"
                />

              </div>

              <div className="absolute left-5 top-5 h-3 w-3 rounded-full bg-violet-400 animate-ping" />

              <div className="absolute bottom-8 right-8 h-3 w-3 rounded-full bg-blue-400 animate-ping" />

              <div className="absolute bottom-5 left-12 h-2 w-2 rounded-full bg-white animate-pulse" />

            </div>

          </div>

        </div>

      </Card>
    </motion.div>
  );
}