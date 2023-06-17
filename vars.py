from os import environ
import re

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

SESSION = environ.get("SESSION", "forward bot")
API_ID = int(environ.get('API_ID', '11973721'))
API_HASH = environ.get('API_HASH', '5264bf4663e9159565603522f58d3c18')
BOT_TOKEN = environ('BOT_TOKEN', '5965670031:AAE_nwYbYT9rb3y1H3xjiyVEb8Di2UpSM3c')
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", 0))
PORT = int(environ.get("PORT", "8080"))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1391556668').split()]
FILE_CAPTION = environ.get('FILE_CAPTION', '<b>{file_name}</b>')
TARGET_DB = int(environ.get("TARGET_DB", 0))
UPSTREAM_REPO = environ.get("UPSTREAM_REPO", "https://github.com/Joelkb/File-Forward-Bot")
