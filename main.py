import os
from supabase import create_client, Client

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

# fetching 

response = (
    supabase.table("planets")
    .select("*")
    .execute()
)

# inserting
response = (
    supabase.table("planets")
    .insert({"id": 1, "name": "Pluto"})
    .execute()
)

# updating
response = (
    supabase.table("instruments")
    .update({"name": "piano"})
    .eq("id", 1)
    .execute()
)
#upserting
response = (
    supabase.table("instruments")
    .upsert({"id": 1, "name": "piano"})
    .execute()
)


# deleting
response = (
    supabase.table("instruments")
    .delete()
    .eq("id", 1)
    .execute()
)


