# 1. Python Virtual Environment & Django Installation
**Series:** Setup

Virtual environments let you install Python software and its dependencies in a _virtual environment_, rather than globally on the system. The benefits include:

- Using different versions of the same software in different virtual environments without conflict
- Portability of dependencies (export to `requirements.txt`, re-import elsewhere)

Getting set up with `python`, `pip` and `virtualenv` is trivial and can be followed from the first few steps of [this guide](http://timmyreilly.azurewebsites.net/python-pip-virtualenv-installation-on-windows/).

## Using Virtual Environments
Virtual Environments are stored in `C:\Users\Aaron\Envs` on Windows. This means dependencies are stored in these folders (so they can get pretty big), as well as management files such as the `activate.bat` script.

- Type `workon bbn-env` to enter the `bbn-env` virtual environment from anywhere
- Use `pip install` from within the virtual environment to manage dependencies

*If you run software without activating the virtual environment, it will fall back to global installations (and subsequently break, probably).*

