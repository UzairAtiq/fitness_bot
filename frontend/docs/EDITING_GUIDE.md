# Frontend Editing Guide

Quick guide on which files to modify for common development tasks in the frontend.

---

## 1. Changing UI Text & Copy
- **Header & Title**: Edit `src/components/Header.tsx`.
- **Suggested Questions / Welcome Screen**: Edit `src/components/Chatbox.tsx`.
- **Access Lock Screen Text**: Edit `src/components/AccessModal.tsx`.
- **Message Disclaimers / Placeholders**: Edit `src/components/ChatInput.tsx`.

---

## 2. Changing Styles, Fonts, or Themes
- **Global Styles & CSS Variables**: Edit `src/index.css`.
- **Theme Colors & Font Definitions**: Edit `tailwind.config.js`.
- **Component-Specific Styling**: Edit Tailwind utility classes directly in the component file (e.g., `src/components/ChatMessage.tsx`).

---

## 3. Changing API Endpoints or Backend URL
- **Backend Host URL**: Change `VITE_BACKEND_URL` in `frontend/.env` (default is `http://localhost:8000`).
- **Endpoint Calls (`/ask`, `/verify-key`, `/health`)**: Edit `src/services/api.ts`.
- **Header / Auth Token Handling**: Edit `send_ask_query` and `verify_access_key` in `src/services/api.ts`.

---

## 4. Adding a New Component
- **UI Primitives (buttons, inputs, cards)**: Add to `src/components/ui/` and export.
- **Feature Components**: Add to `src/components/` and import into `src/App.tsx` or parent component.

---

## 5. Adding New TypeScript Types
- **Chat, Messages, or Session Models**: Add interfaces to `src/types/chat.ts`.
- **Component Prop Types**: Define directly within the component file or export from `src/types/`.
