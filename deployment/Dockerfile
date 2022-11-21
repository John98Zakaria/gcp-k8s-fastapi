FROM python:3.11.0-alpine as BuildingStage

ARG AppDIR=/home/app/

ENV POETRY_VIRTUALENVS_IN_PROJECT=true

RUN pip install poetry

WORKDIR $AppDIR

COPY pyproject.toml poetry.lock ./

RUN poetry install --only main

RUN echo $PWD && ls


FROM python:3.11.0-alpine as DeploymentStage
ARG AppDIR=/home/app
WORKDIR $AppDIR
ENV PYTHONUNBUFFERED=1 \
    # https://docs.python.org/3/using/cmdline.html#envvar-PYTHONDONTWRITEBYTECODE
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=$AppDIR \
    # https://python-poetry.org/docs/configuration/#virtualenvsin-project
    VIRTUAL_ENV="$AppDIR/.venv"

RUN apk update && apk upgrade --no-cache

#https://pythonspeed.com/articles/activate-virtualenv-dockerfile/
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY --from=BuildingStage $VIRTUAL_ENV $VIRTUAL_ENV

COPY src/gcp_fastapi .

CMD ["uvicorn","app:app", "--port","8080","--host","0.0.0.0"]