"use client";

export const dynamic = "force-dynamic";

import { Suspense } from "react";
import { ProtectedRoute } from "../../../components/ProtectedRoute";
import { Spinner } from "../../../components/Spinner";
import { DashboardPage } from "../../../views/DashboardPage";

export default function DashboardRoutePage() {
  return (
    <Suspense
      fallback={
        <div className="page-shell flex min-h-[60vh] items-center justify-center">
          <Spinner label="Loading..." />
        </div>
      }
    >
      <ProtectedRoute>
        <DashboardPage />
      </ProtectedRoute>
    </Suspense>
  );
}
