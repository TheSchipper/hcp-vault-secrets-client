FROM python:3.10-slim

#ENV PIP_TOOLS_VERSION 7.4.1

# Copy workspace
WORKDIR /hcp-vault-secrets-client
COPY . /hcp-vault-secrets-client

RUN apt-get update

# Upgrade pip to the latest version
RUN python -m pip install --no-cache-dir --upgrade pip==24.0

# Install pip-tools as the package manager and dev dependencies
RUN pip install --no-cache-dir pip-tools==7.4.1

RUN pip install --no-cache-dir -r requirements-dev.txt

ENTRYPOINT ["/bin/bash"]
