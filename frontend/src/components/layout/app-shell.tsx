"use client";

import { ReactNode } from "react";

import Sidebar from "./sidebar";
import Navbar from "./navbar";

interface AppShellProps {
  children: ReactNode;
}

export default function AppShell({
  children,
}: AppShellProps) {
  return (
    <div className="flex h-screen overflow-hidden bg-[#050816]">

      {/* Sidebar */}

      <Sidebar />

      {/* Main */}

      <div className="flex min-w-0 flex-1 flex-col">

        <Navbar />

        <main className="flex-1 overflow-y-auto bg-[#050816]">

          <div className="mx-auto w-full max-w-[1700px] px-8 py-8">

            {children}

          </div>

        </main>

      </div>

    </div>
  );
}