from supabase import create_client
from config import SUPABASE_URL, SUPABASE_KEY

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


def get_memory(user_id: int):
    try:
        result = (
            supabase.table("memory")
            .select("*")
            .eq("user_id", user_id)
            .limit(1)
            .execute()
        )

        if result.data:
            return result.data[0]["memory"]

        return ""

    except Exception:
        return ""


def save_memory(user_id: int, memory: str):

    data = {
        "user_id": user_id,
        "memory": memory,
    }

    try:

        old = (
            supabase.table("memory")
            .select("*")
            .eq("user_id", user_id)
            .limit(1)
            .execute()
        )

        if old.data:

            supabase.table("memory").update(
                {"memory": memory}
            ).eq("user_id", user_id).execute()

        else:

            supabase.table("memory").insert(data).execute()

    except Exception as e:
        print(e)