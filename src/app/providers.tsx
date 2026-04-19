"use client";

import type { PropsWithChildren } from "react";
import { AuthProvider } from "../providers/AuthProvider";

export function Providers({ children }: PropsWithChildren) {
  return <AuthProvider>{children}</AuthProvider>;
}
