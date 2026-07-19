import google.generativeai as genai
from decouple import config

# Configure Gemini API
genai.configure(
    api_key=config("GEMINI_API_KEY")
)

# Create Gemini model
model = genai.GenerativeModel("gemini-2.0-flash")


def ask_gemini(prompt):

    print("➡️ Calling Gemini...")

    try:
        response = model.generate_content(prompt)
        print("✅ Gemini Success")
        return response.text

    except Exception as e:

        print("❌ Gemini Error:", e)

        if "429" in str(e):
            return (
                "⚠️ AI service is temporarily unavailable because the free API limit has been reached. "
                "Please wait about one minute and try again."
            )

        return f"Error: {e}"