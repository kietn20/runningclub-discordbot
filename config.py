import os 
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = '!'
DATABASE_NAME = 'running_club.db'

