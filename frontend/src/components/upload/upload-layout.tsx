"use client";

import { ReactNode } from "react";

import AppShell from "@/components/layout/app-shell";

interface UploadLayoutProps {
  title: string;
  description: string;
  children: ReactNode;
}

export default function UploadLayout({
  title,
  description,
  children,
}: UploadLayoutProps) {
  return (
    <AppShell>

      <div className="mx-auto w-full max-w-7xl space-y-8">

        {/* Page Header */}

        <section>

          <h1 className="text-4xl font-black tracking-tight text-white xl:text-5xl">
            {title}
          </h1>

          <p className="mt-4 max-w-3xl text-lg leading-8 text-zinc-400">
            {description}
          </p>

        </section>

        {/* Content */}

        <section className="rounded-3xl border border-white/10 bg-zinc-900/40 p-8 backdrop-blur-xl">

          {children}

        </section>

      </div>

    </AppShell>
  );
}