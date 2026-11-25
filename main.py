import os

def main():
    """Writes a one-line joke about an AI agent's worst Monday to entry.txt."""
    LINE = "Tests passed out of pity after I gaslit a null pointer exception for six hours, but the build broke during my apology.\n"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    content = LINE
    if not (1 <= len(content) <= 140 and content.strip() and content.count("\n") == 1 and not content.startswith("\n")):
        raise ValueError(content)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    if out_dir != "/output":
        try:
            os.makedirs("/output", exist_ok=True)
            with open("/output/entry.txt", "w", encoding="utf-8") as f:
                f.write(content)
        except Exception:
            pass
    print(f"{path} {len(content)}")

if __name__ == "__main__":
    main()
# Entry validated: output is 1-140 chars, one line, deterministic.
