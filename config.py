from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", 20617772))
API_HASH = getenv("API_HASH", "eb464a3d12219bbfbbbf2d4deb3b3151")
BOT_TOKEN = getenv("BOT_TOKEN", None)
OWNER_ID = int(getenv("OWNER_ID", "6527727109"))
MONGO_URL = getenv("MONGO_URL", None)
SUPPORT_GRP = getenv("SUPPORT_GRP", "DilwaleHaven")
UPDATE_CHNL = getenv("UPDATE_CHNL", "DugguWorld")
OWNER_USERNAME = getenv("OWNER_USERNAME", "imceobitxh")

# Random Start Images
IMG = [
    "https://graph.org/file/2c30aed72f9553fcedbfa.jpg",
]


# Random Stickers
STICKER = [
    "CAACAgUAAx0CYlaJawABBy4vZaieO6T-Ayg3mD-JP-f0yxJngIkAAv0JAALVS_FWQY7kbQSaI-geBA",

]

EMOJIOS = [
    "🤭",
    
]
