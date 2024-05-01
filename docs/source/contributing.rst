============
Contributing
============

Dev Environment
---------------
+------------------------+----------------------------------------------+
| Tools                  | Description                                  |
+========================+==============================================+
| `pip-tools`_           | Used to generate requirements.txt            |
+------------------------+----------------------------------------------+
| `pytest`_              | Used to run tests                            |
+------------------------+----------------------------------------------+
| `pytest-cove`_         | Used to generate test coverage reports       |
+------------------------+----------------------------------------------+
| `JSON-log-formatter`_  | Used for JSON logging                        |
+------------------------+----------------------------------------------+
| `mypy`_                | Used for type checking                       |
+------------------------+----------------------------------------------+
| `black`_               | Used for code formatting                     |
+------------------------+----------------------------------------------+
| `tox`_                 | Used for testing in multiple python versions |
+------------------------+----------------------------------------------+

.. _pip-tools: https://pypi.org/project/pip-tools/
.. _pytest: https://pypi.org/project/pytest/
.. _pytest-cove: https://pypi.org/project/pytest-cov/
.. _JSON-log-formatter: https://pypi.org/project/json-log-formatter/
.. _mypy: https://pypi.org/project/mypy/
.. _black: https://pypi.org/project/black/
.. _tox: https://pypi.org/project/tox/

Optional Tools
~~~~~~~~~~~~~~
+----------------------+------------------------------------------------+
| Tools                | Description                                    |
+======================+================================================+
| `Docker`_            | Used to run the dev environment in a container |
+----------------------+------------------------------------------------+

.. _Docker: https://www.docker.com/

Building enviornment
--------------------

Python virtual environment
~~~~~~~~~~~~~~~~~~~~~~~~~~
1. Clone the repo

.. code-block:: bash

       git clone https://github.com/TheSchipper/hcp-vault-secrets-client.git

2. Use the setup script to create a virtual environment

.. code-block:: bash

       ./venvsetup.sh

3. Activate the virtual environment

.. code-block:: bash

       source .venv/bin/activate

4.  When finished, deactivate the virtual environment

.. code-block:: bash

       deactivate

Using docker (optional)
~~~~~~~~~~~~~~~~~~~~~~~
1. Clone the repo

.. code-block:: bash

       git clone https://github.com/TheSchipper/hcp-vault-secrets-client.git

2. Build the docker image

.. code-block:: bash

       docker build . -t hcp


3. Run the docker image

.. code-block:: bash

       docker run -ti --rm hcp

4. Activate the virtual environment

.. code-block:: bash

       source .venv/bin/activate

5. When finished, exit the docker image

.. code-block:: bash

       exit

Testing
-------
1. Run tox

.. code-block:: bash

       tox

Compiling Requirements
----------------------

Requirements.txt
~~~~~~~~~~~~~~~~
1. Updating the requirements.txt file

.. code-block:: bash

       pip-compile pyproject.toml

Requirements-dev.txt
~~~~~~~~~~~~~~~~~~~~
1. Updating the requirements-dev.txt file

.. code-block:: bash

       pip-compile --extra=dev --output-file=requirements-dev.txt pyproject.toml

Updating Package Version
------------------------
This project follows semantic versioning, a widely adopted versioning scheme for managing software releases. Semantic
versioning uses a three-part version number in the format MAJOR.MINOR.PATCH, where:

* MAJOR version is incremented when incompatible API changes are introduced.
* MINOR version is incremented when functionality is added in a backward-compatible manner.
* PATCH version is incremented when backward-compatible bug fixes are made.

Additional labels for pre-release and build metadata are available as extensions to the MAJOR.MINOR.PATCH format.
When making changes to the codebase, it's important to follow these rules:

1. Patch releases should be incremented for bug fixes and other minor changes that don't affect the public API. These
   changes should maintain backward compatibility.
2. Minor releases should be incremented when new features or functionality are introduced in a backward-compatible way.
   Minor releases should not break existing functionality.
3. Major releases should be incremented when breaking changes are made to the public API. These changes might include
   removing or renaming existing functionality, changing method signatures, or modifying data structures in an incompatible
   way.

For more details, refer to the `Semantic Versioning specification`_.

.. _Semantic Versioning specification: https://semver.org/

Locations to Update
~~~~~~~~~~~~~~~~~~~

1. Update the ``version`` in `pyproject.toml`_
2. Update the ``release`` in `docs/source/conf.py`_
3. Update the ``sonar.projectVersion`` in `sonar-project.properties`_

.. _pyproject.toml: https://github.com/TheSchipper/hcp-vault-secrets-client/blob/main/pyproject.toml
.. _docs/source/conf.py: https://github.com/TheSchipper/hcp-vault-secrets-client/blob/main/docs/source/conf.py
.. _sonar-project.properties: https://github.com/TheSchipper/hcp-vault-secrets-client/blob/main/sonar-project.properties

Pre-commit Hooks
----------------
<TBD>

Creating a Pull Request
-----------------------
Please review the `Contributing Guidelines`_ before submitting a pull request. When submitting a pull request, please
use the provided `template`_.

.. _Contributing Guidelines: https://theschipper.github.io/hcp-vault-secrets-client/contributing.html
.. _template: https://github.com/TheSchipper/hcp-vault-secrets-client/blob/main/.github/PULL_REQUEST_TEMPLATE.md

Opening an Issue
----------------
* When creating a new issue, please use the provided `template`_.

.. _template: https://github.com/TheSchipper/hcp-vault-secrets-client/blob/main/.github/ISSUE_TEMPLATE.md

Workflow Actions
----------------
Add description about workflow actions.

* `CD`_ - Continuous Delivery workflow to publish to `PyPI`_
* `CI`_ - Continuous Integration workflow
* `Linter`_ - Linting workflow provided by `Super Linter`_
* `pages`_ - `Sphinx`_ Documentation workflow
* `Sonarcloud`_ - Code quality workflow provided by `SonarCloud`_
* `Sonarcloud_pr`_ - Code quality workflow for PRs provided by `SonarCloud`_

.. _CD: https://github.com/TheSchipper/hcp-vault-secrets-client/actions/workflows/cd.yml
.. _PyPI: https://pypi.org/project/hcp-vault-secrets-client/
.. _CI: https://github.com/TheSchipper/hcp-vault-secrets-client/actions/workflows/ci.yml
.. _Linter: https://github.com/TheSchipper/hcp-vault-secrets-client/actions/workflows/linter.yml
.. _Super Linter: https://github.com/github/super-linter
.. _pages: https://github.com/TheSchipper/hcp-vault-secrets-client/actions/workflows/pages.yml
.. _Sphinx: https://www.sphinx-doc.org/en/master/
.. _Sonarcloud: https://github.com/TheSchipper/hcp-vault-secrets-client/actions/workflows/sonarcloud.yml
.. _Sonarcloud_pr: https://github.com/TheSchipper/hcp-vault-secrets-client/actions/workflows/sonarcloud_pr.yml
.. _SonarCloud: https://sonarcloud.io/
