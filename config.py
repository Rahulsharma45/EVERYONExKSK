from os import getenv
from dotenv import load_dotenv

load_dotenv()

get_queue = {}


API_ID = int(getenv("API_ID", "13916313"))
API_HASH = getenv("4ced9f94162d9bbe1d3829a9fb601847")

ASS_HANDLER = list(getenv("ASS_HANDLER", ".").split())
BOT_TOKEN = getenv("5365851389:AAGihr5BvNTrbjejG9GEhUz-rfccIP7Ik6k")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "140"))
LOGGER_ID = int(getenv(""))
MONGO_DB_URI = getenv("mongodb+srv://kskop:kakujai253@cluster0.ew9p1.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
OWNER_ID = list(map(int, getenv("OWNER_ID", "2102097596").split()))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/855679eca3bca0bb1806f.jpg")
START_IMG = getenv("START_IMG")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://BGMIxCHATS")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/KSKxCHEATS")

STRING_SESSION = getenv("STRING_SESSION", None)
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
