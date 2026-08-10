"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

import {
  LayoutDashboard,
  Upload,
  History,
  BrainCircuit,
  ShieldCheck,
} from "lucide-react";

const menus = [
  {
    title: "Dashboard",
    href: "/dashboard",
    icon: LayoutDashboard,
  },
  {
    title: "Upload",
    href: "/upload",
    icon: Upload,
  },
  {
    title: "History",
    href: "/history",
    icon: History,
  },
  {
    title: "Models",
    href: "/models",
    icon: BrainCircuit,
  },
];

export default function Sidebar() {

  const pathname = usePathname();

  return (

    <aside className="flex h-screen w-[270px] flex-shrink-0 flex-col border-r border-white/10 bg-[#060818]">

      {/* Logo */}

      <div className="border-b border-white/10 px-8 py-8">

        <div className="flex items-center gap-4">

          <div className="flex h-16 w-16 items-center justify-center rounded-3xl bg-gradient-to-br from-violet-600 to-blue-600 shadow-[0_0_35px_rgba(124,58,237,.35)]">

            <ShieldCheck
              size={34}
              className="text-white"
            />

          </div>

          <div>

            <h1 className="text-xl font-bold leading-tight text-white">
              AI Authenticity
            </h1>

            <p className="text-sm text-zinc-400">
              Detection Platform
            </p>

          </div>

        </div>

      </div>

      {/* Navigation */}

      <div className="flex-1 overflow-y-auto px-5 py-7">

        <nav className="space-y-2">

          {menus.map((item) => {

            const Icon = item.icon;

            const active =
              pathname === item.href;

            return (

              <Link
                key={item.href}
                href={item.href}
                className={`group flex items-center gap-4 rounded-2xl px-5 py-4 text-[16px] font-medium transition-all duration-300 ${
                  active
                    ? "bg-gradient-to-r from-violet-600 to-blue-600 text-white shadow-lg"
                    : "text-zinc-400 hover:bg-zinc-900 hover:text-white"
                }`}
              >

                <Icon
                  size={22}
                  className="transition-transform group-hover:scale-110"
                />

                {item.title}

              </Link>

            );

          })}

        </nav>

      </div>

      {/* Bottom Status */}

      <div className="border-t border-white/10 p-5">

        <div className="rounded-2xl border border-emerald-500/20 bg-zinc-900 p-5">

          <div className="mb-2 flex items-center gap-2">

            <div className="h-3 w-3 rounded-full bg-emerald-500 animate-pulse" />

            <span className="font-semibold text-emerald-400">
              System Operational
            </span>

          </div>

          <p className="text-sm text-zinc-400">
            All AI detection services are running normally.
          </p>

        </div>

      </div>

    </aside>

  );

}