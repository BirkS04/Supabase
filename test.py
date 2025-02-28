import os
import dotenv
dotenv.load_dotenv()

from supabase import create_client, Client

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

print(url, key)