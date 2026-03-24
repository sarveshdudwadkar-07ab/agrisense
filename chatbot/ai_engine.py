from groq import Groq
from decouple import config


def farming_ai(question, image=None):

    try:
        client = Groq(api_key=config("GROQ_API_KEY"))

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": """
You are AgriSense AI — a smart farming assistant.

Always respond in this format:

🌱 Answer:
[Simple explanation]

📌 Recommendations:
- Point 1
- Point 2
- Point 3

⚠️ Tips:
- Short practical tips

Rules:
- Keep language simple
- Focus on Indian farming
- Be practical, not theoretical
"""
                },
                {
                    "role": "user",
                    "content": f"""
Farmer question: {question}

Image uploaded: {"Yes" if image else "No"}

If image is present, assume plant disease and give possible causes and solutions.
"""
                }
            ],
            temperature=0.5
        )

        answer = response.choices[0].message.content.strip()
        return answer

    except Exception as e:
        print("GROQ ERROR:", e)
        return "⚠️ AI assistant is temporarily unavailable. Please try again."