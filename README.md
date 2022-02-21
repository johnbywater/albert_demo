# Welcome to albert_demo

This repo demonstrates how an event processing policy can be implemented on an application class.

## Developers

After cloning the repository, you can set up a virtual environment and
install dependencies by running the following command in the root
folder.

    $ make install

The ``make install`` command uses the build tool Poetry to create a dedicated
Python virtual environment for this project, and installs popular development
dependencies such as Black, isort and pytest.

Add tests in `./tests`. Add code in `./albert_demo`.

Run tests.

    $ make test

Check the formatting of the code.

    $ make lint

Reformat the code.

    $ make fmt

Add dependencies in `pyproject.toml` and then update installed packages.

    $ make update-packages
