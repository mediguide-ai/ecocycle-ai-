import google.generativeai as genai
import os

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise Exception("GOOGLE_API_KEY not found in Streamlit Secrets")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-pro")

def classification_agent(user_input):
    prompt = f"""
    Classify waste into ONE word only:
    plastic, glass, battery, food, e-waste, metal, other.

    Input: {user_input}
    """

    response = model.generate_content(prompt)
    return response.text.strip().lower()


def disposal_agent(category):
    mapping = {
        "plastic": "Recycle in dry waste bin",
        "glass": "Send to recycling center",
        "battery": "Dispose at e-waste facility",
        "food": "Compost organic waste",
        "e-waste": "Take to certified e-waste center",
        "metal": "Send to scrap recycling"
    }
    return mapping.get(category, "Follow local waste rules")


def impact_agent(category):
    mapping = {
        "plastic": "High pollution, 500+ years to degrade",
        "battery": "Toxic chemicals harm soil and water",
        "glass": "Reusable but energy intensive",
        "food": "Produces methane in landfill",
        "e-waste": "Contains heavy metals"
    }
    return mapping.get(category, "Moderate impact")


def education_agent(category):
    mapping = {
        "plastic": "Avoid single-use plastics",
        "glass": "Reuse before recycling",
        "battery": "Use rechargeable options",
        "food": "Separate wet/dry waste",
        "e-waste": "Recycle responsibly"
    }
    return mapping.get(category, "Practice waste segregation")
