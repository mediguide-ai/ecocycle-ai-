import os
from google import genai
model="gemini-pro"
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise Exception("GOOGLE_API_KEY missing")

client = genai.Client(api_key=api_key)


def classification_agent(user_input):

    prompt = f"""
    Classify waste into one word:
    plastic, glass, battery, food, e-waste, metal, other.

    Input: {user_input}
    """

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt
    )

    return response.text.strip().lower()


def disposal_agent(category):
    mapping = {
        "plastic": "Recycle in dry waste bin",
        "glass": "Send to recycling center",
        "battery": "Dispose at e-waste facility",
        "food": "Compost organic waste",
        "e-waste": "Use certified recycling center",
        "metal": "Send to scrap recycling"
    }
    return mapping.get(category, "Follow waste rules")


def impact_agent(category):
    mapping = {
        "plastic": "High pollution, long decomposition time",
        "battery": "Toxic to soil and water",
        "glass": "Energy intensive recycling",
        "food": "Produces methane in landfill",
        "e-waste": "Contains heavy metals"
    }
    return mapping.get(category, "Moderate impact")


def education_agent(category):
    mapping = {
        "plastic": "Avoid single-use plastics",
        "glass": "Reuse items when possible",
        "battery": "Use rechargeable batteries",
        "food": "Separate wet waste",
        "e-waste": "Recycle responsibly"
    }
    return mapping.get(category, "Follow proper segregation")
