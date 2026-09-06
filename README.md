# zyra-ui

Component-driven, reactive UI and Virtual DOM library for the [Zyra Programming Language](https://github.com/AndreaPallotta/zyra).

Inspired by the component and reactivity mental models of Vue and React.

## Features

- **Virtual DOM Primitives**: Lightweight `VNode` representation of elements and attributes.
- **Component Constructors**: Ergonomic element helper functions (`h`, `div`, `h1`, `p`, `button`, `input`).
- **Clean HTML String Rendering**: Server-side rendering (SSR) and static markup generation with `render_html` and `render_page`.
- **Standalone Package**: Zero external dependencies, designed as a standard Zyra 3rd-party library.

## Installation

Add `zyra-ui` to your project using the Zyra package manager:

```bash
zyra add github.com/AndreaPallotta/zyra-ui
```

Or declare it in your `zyra.json`:

```json
{
  "dependencies": {
    "github.com/AndreaPallotta/zyra-ui": "0.1.0"
  }
}
```

## Quick Start

```zyra
import "github.com/AndreaPallotta/zyra-ui"

def main(): Int {
  const card = div("card", "Welcome to Zyra UI")
  const page = render_page("My Dashboard", render_html(card))
  print(page)
  return 0
}
```

## Running Examples

The repository includes ready-to-run examples in the `examples/` directory:

```bash
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