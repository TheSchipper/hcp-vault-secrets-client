FROM python:3.12-slim

# Copy workspace
WORKDIR /hcp-vault-secrets-client
COPY . /hcp-valut-secrets-client

RUN apt-get update

# Install Python packages
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]