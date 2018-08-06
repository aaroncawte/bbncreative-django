# Django App for bbncreative
A Django-powered server and custom CMS for the bbncreative website, built in summer 2018.

[![CircleCI](https://circleci.com/gh/aaroncawte/bbncreative-django/tree/master.svg?style=svg&circle-token=dbf29770a59f46187030dc984ae4c03e1f988f42)](https://circleci.com/gh/aaroncawte/bbncreative-django)

## Stack
Primary tools and requirements used for this project.

| Function | Tool | Version |
|:--|:--|:--|
| Database | PostgreSQL | 10.4 |
| Language | Python | 3.7.0 |

### Python Packages
This table replicates the contents of [requirements.txt](requirements.txt).

| Package | Version |
|:--|:--|
| nodeenv | 1.3.2 |
| Pillow | 5.2.0 |
| psycopg2 | 2.7.5 |
| pytz | 2018.5 |


## Setup
Creation of this system involves a set of new technologies, which can be complicated at times. The initial setup has been documented for future reference, debugging and testing.

1. [Python virtual environment & Django installation](/setup/virtualenv.md)
2. [Switching to PostgreSQL](/setup/postgresql.md)
3. [Environment Variables](/setup/envvars.md)
4. [JavaScript Package Management](/setup/jspackages.md)

## Appendices
1. [Removing a file from git commit history](/appendices/githistory.md)