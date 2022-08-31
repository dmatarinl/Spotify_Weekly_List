# Using authorization from spotify developers:
# Spotify for developers, console, create token with public and private inputs
# This link will guide you through all the process https://developer.spotify.com/documentation/general/guides/authorization/

# The name of your account
spotify_myuser= ""

# You have to copy a similar part of the link of the weekly spotify songs recommended for you
id_weekly_spotify = ""


# When you put every step together and call the function in your cmd, it will appear a section called refresh token
refreshed_token = ""
# Explanation STEP BY STEP:
# To obtain refreshed token you will call a function using curl, and example will be:
# curl -H "Authorization: Basic Zos...sdfjo" -d grant_type=authorization_code -d code=MSDF4e.....5K6N -d redirect_uri=https%3A%2F%2Fgithub.com%2Fdmatarinl https://accounts.spotify.com/api/token

# curl -H "Authorization: Basic example=" -> example will be client_id:client_secret encoded in base 64
# client_id and client_secret is provided by spotify developer page when you register yourself to make and app

# Request body parameter, and thats how we need it to obtain the authorization
# -d grant_type=authorization_code 

# the code= part is obtained by a GET request sent to the /authorize endpoint of the accounts service
# GET https://accounts.spotify.com/authorize?client_id=YOURCLIENT_ID&response_type=code&redirect_uri=YOUR_REDIRECTED_URL_ENCODED&scope=playlist-modified-public%20playlist-modified-private
# When you enter this get request in your browser, it will appear the page you set as the redirection page after the authorization page, 
# The link you have to copy is the link it appears after code=
# -d code=example

# A url encoded by your choice to make the redirection possible -> https%3A%2F%2Fgithub.com%2Fdmatarinl
# -d redirect_uri=https%3A%2F%2Fgithub.com%2Fdmatarinl https://accounts.spotify.com/api/token


# client_id:client_secret encoded in base 64
base_64 =  ""
