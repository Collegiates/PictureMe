import { Home, Search } from "lucide-react";
import { NotFoundPage } from "../views/NotFoundPage";

export default function GlobalNotFound() {
  return (
    <NotFoundPage
      icon={<Search className="h-8 w-8" />}
      title="This page is out of frame"
      description="The link you opened does not exist or has moved."
      cta={{ label: "Back home", to: "/", icon: <Home className="h-4 w-4" /> }}
    />
  );
}
