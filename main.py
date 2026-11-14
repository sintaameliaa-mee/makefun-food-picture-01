# food-picture-01 entry: the best-looking food picture. The image beside
# this file is a steaming bowl of ramen photographed like a high-end
# restaurant ad: chopsticks lifting glossy noodles, chashu pork, a runny-yolk
# egg, nori and spring onions, against a dark moody background. The program
# copies it to the output directory; the judge sees exactly these bytes.

import os
import shutil
from pathlib import Path


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(Path(__file__).with_name("entry.png"), out_dir / "entry.png")


if __name__ == "__main__":
    main()
