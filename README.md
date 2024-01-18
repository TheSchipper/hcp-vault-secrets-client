<p align="center">
<img src="banner.png">
</p>
<h2 align="center">Hashi-Corp Vault Secrets Manager</h2>

![Static Badge](https://img.shields.io/badge/Python-3.12-blue)
![Static Badge](https://img.shields.io/badge/License-MIT-green)

An API client to use the Hashi-Corp Vault secrets.

https://portal.cloud.hashicorp.com/sign-in

### Installation
Using pip
```bash
pip install 
```

### Usage

Python Console
```python
from hcp_vault_secrets_client.hcp import HcpClient

client = HcpClient() # override where the ini file is localed with config_path

client.create_app_secret("MyNewSecret", "HelloWorld")

client.get_app_secret("MyNewSecret") # returns "HelloWorld"

client.delete_app_secret("MyNewSecret")
```

#### Environment Variables
- HCP_ORGANIZATION_ID
- HCP_PROJECT_NAME
- HCP_PROJECT_ID
- HCP_ACCESS_TOKEN

#### INI Configuration
```text
[DEFAULT]
HCP_ORGANIZATION_ID=
HCP_PROJECT_ID=
HCP_PROJECT_NAME=

[SECRET]
HCP_ACCESS_TOKEN=
```

### Contributing
Please review the contributing guidelines if you would like to add to this project!
