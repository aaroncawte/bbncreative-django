import os

from twython import Twython, TwythonAuthError

from bbncreative_cms.models import Credit


def generate_logo_rgba(color: str, hover: bool):
    alpha_value = 0.9
    if hover:
        alpha_value = 1
    return tuple(int(color[i:i + 2], 16) for i in (0, 2, 4)) + (alpha_value,)


def count_children_projects(projects):
    for p in projects:
        p.collaborator_count = p.count_collaborators()
        p.credit_count = Credit.objects.filter(project=p).count()
        p.asset_count = p.count_assets()
    return projects


def get_twitter_pictures(users):
    user_dict = {}
    try:
        APP_KEY = os.environ.get("TWITTER_APP_KEY")
        ACCESS_TOKEN = os.environ.get("TWITTER_ACCESS_TOKEN")
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
