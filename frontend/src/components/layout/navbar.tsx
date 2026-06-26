"use client";

import {
  Bell,
  Search,
  UserCircle,
} from "lucide-react";

export default function Navbar() {
  return (
    <header className="flex h-20 items-center justify-between border-b border-white/10 bg-zinc-950 px-8">
      <div>
        <h2 className="text-2xl font-bold text-white">
          Dashboard
        </h2>

        <p className="text-sm text-zinc-400">
          Welcome to the AI Fake Detection Platform
        </p>
      </div>

      <div className="flex items-center gap-4">
        <div className="flex items-center gap-2 rounded-xl border border-white/10 bg-zinc-900 px-4 py-2">
          <Search
            size={18}
            className="text-zinc-500"
          />

          <input
            type="text"
            placeholder="Search..."
            className="bg-transparent text-white outline-none placeholder:text-zinc-500"
          />
        </div>

        <button className="rounded-xl bg-zinc-900 p-3 transition hover:bg-zinc-800">
          <Bell className="text-white" />
        </button>

        <button className="rounded-full bg-blue-600 p-2 transition hover:bg-blue-500">
          <UserCircle
            size={32}
            className="text-white"
          />
        </button>
      </div>
    </header>
  );
}