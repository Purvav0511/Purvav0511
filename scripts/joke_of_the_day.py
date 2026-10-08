"""Swap today's joke into README.md between the JOKE markers."""
import datetime
import pathlib
import re

root = pathlib.Path(__file__).resolve().parent.parent
jokes = [line.strip() for line in (root / "jokes.txt").read_text().splitlines() if line.strip()]
today = datetime.date.today()
joke = jokes[today.toordinal() % len(jokes)]

readme = root / "README.md"
text = readme.read_text()
updated = re.sub(
    r"<!--JOKE:START-->.*?<!--JOKE:END-->",
    f"<!--JOKE:START-->\n> {joke}\n<!--JOKE:END-->",
    text,
    flags=re.S,
)
readme.write_text(updated)
print(f"{today}: {joke}")
