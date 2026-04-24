from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GOOGLE_API_KEY)

def run_smart_support_agent(query: str):
    print("🔥 SMART AGENT CALLED")

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",   # ✅ WORKING MODEL
            contents=query,
        )
        return response.text

    except Exception as e:
        print("❌ ERROR:", e)
        return "⚠️ AI service error"