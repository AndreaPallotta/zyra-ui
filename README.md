# zyra-ui

Component-driven, reactive UI library and declarative **ZYX** markup preprocessor for the [Zyra Programming Language](https://github.com/AndreaPallotta/zyra).

Inspired by the component and reactivity mental models of Vue and React.

## Features

- **Declarative ZYX Syntax**: Write HTML/XML-like markup directly in `.zyx` files with `{expression}` interpolation.
- **Virtual DOM Primitives**: Lightweight `VNode` representation of elements and attributes.
- **Component Constructors**: Ergonomic element helper functions (`h`, `div`, `h1`, `p`, `button`, `input`).
- **Clean HTML String Rendering**: Server-side rendering (SSR) and static markup generation with `render_html` and `render_page`.
- **Standalone Package**: Zero compiler modifications required. Ships with its own `zyx` build tool.

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

## Declarative ZYX Example (`src/App.zyx`)

```zyra
import "github.com/AndreaPallotta/zyra-ui"

def user_card(username: String, role: String): String {
  return (
    <div class="card">
      <h1 class="title">Welcome, {username}!</h1>
      <p class="role">Role: {role}</p>
      <button class="btn-primary">Access Dashboard</button>
    </div>
  )
}

def main(): Int {
  const card_html = user_card("Andrea".to_string(), "Architect".to_string())
  const page = render_page("Dashboard", card_html)
  print(page)
  return 0
}
```

Compile and run `.zyx` directly:

```bash
python .zyra_modules/github.com/AndreaPallotta/zyra-ui/latest/bin/zyx.py run src/App.zyx
```

## Running Examples

```bash
# Run declarative ZYX example
zyra run example:zyx

# Run reactive counter example
zyra run example:counter

# Run task tracker example
zyra run example:todo
```

## Testing

Run the test suite using Zyra's built-in test runner:

```bash
zyra run test
# or directly:
zyra test tests/test_ui_suite.zy
```

## License

MIT License. Copyright (c) 2026 Andrea Pallotta.