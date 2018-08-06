# Django App for bbncreative
A Django-powered server and custom CMS for the bbncreative website, built in summer 2018.

[![CircleCI](https://circleci.com/gh/aaroncawte/bbncreative-django/tree/master.svg?style=svg&circle-token=dbf29770a59f46187030dc984ae4c03e1f988f42)](https://circleci.com/gh/aaroncawte/bbncreative-django)

## Stack
Primary tools and requirements used for this project.

| Function | Tool | Version | Updated |
|:--|:--|:--|:--|
| Database | PostgreSQL | 10.4 | 06.08.2018 |
| Language | Python | 3.7.0 | 06.08.2018 |

### Python Packages
This table replicates the contents of [requirements.txt](requirements.txt).

| Package | Version | Purpose | Updated |
|:--|:--|:--|:--|
| Django | 2.1 | Web Server | 06.08.2018 |
| pytz | 2018.5 | World timezone definitions | 06.08.2018 |
| Pillow | 5.2.0 | Fork of PIL, the Python Imaging Library | 06.08.2018 |
| psycopg2 | 2.7.5 | PostgreSQL Adapter | 06.08.2018 |
| nodeenv | 1.3.2 | Syncs node environment with virtualenv | 06.08.2018 |


## Setup
Creation of this system involves a set of new technologies, which can be complicated at times. The initial setup has been documented for future reference, debugging and testing.

1. [Python virtual environment & Django installation](/setup/virtualenv.md)
2. [Switching to PostgreSQL](/setup/postgresql.md)
3. [Environment Variables](/setup/envvars.md)
4. [JavaScript Package Management](/setup/jspackages.md)

## Appendices
1. [Removing a file from git commit history](/appendices/githistory.md)