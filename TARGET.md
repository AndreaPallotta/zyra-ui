# Target Implementation Spec

> Blueprint defining the target file tree, public signatures, and invariant contracts for the active task.

---

## 1. Target File Tree Delta
<!-- Mark files as [NEW], [MODIFIED], or [DELETED] with expected line changes -->
- `[MODIFIED]` `src/path/to/file` (~+20 lines)
- `[NEW]`      `src/path/to/new_file` (~+50 lines)

---

## 2. Target Public Signatures & Types
<!-- Define the exact public interface so agents do not drift in naming or types -->
```
// Target types and function signatures here
```

---

## 3. Invariant Acceptance Contract
<!-- Concrete boundary conditions that MUST hold true in the final implementation -->
1. `function(empty_input)` -> returns `Err` or raises `ValueError`.
2. `function(boundary_value)` -> returns expected concrete value.
3. Zero unhandled errors, no silent error swallowing.
