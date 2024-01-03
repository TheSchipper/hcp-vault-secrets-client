FROM python:3.12-slim

ENV POETRY_VERSION=1.7.1

# Copy workspace
WORKDIR /hcp-vault-secrets-client
COPY . /hcp-valut-secrets-client

# Install Curl
RUN apt-get update && apt-get install curl -y

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - --version POETRY_VERSION
ENV PATH="/root/.local/bin:$PATH"

RUN poetry install --no-root

ENTRYPOINT ["poetry", "run", "python"]