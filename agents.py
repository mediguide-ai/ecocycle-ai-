import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def classification_agent(user_input):

    prompt = f"""
    Classify this waste into one word:
    plastic, glass, battery, food, e-waste, metal, other.

    Waste: {user_input}
    """

    try:
        response = model.generate_content(prompt)
        return response.text.strip().lower()
    except:
        return "unknown"

def disposal_agent(category):
    data = {
        "plastic": "Recycle in dry waste bin",
        "glass": "Send to glass recycling center",
        "battery": "Dispose at e-waste facility",
        "food": "Compost organic waste",
        "e-waste": "Take to authorized center"
    }
    return data.get(category, "Check local rules")

def impact_agent(category):
    data = {
        "plastic": "Takes hundreds of years to decompose",
        "battery": "Highly toxic to soil and water",
        "glass": "Reusable but energy intensive",
        "food": "Produces methane if dumped",
        "e-waste": "Contains heavy metals"
    }
    return data.get(category, "Moderate environmental impact")

def education_agent(category):
    data = {
        "plastic": "Avoid single-use plastic",
        "battery": "Use rechargeable batteries",
        "food": "Segregate wet waste",
        "glass": "Reuse before recycling",
        "e-waste": "Recycle responsibly"
    }
    return data.get(category, "Follow proper waste segregation")
def education_agent(category):
    return data.get(category, {}).get("tip", "Segregate waste properly")
