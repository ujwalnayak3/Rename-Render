# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "25953006")

API_HASH = os.environ.get("API_HASH", "d5850aeef7dd3d01fe6b698c0a0d4be8")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8586422259:AAHdRqBKzYjlSNePbik2EN9b_tS8Qc_NPVc") 

FORCE_SUB = os.environ.get("FORCE_SUB", "Kannada_Cineflix") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "kfcinemas")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://Kfcinemas:ujwal@cluster0.olxb2bz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1981280736').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
