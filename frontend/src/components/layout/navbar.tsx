"use client";

import {
  Bell,
  Moon,
  Search,
  UserCircle2,
} from "lucide-react";

export default function Navbar() {
  return (
    <header className="sticky top-0 z-40 h-20 border-b border-white/10 bg-[#050816]/95 backdrop-blur-xl">

      <div className="flex h-full items-center justify-between gap-6 px-8">

        {/* Left */}

        <div className="min-w-[220px]">

          <h1 className="text-3xl font-bold text-white">
            Dashboard
          </h1>

          <p className="mt-1 text-sm text-zinc-400">
            Welcome back,
            <span className="ml-1 font-semibold text-violet-400">
              Mukund Kumar
            </span>
            👋
          </p>

        </div>

        {/* Center */}

        <div className="flex flex-1 justify-center">

          <div className="relative w-full max-w-xl">

            <Search
              className="absolute left-4 top-1/2 -translate-y-1/2 text-zinc-500"
              size={20}
            />

            <input
              type="text"
              placeholder="Search..."
              className="h-14 w-full rounded-2xl border border-white/10 bg-zinc-900 pl-12 pr-4 text-white outline-none transition focus:border-violet-500"
            />

          </div>

        </div>

        {/* Right */}

        <div className="flex items-center gap-4">

          <button className="relative flex h-14 w-14 items-center justify-center rounded-2xl bg-zinc-900 transition hover:bg-zinc-800">

            <Bell className="text-white" />

            <span className="absolute right-3 top-3 h-2.5 w-2.5 rounded-full bg-violet-500" />

          </button>

          <button className="flex h-14 w-14 items-center justify-center rounded-2xl bg-zinc-900 transition hover:bg-zinc-800">

            <Moon className="text-white" />

          </button>

          <div className="flex items-center gap-3 rounded-2xl border border-white/10 bg-zinc-900 px-4 py-3">

            <UserCircle2
              size={42}
              className="text-blue-500"
            />

            <div className="hidden lg:block">

              <h3 className="text-sm font-semibold text-white">
                Mukund Kumar
              </h3>

              <p className="text-xs text-zinc-500">
                Administrator
              </p>

            </div>

          </div>

        </div>

      </div>

    </header>
  );
}