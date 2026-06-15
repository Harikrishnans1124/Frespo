# Frespo 🎵

Frespo is a web application that seamlessly converts Spotify playlists into YouTube playlists. Users can authenticate with their Spotify and YouTube accounts, select a Spotify playlist, and automatically recreate it on YouTube without manually searching for songs.

## Features

* Spotify OAuth Authentication
* YouTube OAuth Authentication
* Fetch Spotify playlists
* Match Spotify tracks with YouTube videos
* Create YouTube playlists automatically
* User-friendly web interface
* Fast and efficient playlist migration

## Tech Stack

### Backend

* FastAPI
* Python

### Database

* PostgreSQL

### Frontend

* HTML
* CSS
* JavaScript

### APIs

* Spotify Web API
* YouTube Data API v3

## Project Structure

```text
Frespo/
│
├── app.py
├── db.py
├── playlist_create.py
├── songs_insert.py
├── youtube_auth.py
├── requirements.txt
│
├── static/
│   ├── css/
│   └── js/
│
└── templates/
    ├── index.html
    ├── processing.html
    ├── success.html
    ├── error.html
    └── guide.html
```

## Installation

1. Clone the repository

```bash
git clone https://github.com/Harikrishnans1124/Frespo.git
cd Frespo
```

2. Create a virtual environment

```bash
python -m venv .venv
```

3. Activate the virtual environment

Windows:

```bash
.venv\Scripts\activate
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

5. Configure Spotify and Google API credentials.

6. Run the application

```bash
uvicorn app:app --reload
```

7. Open your browser

```text
http://localhost:8000
```

## How It Works

1. Sign in with Spotify.
2. Select a Spotify playlist.
3. Frespo retrieves playlist tracks.
4. Songs are matched with YouTube videos.
5. A new YouTube playlist is automatically created.
6. The matched songs are added to the playlist.

## Future Improvements

* Improved song matching accuracy
* User accounts and playlist history
* Bulk playlist migration
* Analytics dashboard
* Playlist synchronization

## Author

Harikrishnan S

---

Made with ❤️ using FastAPI, Spotify API, and YouTube Data API.
