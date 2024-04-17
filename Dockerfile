FROM python:3

ENV PIP_TOOLS_VERSION=7.4.1
ENV PIP_VERSION=24.0

# Copy workspace
WORKDIR /hcp-vault-secrets-client
COPY . /hcp-vault-secrets-client

RUN apt-get update

# Create virtual environment
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Upgrade pip to the latest version
RUN python -m pip install --no-cache-dir --upgrade pip==$PIP_VERSION

# Install pip-tools as the package manager and dev dependencies
RUN pip install --no-cache-dir pip-tools==$PIP_TOOLS_VERSION

RUN pip install --no-cache-dir -e .

RUN pip install --no-cache-dir -r requirements-dev.txt

ENTRYPOINT ["/bin/bash"]
