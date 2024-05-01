FROM python:3

WORKDIR /hcp-vault-secrets-client
COPY . /hcp-vault-secrets-client

RUN apt-get update

RUN ./venvsetup.sh

ENTRYPOINT ["/bin/bash"]
