"use client";

export const dynamic = "force-dynamic";

import { Suspense } from "react";
import { PublicOnlyRoute } from "../../../components/PublicOnlyRoute";
import { Spinner } from "../../../components/Spinner";
import { LoginPage } from "../../../views/LoginPage";

export default function LoginRoutePage() {
  return (
    <Suspense
      fallback={
        <div className="page-shell flex min-h-[60vh] items-center justify-center">
          <Spinner label="Loading..." />
        </div>
      }
    >
      <PublicOnlyRoute>
        <LoginPage />
      </PublicOnlyRoute>
    </Suspense>
  );
}
