import json

data = {
    "plastic": {
        "disposal": "Put in dry waste / recycling bin",
        "impact": "Reduces landfill waste and pollution",
        "tip": "Avoid single-use plastic items"
    },
    "glass": {
        "disposal": "Recycle in glass bin",
        "impact": "Glass can be recycled many times",
        "tip": "Do not mix with ceramics"
    },
    "battery": {
        "disposal": "Take to e-waste collection center",
        "impact": "Prevents toxic soil contamination",
        "tip": "Never throw batteries in trash"
    },
    "food": {
        "disposal": "Compost organic waste",
        "impact": "Reduces methane emissions",
        "tip": "Separate wet and dry waste"
    }
}

def classification_agent(text):
    text = text.lower()
    for key in data:
        if key in text:
            return key
    return "unknown"

def disposal_agent(category):
    return data.get(category, {}).get("disposal", "No info")

def impact_agent(category):
    return data.get(category, {}).get("impact", "No info")

def education_agent(category):
    return data.get(category, {}).get("tip", "Segregate waste properly")
