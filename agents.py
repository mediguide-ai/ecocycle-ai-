def classification_agent(text):
    text = text.lower()

    if "plastic" in text:
        return "plastic"
    elif "battery" in text:
        return "e-waste"
    elif "food" in text:
        return "food"
    elif "glass" in text:
        return "glass"
    else:
        return "general"


def disposal_agent(cat):
    return {
        "plastic": "Recycle in plastic waste bin",
        "e-waste": "Dispose at e-waste center",
        "food": "Compost organic waste",
        "glass": "Recycle glass properly",
        "general": "Follow municipal waste rules"
    }.get(cat, "")


def impact_agent(cat):
    return {
        "plastic": "High pollution, long degradation time",
        "e-waste": "Releases toxic metals",
        "food": "Produces methane in landfill",
        "glass": "Energy intensive recycling"
    }.get(cat, "")


def education_agent(cat):
    return {
        "plastic": "Use reusable bags",
        "e-waste": "Recycle electronics responsibly",
        "food": "Avoid food waste",
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
    else:
        return "Beginner"


def city_simulator():
    return {
        "daily_waste": "120 Tons",
        "recycling_rate": "42%",
        "co2_impact": "High",
        "prediction": "Waste increasing 8% monthly"
    }
