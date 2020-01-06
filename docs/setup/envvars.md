# 3. Environment Variables

For security, various protected credentials for the project are not stored in any version controlled files. These are instead stored as environment variables, the setup of which depends on environment.

| Variable Name | Example Value | Purpose |
|:-------|:-------|:--------|
| `DJANGO_DEBUG_MODE` | True | Boolean value for Django debug mode |
| `DJANGO_SETTINGS_MODULE` | bbncreative.settings.dev | Location of settings file |
| `EMAIL_HOST` | | Email host URL |
| `EMAIL_HOST_PASSWORD` | | Email host platform password |
| `EMAIL_HOST_USER` | | Email host platform username |
| `LOCKDOWN_PASSWORD` | | Access password if Lockdown is enabled |
| `POSTGRES_HOST` | localhost | The database location |
| `POSTGRES_NAME` | bbncreative | The name of the database |
| `POSTGRES_PASSWORD` |  | The access password |
| `POSTGRES_PROD_PASSWORD` |  | The access password |
| `POSTGRES_PORT` | 5432 | The access port |
| `POSTGRES_USER` | postgres | The access username |
| `RECAPTCHA_SECRET` | | reCaptcha account credential |
| `RECAPTCHA_SITE_KEY` | | reCaptcha account credential |
| `SECRET_KEY` | | Django secret key |
| `TWITTER_ACCESS_TOKEN` | | Twitter account credential |
| `TWITTER_APP_KEY` | | Twitter account credential |

## Continuous Integration & Others

Note that the database may not be created with the same customisations in the CI environment, and that the environment variables must be appropriately configured.

In terms of the database, the code does not need to be changed when credentials change. Only the database configuration itself and the envvars of any connected environment.
