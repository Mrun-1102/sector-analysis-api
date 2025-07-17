import os
import httpx
from dotenv import load_dotenv

# Loading environment variable
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  # ✅ Ensure it's set

async def analyze_with_gemini(prompt: str) -> str:
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent" 
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [{"parts": [{"text": prompt}]}]
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{url}?key={GEMINI_API_KEY}",  # ✅ Used actual key from .env
                json=payload,
                headers=headers,
                timeout=30
            )
            response.raise_for_status()
            response_json = response.json()
            return response_json["candidates"][0]["content"]["parts"][0]["text"]

    except httpx.HTTPStatusError as http_err:
        print("=== Gemini API HTTP Error ===")
        print(f"Status Code: {http_err.response.status_code}")
        print("Response content:")
        print(http_err.response.text)  
        raise Exception(f"Gemini API Error: {http_err.response.text}")

    except Exception as e:
        print("=== Gemini API General Exception ===")
        print(str(e))
        raise Exception(f"Gemini API General Error: {str(e)}")
