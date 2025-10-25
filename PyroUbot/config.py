import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "700"))

DEVS = list(map(int, os.getenv("DEVS", "7504137934").split()))

API_ID = int(os.getenv("API_ID", "24721040"))

API_HASH = os.getenv("API_HASH", "62acb8a14d937834bcf2fc8e45571e2f")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8252544403:AAGOCB1GMjLt9LQIeqomicN16vPbUdR7cwc")

OWNER_ID = int(os.getenv("OWNER_ID", "7504137934"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002125842026 -1002053287763 -1002044997044 -1002022625433 -1002050846285 -1002400165299 -1002416419679 -1001473548283").split()))

RMBG_API = os.getenv("RMBG_API", "a6q")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://khusususer:whoadmin98@alluserbot1.iws9dgj.mongodb.net/")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1003038185747"))
