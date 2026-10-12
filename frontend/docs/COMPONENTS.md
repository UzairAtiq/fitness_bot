# Component Architecture

Overview of how React components connect, manage state, and pass data down the component hierarchy.

---

## Component Hierarchy

```text
App
├── Header
│   └── ChatStatusIndicator
├── Sidebar
└── Chatbox
    ├── Carousel (Suggested Questions)
    ├── ChatMessage (User & Assistant bubbles)
    │   └── Typewriter (via useTypewriter)
    └── ChatInput
```

---

## Component Roles & Data Flow

- **`App`**:
  - Root container holding top-level state: current sessions, active session ID, input loading states, and access key modal state.
  - Passes session actions to `Sidebar` and active message list to `Chatbox`.
- **`Header`**:
  - Displays application branding.
  - Mounts `ChatStatusIndicator` displaying active backend status badge (idle, retrieving, reranking, answering).
  - Triggers opening of the `AccessModal` to configure shared passwords.
- **`Sidebar`**:
  - Renders list of previous conversations stored in local state.
  - Allows switching active sessions, creating new sessions, and deleting old ones.
- **`Chatbox`**:
  - Contains the scrollable message stream.
  - Renders suggestion prompts via `Carousel` when the active conversation is empty.
  - Renders list of `ChatMessage` components and mounts `ChatInput` at the bottom.
- **`ChatMessage`**:
  - Formats user prompts and assistant answers.
  - Renders assistant responses using `useTypewriter` hook for streaming text effect.
  - Provides a copy button to copy markdown text to the clipboard.
- **`ChatInput`**:
  - Captures text input from the user.
  - Dispatches queries to `App` on Enter or submit button click.
