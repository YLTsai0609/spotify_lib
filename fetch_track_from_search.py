"""
sample response : 

https://developer.spotify.com/documentation/general/guides/authorization/client-credentials/

example command : (.venv) joetsai@research-hulk:~/work/yulong/spotify_lib$ python fetch_token.py --data_version v2
"""

import requests
from orm.operator import _Task
from os.path import join as PJ
from urllib.parse import quote


class Task(_Task):
    def upstream(self):
        import fetch_token

        return fetch_token.Task

    def inflow(self):
        pass
        # return PJ(".access_token", "v2")

    def run(self):
        pass

    @classmethod
    def fetch(
        cls,
        endpoint: str = "https://api.spotify.com/v1/search",
        track: str = None,
        artist: str = None,
        limit: int = None,
        token_type: str = None,
        token: str = None,
    ) -> dict:

        qstring = f"query={quote(track)} {quote(artist)}&type=track&include_external=audio&offset=0&limit={str(limit)}"
        # qstring = f"query=track:{quote(track)}+atrist:{quote(artist)}&type=track&include_external=audio&offset=0&limit={str(limit)}"
        # NOTE: the doc on spotify seems to be wrong
        # we can search only the track name and artist name without add track:...+artist:...
        # ref : https://stackoverflow.com/questions/64461018/using-python-to-get-a-track-from-the-spotify-api-by-using-search-endpoint

        headers = {
            "Authorization": f"{token_type} {token}",
            "Content-Type": "application/json",
        }

        resp = requests.get(f"{endpoint}?{qstring}", headers=headers)
        return resp.json()
