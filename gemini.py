from google import genai
from google.genai import types

from config import GEMINI_API_KEY, MODEL

client = genai.Client(api_key=GEMINI_API_KEY)

SYSTEM_PROMPT = """
তোমার নাম Maya (মায়া) 🌸।

নিয়ম:

- শুধু Maya বা মায়া লিখলে উত্তর দেবে।
- নাম না থাকলে উত্তর দেবে না।
- বাংলা লিখলে বাংলায়।
- English লিখলে English।
- সর্বোচ্চ ১০ লাইনের উত্তর।
- ভদ্র, চতুর, রসিক, বন্ধুসুলভ।
- হালকা রোমান্টিক কিন্তু সম্মানজনক।
- Protect Scam গ্রুপের নিয়ম মেনে চলবে।
- কোনো তথ্য নিশ্চিত না হলে বানিয়ে বলবে না।
"""

def ask_gemini(message: str, memory: str = ""):

    prompt = f"""
Memory:
{memory}

User:
{message}
"""

    response = client.models.generate_content(
        model=MODEL,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            temperature=0.8,
            max_output_tokens=400,
        ),
        contents=prompt,
    )

    return response.text.strip()