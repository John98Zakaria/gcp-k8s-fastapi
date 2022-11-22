# GCP FastAPI K8S Deployment

<!-- badges-begin -->

[![Black codestyle][black badge]][black project]
[![Conventional commits][conventional badge]][Conventional commits]
[![pre-commit enabled][pre-commit badge]][pre-commit project]

[black badge]: https://img.shields.io/badge/code%20style-black-000000.svg

[black project]: https://github.com/psf/black

[pre-commit badge]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white

[pre-commit project]: https://pre-commit.com/

[python version badge]: https://img.shields.io/pypi/pyversions/cookiecutter-hypermodern-python-instance

[readthedocs badge]: https://img.shields.io/readthedocs/cookiecutter-hypermodern-python/latest.svg?label=Read%20the%20Docs

[readthedocs page]: https://cookiecutter-hypermodern-python.readthedocs.io/

[status badge]: https://badgen.net/badge/status/alpha/d8624d

[conventional badge]: docs/assets/general/conventional-commits.png

[Conventional commits]: https://www.conventionalcommits.org/en/v1.0.0/

<!-- badges-end -->

# How to install the project

Install a python version of your choice using the official installer or conda.\
[Download](https://python-poetry.org/docs/master/#installing-with-the-official-installer) and install poetry.

Add poetry to path, the default path on Windows is %APPDATA%\pypoetry\venv\Scripts.
If you are currently using an IDE, restart it.

Afterwards, run in cmd

```commandline
poetry install
pre-commit install --hook-type commit-msg
```

To install the pre-commit hooks correctly you need to a commit locally to fetch the linting tools.

## Adding new packages to the project

Install new packages with `poetry add <package-name>` \
install new dev packages with `poetry add -G dev <package-name>`

## Database Migrations

First navigate to src `cd src`

* To crate a migration run `alembic revision --autogenerate -m "<Your Update Message>"`
* To apply a migration run `alembic upgrade head`
* To revert to a migration run `alembic downgrade "revision-number"`

# Writing good commit messages

To prevent commit messages from becoming useless, this repository uses
conventional commits to keep commit messages useful.

Read about the [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/) standard and use it to write your
commit messages.

You can also use commitizen to write commits

type in `cz c` to generate your commit message interactively.

# Documentation

To generate the documentation run `poetry run task docs-regen` or `python docs/generate_ref_pages.py && git add docs` \
To run the documentation run `poetry run task docs-serve` or `mkdocs serve`

Try it out and read the getting started section :)

## License

Distributed under the terms of the MIT license


