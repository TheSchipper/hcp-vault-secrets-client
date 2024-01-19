FROM python:3.12-slim

ARG secret_name
ARG secret_value=None

ARG hcp_organization_id=$HCP_ORGANIZATION_ID
ARG hcp_project_name=$HCP_PROJECT_NAME
ARG hcp_project_id=$HCP_PROJECT_ID
ARG hcp_access_token=$HCP_ACCESS_TOKEN

ENV HCP_ORGANIZATION_ID $hcp_organization_id
ENV HCP_PROJECT_NAME $hcp_project_name
ENV HCP_PROJECT_ID $hcp_project_id
ENV HCP_ACCESS_TOKEN $hcp_access_token
ENV SECRET_NAME $secret_name
ENV SECRET_VALUE $secret_value

# Copy workspace
WORKDIR /hcp-vault-secrets-client
COPY . /hcp-valut-secrets-client

RUN apt-get update

# Install Python packages
RUN pip install -r requirements.txt

ENTRYPOINT /bin/bash
#ENTRYPOINT ["python", "main.py", "-name", "$SECRET_NAME", "-value", "$SECRET_VALUE"]