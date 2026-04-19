"use client";

export const dynamic = "force-dynamic";

import { ProtectedRoute } from "../../../../components/ProtectedRoute";
import { EventGalleryPage } from "../../../../views/EventGalleryPage";

export default function EventGalleryRoutePage() {
  return (
    <ProtectedRoute>
      <EventGalleryPage />
    </ProtectedRoute>
  );
}
