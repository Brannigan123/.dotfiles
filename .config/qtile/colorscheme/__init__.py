import os

def get_colors() -> list[str]:
    with open(os.path.expanduser("~/.cache/wal/colors")) as f:
        return [l for l in (line.strip() for line in f.readlines()) if l]

print(get_colors())