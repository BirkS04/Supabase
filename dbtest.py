import os
import dotenv
dotenv.load_dotenv()

from supabase import create_client, Client

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

response = (
    supabase.table("users")
    .insert({"email": "irkscheben@gmail.com", "password": "hallo"})
    .execute()
)
print(response)

# print(url, key)
