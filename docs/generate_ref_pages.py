"""Generate the code reference pages."""

# Taken from https://mkdocstrings.github.io/recipes/
# Should run with CWD = repository root.

from pathlib import Path
from typing import Generator, Iterable

import mkdocs_gen_files

source_files = sorted(Path("src").rglob("*.py"))


def remove_init_files(paths: Iterable[Path]) -> Generator[Path, None, None]:
    for file_path in paths:
        if file_path.is_file() and file_path.name == "__init__.py":
            continue
        yield file_path


for path in remove_init_files(source_files):  #

    module_path = path.relative_to("src").with_suffix("")  #

    doc_path = path.relative_to("src").with_suffix(".md")  #

    full_doc_path = Path("reference", doc_path)  #

    parts = list(module_path.parts)

    if parts[-1] == "__init__":  #

        parts = parts[:-1]
    elif parts[-1] == "__main__":
        continue

    with mkdocs_gen_files.open(full_doc_path, "w") as fd:  #

        identifier = ".".join(parts)  #

        print("::: " + identifier, file=fd)  #

    mkdocs_gen_files.set_edit_path(full_doc_path, path)  #
