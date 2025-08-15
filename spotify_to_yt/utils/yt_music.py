from ytmusicapi import YTMusic

yt = YTMusic("headers_auth.json")


def search_youtube_track(title, artist):
    query = f"{title} {artist}"
    results = yt.search(query, filter="songs")

    if not results:
        return None

    # Grab the first result (best match)
    top_result = results[0]
    return {
        'videoId': top_result['videoId'],
        'title': top_result['title'],
        'artist': top_result['artists'][0]['name']
    }
