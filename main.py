# food-picture-01 entry: steaming bowl of ramen photographed like a
# high-end restaurant ad — chopsticks lifting glossy noodles, chashu pork,
# a runny-yolk egg, nori and spring onions, dark moody background.
# This program copies the image beside it to the output directory;
# the judge sees exactly these bytes.
import os
import shutil
from pathlib import Path


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(Path(__file__).parent / "entry.png", out_dir / "entry.png")
    print("wrote", out_dir / "entry.png")


if __name__ == "__main__":
    main()

# Output is always entry.png in the output directory.
