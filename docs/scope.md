# PictureMe Scope

## End Goal

Build a product that allows users to register their face to their account once, join events through QR check-in or organizer assignment, and automatically receive access to the professional photos they appear in whenever authorized photographers upload event images.

## Core Moving Parts

### Photo Ingestion

- Authorized photographers upload event photo sets to a specific event.
- The system stores and organizes event images for later processing and delivery.

### User Registration And Face Enrollment

- Users create accounts in the platform.
- Each user scans their face during sign-up so it can be attached to their account.
- Registered face data becomes the reference identity for future event photo matching.

### Face Detection And Matching

- Faces are detected from uploaded photos.
- The system compares registered user face data against indexed event photo face data.

### Event Enrollment

- Each event exposes a QR code.
- Scanning the QR code registers the user as an attendee for that event.
- Organizers can also manually add users to an event attendee list.

### Personalized Galleries And Notifications

- Matching photos are assembled into a personal user gallery for that event.
- Users can also browse the full event gallery when permitted.
- Users receive SMS notifications when photos are uploaded to events they attended.

### Event History

- Users can review all current and previous events they attended.
- Each event acts as an entry point to personal photos and the broader event gallery.

## In-Scope Integrations

- `AWS Rekognition` for face detection and matching
- `Cloudinary` for photo storage and delivery
- `Twilio SMS` for upload notifications and gallery link delivery
- `Supabase` for database storage and `pgvector` similarity search
- `qrcode.react` for QR code generation in the frontend

## Scope Guardrails

- Prioritize a working end-to-end account registration, event enrollment, matching, and gallery flow over advanced admin features.
- Prioritize reliable matching and delivery over social or editing features.
- Keep photographer tools focused on authorized upload workflows, not full studio management.

## Success Criteria

- A user can create an account and register their face.
- A user can be attached to an event by QR scan or organizer assignment.
- An authorized photographer can upload event photos.
- The system can identify likely matching photos for each registered user.
- A user can view their personal event photos and the full event gallery.
- A user receives text notifications when new event photos are uploaded.
- A user can see a history of previous events.
