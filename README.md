# zyra-ui

Component-driven, reactive UI library and declarative **ZYX** markup for the [Zyra Programming Language](https://github.com/AndreaPallotta/zyra).

Inspired by the component and reactivity mental models of modern web frameworks, implemented natively in pure Zyra with zero runtime dependencies.

## Features

- **Declarative ZYX Syntax**: Write HTML/XML-like markup directly in `.zyx` files with `{expression}` interpolation and attribute binding.
- **Built-in Design System**: Six built-in themes (`dark`, `light`, `nord`, `dracula`, `emerald`, `cyberpunk`) and custom CSS injection.
- **Comprehensive Component Suite**:
  - **Layout & Navigation**: `Navbar`, `Sidebar`, `Breadcrumb`, `Tabs`, `TabPanel`, `Container`, `Grid`, `Card`, `SectionHeader`, `Divider`
  - **Data Display & Viz**: `Sparkline` (pure inline SVG), `StatCard`, `DataTable`, `Badge`, `Avatar`, `ProgressBar`
  - **Disclosure & Feedback**: `Accordion`, `Toast`, `Alert`, `Tooltip`, `Dropdown`, `EmptyState`
  - **Overlays**: `Modal`, `Drawer` (Slide-over panel)
  - **Form Controls**: `Button`, `FormField`, `SelectField`, `TextareaField`, `CheckboxField`, `Pagination`
  - **Loading States**: `Skeleton` (with shimmer animation in circle, text, or rect variants)
  - **Developer Tools**: `CodeBlock` with language tags and clipboard copy
- **Client Interactivity Micro-Runtime**: Zero-dependency vanilla runtime injected into `render_themed_page` that handles tabs, accordions, modals, drawers, and toasts directly in the browser.
- **Utility CSS Classes**: Flexbox, CSS Grid, glassmorphism (`.glass`), shimmer animations (`.skeleton`), elevation glows (`.glow-primary`), and typography scales.
- **High-Performance SSR**: Fast server-side and static HTML rendering with `render_themed_page` and `render_dashboard`.

## Installation

Add `zyra-ui` to your project using the Zyra package manager:

```bash
zyra add github.com/AndreaPallotta/zyra-ui
```

Or declare it in your `zyra.json`:

```json
{
  "dependencies": {
    "github.com/AndreaPallotta/zyra-ui": "latest"
  }
}
```

## Running Examples

```bash
# Run interactive micro-runtime demo (tabs, drawer, modal, accordions, toast)
zyra run example:interactive

# Run SaaS analytics dashboard demo (with SVG sparklines and breadcrumbs)
zyra run example:dashboard

# Run full component gallery showcase
zyra run example:showcase

# Run declarative ZYX counter demo
zyra run example:zyx

# Run reactive counter demo
zyra run example:counter

# Run task tracker demo
zyra run example:todo
```

## Interactive Micro-Runtime Data Attributes

Pages rendered via `render_themed_page` automatically include client interactivity through data attributes:

- `data-tab-target="tab-id"`: Switches active tab and displays the corresponding `TabPanel`.
- `data-accordion-toggle`: Expands or collapses the accordion section.
- `data-modal-open="modal-id"`: Opens the target modal dialog.
- `data-modal-close`: Closes the enclosing modal backdrop.
- `data-drawer-open="drawer-id"`: Slides open the target off-canvas drawer.
- `data-drawer-close`: Closes the enclosing drawer panel.
- `data-toast-close`: Dismisses and removes the toast banner.

## Pure SVG Sparklines

Render crisp inline metric trendlines without any charting dependencies:

```zyra
const trend = Sparkline("0,20 15,16 30,22 45,10 60,14 75,8 90,18 105,6 120,4", "success", 28)
```

## Built-In Themes

```zyra
const dark_theme = theme_dark()
const light_theme = theme_light()
const nord_theme = theme_nord()
const dracula_theme = theme_dracula()
const emerald_theme = theme_emerald()
const cyberpunk_theme = theme_cyberpunk()
```

## Testing

Run the test suite using Zyra's built-in test runner:

```bash
zyra test tests/test_ui_suite.zy
```

## License

MIT License. Copyright (c) 2026 Andrea Pallotta.