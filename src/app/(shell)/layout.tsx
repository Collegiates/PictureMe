"use client";

import type { PropsWithChildren } from "react";
import { Navbar } from "../../components/Navbar";

export default function ShellLayout({ children }: PropsWithChildren) {
  return (
    <div className="min-h-screen bg-soft-radial">
      <Navbar />
      <main>{children}</main>
      <footer className="mx-auto max-w-6xl px-4 pb-8 text-center text-xs uppercase tracking-[0.24em] text-slate/70 sm:px-6">
        PictureMe keeps every event gallery one tap away.
      </footer>
    </div>
  );
}
