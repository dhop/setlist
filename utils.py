def playlist_to_track_ids(playlist):
    """
    Input: a dict containing the response from sp.user_playlist
    Output: a list of track IDs
    """
    return [playlist["tracks"]["items"][i]["track"]["id"] for i in range(len(playlist))]


def features_to_track_ids(features):
    """
    Input: a dict containing the response from sp.audio_features
    Output: a list of track IDs
    """
    return [track["uri"] for track in features]
