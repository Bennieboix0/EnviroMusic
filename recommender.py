import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI
import json
import os
from camera import capture_and_analyse

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope="user-top-read"
))

PREFS_FILE = "preferences.json"

def load_preferences():
    if os.path.exists(PREFS_FILE):
        with open(PREFS_FILE, "r") as f:
            return json.load(f)
    return {}

def save_preferences(prefs):
    with open(PREFS_FILE, "w") as f:
        json.dump(prefs, f, indent=2)

environments = {
    "Studying":   {"query": "lofi study beats"},
    "Gym":        {"query": "high energy workout hip hop"},
    "Relaxing":   {"query": "chill relaxing acoustic"},
    "Commuting":  {"query": "pop commute playlist"},
    "Sleeping":   {"query": "sleep ambient calm"},
    "Socialising":{"query": "party social pop hits"},
}

print("\n🎵 Welcome to EnviroMusic!\n")
print("How would you like to detect your environment?")
print("1. 📸 Use camera (AI detection)")
print("2. ⌨️  Enter manually")

mode = input("\nEnter 1 or 2: ").strip()

if mode == "1":
    env_name = capture_and_analyse()
    if not env_name:
        print("Camera failed, switching to manual...")
        mode = "2"

if mode == "2":
    print("\nWhat environment are you in?")
    env_list = list(environments.keys())
    for i, name in enumerate(env_list):
        print(f"{i+1}. {name}")
    choice = input("\nEnter a number: ").strip()
    env_name = env_list[int(choice) - 1]

# Match detected environment to our list
if env_name not in environments:
    print(f"Environment '{env_name}' not recognised, defaulting to Relaxing")
    env_name = "Relaxing"

print(f"\n🌍 Environment: {env_name}")

# Load preferences
prefs = load_preferences()
liked_artists = prefs.get(env_name, {}).get("liked_artists", [])

if liked_artists:
    query = f"{environments[env_name]['query']} artist:{liked_artists[0]}"
    print("(Personalising based on your preferences...)\n")
else:
    query = environments[env_name]["query"]

results = sp.search(q=query, type="track", limit=5)
tracks = results["tracks"]["items"]

print("🎵 Recommended Songs:\n")
for i, track in enumerate(tracks):
    print(f"  {i+1}. {track['name']} — {track['artists'][0]['name']}")

# Rate recommendations
print("\nWhich songs did you like? (enter numbers separated by commas, or press Enter to skip)")
liked_input = input("e.g. 1,3: ").strip()

if liked_input:
    liked_indices = [int(x.strip()) - 1 for x in liked_input.split(",") if x.strip().isdigit()]

    if env_name not in prefs:
        prefs[env_name] = {"liked_artists": [], "liked_songs": []}

    for i in liked_indices:
        if 0 <= i < len(tracks):
            track = tracks[i]
            artist = track["artists"][0]["name"]
            song = track["name"]

            if artist not in prefs[env_name]["liked_artists"]:
                prefs[env_name]["liked_artists"].append(artist)
            if song not in prefs[env_name]["liked_songs"]:
                prefs[env_name]["liked_songs"].append(song)

            print(f"  ✅ Saved: {song} — {artist}")

    save_preferences(prefs)
    print("\n✨ Preferences saved! Next time you'll get personalised recommendations.")

print("\nEnjoy your music! 🎵")