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
        "plastic": "Recycle in industrial plastic recovery system",
        "e-waste": "Send to certified e-waste facility",
        "food": "Compost or bio-waste processing",
        "glass": "Recycle into new glass products",
        "general": "Follow municipal waste segregation rules"
    }.get(cat, "")


def impact_agent(cat):
    return {
        "plastic": "Ocean pollution, microplastic generation",
        "e-waste": "Heavy metal contamination",
        "food": "Methane emission from landfill",
        "glass": "High energy recycling cost"
    }.get(cat, "")


def education_agent(cat):
    return {
        "plastic": "Use reusable alternatives",
        "e-waste": "Recycle electronics properly",
        "food": "Reduce food waste habits",
        "glass": "Reuse containers when possible"
    }.get(cat, "")


def eco_score(cat):
    return {
        "plastic": 50,
        "e-waste": 85,
        "food": 45,
        "glass": 60,
        "general": 55
    }.get(cat, 50)


def user_level(score):
    if score >= 80:
        return "🌟 Eco Master"
    elif score >= 60:
        return "🌿 Responsible Citizen"
    return "🌱 Beginner"


def city_simulator():
    return {
        "daily_waste": "150 Tons",
        "recycling_rate": "52%",
        "co2_impact": "Moderate",
        "prediction": "Smart recycling policies improving city sustainability"
    }
