import os
import spotipy
from dotenv import load_dotenv
from spotipy import SpotifyOAuth

load_dotenv()


def get_spotify_client():
    scope = "playlist-read-private playlist-read-collaborative"
    sp_oauth = SpotifyOAuth(
        client_id=os.getenv("SPOTIFY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
        redirect_uri=os.getenv("SPOTIFY_REDIRECT_URI"),
        scope=scope
    )
    return spotipy.Spotify(auth_manager=sp_oauth)


def get_user_playlists(sp):
    playlists = sp.current_user_playlists()
    result = []
    for item in playlists['items']:
        result.append({
            'name': item['name'],
            'id': item['id']
        })
    return result


def get_playlist_tracks(sp, playlist_id):
    tracks = []
    results = sp.playlist_tracks(playlist_id)
    while results:
        for item in results['items']:
            track = item['track']
            if track:
                tracks.append({
                    'title': track['name'],
                    'artist': track['artists'][0]['name']
                })
        if results['next']:
            results = sp.next(results)
        else:
            results = None
    return tracks