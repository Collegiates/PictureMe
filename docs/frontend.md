# Frontend

## Purpose

The frontend now lives in the root Next.js application instead of a separate Vite app. It owns the browser experience, Supabase browser authentication, and the temporary direct-to-Supabase data adapter for supported authenticated screens while the backend continues to expand.

## Key Structure

- [src/app](/Users/tervin23/Documents/AG/PictureMe/src/app): Next.js App Router entrypoint and file-based routes.
- [src/app/(shell)](/Users/tervin23/Documents/AG/PictureMe/src/app/%28shell%29): Shared app-shell layout for login, signup, dashboard, join, gallery, and settings flows.
- [src/views](/Users/tervin23/Documents/AG/PictureMe/src/views): Preserved route-level UI modules migrated from Vite and wrapped by Next route files.
- [src/components](/Users/tervin23/Documents/AG/PictureMe/src/components): Reusable UI building blocks such as navigation, upload modal, photo grids, and route guards.
- [src/providers/AuthProvider.tsx](/Users/tervin23/Documents/AG/PictureMe/src/providers/AuthProvider.tsx): Tracks the current session and hydrates the signed-in user from `public.users`.
- [src/lib/supabase.ts](/Users/tervin23/Documents/AG/PictureMe/src/lib/supabase.ts): Initializes the Supabase browser client from Next public environment variables.
- [src/lib/api.ts](/Users/tervin23/Documents/AG/PictureMe/src/lib/api.ts): Central request layer. It uses demo responses when demo mode is active, uses the backend when `NEXT_PUBLIC_API_BASE_URL` is configured, and otherwise routes supported authenticated requests directly into Supabase.
- [src/lib/react-router-dom.tsx](/Users/tervin23/Documents/AG/PictureMe/src/lib/react-router-dom.tsx): Small compatibility shim that lets the migrated client pages keep their routing API while Next.js owns the real file-based routes.

## Routing Logic

- Next.js file-based routes now mirror the documented product URLs:
  - `/`
  - `/login`
  - `/signup`
  - `/dashboard`
  - `/join/[token]`
  - `/gallery/[token]`
  - `/event/[id]`
  - `/event/[id]/settings`
  - `/account/settings`
- The root route stays outside the app shell so the landing page can remain distinct.
- Shared navigation and footer live in `src/app/(shell)/layout.tsx`.
- Protected and public-only behavior is still handled on the client through the existing guard components, which keeps the migration smaller while leaving room for later server-aware auth hardening.

## Current Supabase Boundary

- Browser auth still runs through Supabase Auth.
- Email/password and Google OAuth entry points are retained.
- Authenticated reads and simple writes can still fall back to Supabase directly where backend coverage is incomplete.
- Media uploads, public gallery token resolution, invite preview for unauthenticated users, and face-indexing workflows remain backend responsibilities.
