def classification_agent(text):
    text = text.lower()

    if "plastic" in text or "bottle" in text:
        return "plastic"
    elif "battery" in text or "phone" in text:
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
        "e-waste": "Dispose at certified e-waste center",
        "food": "Compost organic waste",
        "glass": "Send to glass recycling plant",
        "general": "Follow municipal waste rules"
    }.get(cat, "No data")


def impact_agent(cat):
    return {
        "plastic": "High pollution and long decomposition time",
        "e-waste": "Toxic metals contaminate soil and water",
        "food": "Produces methane in landfills",
        "glass": "Energy intensive recycling"
    }.get(cat, "No data")


def education_agent(cat):
    return {
        "plastic": "Use reusable alternatives",
        "e-waste": "Recycle electronics responsibly",
        "food": "Reduce food waste",
        "glass": "Reuse containers"
    }.get(cat, "No data")


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
        "prediction": "Waste will increase by 8% in next 30 days"
    }
