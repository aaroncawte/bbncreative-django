# 2. Using PostgreSQL

bbncreative-portfolio is built using a PostgresQL database rather than the Django default of SQLite, due to the extra flexibilty it offers. The Postgres version currently in production is listed on the [README](../../README.md).

## Production configuration

[This guide](https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04) from DigitalOcean details the process for an Ubuntu installation. I followed its steps after the `psql` command.

## Issues

Perhaps due to the Windows/Ubuntu differences, or PostgreSQL versions, a couple of issues arose where the second user account (username `aaron`) was not given the right permissions on the various structures in the database.

I found that these could be solved by simply searching the web for the errors that were thrown.

## Test

The installation should now be fully functional! In a development environment, run:

```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
```

If these are working, it is likely that the installation is working ok. Don't forget to test with various model operations later on!
