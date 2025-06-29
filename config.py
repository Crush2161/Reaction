from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", None))
# -------------------------------------------------------------
BOT_TOKEN = getenv("API_HASH", None)
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", None)
MONGO_URL = getenv("MONGO_URL", None)
OWNER_ID = int(getenv("OWNER_ID", "2047173815"))
SUPPORT_GRP = "https://t.me/+Rv1BIrd2MsgxMWVl"
UPDATE_CHNL = "CRUSH_FOREVER"
OWNER_USERNAME = "FOREVER_CRUSH"
    
