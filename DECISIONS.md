# Architectural Decisions & Agent Context Handoffs

> Shared state and decision records for human developers and AI agents.

---

## 1. Architectural Decisions (ADR)

### ADR-001: 3rd-Party Standalone Package Architecture
- **Date**: 2026-09-05
- **Status**: Accepted
- **Context**: Deciding whether component-driven UI should be built into Zyra core compiler or maintained as an ecosystem library.
- **Decision**: Implemented `zyra-ui` as an external package separate from the core compiler, distributed via Git repository import.
- **Consequences**: Zyra core runtime remains lean; `zyra-ui` can evolve components and Virtual DOM abstractions independently.

### ADR-002: Vue/React Component & Reactivity Model
- **Date**: 2026-09-05
- **Status**: Accepted
- **Context**: Choosing between Elm-style rigid model-update-view vs. component/reactivity mental model.
- **Decision**: Adopted component-centric Virtual DOM trees (`VNode`) and composable helper functions (`h`, `div`, `button`, etc.) aligned with Vue and React mental models.
- **Consequences**: Familiar developer experience for web engineers transitioning to Zyra.

---

## 2. Agent Session Handoffs

### Handoff: 2026-09-05 22:12:00
- **Previous Agent / Session Goal**: Initialize `zyra-ui` repository, construct Virtual DOM primitives, HTML renderer, test suite, and examples.
- **Work Completed**:
  - Initialized repository structure with `src/lib.zy`, `tests/test_ui_suite.zy`, `examples/counter.zy`, `examples/todo.zy`, and `zyra.json`.
  - Configured test runner and verified all 4 test suites pass (`test result: ok. 4 passed; 0 failed; 0 ignored`).
  - Added documentation (`README.md`, `CODEBASE.md`, `DEPS.md`, `TARGET.md`).
- **Current Blockers / In-Progress State**: None. All tests passing cleanly.
- **Next Immediate Action**: Run scan and commit initial release.
- **Key State / Symbols**:
  - `src/lib.zy` -> `VNode`, `h()`, `render_html()`, `render_page()`