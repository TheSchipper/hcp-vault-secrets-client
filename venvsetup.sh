#!/bin/bash -e

PIP_TOOLS_VERSION=7.4.1
PIP_VERSION=24.0

create_environment() {
    echo "Creating environment"
    python3 -m venv .venv
    # shellcheck source=/dev/null
    source .venv/bin/activate
    python -m pip install --no-cache-dir --upgrade pip==$PIP_VERSION
}

install_pip_tools() {
    echo "Installing pip-tools"
    pip install --no-cache-dir pip-tools==$PIP_TOOLS_VERSION
}

install_dev_dependencies() {
    echo "Installing dev dependencies"
    pip install --no-cache-dir -r requirements-dev.txt
}

install_package() {
    echo "Installing editable package"
    pip install --no-cache-dir -e .
}

create_environment
install_pip_tools
install_dev_dependencies
install_package

echo "🚀 Environment Setup Complete! 🚀"
exit 0