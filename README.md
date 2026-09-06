# zyra-ui

Component-driven, reactive UI library and declarative **ZYX** markup for the [Zyra Programming Language](https://github.com/AndreaPallotta/zyra).

Inspired by the component and reactivity mental models of modern web frameworks, implemented natively in pure Zyra with zero runtime dependencies.

## Features

- **Declarative ZYX Syntax**: Write HTML/XML-like markup directly in `.zyx` files with `{expression}` interpolation and attribute binding.
- **Built-in Design System**: Six built-in themes (`dark`, `light`, `nord`, `dracula`, `emerald`, `cyberpunk`), custom CSS injection, and responsive utility classes.
- **Comprehensive Component Suite (50+ Primitives)**:
  - **Layout & Structure**: `Navbar`, `Sidebar`, `Breadcrumb`, `Tabs`, `TabPanel`, `Container`, `Grid`, `Card`, `SectionHeader`, `Divider`, `HStack`, `VStack`, `AspectRatio`, `Splitter`, `Sticky`, `Masonry`.
  - **Pure-SVG Data Visualization**: `BarChart`, `DonutChart`, `AreaChart`, `ProgressRing`, `Sparkline`.
  - **Data Display & Typography**: `StatCard`, `KpiComparison`, `DataTable`, `Badge`, `Avatar`, `AvatarGroup`, `ProgressBar`, `Timeline`, `TreeView`, `Rating`, `DiffViewer`, `Kbd`, `Carousel`.
  - **Form & Input Controls**: `Button`, `FormField`, `SelectField`, `TextareaField`, `CheckboxField`, `Switch`, `RadioGroup`, `Slider`, `SearchInput`, `NumberInput`, `PinInput`, `TagInput`, `DropZone`, `DatePicker`, `TimePicker`, `ColorPicker`, `Pagination`.
  - **Navigation Systems**: `Stepper`, `CommandPalette`, `ContextMenu`, `TocNav`, `BottomNav`.
  - **Overlays & Feedback**: `Modal`, `Drawer`, `Popover`, `ConfirmDialog`, `Banner`, `HoverCard`, `NotificationCenter`, `Lightbox`, `Accordion`, `Toast`, `Alert`, `Tooltip`, `Dropdown`, `EmptyState`.
  - **Loading States & DevTools**: `Skeleton`, `CodeBlock`.
  - **Production Page Templates**: `render_landing_page`, `render_auth_page`, `render_settings_page`, `render_docs_page`, `render_error_page`, `render_dashboard`, `render_themed_page`, `render_page`.
  - **Utilities & Metadata**: `ThemeToggle`, `meta_tags`.
- **Client Interactivity Micro-Runtime**: Zero-dependency vanilla runtime injected into `render_themed_page` (<3KB) that handles tabs, accordions, modals, drawers, toasts, popovers, command palettes, theme switching, and keyboard shortcuts (`Escape`, `Ctrl+K`).
- **High-Performance SSR**: Sub-millisecond server-side and static HTML rendering compiling to native machine code.

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
# Run 100% complete component suite gallery
zyra run example:complete

# Run SaaS landing page demo
zyra run example:landing

# Run authentication portal demo
zyra run example:auth

# Run interactive micro-runtime demo
zyra run example:interactive

# Run cloud analytics dashboard demo
zyra run example:dashboard

# Run component gallery showcase
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
- `data-popover-toggle`: Toggles floating popover card visibility.
- `data-cmd-open="palette-id"`: Opens the targeted command palette modal and focuses input.
- `data-cmd-close`: Closes the enclosing command palette.
- `data-theme-toggle`: Toggles document body theme attribute between dark and light.
- Keyboard shortcuts: `Escape` closes all active overlays, and `Ctrl+K` / `Cmd+K` launches command palette.

## Pure SVG Data Visualization Suite

Render vector charts without any third-party JavaScript or NPM packages:

```zyra
// Inline SVG bar chart
const bar = BarChart("Jan,Feb,Mar,Apr,May,Jun", "30,55,40,75,90,110", 160, "primary")

// Segmented SVG donut chart with center sum
const donut = DonutChart("Compute,Memory,Storage", "50,30,20", 140)

// Filled gradient area chart
const area = AreaChart("0,100 80,60 160,80 240,30 320,10", "accent", 120)

// Radial circular progress ring
const ring = ProgressRing(78, 80, 8, "success")

// Metric sparkline trend
const spark = Sparkline("0,20 15,16 30,22 45,10 60,14", "primary", 24)
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

Run the full unit test suite:

```bash
zyra test tests/test_ui_suite.zy
```

## License

MIT License. Copyright (c) 2026 Andrea Pallotta.