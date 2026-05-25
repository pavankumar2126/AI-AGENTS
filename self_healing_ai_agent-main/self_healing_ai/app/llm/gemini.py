from google import genai
from ollama import chat

from app.config import GOOGLE_API_KEY


# =====================================================
# GEMINI CLIENT
# =====================================================

client = genai.Client(
    api_key=GOOGLE_API_KEY
)

MODEL_NAME = "gemini-2.5-flash-lite"


# =====================================================
# OLLAMA FALLBACK
# =====================================================

def ollama_fallback(prompt):

    response = chat(

        model="qwen2.5-coder:7b",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


# =====================================================
# MAIN LLM FUNCTION
# =====================================================

def call_gemini(prompt, image=None):

    try:

        contents = [prompt]

        if image:
            contents.append(image)

        response = client.models.generate_content(

            model=MODEL_NAME,

            contents=contents
        )

        return response.text

    # =====================================================
    # FALLBACK TO OLLAMA
    # =====================================================

    except Exception as e:

        print("\n🚨 GEMINI ERROR:\n")
        print(e)

        print("\n⚠️ SWITCHING TO OLLAMA\n")

        return ollama_fallback(prompt)