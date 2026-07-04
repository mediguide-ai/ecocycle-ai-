def classification_agent(text):
    text = text.lower()

    if "plastic" in text or "bottle" in text:
        return "plastic"
    if "battery" in text or "phone" in text:
        return "e-waste"
    if "food" in text:
        return "food"
    if "glass" in text:
        return "glass"
    return "general"


def disposal_agent(cat):
    return {
        "plastic": "Recycle in plastic recovery units",
        "e-waste": "Send to certified e-waste facility",
        "food": "Compost organic waste",
        "glass": "Recycle glass material",
        "general": "Follow municipal waste guidelines"
    }.get(cat, "")


def impact_agent(cat):
    return {
        "plastic": "Long-term ocean pollution risk",
        "e-waste": "Toxic heavy metal leakage",
        "food": "Methane emission in landfills",
        "glass": "High energy recycling cost"
    }.get(cat, "")


def education_agent(cat):
    return {
        "plastic": "Switch to reusable materials",
        "e-waste": "Recycle electronics responsibly",
        "food": "Reduce food wastage",
        "glass": "Reuse containers"
    }.get(cat, "")


def eco_score(cat):
    return {
        "plastic": 55,
        "e-waste": 85,
        "food": 45,
        "glass": 60,
        "general": 50
    }.get(cat, 50)


def user_level(score):
    if score >= 80:
        return "🌟 Eco Master"
    elif score >= 60:
        return "🌿 Responsible User"
    return "🌱 Beginner"


def city_simulator():
    return {
        "daily_waste": "135 Tons",
        "recycling_rate": "48%",
        "co2_impact": "Medium",
        "prediction": "Waste growth stabilizing due to recycling policies"
    }
