FROM python:3.10-slim

ARG secret_name
ARG secret_value
ARG mode=read

ENV SECRET_NAME $secret_name
ENV SECRET_VALUE $secret_value
ENV HCP_MODE $mode

# Copy workspace
WORKDIR /hcp-vault-secrets-client
COPY . /hcp-vault-secrets-client

RUN apt-get update

# Install Python packages
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]