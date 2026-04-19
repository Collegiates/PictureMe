"use client";

export const dynamic = "force-dynamic";

import { Suspense } from "react";
import { ProtectedRoute } from "../../../../components/ProtectedRoute";
import { Spinner } from "../../../../components/Spinner";
import { AccountSettingsPage } from "../../../../views/AccountSettingsPage";

export default function AccountSettingsRoutePage() {
  return (
    <Suspense
      fallback={
        <div className="page-shell flex min-h-[60vh] items-center justify-center">
          <Spinner label="Loading..." />
        </div>
      }
    >
      <ProtectedRoute>
        <AccountSettingsPage />
      </ProtectedRoute>
    </Suspense>
  );
}
