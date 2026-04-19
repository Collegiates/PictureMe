"use client";

export const dynamic = "force-dynamic";

import { Suspense } from "react";
import { PublicOnlyRoute } from "../../../components/PublicOnlyRoute";
import { Spinner } from "../../../components/Spinner";
import { SignupPage } from "../../../views/SignupPage";

export default function SignupRoutePage() {
  return (
    <Suspense
      fallback={
        <div className="page-shell flex min-h-[60vh] items-center justify-center">
          <Spinner label="Loading..." />
        </div>
      }
    >
      <PublicOnlyRoute>
        <SignupPage />
      </PublicOnlyRoute>
    </Suspense>
  );
}
