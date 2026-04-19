"use client";

export const dynamic = "force-dynamic";

import { ProtectedRoute } from "../../../../../components/ProtectedRoute";
import { EventSettingsPage } from "../../../../../views/EventSettingsPage";

export default function EventSettingsRoutePage() {
  return (
    <ProtectedRoute>
      <EventSettingsPage />
    </ProtectedRoute>
  );
}
