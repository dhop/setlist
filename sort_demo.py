from user import SpotifyUser
from utils import features_to_track_ids, playlist_to_track_ids

TEST_USER = "djhopper"
TEST_PLAYLIST = "spotify:playlist:5W4m55XzK6XeayO4jBWUU4"
TEST_SORT_KEY = "tempo"

if __name__ == "__main__":

    # Authenticate and get the SpotifyUser object
    user = SpotifyUser("djhopper")

    # Query for playlist and split into just the track IDs
    original_playlist = user.get_playlist(TEST_PLAYLIST)
    original_tracks = playlist_to_track_ids(original_playlist)

    # Use track IDs to query for audio features
    original_features = user.get_audio_features(original_tracks)

    # Sort tracks by desired feature
    new_features = sorted(original_features, key=lambda x: x[TEST_SORT_KEY])

    # Extract track IDs and modify exisitng playlist
    new_tracks = features_to_track_ids(new_features)
    user.set_playlist(TEST_PLAYLIST, new_tracks)
