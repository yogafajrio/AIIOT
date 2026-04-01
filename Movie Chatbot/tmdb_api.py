import requests
import os
from dotenv import load_dotenv

# Load file .env
load_dotenv()

API_KEY = "dbb2d41d4255e0cd5ec4281bde35b249"
BASE_URL = "https://api.themoviedb.org/3"

def search_movie(title):
    url = f"{BASE_URL}/search/movie"

    params = {
        "query": title,
        "api_key": API_KEY
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        results = response.json().get("results", [])

        if results:
            return results[0]

    return None


def format_movie_info(movie):
    title = movie.get("title", "Unknown Title")
    release_date = movie.get("release_date", "N/A")
    year = release_date[:4] if release_date != "N/A" else "N/A"
    rating = movie.get("vote_average", "N/A")
    overview = movie.get("overview", "No description available.")

    return f"""
🎬 **{title}** ({year})

⭐ Rating: {rating}/10

📖 {overview}
"""
