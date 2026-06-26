"use client";

import Link from "next/link";

import {
  Shield,
  LayoutDashboard,
  Upload,
  History,
  FileText,
  User,
  Settings
} from "lucide-react";

const menu = [
  {
    title: "Dashboard",
    icon: LayoutDashboard,
    href: "/",
  },
  {
    title: "Upload",
    icon: Upload,
    href: "/upload",
  },
  {
    title: "Detection History",
    icon: History,
    href: "/history",
  },
  {
    title: "Reports",
    icon: FileText,
    href: "/reports",
  },
  {
    title: "Profile",
    icon: User,
    href: "/profile",
  },
  {
    title: "Settings",
    icon: Settings,
    href: "/settings",
  },
];

export default function Sidebar() {
  return (
    <aside className="flex h-screen w-72 flex-col border-r border-white/10 bg-zinc-950">
      <div className="flex items-center gap-3 border-b border-white/10 px-6 py-6">
        <div className="rounded-xl bg-blue-600 p-3">
          <Shield className="h-6 w-6 text-white" />
        </div>

        <div>
          <h1 className="text-lg font-bold text-white">
            Fake Detection
          </h1>

          <p className="text-xs text-zinc-400">
            Multi-Modal AI
          </p>
        </div>
      </div>

      <nav className="mt-6 flex flex-1 flex-col gap-2 px-3">
        {menu.map((item) => {
          const Icon = item.icon;

          return (
            <Link
              key={item.title}
              href={item.href}
              className="flex items-center gap-3 rounded-xl px-4 py-3 text-zinc-300 transition-all duration-200 hover:bg-blue-600 hover:text-white"
            >
              <Icon size={20} />

              <span>{item.title}</span>
            </Link>
          );
        })}
      </nav>
    </aside>
  );
}