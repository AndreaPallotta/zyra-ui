# Codebase Map
Generated: 2026-09-06 19:15:00
Commit: uncommitted / local

This file is a compact index of the codebase for AI agents to understand project structure without full recursive file scans.

## File Index

- `src/lib.zy`: Core UI library containing Virtual DOM primitives (`VNode`, `StateEntry`), element constructors, Theme tokens and 6 presets, CSS utility stylesheet generator, rich component library (50+ components), form controls, tables, pure-SVG data visualization suite (`BarChart`, `DonutChart`, `AreaChart`, `ProgressRing`, `Sparkline`), navigation systems, overlays, application page templates, utilities (`ThemeToggle`, `meta_tags`), and client-side interactivity micro-runtime.
- `examples/complete_suite.zyx`: Comprehensive catalog showcasing all 50+ components, pure SVG charts, and interactive overlay controls.
- `examples/landing.zyx`: Complete SaaS marketing landing page demonstrating hero, feature grid, and pricing cards via `render_landing_page`.
- `examples/auth.zyx`: Authentication portal demonstration using `render_auth_page`.
- `examples/declarative.zyx`: Minimal declarative ZYX component example.
- `examples/dashboard.zyx`: Complete SaaS operations and cloud telemetry dashboard example featuring breadcrumbs, SVG sparklines, and pagination.
- `examples/showcase.zyx`: Comprehensive component gallery displaying buttons, badges, alerts, stat cards, progress meters, avatars, and form controls.
- `examples/interactive.zyx`: Live interactive application featuring tabs, accordions, modals, slide-over drawers, toasts, code blocks, and SVG sparklines driven by the zero-dependency client micro-runtime.
- `examples/counter.zy`: Interactive counter component demo.
- `examples/todo.zy`: Task list component demo.
- `tests/test_ui_suite.zy`: Comprehensive unit test suite with 22 test suites covering VDOM nodes, HTML rendering, theme tokens, CSS stylesheet generation, form controls, layout primitives, data display, SVG charts, navigation systems, overlays, and page templates.
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
- `def Switch(name: String, label: String, is_checked: Bool, disabled: Bool): String`: Sliding toggle switch.
- `def RadioGroup(name: String, label: String, options_csv: String, selected_val: String): String`: Grouped radio buttons with active state.
- `def Slider(name: String, label: String, min_val: Int, max_val: Int, current_val: Int): String`: Interactive numeric range slider.
- `def SearchInput(name: String, placeholder: String, value: String): String`: Search box with icon.
- `def NumberInput(name: String, label: String, min_val: Int, max_val: Int, val: Int): String`: Increment/decrement stepper control.
- `def PinInput(name: String, length: Int): String`: Segmented 2FA security code verification boxes.
- `def TagInput(name: String, label: String, tags_csv: String, placeholder: String): String`: Tag chip list with dismissal triggers.
- `def DropZone(name: String, title: String, subtitle: String, accept_exts: String): String`: Drag-and-drop file upload zone.
- `def DatePicker(name: String, label: String, val: String): String`: HTML5 date input with calendar trigger.
- `def TimePicker(name: String, label: String, val: String): String`: Time selection input.
- `def ColorPicker(name: String, label: String, hex_val: String): String`: Color picker with hex preview swatch.
- `def HStack(spacing_cls: String, content: String): String`: Horizontal flexbox layout container.
- `def VStack(spacing_cls: String, content: String): String`: Vertical flexbox layout container.
- `def AspectRatio(ratio: String, content: String): String`: Fixed aspect ratio wrapper (16/9, 4/3, 1/1).
- `def Splitter(left_content: String, right_content: String, initial_split_pct: Int): String`: Resizable split-pane layout.
- `def Sticky(content: String, is_bottom: Bool): String`: Viewport-pinned layout container.
- `def Masonry(cols: Int, content: String): String`: Staggered multi-column layout.
- `def Timeline(events_csv: String): String`: Connected event node list with timestamps.
- `def TreeView(nodes_csv: String): String`: Hierarchical folder and file explorer list.
- `def AvatarGroup(names_csv: String, max_display: Int, size: String): String`: Stacked avatar row with overflow count.
- `def Rating(stars: Int, max_stars: Int): String`: Visual star rating meter.
- `def DiffViewer(removed_lines_csv: String, added_lines_csv: String): String`: Unified code diff container.
- `def Kbd(key_label: String): String`: Stylized keyboard shortcut keycap.
- `def KpiComparison(title: String, current_val: String, baseline_val: String, target_val: String, delta_pct: String, is_positive: Bool): String`: Multi-period comparative KPI card.
- `def Carousel(items_html_csv: String): String`: Multi-slide viewport track.
- `def BarChart(labels_csv: String, values_csv: String, height: Int, color: String): String`: Pure-SVG bar chart.
- `def DonutChart(labels_csv: String, values_csv: String, size: Int): String`: Pure-SVG segmented circular donut chart.
- `def AreaChart(points_str: String, color: String, height: Int): String`: Pure-SVG gradient-filled area chart.
- `def ProgressRing(percentage: Int, size: Int, stroke_width: Int, color: String): String`: Pure-SVG radial circular progress indicator.
- `def Sparkline(points_str: String, color: String, height: Int): String`: Pure inline SVG polyline metric trend chart.
- `def Stepper(steps_csv: String, active_step_index: Int): String`: Multi-step progress pipeline.
- `def CommandPalette(modal_id: String, placeholder: String, items_csv: String): String`: Global shortcut and command search launcher.
- `def ContextMenu(menu_id: String, items_csv: String): String`: Contextual floating menu.
- `def TocNav(headers_csv: String): String`: Table of contents scroll-spy navigation.
- `def BottomNav(items_csv: String, active_item: String): String`: Mobile bottom navigation bar.
- `def Popover(trigger_html: String, content_html: String): String`: Anchored popover card.
- `def ConfirmDialog(dialog_id: String, title: String, message: String, confirm_label: String, is_danger: Bool): String`: Action confirmation modal dialog.
- `def Banner(title: String, message: String, action_label: String, variant: String): String`: Persistent announcement strip.
- `def HoverCard(trigger_html: String, preview_html: String): String`: Hover preview card.
- `def NotificationCenter(unread_count: Int, notifications_csv: String): String`: Bell icon with badge and notification feed.
- `def Lightbox(modal_id: String, image_url: String, caption: String): String`: Fullscreen image viewer.
- `def ThemeToggle(): String`: Theme toggle button for switching light and dark modes.
- `def meta_tags(title: String, description: String, og_image: String, url: String): String`: OpenGraph, Twitter card, and SEO metadata tags generator.
- `def render_auth_page(title: String, brand: String, form_type: String, theme: Theme): String`: Authentication page template (login, signup, reset).
- `def render_landing_page(title: String, brand: String, hero_title: String, hero_sub: String, features_html: String, pricing_html: String, theme: Theme): String`: SaaS landing page template.
- `def render_settings_page(title: String, brand: String, active_tab: String, content_html: String, theme: Theme): String`: Account and workspace settings template.
- `def render_docs_page(title: String, brand: String, sidebar_csv: String, active_article: String, article_html: String, toc_csv: String, theme: Theme): String`: 3-column documentation template.
- `def render_error_page(code: Int, title: String, message: String, theme: Theme): String`: Status error page template (404, 500).
- `def render_themed_page(title: String, body_html: String, theme: Theme, custom_css: String): String`: HTML5 page scaffold with injected theme stylesheet, custom CSS, and zero-dependency interactive micro-runtime.
- `def render_dashboard(title: String, brand: String, nav_links_csv: String, active_nav: String, content_html: String, theme: Theme): String`: Ready-to-use application dashboard layout.
- `def render_page(title: String, body_html: String): String`: Default dark themed page renderer.