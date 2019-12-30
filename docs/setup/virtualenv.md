# 1. Python Virtual Environment & Django Installation

As a Python-based project, `bbncreative-portfolio` is run in a virtual environment in all configurations. The setup is slightly different between operating systems (as the project is built and run on different ones), so a few notes are left for both.

## Project requirements

Python dependencies can be persisted for future reference using `pip freeze`, which by convention should be stored in `requirements.txt`. The project's dependencies can be easily re-installed at a later date by calling `pip install` on that file.

| Task | Command | Description |
|:--|:--|:--|
| Save requirements | `pip freeze > requirements.txt` | Use to update requirements file |
| Load requirements | `pip install requirements.txt` | Use to install requirements |

## Virtual environments on Windows

A Python virtual environment on Windows can be configured using the [virtualenvwrapper-win](https://pypi.org/project/virtualenvwrapper-win/) software.

Use `workon {{env_name}}` and `deactivate` from Cmd to enter and exit your virtual environment. See the [documentation](https://pypi.org/project/virtualenvwrapper-win/) for more options.

## Virtual environments on Ubuntu

Details on the native `virtualenv` package used on Linux distributions can be found in its [documentation](https://virtualenv.pypa.io/en/latest/userguide/).

Use `source activate` in the environment's `bin` folder, and the `deactivate` to exit.

## Virtual Environments and PyCharm

In order to run the project from PyCharm and benefit from other integrations, you will need to configure it to "interpret" the project from the virtual environment's perspective. Follow [this guide](https://www.jetbrains.com/help/pycharm-edu/project-interpreter.html) from JetBrains on how to do this.
