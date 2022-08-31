from personal_data import refreshed_token, base_64

import requests

import json


class Refresh:

    def __init__(self):

        # Initializing variables from personal_data referencing refresh token and client_id:client_secret encoded in base 64

        self.refreshed_token = refreshed_token

        self.base_64 = base_64

    def refresh(self):

        query = "https://accounts.spotify.com/api/token"

        resp = requests.post(query,
                                 data={"grant_type": "refresh_token",
                                       "refresh_token": refreshed_token},
                                 headers={"Authorization": "Basic " + base_64})

        resp_json = resp.json()

        print(resp_json)

        return resp_json["access_token"]


r = Refresh()

r.refresh()