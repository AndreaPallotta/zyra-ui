# Codebase Map
Generated: 2026-09-06 19:15:00
Commit: uncommitted / local

This file is a compact index of the codebase for AI agents to understand project structure without full recursive file scans.

## File Index

- `src/lib.zy`: Core UI library containing Virtual DOM primitives (`VNode`, `StateEntry`), element constructors, Theme tokens and 6 presets, CSS utility stylesheet generator, rich component library, form controls, tables, data visualization, client-side interactivity micro-runtime, and page renderers (`render_themed_page`, `render_dashboard`).
- `examples/declarative.zyx`: Minimal declarative ZYX component example.
- `examples/dashboard.zyx`: Complete SaaS operations and cloud telemetry dashboard example featuring breadcrumbs, SVG sparklines, and pagination.
- `examples/showcase.zyx`: Comprehensive component gallery displaying buttons, badges, alerts, stat cards, progress meters, avatars, and form controls.
- `examples/interactive.zyx`: Live interactive application featuring tabs, accordions, modals, slide-over drawers, toasts, code blocks, and SVG sparklines driven by the zero-dependency client micro-runtime.
- `examples/counter.zy`: Interactive counter component demo.
- `examples/todo.zy`: Task list component demo.
- `tests/test_ui_suite.zy`: Comprehensive unit test suite covering VDOM nodes, HTML rendering, theme tokens, CSS stylesheet generation, components, form controls, tables, modals, tabs, breadcrumbs, accordions, toasts, pagination, tooltips, dropdowns, skeletons, code blocks, empty states, drawers, sparklines, and the client micro-runtime.
- `zyra.json`: Package manifest defining project metadata and CLI scripts.
- `README.md`: Library overview, design system documentation, component reference, and quickstart guide.

## Key Symbol and Interface Index

- `struct Theme`: Design token container for backgrounds, surfaces, text, primary, borders, accents, semantic states, and typography.
- `def theme_dark(): Theme`: Slate dark theme preset.
- `def theme_light(): Theme`: Clean light theme preset.
- `def theme_nord(): Theme`: Arctic cool Nord theme preset.
- `def theme_dracula(): Theme`: Vibrant Dracula theme preset.
- `def theme_emerald(): Theme`: Deep green Emerald theme preset.
- `def theme_cyberpunk(): Theme`: Neon high-contrast Cyberpunk theme preset.
- `def theme_to_css(t: Theme): String`: Exports theme tokens to native CSS custom properties.
- `def generate_stylesheet(t: Theme, custom_css: String): String`: Generates CSS variable definitions, responsive layout utilities, glassmorphism, animations, and component styling.
- `def Navbar(brand: String, links_csv: String, active_link: String, actions_html: String): String`: Top navigation bar with active link indicator.
- `def Sidebar(brand: String, menu_items_csv: String, active_item: String): String`: Vertical side navigation bar.
- `def Breadcrumb(items_csv: String): String`: Navigation path breadcrumb list with active leaf and separators.
- `def Tabs(tab_labels_csv: String, active_tab: String, panels_html: String): String`: Tabbed container with interactive button switching.
- `def TabPanel(tab_name: String, is_active: Bool, content: String): String`: Individual tab panel container.
- `def Accordion(title: String, content: String, is_open: Bool): String`: Expandable disclosure section with chevron indicator.
- `def Toast(title: String, message: String, variant: String): String`: Dismissible floating toast notification banner.
- `def Pagination(current_page: Int, total_pages: Int): String`: Numbered pagination bar with active page indicator.
- `def Tooltip(text: String, content_html: String): String`: Hoverable floating tooltip wrapper.
- `def Dropdown(button_label: String, items_csv: String): String`: Dropdown button with toggleable item list.
- `def Skeleton(variant: String, width: String, height: String): String`: Shimmering placeholder animation for loading states.
- `def CodeBlock(code: String, language: String): String`: Preformatted syntax code card with language badge and clipboard copy trigger.
- `def EmptyState(title: String, description: String, action_html: String): String`: Centered empty collection placeholder.
- `def Drawer(drawer_id: String, title: String, content: String, is_right: Bool): String`: Slide-over overlay panel from left or right.
- `def Sparkline(points_str: String, color: String, height: Int): String`: Pure inline SVG polyline metric trend chart.
- `def Container(max_width: String, content: String): String`: Centered responsive container layout.
- `def Grid(cols: Int, content: String): String`: Multi-column responsive CSS grid container.
- `def Card(title: String, subtitle: String, body_content: String, footer_content: String): String`: Content container with header, body, and footer.
- `def SectionHeader(title: String, description: String): String`: Heading block with title and subtitle.
- `def Button(label: String, variant: String, size: String, disabled: Bool): String`: Stylized button with variant and disabled states.
- `def Badge(label: String, variant: String): String`: Pill badge for status indicators and counters.
- `def Alert(title: String, message: String, variant: String): String`: Contextual alert banner.
- `def StatCard(title: String, value_str: String, delta_str: String, is_positive: Bool): String`: KPI stat metric card with positive or negative indicator.
- `def ProgressBar(progress: Int, variant: String): String`: Horizontal progress meter with animated fill.
- `def Avatar(name: String, size: String): String`: User avatar icon showing initials.
- `def FormField(name: String, label: String, input_type: String, placeholder: String, value: String, error_msg: String): String`: Form input field with error feedback.
- `def SelectField(name: String, label: String, options_csv: String, selected_val: String): String`: Dropdown select menu with options list.
- `def TextareaField(name: String, label: String, rows: Int, placeholder: String, value: String): String`: Multi-line text input area.
- `def CheckboxField(name: String, label: String, is_checked: Bool): String`: Checkbox input with label.
- `def DataTable(headers_csv: String, rows_csv: String): String`: HTML data table constructed from delimited strings.
- `def Modal(modal_id: String, title: String, content: String, footer: String): String`: Dialog overlay with backdrop, header, content, and footer.
- `def render_themed_page(title: String, body_html: String, theme: Theme, custom_css: String): String`: HTML5 page scaffold with injected theme stylesheet, custom CSS, and zero-dependency interactive micro-runtime.
- `def render_dashboard(title: String, brand: String, nav_links_csv: String, active_nav: String, content_html: String, theme: Theme): String`: Ready-to-use application dashboard layout.