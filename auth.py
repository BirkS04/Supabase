import os
import dotenv
dotenv.load_dotenv()

from supabase import create_client, Client

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

email = "birkscheben@gmail.com"
password = "hallo"
response = supabase.auth.sign_up(
    {
        "email": "birkscheben@gmail.com", 
        "password": "hallo1234",
    }
)
