from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", 27353035))
API_HASH = getenv("API_HASH", "cf2a75861140ceb746c7796e07cbde9e")
BOT_TOKEN = getenv("BOT_TOKEN", None)
OWNER_ID = int(getenv("OWNER_ID", "6440277281"))
MONGO_URL = getenv("MONGO_URL", None)
SUPPORT_GRP = getenv("SUPPORT_GRP", "StatusWorld_05")
UPDATE_CHNL = getenv("UPDATE_CHNL", "Heartwritez_09")
OWNER_USERNAME = getenv("OWNER_USERNAME", "MafiaXD_05")

# Random Start Images
IMG = [
    "https://telegra.ph/file/c69b9f86e2d2bb12d00f4.jpg",
]


# Random Stickers
STICKER = [
    "CAACAgUAAx0CYlaJawABBy4vZaieO6T-Ayg3mD-JP-f0yxJngIkAAv0JAALVS_FWQY7kbQSaI-geBA",

]

EMOJIOS = [
    "🤭",
    
]
