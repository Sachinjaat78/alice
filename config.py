import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 22336203
API_HASH = "a4a1652608b46bb6890ef05d2bed44f0"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7758506642:AAEmmfxq6rmN4TTZl0o1Pt33SbOmiTCIai8"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://Sachin:Sachin@cluster0.07s3s.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = -4668945198

# Get this value from @ultron2_robot on Telegram by /id
OWNER_ID = 7111568434

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/rishabhops/alice",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = "https://t.me/Sachinjaat78"
SUPPORT_GROUP = "https://t.me/Sachinjaat78"

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = "BQFU0ssAosV-QwOLZalDswKjn06PQAJQdpSIGW45nKG2F3uvfDn1sGso3YVymGhVBumIL773CRlvtTPoGER-JZFtV2RZfoYBl8SYYtsS22gFjLNUu0CZM5Q21El775KbYZ7kIMs6y0XnASgnhHk9_q7t3YlMwcNK3XUi05MTFlBFgCgJKfenGH4p4YkSzcLoDosx0Dxcc7WRexEqyNAvXFvzFQAG6oU8W0S3JXRNUNiUJP1sRARru5EIkqqQlmIZe2-aOX0Uvzen0RyWDdRtVBwHY_SdqnMYz1Gy6utLR-E9UhCTo827gGjlB1jplzK1uhNSwNIqqA_rTpuHQID6pfTnXxyWKwAAAAGn4ewyAA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = "https://graph.org/file/895237e1a7d9a1793b0bf-b5ef92e46b92d1bf2f.jpg"

PING_IMG_URL = "https://graph.org/file/895237e1a7d9a1793b0bf-b5ef92e46b92d1bf2f.jpg"

PLAYLIST_IMG_URL = "https://graph.org/file/895237e1a7d9a1793b0bf-b5ef92e46b92d1bf2f.jpg"
STATS_IMG_URL = "https://graph.org/file/895237e1a7d9a1793b0bf-b5ef92e46b92d1bf2f.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/895237e1a7d9a1793b0bf-b5ef92e46b92d1bf2f.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/895237e1a7d9a1793b0bf-b5ef92e46b92d1bf2f.jpg"
STREAM_IMG_URL = "https://graph.org/file/895237e1a7d9a1793b0bf-b5ef92e46b92d1bf2f.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/895237e1a7d9a1793b0bf-b5ef92e46b92d1bf2f.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/895237e1a7d9a1793b0bf-b5ef92e46b92d1bf2f.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/895237e1a7d9a1793b0bf-b5ef92e46b92d1bf2f.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/895237e1a7d9a1793b0bf-b5ef92e46b92d1bf2f.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/895237e1a7d9a1793b0bf-b5ef92e46b92d1bf2f.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
