def classification_agent(text):
    text = text.lower()

    if any(word in text for word in ["plastic", "bottle", "bag"]):
        return "plastic"
    elif any(word in text for word in ["battery", "cell", "charger"]):
        return "battery"
    elif any(word in text for word in ["food", "fruit", "leftover"]):
        return "food"
    elif any(word in text for word in ["glass", "bottle glass"]):
        return "glass"
    elif any(word in text for word in ["laptop", "phone", "e-waste", "electronics"]):
        return "e-waste"
    else:
        return "other"


def disposal_agent(category):
    data = {
        "plastic": "Recycle in dry waste bin. Avoid burning plastics.",
        "battery": "Dispose at authorized e-waste collection center.",
        "food": "Compost in organic waste bin.",
        "glass": "Send to glass recycling facility.",
        "e-waste": "Hand over to certified e-waste recycler.",
        "other": "Check local municipal guidelines."
    }
    return data.get(category, "Follow local waste rules.")


def impact_agent(category):
    data = {
        "plastic": "High pollution risk. Takes 100–500 years to decompose.",
        "battery": "Leads to toxic soil and water contamination.",
        "food": "Produces methane gas in landfills.",
        "glass": "Non-biodegradable but recyclable.",
        "e-waste": "Releases heavy metals and toxins.",
        "other": "Moderate environmental impact."
    }
    return data.get(category, "Unknown impact")


def education_agent(category):
    data = {
        "plastic": "Use reusable bags and reduce single-use plastic.",
        "battery": "Prefer rechargeable batteries.",
        "food": "Avoid food waste and compost properly.",
        "glass": "Reuse bottles before recycling.",
        "e-waste": "Recycle electronics responsibly."
    }
    return data.get(category, "Follow sustainable habits.")


def eco_score(category):
    scores = {
        "plastic": 70,
        "battery": 95,
        "food": 50,
        "glass": 40,
        "e-waste": 90,
        "other": 60
    }
    return scores.get(category, 50)
