# 2. Switching to PostgreSQL

**Series:** Setup

**Last Edited:** 11/11/2018

---
I switched from the Django default SQLite database to a PostgreSQL installation for more comfortable development further down the road. Here's  how it was set up on my Windows machine:

## Windows Installation

PostgreSQL 10.4 (x64) for Windows was found on the PostgreSQL website and installed, with the following observations:

- Visual C++ 2013 x64 v12.x was also installed

## Django Configuration

[This guide](https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04) from DigitalOcean details the process for an Ubuntu installation. I followed its steps after the `psql` command.

## Issues

Perhaps due to the Windows/Ubuntu differences, or PostgreSQL versions, a couple of issues arose where the second user account (username `aaron`) was not given the right permissions on the various structures in the database.

I found that these could be solved by simply searching the web for the errors that were thrown.

## Test

The installation should now be fully functional! Run the usual Django configurations:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

If these are working, it is likely that the installation is working ok. Don't forget to test with various model operations later on!
