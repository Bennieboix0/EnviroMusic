# EnviroMusic
Context-aware music recommendation system using AI vision and Spotify

# 🎵 EnviroMusic

> A context-aware music recommendation system that uses AI computer vision and the Spotify API to automatically detect your environment and deliver personalised music recommendations in real time.

## 🔬 Research Question

*"Can context-aware, preference-learning music recommendation increase user satisfaction compared to standard genre-based recommendations?"*

## 🌍 How It Works

1. **📸 Camera Capture** — Takes a photo of your current environment
2. **🤖 AI Vision Analysis** — Sends the image to Claude AI which identifies your environment
3. **🎵 Spotify Recommendation** — Queries Spotify for songs matched to your environment
4. **🧠 Preference Learning** — Remembers which songs you liked and personalises future recommendations

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Spotify API + Spotipy | Music data and recommendations |
| Anthropic Claude API | Computer vision / environment detection |
| OpenCV | Camera capture |
| JSON | Preference storage and learning |

## 🌱 Supported Environments

- 📚 Studying
- 🏋️ Gym / Working out
- 😌 Relaxing
- 🚌 Commuting
- 😴 Sleeping
- 🎉 Socialising

## 📊 Research Methodology

This project forms the basis of an independent research study investigating whether AI-detected environmental context improves music recommendation satisfaction. Participants use the app across multiple sessions, rating recommendations each time. Data is analysed to determine whether personalised, context-aware recommendations score higher than standard recommendations over time.

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- Spotify Developer Account
- Anthropic API Key

### Installation

```bash
git clone https://github.com/Bennieboix0/EnviroMusic.git
cd EnviroMusic
pip3 install spotipy anthropic opencv-python
```

### Configuration
Create a `config.py` file with your credentials:
```python
CLIENT_ID = "your_spotify_client_id"
CLIENT_SECRET = "your_spotify_client_secret"
REDIRECT_URI = "http://127.0.0.1:8888/callback"
ANTHROPIC_API_KEY = "your_anthropic_api_key"
```

### Run
```bash
python3 recommender.py
```

## 👨‍💻 About

Built by Benjamin Roberts — Year 10 IB student exploring the intersection of artificial intelligence, music, and human behaviour.

*This project is part of an independent research initiative investigating context-aware recommendation systems.*
