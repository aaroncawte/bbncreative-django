# 3 Environment Variables

**Series:** Setup

**Last Edited:** 09/06/2018

---

For security, various protected credentials for the project are not stored in any version controlled files. These are instead stores as _environment variables_, the setup of which depends on environment.

## Current Credentials

- `SECRET_KEY`, the Django project's secret key
- The Postgres database configuration:
        - `POSTGRES_NAME`, the database name
        - `POSTGRES_USER`, the access username
        - `POSTGRES_PASSWORD`, the access user's password
        - `POSTGRES_HOST`, default localhost
        - `POSTGRES_PORT`, default 5432

| Credential | Default Value | Purpose |
|:-------|:-------|:--------|
| `POSTGRES_NAME` | N/A | The name of the database |
| `POSTGRES_USER` | postgres | The access username |
| `POSTGRES_PASSWORD` |  | The access password |
| `POSTGRES_HOST` | localhost | The database location |
| `POSTGRES_PORT` | 5432 | The access port |

## Continuous Integration & Others

Note that the database may not be created with the same customisations in the CI environment, and that the environment variables must be appropriately configured.

In terms of the database, the code does not need to be changed when credentials change. Only the database configuration itself and the envvars of any connected environment.
