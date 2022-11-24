import pathlib

import pytest
from mktestdocs import check_md_file  # type: ignore

# Has to run from repository root


# Note the use of `str`, makes for pretty output
@pytest.mark.parametrize("fpath", pathlib.Path("docs").glob("**/*.md"), ids=str)
def test_files_good(fpath):
    check_md_file(fpath=fpath)
