import requests

_access_token = "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"
_headers = {'Authorization': "Token " + _access_token}


def get(url):
    return requests.get(url, headers=_headers).json()
