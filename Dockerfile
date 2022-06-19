FROM python:3.10.4-slim

ENV \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1

ENV \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

WORKDIR /code

# install poetry
ENV \
    POETRY_VERSION=1.1.13 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1 \
    PATH="/root/.local/bin:$PATH"
COPY install-poetry.py ./
RUN python ./install-poetry.py

# install python dependencies
COPY poetry.lock pyproject.toml ./
RUN poetry install --no-dev

COPY . .

CMD ["./scripts/command.sh"]
