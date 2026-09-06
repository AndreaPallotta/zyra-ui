import os
import sys
import re
from pathlib import Path

def transpile_zyx_content(source: str) -> str:
    # Match JSX-like blocks enclosed in parentheses: ( <tag ...> ... </tag> ) or ( <tag ... /> )
    # Also match multiline blocks starting with <tag and ending with </tag> after return or =
    pattern = re.compile(
        r'(\breturn\s*|\b=\s*)\(\s*(<([a-zA-Z0-9_-]+)[^>]*>[\s\S]*?<\/\3>|<([a-zA-Z0-9_-]+)[^>]*\/>)\s*\)',
        re.MULTILINE
    )

    def lower_jsx(prefix: str, markup: str) -> str:
        lines = markup.strip().splitlines()
        clean_parts = []
        for line in lines:
            trimmed = line.strip()
            if not trimmed:
                continue
            # Handle expression interpolations: {expr}
            parts = re.split(r'(\{.*?\})', trimmed)
            assembled = []
            for p in parts:
                if p.startswith('{') and p.endswith('}'):
                    expr = p[1:-1].strip()
                    assembled.append('" + (' + expr + ') + "')
                else:
                    escaped = p.replace('"', '\\"')
                    assembled.append(escaped)
            clean_parts.append("".join(assembled))
        
        joined = "".join(clean_parts)
        return f'{prefix}"{joined}"'

    def replacer(match):
        prefix = match.group(1)
        markup = match.group(2)
        return lower_jsx(prefix, markup)

    lowered = pattern.sub(replacer, source)

    # Also handle standalone JSX without wrapping parens: return <tag ...> ... </tag>
    standalone_pattern = re.compile(
        r'(\breturn\s+)(<([a-zA-Z0-9_-]+)[^>]*>[\s\S]*?<\/\3>|<([a-zA-Z0-9_-]+)[^>]*\/>)',
        re.MULTILINE
    )
    def standalone_replacer(match):
        prefix = match.group(1)
        markup = match.group(2)
        return lower_jsx(prefix, markup)

    lowered = standalone_pattern.sub(standalone_replacer, lowered)
    return lowered

def compile_zyx_file(in_path: Path, out_path: Path):
    content = in_path.read_text(encoding="utf-8")
    transpiled = transpile_zyx_content(content)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(transpiled, encoding="utf-8")
    print(f"[OK] Compiled ZYX: {in_path} -> {out_path}")

def main():
    if len(sys.argv) < 2:
        print("Usage: zyx <build|run> [file.zyx] [--out <output.zy>]")
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == "build":
        in_file = Path(sys.argv[2] if len(sys.argv) > 2 else "src/App.zyx")
        out_file = in_file.with_suffix(".zy")
        if "--out" in sys.argv:
            idx = sys.argv.index("--out")
            if idx + 1 < len(sys.argv):
                out_file = Path(sys.argv[idx + 1])
        compile_zyx_file(in_file, out_file)
    elif cmd == "run":
        in_file = Path(sys.argv[2] if len(sys.argv) > 2 else "src/App.zyx")
        out_file = in_file.with_suffix(".zy")
        compile_zyx_file(in_file, out_file)
        # Execute with zyra
        import subprocess
        res = subprocess.run(["zyra", "run", str(out_file)])
        sys.exit(res.returncode)
    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)

if __name__ == "__main__":
    main()