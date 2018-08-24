import json
from urllib import request as urlrequest, parse

from twython import Twython, TwythonAuthError

from bbncreative import secrets
from bbncreative_cms.models import Credit


def get_recaptcha(response_data: str) -> dict:
    print("IN: " + str(type(response_data)))
    url = 'https://www.google.com/recaptcha/api/siteverify'
    values = {
        'secret': secrets.RECAPTCHA_SECRET,
        'response': response_data
    }
    data = parse.urlencode(values).encode("utf-8")
    req = urlrequest.Request(url)
    response = urlrequest.urlopen(req, data)
    result = json.load(response)
    print("OUT: " + str(type(result)))
    return result


def generate_logo_rgba(color: str, hover: bool) -> tuple:
    alpha_value = 0.9
    if hover:
        alpha_value = 1
    return tuple(int(color[i:i + 2], 16) for i in (0, 2, 4)) + (alpha_value,)


def count_children_projects(projects: list) -> list:
    for p in projects:
        p.collaborator_count = p.count_collaborators()
        p.credit_count = Credit.objects.filter(project=p).count()
        p.asset_count = p.count_assets()
    return projects


def get_twitter_pictures(users: list) -> dict:
    user_dict = {}
    try:
        APP_KEY = secrets.TWITTER_APP_KEY
        ACCESS_TOKEN = secrets.TWITTER_ACCESS_TOKEN
        twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)
        users_data = twitter.lookup_user(screen_name=users)
        if len(users_data):
            for user in users_data:
                key = str(user.get("screen_name")).lower()
                images = {
                    "profile": str(user.get("profile_image_url_https")).replace("_normal", ""),
                    "cover": str(user.get("profile_banner_url"))
                }
                val = images
                user_dict[key] = val
    except TwythonAuthError:
        print("ERROR: Unable to connect to Twitter API - Authentication Error.")
    return user_dict
