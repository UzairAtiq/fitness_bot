# Frontend Documentation

Index and file reference for the React/TypeScript frontend client.

---

## Documentation Guides

- **[Editing Guide](EDITING_GUIDE.md)**: Quick guide on where to make common UI, styling, and API modifications.
- **[Component Architecture](COMPONENTS.md)**: Diagram and explanation of component hierarchy and data flow.

---

## Configuration Files

- `package.json`: Declares npm dependencies and build scripts (`dev`, `build`, `lint`).
- `package-lock.json`: Pinned tree of installed node modules and exact versions.
- `vite.config.ts`: Configures Vite build server, plugins, and `@/` path alias.
- `tailwind.config.js`: Defines theme colors, custom font families, and animation tokens.
- `postcss.config.js`: PostCSS configuration with Tailwind CSS and Autoprefixer.
- `tsconfig.json`: Root TypeScript configuration referencing app and node tsconfigs.
- `tsconfig.app.json`: TypeScript compiler options and path mappings for application code.
- `tsconfig.node.json`: TypeScript compiler options for Vite tooling scripts.
- `index.html`: Entry HTML page mounting the root React application.
- `.env.example`: Template for frontend environment variables (`VITE_BACKEND_URL`).
- `.oxlintrc.json`: Linting rules configuration for Oxlint.

---

## Source Files (`src/`)

- `main.tsx`: Application entry point mounting `App` into the DOM.
- `App.tsx`: Top-level component managing active sessions, message lists, and modal visibility.
- `index.css`: Global styles, font definitions, and Tailwind CSS directives.
- `components/AccessModal.tsx`: Modal dialog for validating and storing the user access key.
- `components/Header.tsx`: Navigation bar with branding, live status badge, and key settings trigger.
- `components/Sidebar.tsx`: Session drawer managing history list, session selection, and deletions.
- `components/Chatbox.tsx`: Chat container handling message feed rendering, auto-scrolling, and suggestions.
- `components/ChatMessage.tsx`: Renders individual user and assistant bubbles with markdown formatting.
- `components/ChatInput.tsx`: Textarea input box with keyboard shortcuts and submit actions.
- `components/ChatStatusIndicator.tsx`: Animated pill displaying backend pipeline phases.
- `components/ui/badge.tsx`: Stylized badge UI primitive.
- `components/ui/button.tsx`: Variant-driven button UI primitive.
- `components/ui/card.tsx`: Composable card container primitives.
- `components/ui/carousel.tsx`: Embla Carousel horizontal card slider.
- `components/ui/input.tsx`: Form input UI primitive.
- `components/ui/scroll-area.tsx`: Radix UI custom scroll container.
- `components/ui/skeleton.tsx`: Pulsing loading placeholder primitive.
- `hooks/useTypewriter.ts`: Hook generating smooth typewriter text reveals for assistant answers.
- `lib/utils.ts`: Tailwind class combination helper (`cn`).
- `services/api.ts`: API client communicating with backend endpoints and managing localStorage keys.
- `types/chat.ts`: TypeScript definitions for messages, sessions, statuses, and API models.
