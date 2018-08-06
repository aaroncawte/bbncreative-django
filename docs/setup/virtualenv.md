# 1. Python Virtual Environment & Django Installation

**Series:** Setup

**Last Edited:** 09/06/2018

---
Virtual environments let you install Python software and its dependencies in a _virtual environment_, rather than globally on the system. The benefits include:

- Using different versions of the same software in different virtual environments without conflict
- Portability of dependencies (export to `requirements.txt`, re-import elsewhere)

Getting set up with `python`, `pip` and `virtualenv` is trivial and can be followed from the first few steps of [this guide](http://timmyreilly.azurewebsites.net/python-pip-virtualenv-installation-on-windows/).

## Using Virtual Environments
Virtual Environments are stored in `C:\Users\Aaron\Envs` on Windows. This means dependencies are stored in these folders (so they can get pretty big), as well as management files such as the `activate.bat` script.

| Task | Command | Description |
|:--|:--|:--|
| Create | `mkvirtualenv {name} -p {pythonpath} -r requirements.txt` | Type from the project directory to create a virtualenv |
| Remove | `rmvirtualenv {name}` | Type to remove the virtualenv (but not the project files) |
| Use | `workon bbn-env` |  Type to enter the virtualenv from anywhere |
| Save requirements | `pip freeze > requirements.txt` | Use to update requirements file |
| Load requirements | `pip install requirements.txt` | Use to install requirements |

*If you run software without activating the virtual environment, it will fall back to global installations (and subsequently break, probably).*

## Virtual Environments and PyCharm
In order to run the project from PyCharm and benefit from other integrations, you will need to configure it to "interpret" the project from the virtual environment's perspective. Follow [this guide](https://www.jetbrains.com/help/pycharm-edu/project-interpreter.html) from JetBrains on how to do this.

