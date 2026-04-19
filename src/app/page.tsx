"use client";

export const dynamic = "force-dynamic";

import { useEffect } from "react";
import { useRouter } from "next/navigation";
import { Spinner } from "../components/Spinner";
import { useAuth } from "../hooks/useAuth";
import { LandingPage } from "../views/LandingPage";

export default function HomePage() {
  const router = useRouter();
  const { loading, session } = useAuth();

  useEffect(() => {
    if (session) {
      router.replace("/dashboard");
    }
  }, [router, session]);

  if (loading) {
    return (
      <div className="page-shell flex min-h-[60vh] items-center justify-center">
        <Spinner label="Loading PictureMe..." />
      </div>
    );
  }

  if (session) {
    return null;
  }

  return <LandingPage />;
}
