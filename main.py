from hcp_vault_secrets_client.hcp import HcpClient

import argparse
import os


def parse_args():
    parser = argparse.ArgumentParser(description='HCP Vault Secrets Client')
    parser.add_argument('-m', '--mode', help='Mode to run the client in', default='read')
    parser.add_argument('-n', '--name', help='Name of the secret to read/create/delete', default=os.getenv("SECRET_NAME"))
    parser.add_argument('-v', '--value', help='Value of the secret to create', default=os.getenv("SECRET_VALUE"))
    return parser.parse_args()


def main(mode="read", name=None, value=None):
    client = HcpClient()

    if mode == 'read':
        print(client.get_app_secret(name))
    if mode == 'create':
        print(client.create_app_secret(name, value))
    if mode == 'delete':
        print(client.delete_app_secret(name))


if __name__ == "__main__":
    args = parse_args()
    main(args.mode, args.name, args.value)
