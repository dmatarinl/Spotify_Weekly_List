import json
import requests
from personal_data import spotify_myuser, id_weekly_spotify

from datetime import date
from new_token import Refresh

# Creation of the class and variables
class SongSaver:

    def __init__(self):

        self.user_id = spotify_myuser

        self.token_from_Spotify = ""

        self.id_weekly_spotify = id_weekly_spotify

        self.songs = ""

        self.My_Playlist = ""

    # This function will repeat through playlist songs, adding them to the list
    def SongSearcher(self):

        print("Searching for the songs in discover weekly...")
        

        query = "https://api.spotify.com/v1/playlists/{}/tracks".format(id_weekly_spotify)

        resp = requests.get(query, headers={"Content-Type": "application/json",
                                         "Authorization": "Bearer {}".format(self.token_from_Spotify)})

        resp_json = resp.json()

        print(resp)

        for i in resp_json["items"]:

            self.songs += (i["track"]["uri"] + ",")

        self.songs = self.songs[:-1]

        self.AddSongs()
    
    # Function that will create our new list
    def PlaylistCreation(self):
        
        print("Creating a new playlist")

        Current_date = date.today()

        FormattedDate = Current_date.strftime("%d/%m/%Y")

        query = "https://api.spotify.com/v1/users/{}/playlists".format(spotify_myuser)

        req_body = json.dumps({"name": FormattedDate + " Weekly Discover", "description": "Discover weekly list was saved", "public": True})

        resp = requests.post(query, data=req_body, headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(self.token_from_Spotify)
        })

        resp_json = resp.json()

        return resp_json["id"]

    # Simple function that will add songs in our playlist with the correct format
    def AddSongs(self):

        print("Please wait while we are adding the songs")

        self.My_Playlist = self.PlaylistCreation()

        query = "https://api.spotify.com/v1/playlists/{}/tracks?uris={}".format(
            self.My_Playlist, self.songs)

        requests.post(query, headers={"Content-Type": "application/json",
                                                 "Authorization": "Bearer {}".format(self.token_from_Spotify)})

        print ("Your Weekly Playlist is created successfully ")

    # This function will call the Refresh function from new_token and start the search for songs
    def Refresh_Token(self):

        print("We are refreshing the token")

        refresh_func = Refresh()

        self.token_from_Spotify = refresh_func.refresh()

        self.SongSearcher()


s = SongSaver()

s.Refresh_Token()