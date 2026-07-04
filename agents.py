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
        "plastic": "Recycle in proper bin",
        "e-waste": "Dispose at certified e-waste center",
        "food": "Compost organic waste",
        "glass": "Send to recycling plant",
        "general": "Follow municipal rules"
    }.get(cat, "")


def impact_agent(cat):
    return {
        "plastic": "High pollution, long decomposition time",
        "e-waste": "Toxic metals contaminate soil",
        "food": "Methane emissions in landfill",
        "glass": "Energy intensive recycling"
    }.get(cat, "")


def education_agent(cat):
    return {
        "plastic": "Use reusable alternatives",
        "e-waste": "Recycle electronics responsibly",
        "food": "Reduce food waste",
        "glass": "Reuse containers"
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
        "prediction": "Waste increasing 8% monthly"
    }
