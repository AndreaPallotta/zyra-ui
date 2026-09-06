# zyra-ui

Component-driven, reactive UI library and declarative **ZYX** markup for the [Zyra Programming Language](https://github.com/AndreaPallotta/zyra).

Inspired by the component and reactivity mental models of modern web frameworks, implemented natively in pure Zyra with zero runtime dependencies.

## Features

- **Declarative ZYX Syntax**: Write HTML/XML-like markup directly in `.zyx` files with `{expression}` interpolation and attribute binding.
- **Built-in Design System**: Six built-in themes (`dark`, `light`, `nord`, `dracula`, `emerald`, `cyberpunk`) and custom CSS injection.
- **Rich Component Suite**:
  - **Layout**: `Navbar`, `Sidebar`, `Container`, `Grid`, `Card`, `SectionHeader`, `Divider`
  - **Data Display**: `StatCard`, `DataTable`, `Badge`, `Avatar`, `ProgressBar`
  - **Feedback & Overlays**: `Alert`, `Modal`
  - **Form Controls**: `Button`, `FormField`, `SelectField`, `TextareaField`, `CheckboxField`
- **Utility CSS Classes**: Flexbox, CSS Grid, spacing, typography scales, shadows, and borders generated directly into page stylesheets.
- **High-Performance SSR**: Fast server-side and static HTML rendering with `render_themed_page` and `render_dashboard`.
- **Native Compiler Integration**: First-class compilation support in `zyra build` and `zyra run`.

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

## Quickstart: Dashboard Example (`examples/dashboard.zyx`)

```zyra
import "github.com/AndreaPallotta/zyra-ui"

def DashboardView(): String {
  const alert = Alert(
    "All Systems Operational".to_string(),
    "Global edge clusters running nominal across all 14 regions.".to_string(),
    "success".to_string()
  )

  const s1 = StatCard("Active Services".to_string(), "48".to_string(), "4 new".to_string(), true)
  const s2 = StatCard("Total Requests".to_string(), "14.2M".to_string(), "12.5%".to_string(), true)
  const s3 = StatCard("P99 Latency".to_string(), "18ms".to_string(), "3ms slower".to_string(), false)
  const stats = Grid(3, s1 + &s2 + &s3)

  const headers = "Service Name, Cluster, Traffic, Uptime, Status"
  const rows = "auth-gateway, us-east-1, 4.2k req/s, 99.99%, Active; billing-api, us-east-1, 1.1k req/s, 99.95%, Active"
  const table = DataTable(headers.to_string(), rows.to_string())

  const content = alert + &stats + "<div class=\"mb-6\"></div>" + &table
  return render_dashboard(
    "ZyraOps Cloud Dashboard".to_string(),
    "ZyraOps".to_string(),
    "Overview, Metrics, Deployments, Settings".to_string(),
    "Overview".to_string(),
    content,
    theme_nord()
  )
}

def main(): Int {
  const html = DashboardView()
  print(html)
  return 0
}
```

## Running Examples

```bash
# Run SaaS analytics dashboard demo
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

## Built-In Themes

```zyra
const dark_theme = theme_dark()
const light_theme = theme_light()
const nord_theme = theme_nord()
const dracula_theme = theme_dracula()
const emerald_theme = theme_emerald()
const cyberpunk_theme = theme_cyberpunk()
```

Each theme provides CSS variables for `--zy-bg`, `--zy-surface`, `--zy-surface-hover`, `--zy-text`, `--zy-text-muted`, `--zy-primary`, `--zy-primary-hover`, `--zy-border`, `--zy-accent`, `--zy-danger`, `--zy-success`, `--zy-warning`, and `--zy-font`.

## Testing

Run the test suite using Zyra's built-in test runner:

```bash
zyra test tests/test_ui_suite.zy
```

## License

MIT License. Copyright (c) 2026 Andrea Pallotta.