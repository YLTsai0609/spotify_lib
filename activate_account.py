"""
sample response : 

https://developer.spotify.com/documentation/general/guides/authorization/client-credentials/

example command : (.venv) joetsai@research-hulk:~/work/yulong/spotify_audio_feature$ python activate_account.py
"""
import requests
import os
from os.path import join as PJ
import pandas as pd
import pendulum
import click
from dotenv import load_dotenv


@click.command()
@click.option(
    "--out_folder",
    default=".access_token",
    help="the path you put your tempory access_token.",
)
def main(out_folder: str) -> None:

    load_dotenv()
    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    TOKEN_URL = "https://accounts.spotify.com/api/token"
    payload = {
        "Content-Type": "application/x-www-form-urlencoded",
        "grant_type": "client_credentials",
    }

    date: str = pendulum.now("Asia/Taipei").format("YYYYMMDD")
    timestamp: str = pendulum.now("Asia/Taipei").format("YYYYMMDD_HHmmss")
    out_filepath = PJ(out_folder, f"{date}.csv")

    resp = requests.post(TOKEN_URL, auth=(CLIENT_ID, CLIENT_SECRET), data=payload)
    access_token_log = resp.json()

    pdf = pd.DataFrame.from_dict(
        {**access_token_log, **{"date": date, "timestamp": timestamp}}, orient="index"
    ).T

    pdf.to_csv(
        out_filepath, index=False, mode="a", header=not os.path.exists(out_filepath)
    )


if __name__ == "__main__":
    main()
