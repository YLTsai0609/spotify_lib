# Spotify Audio Feature

1. [api doc](https://developer.spotify.com/documentation/web-api/reference/#/)

2. [my app dashboard](https://developer.spotify.com/dashboard/applications/24c65b22bb194a7f959900db705771c9)
  

# Steps

1. access token (OAuth2.0)
   - [x] login to create app, get client_id, client_secret
   - [x] pick a OAuth flow (scope)
     - I pick `applications running on the backend, such as CLIs or daemons, the system authenticates and authorizes the app rather than a user.` 
     - send a request to spotify server to activate my app.
     - a simple versioned activation log (using csv file)


# Related-package

use poetry to init your project

1. [python-dotenv](https://github.com/theskumar/python-dotenv) - env variable management
2. [absl](https://github.com/abseil/abseil-py) - parser