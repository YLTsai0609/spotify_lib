"""
sample response : 

https://developer.spotify.com/documentation/general/guides/authorization/client-credentials/

example command : (.venv) joetsai@research-hulk:~/work/yulong/spotify_lib$ python fetch_token.py
"""
import requests
import os
from os.path import join as PJ
import pandas as pd
import pendulum
from typing import Union
from dotenv import load_dotenv
from orm.operator import _Task


class Task(_Task):
    @property
    def inflow(self) -> None:
        return

    @property
    def upstream(self) -> None:
        return

    @property
    def outflow(self) -> str:
        return PJ(".access_token", "v2")

    def run(self, save: bool = True) -> Union[str, pd.DataFrame]:

        load_dotenv()
        token_log = self.fetch(
            client_id=os.getenv("CLIENT_ID"), client_secret=os.getenv("CLIENT_SECRET")
        )

        now: pendulum.datetime.DateTime = pendulum.now("Asia/Taipei")
        date: str = now.format("YYYYMMDD")
        timestamp: str = now.format("YYYYMMDD_HHmmss")
        expire_at: int = now.add(hours=1).int_timestamp
        out_filepath: str = PJ(self.outflow, f"{date}.csv")

        pdf = pd.DataFrame.from_dict(
            {
                **token_log,
                **{"date": date, "timestamp": timestamp, "expire_at": expire_at},
            },
            orient="index",
        ).T

        if save:
            pdf.to_csv(
                out_filepath,
                index=False,
                mode="a",
                header=not os.path.exists(out_filepath),
            )
        else:
            return pdf

    @classmethod
    def fetch(
        cls,
        endpoint: str = "https://accounts.spotify.com/api/token",
        client_id: str = None,
        client_secret: str = None,
    ) -> dict:
        payload = {
            "Content-Type": "application/x-www-form-urlencoded",
            "grant_type": "client_credentials",
        }
        # print(client_id, client_secret)
        resp = requests.post(endpoint, auth=(client_id, client_secret), data=payload)
        return resp.json()


if __name__ == "__main__":
    t = Task()
    t.run()
