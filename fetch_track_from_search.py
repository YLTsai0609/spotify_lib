"""
sample response : 

https://developer.spotify.com/documentation/general/guides/authorization/client-credentials/

example command : (.venv) joetsai@research-hulk:~/work/yulong/spotify_lib$ python fetch_token.py --data_version v2
"""

import requests
from orm.operator import _Task
from os.path import join as PJ
from urllib.parse import quote


# Inflow - csv
# track artist

# Outflow - csv
# orm


class Task(_Task):
    def upstream(self):
        import fetch_token

        return fetch_token.Task

    def inflow(self):
        return PJ(".access_token", "v2")

    def run(self):
        pass

    @classmethod
    def fetch(
        cls,
        endpoint: str = "https://api.spotify.com/v1/search",
        track: str = None,
        atrist: str = None,
        token: str = None,
    ):
        params = dict(
            q=f"track:{quote(track)}+atrist:{quote(atrist)}",
            type="track",
            limit=1,
        )
        headers = dict(Authorization=f"Bearer {token}")

        resp = requests.get(endpoint, params=params, headers=headers)
        return resp.json()
