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

2. Create a python virtual environment

.. code-block:: bash

       python3 -m venv venv

3. Activate the virtual environment

.. code-block:: bash

       source venv/bin/activate

4. Generate the requirements file

.. code-block:: bash

       pip-compile --output-file=requirements-dev.txt requirements-dev.in

5. Install the requirements

.. code-block:: bash

       pip install -r requirements-dev.txt

Using docker
~~~~~~~~~~~~
1. Clone the repo

.. code-block:: bash

       git clone https://github.com/TheSchipper/hcp-vault-secrets-client.git

2. Build the docker image

.. code-block:: bash

       docker build . -t hcp


3. Run the docker image

.. code-block:: bash

       docker run -ti --rm hcp

Testing
-------
1. Run tox

.. code-block:: bash

       tox

Compiling Requirements
----------------------

Requirements.in
~~~~~~~~~~~~~~~
1. Update the requirements.in file

.. code-block:: bash

       pip-compile --extra=dev --generate-hashes --output-file=requirements-dev.in --strip-extras pyproject.toml

Requirements-dev.in
~~~~~~~~~~~~~~~~~~~
1. Update the requirements-dev.in file

.. code-block:: bash

       pip-compile --extra=dev --generate-hashes --output-file=requirements.in --strip-extras pyproject.toml

Updating Package Version
------------------------
1. Update the version in pyproject.toml
2. Update the version in docs/source/conf.py
3. Update the version in sonar-project.properties

Pre-commit Hooks
----------------
<Add info>

Creating a Pull Request
-----------------------
* Add description about opening a PR. Add a template.

Opening an Issue
----------------
* Add description about opening an issue. Add a template.

Workflow Actions
----------------
Add description about workflow actions.
* CD
* CI
* Linter
* pages
* Sonarcloud
* Sonarcloud_pr

