import requests
import os


_access_token = os.getenv("GITHUB_TOKEN")
_headers = {'Authorization': "Token " + _access_token}


def get(url):
    return requests.get(url, headers=_headers).json()
