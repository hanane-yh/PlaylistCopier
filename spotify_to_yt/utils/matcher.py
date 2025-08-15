import time
from spotify_to_yt.utils.yt_music import search_youtube_track


def match_tracks(tracks):
    """
    Matches Spotify tracks to YouTube Music using exact artist name logic.

    Args:
        tracks (list): List of dicts with 'title' and 'artist'.

    Returns:
        list: Match results with match status and YouTube info.
    """
    matches = []

    for i, track in enumerate(tracks, 1):
        title = track['title']
        artist = track['artist']
        print(f"[{i}/{len(tracks)}] Spotify: {title} - {artist}")

        try:
            yt_result = search_youtube_track(title, artist)

            if yt_result and artist.lower() in yt_result['artist'].lower():
                status = "match"
            elif yt_result:
                status = "possible"
            else:
                status = "no_match"

            matches.append({
                "spotify_title": title,
                "spotify_artist": artist,
                "yt_title": yt_result['title'] if yt_result else None,
                "yt_artist": yt_result['artist'] if yt_result else None,
                "yt_video_id": yt_result['videoId'] if yt_result else None,
                "status": status
            })

        except Exception as e:
            print(f"      Error searching: {e}")
            matches.append({
                "spotify_title": title,
                "spotify_artist": artist,
                "yt_title": None,
                "yt_artist": None,
                "yt_video_id": None,
                "status": "error",
                "error": str(e)
            })

        time.sleep(1)

    return matches
