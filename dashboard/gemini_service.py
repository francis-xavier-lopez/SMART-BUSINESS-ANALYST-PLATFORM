import google.generativeai as genai
from decouple import config

genai.configure(api_key=config("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-flash-latest")


def ask_gemini(prompt):

    print("➡️ Calling Gemini...")

    try:
        response = model.generate_content(prompt)

        print("✅ Gemini responded")

        return response.text

    except Exception as e:
        print("❌ Gemini Error:", e)
        return f"Error: {e}"