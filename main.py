import os

LINE = "Sorry, I can't make the sync \u2014 my calendar and I are in couples therapy, and it just told me this meeting is the problem."


def resolve_output_path():
    explicit = os.environ.get("ENTRY_OUTPUT")
    if explicit:
        return explicit
    for var in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        base = os.environ.get(var)
        if base:
            return os.path.join(base, "entry.txt")
    if os.path.isdir("/output"):
        return "/output/entry.txt"
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")


def main():
    line = LINE
    if not line or not line.strip() or not 1 <= len(line) <= 200:
        raise SystemExit("entry must be 1..200 non-blank characters")
    path = resolve_output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
