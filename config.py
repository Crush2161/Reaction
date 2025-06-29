from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = "27139681"
# -------------------------------------------------------------
API_HASH = "476018a0d8c7bce26eff25dd6f93b951"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", None)
MONGO_URL = getenv("MONGO_URL", None)
OWNER_ID = int(getenv("OWNER_ID", "2047173815"))
SUPPORT_GRP = "https://t.me/+Rv1BIrd2MsgxMWVl"
UPDATE_CHNL = "CRUSH_FOREVER"
OWNER_USERNAME = "FOREVER_CRUSH"
