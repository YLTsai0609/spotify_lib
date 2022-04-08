# Spotify Web API

1. [api doc](https://developer.spotify.com/documentation/web-api/reference/#/)

2. [my app dashboard](https://developer.spotify.com/dashboard/applications/24c65b22bb194a7f959900db705771c9)
  
# Installation

1. `git clone https://github.com/YLTsai0609/spotify_lib.git`
2. `cd spotify_lib`
3. `python -m venv .venv` (python 3.8)
4. `poetry install`
  
# Activation Steps

1. access token (OAuth2.0)
   - [x] login to create app, get client_id, client_secret 
   - [x] pick a OAuth flow (scope)
     - I pick `applications running on the backend, such as CLIs or daemons, the system authenticates and authorizes the app rather than a user.` 
     - send a request to spotify server to activate my app.
     - a simple versioned activation log (using csv file)
2. get access token
   - [x] create a private folder `access_token`
   - [x] python activate_account.py

## Audio Feature
 