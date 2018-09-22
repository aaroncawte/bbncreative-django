import os

# For security and portability, the secrets file uses environment variables to obscure sensitive information in
# development and on GitHub

DJANGO_SECRET = os.environ.get("SECRET_KEY")

POST_DB = {
    "NAME": os.environ.get("POSTGRES_NAME"),
    "USER": os.environ.get("POSTGRES_USER"),
    "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
    "HOST": os.environ.get("POSTGRES_HOST"),
    "PORT": os.environ.get("POSTGRES_PORT"),
}
RECAPTCHA_SITE_KEY = os.environ.get("RECAPTCHA_SITE_KEY")
RECAPTCHA_SECRET = os.environ.get("RECAPTCHA_SECRET")

EMAIL_HOST = os.environ.get("EMAIL_HOST")
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")

TWITTER_APP_KEY = os.environ.get("TWITTER_APP_KEY")
TWITTER_ACCESS_TOKEN = os.environ.get("TWITTER_ACCESS_TOKEN")

LOCKDOWN_PASSWORD = os.environ.get("LOCKDOWN_PASSWORD")
