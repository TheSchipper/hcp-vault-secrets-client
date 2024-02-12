FROM python:3.10-slim

# Copy workspace
WORKDIR /hcp-vault-secrets-client
COPY . /hcp-vault-secrets-client

RUN apt-get update

# Install Python packages
RUN pip install . .[test]

ENTRYPOINT ["python"]