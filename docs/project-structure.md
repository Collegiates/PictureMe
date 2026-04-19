# Project Structure

## Repository Purpose

This repository contains the code and documentation for PictureMe, an event photo matching platform built around account-based face registration, event creation, event-specific roles, gallery uploads, personalized galleries, and event history.

## Major Folders

### [src](/Users/tervin23/Documents/AG/PictureMe/src)

Purpose:

- Hosts the Next.js web application.
- Contains the file-based route tree under `src/app`, shared UI components, providers, data helpers, and migrated page-level modules.
- Owns the browser-side Supabase connection used for auth and temporary direct data access before the backend is fully complete.

Current state:

- Active Next.js App Router frontend with migrated React UI modules and preserved product routes.

Documentation:

- [Frontend Notes](/Users/tervin23/Documents/AG/PictureMe/docs/frontend.md)

### [backend](/Users/tervin23/Documents/AG/PictureMe/backend)

Purpose:

- Hosts the Python + FastAPI backend service.
- Owns API routing, Supabase JWT validation, protected runtime configuration boundaries, and the orchestration layer for event, gallery, upload, and matching workflows.
- Coordinates the integrations with Supabase, AWS Rekognition, and Cloudinary as later stages are implemented.

Current state:

- Simplified FastAPI package with one app entrypoint, grouped routers, grouped services, and Vercel-compatible Python function exposure.

Documentation:

- [Backend Notes](/Users/tervin23/Documents/AG/PictureMe/docs/backend.md)

### [api](/Users/tervin23/Documents/AG/PictureMe/api)

Purpose:

- Exposes the FastAPI backend to Vercel Python Functions.
- Keeps the deployment entrypoint separate from the backend implementation modules.

### [docs](/Users/tervin23/Documents/AG/PictureMe/docs)

Purpose:

- Stores project-level documentation.
- Defines the intended scope, architecture direction, and folder responsibilities.

Current files:

- `scope.md`: Defines the product goal, core moving parts, and scope limits.
- `project-structure.md`: Describes the main folders and their responsibilities.
- `backendPlan.md`: Breaks backend implementation into staged delivery milestones tied to the documented product flow.
- `frontend.md`: Documents the current Next.js frontend structure and Supabase integration boundary.
