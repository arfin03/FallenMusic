from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/8e35496377e93a723c418.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/de78daf84b6e6c4653279.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/gcanimecommunity")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/origanimeinfo")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5843270062").split()))


FAILED = "https://telegra.ph/file/7d603abd5450fe81610d3.jpg"
