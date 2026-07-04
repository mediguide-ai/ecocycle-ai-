def classification_agent(text):
    text = text.lower()

    if "plastic" in text:
        return "plastic"
    if "battery" in text:
        return "e-waste"
    if "food" in text:
        return "food"
    if "glass" in text:
        return "glass"
    return "general"


def disposal_agent(cat):
    return {
        "plastic": "Recycle properly",
        "e-waste": "Dispose at e-waste center",
        "food": "Compost it",
        "glass": "Send to recycling plant",
        "general": "Follow local rules"
    }.get(cat, "")


def impact_agent(cat):
    return {
        "plastic": "High pollution impact",
        "e-waste": "Toxic metals risk",
        "food": "Methane emissions",
        "glass": "Energy consumption"
    }.get(cat, "")


def education_agent(cat):
    return {
        "plastic": "Avoid single-use plastic",
        "e-waste": "Recycle electronics",
        "food": "Reduce waste",
        "glass": "Reuse items"
    }.get(cat, "")


def eco_score(cat):
    return {
        "plastic": 60,
        "e-waste": 90,
        "food": 40,
        "glass": 50,
        "general": 55
    }.get(cat, 50)


def user_level(score):
    if score >= 80:
        return "Eco Champion"
    elif score >= 60:
        return "Responsible Citizen"
    return "Beginner"


def city_simulator():
    return {
        "daily_waste": "120 Tons",
        "recycling_rate": "42%",
        "co2_impact": "High",
        "prediction": "Waste rising 8% monthly"
    }
