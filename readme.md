# Django App for bbncreative
A Django-powered server and custom CMS for the bbncreative website, a summer project by Aaron Cawte.

[![CircleCI](https://circleci.com/gh/aaroncawte/bbncreative-django/tree/master.svg?style=svg&circle-token=dbf29770a59f46187030dc984ae4c03e1f988f42)](https://circleci.com/gh/aaroncawte/bbncreative-django)


### Where is this software available?
This software runs a web-based portfolio for Aaron Cawte, live at https://bbncreative.co.

### Why is this repository public?
This software is a custom Content Management System for my personal portfolio. I have made the source code available to view to demonstrate my programming ability. This includes detailed setup documentation.

## Author
This project is built upon the Django framework and uses multiple python packages listed below. Beyond these, all other content is produced by Aaron Cawte.
Contact Aaron via [email](mailto:aaron@bbncreative.co) or on [Twitter](https://twitter.com/aaroncawte).

## License
This software is made available for review, not for re-use. Accordingly, it is licensed under **Attribution-NonCommercial-NoDerivs 3.0 Unported (CC BY-NC-ND 3.0)**. View the license [here](/license.md), or view a summary on [creativecommons.org](https://creativecommons.org/licenses/by-nc-nd/3.0/). If you are unsure, please contact Aaron.
## Stack
Primary tools and requirements used for this project.

| Function | Tool | Version | Updated |
|:--|:--|:--|:--|
| Database | PostgreSQL | 10.5 | 23.08.2018 |
| Language | Python | 3.7.0 | 06.08.2018 |

### Python Packages
This list of necessary python packages is available in [requirements.txt](requirements.txt). Check the latest versions below:

- Django: [![PyPI version](https://badge.fury.io/py/Django.svg)](https://badge.fury.io/py/Django)
- pytz: [![PyPI version](https://badge.fury.io/py/pytz.svg)](https://badge.fury.io/py/pytz)
- Pillow: [![PyPI version](https://badge.fury.io/py/Pillow.svg)](https://badge.fury.io/py/Pillow)
- psycopg2: [![PyPI version](https://badge.fury.io/py/psycopg2.svg)](https://badge.fury.io/py/psycopg2)
- nodeenv: [![PyPI version](https://badge.fury.io/py/nodeenv.svg)](https://badge.fury.io/py/nodeenv)
- twython: [![PyPI version](https://badge.fury.io/py/twython.svg)](https://badge.fury.io/py/twython)

*Note that these packages have further dependencies not listed here.*

## Documentation

### Setup
The initial setup of this system has been documented for future reference, debugging and testing.

1. [Python virtual environment & Django installation](/docs/setup/virtualenv.md)
2. [Switching to PostgreSQL](/docs/setup/postgresql.md)
3. [Environment Variables](/docs/setup/envvars.md)
4. [JavaScript Package Management](/docs/setup/jspackages.md)
5. [Web Server Setup](/docs/setup/webserver.md)

### Appendices
Relevant information to the system has also been documented as follows:

1. [Removing a file from git commit history](/docs/appendices/githistory.md)
2. [Content Aspect Ratios](/docs/appendices/aspect_ratios.md)