import sys

from setlist.user import SpotifyUser
from setlist.utils import features_to_track_ids, playlist_to_track_ids

TEST_USER = "djhopper"
TEST_PLAYLIST = "spotify:playlist:5W4m55XzK6XeayO4jBWUU4"
SORT_KEYS = ["tempo", "danceability", "energy", "key"]

if __name__ == "__main__":

    if len(sys.argv) > 1:
        if sys.argv[1] not in SORT_KEYS:
            print ("Error: sort key must be one of ", SORT_KEYS)
            sys.exit()
        else:
            sort_key = sys.argv[1]
    else:
        print ("Usage: %s sort_key" % (sys.argv[0],))
        sys.exit()

    # Authenticate and get the SpotifyUser object
    user = SpotifyUser(TEST_USER)

    # Query for playlist and split into just the track IDs
    original_playlist = user.get_playlist(TEST_PLAYLIST)
    original_tracks = playlist_to_track_ids(original_playlist)

    # Use track IDs to query for audio features
    original_features = user.get_audio_features(original_tracks)

    # Sort tracks by desired feature
    new_features = sorted(original_features, key=lambda x: x[sort_key])

    # Extract track IDs and modify exisitng playlist
    new_tracks = features_to_track_ids(new_features)
    user.set_playlist(TEST_PLAYLIST, new_tracks)
