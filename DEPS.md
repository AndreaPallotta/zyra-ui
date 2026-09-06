# External & Local Dependency Graph (DEPS.md)

> Maps runtime toolchain environments and cross-repository local package links for AI agents.

---

## 1. Runtime Toolchain & Environment

- **Primary Runtime**: Zyra v2.5.0 Compiler & Runtime
- **Toolchain Executable**: `zyra`
- **Compiler Source**: `../zyra/core/bin/zyra.rs`

---

## 2. Local Cross-Repo Package Links

| Package Name | Local Relative Path | Code Map Path | Purpose |
| :--- | :--- | :--- | :--- |
| `zyra` | `../zyra` | `../zyra/CODEBASE.md` | Core compiler, runtime, standard library, and CLI |

---

## 3. Agent Instructions for Linked Packages
When importing a symbol from any package listed above:
1. Do **not** recursively crawl the linked package's source directory.
2. Read the linked package's `CODEBASE.md` to find exact function signatures and exported types.
3. Jump directly to specific line ranges only if deep implementation logic is needed.