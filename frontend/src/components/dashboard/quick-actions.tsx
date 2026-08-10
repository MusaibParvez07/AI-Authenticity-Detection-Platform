"use client";

import {
  Image,
  Video,
  Mic,
  FileText,
} from "lucide-react";

import QuickActionCard from "./quick-action-card";

export default function QuickActions() {
  return (
    <section className="space-y-8">

      <div>

        <h2 className="text-4xl font-bold text-white">
          Quick Detection
        </h2>

        <p className="mt-3 text-lg text-zinc-400">
          Select the content type you want to analyze using our
          AI-powered authenticity detection models.
        </p>

      </div>

      <div className="grid gap-8 md:grid-cols-2">

        <QuickActionCard
          title="Image Detection"
          description="Detect AI-generated, edited and manipulated images using advanced vision models."
          href="/upload/image"
          icon={Image}
          color="bg-cyan-600"
          formats="JPG • PNG • JPEG • WEBP"
        />

        <QuickActionCard
          title="Video Detection"
          description="Analyze videos for deepfakes, synthetic faces and AI-generated visual content."
          href="/upload/video"
          icon={Video}
          color="bg-pink-600"
          formats="MP4 • AVI • MOV • MKV"
        />

        <QuickActionCard
          title="Audio Detection"
          description="Identify cloned voices, synthetic speech and AI-generated audio samples."
          href="/upload/audio"
          icon={Mic}
          color="bg-orange-600"
          formats="MP3 • WAV • FLAC"
        />

        <QuickActionCard
          title="Text Detection"
          description="Detect AI-generated articles, essays and written content with language models."
          href="/upload/text"
          icon={FileText}
          color="bg-indigo-600"
          formats="TXT • PDF • DOCX"
        />

      </div>

    </section>
  );
}