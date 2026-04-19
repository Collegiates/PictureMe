import type { Metadata } from "next";
import { Providers } from "./providers";
import "../styles/index.css";

export const metadata: Metadata = {
  title: "PictureMe",
  description: "Event photo matching for organizers and attendees.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>
        <Providers>{children}</Providers>
      </body>
    </html>
  );
}
