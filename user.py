import json
import os

import spotipy
import spotipy.util as util

CONFIG_FILE = "config.json"


class SpotifyUser(object):

    DEFAULT_SCOPES = [
        "playlist-read-collaborative",
        "playlist-modify-public",
        "playlist-read-private",
        "playlist-modify-private",
    ]

    def _get_auth_token(self):
        """
        Loads the JSON config file and authenticates with the user token flow.
        """
        with open(CONFIG_FILE) as config_file:
            config = json.load(config_file)
            for k, v in config.items():
                os.environ[k] = v
        return util.prompt_for_user_token(self.username, self.scope)

    def __init__(self, username):
        self.scope = " ".join(self.DEFAULT_SCOPES)
        self.username = username
        self.sp = spotipy.Spotify(auth=self._get_auth_token())

    def get_playlist(self, playlist_uri):
        return self.sp.user_playlist(self.username, playlist_uri)

    def set_playlist(self, playlist_uri, tracks):
        self.sp.user_playlist_replace_tracks(self.username, playlist_uri, tracks)

    def get_audio_features(self, tracks):
        return self.sp.audio_features(tracks)
