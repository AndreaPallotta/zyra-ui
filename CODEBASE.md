# Codebase Map
Generated: 2026-09-05 22:11:00
Commit: uncommitted / local

This file is a compact index of the codebase for AI agents to understand project structure without full recursive file scans.

## File Index

- `src/lib.zy`: Core Virtual DOM types (`VNode`, `StateEntry`), element constructors (`h`, `div`, `h1`, `p`, `button`, `input`), and HTML renderers (`render_html`, `render_page`).
- `examples/counter.zy`: Interactive counter component demo showcasing card layout, buttons, and state rendering.
- `examples/todo.zy`: Task list component demo demonstrating structured items and action triggers.
- `tests/test_ui_suite.zy`: Unit test suite verifying VNode creation, HTML rendering, input element attributes, and page scaffolding.
- `zyra.json`: Package manifest defining scripts (`test`, `example:counter`, `example:todo`) and library metadata.
- `README.md`: Library overview, installation instructions, quickstart guide, and examples.

## Key Symbol & Interface Index

- `struct VNode { tag: String, classes: String, attrs: String, text: String, children_count: Int }`: Virtual DOM element representation.
- `struct StateEntry { key: String, value: String }`: Reactive key-value state entry.
- `def h(tag: String, classes: String, text: String): VNode`: Generic virtual element constructor.
- `def div(classes: String, text: String): VNode`: `<div>` element constructor.
- `def h1(classes: String, text: String): VNode`: `<h1>` element constructor.
- `def p(classes: String, text: String): VNode`: `<p>` element constructor.
- `def button(classes: String, label: String): VNode`: `<button>` element constructor.
- `def input(placeholder: String, value: String): VNode`: `<input>` element constructor with preconfigured attributes.
- `def render_html(node: VNode): String`: Lowers a `VNode` into an HTML element string.
- `def render_page(title: String, body_html: String): String`: Wraps rendered components into a complete HTML5 document scaffolding.