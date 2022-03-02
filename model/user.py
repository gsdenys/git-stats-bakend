from .connector import get

_user_columns = (
    "name",
    "login",
    "email",
    "twitter_username",
    "public_repos",
    "public_gists",
    "created_at",
    "updated_at",
    "bio",
    "html_url"
)


def _parse_user_data(user_json):
    user = {}

    for key in _user_columns:
        user[key] = user_json[key]

    return user


def _get_user_data(login):
    url = f"https://api.github.com/users/{login}"
    user_json = get(url)

    return user_json


def get_user_info(login):
    user_json = _get_user_data(login)
    user_info = _parse_user_data(user_json)

    return user_info
