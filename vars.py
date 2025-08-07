# Rajesh R Mahar
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os

API_ID    = os.environ.get("API_ID", "22470912")
API_HASH  = os.environ.get("API_HASH", "511be78079ed5d4bd4c967bc7b5ee023")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
OWNER = os.environ.get("OWNER", "7678862761")
AUTH_USER = os.environ.get("AUTH_USERS", "7678862761 , "7678862778").split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
