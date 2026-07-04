def classification_agent(text):
    text = text.lower()

    if "plastic" in text or "bottle" in text:
        return "plastic"
    if "battery" in text or "charger" in text:
        return "battery"
    if "food" in text or "leftover" in text:
        return "food"
    if "glass" in text:
        return "glass"
    if "phone" in text or "laptop" in text:
        return "e-waste"
    return "other"


def disposal_agent(cat):
    return {
        "plastic": "Recycle in dry waste bin",
        "battery": "Dispose at e-waste center",
        "food": "Compost organic waste",
        "glass": "Send to recycling facility",
        "e-waste": "Certified e-waste disposal required",
        "other": "Follow local rules"
    }.get(cat, "")


def impact_agent(cat):
    return {
        "plastic": "High pollution, long decomposition time",
        "battery": "Toxic soil and water contamination",
        "food": "Methane emission in landfills",
        "glass": "Energy-intensive recycling",
        "e-waste": "Heavy metal pollution risk"
    }.get(cat, "")


def education_agent(cat):
    return {
        "plastic": "Avoid single-use plastics",
        "battery": "Use rechargeable alternatives",
        "food": "Reduce food waste",
        "glass": "Reuse before recycling",
        "e-waste": "Recycle responsibly"
    }.get(cat, "")


def eco_score(cat):
    return {
        "plastic": 70,
        "battery": 95,
        "food": 50,
        "glass": 40,
        "e-waste": 90,
        "other": 60
    }.get(cat, 50)


def user_level(score):
    if score >= 85:
        return "Green Hero"
    elif score >= 60:
        return "Responsible Citizen"
    return "Eco Beginner"


def city_impact(cat):
    return {
        "plastic": "If 10,000 users → landfill pressure increases significantly",
        "battery": "If 10,000 users → toxic contamination risk rises",
        "food": "If 10,000 users → methane emissions surge",
        "glass": "If 10,000 users → recycling demand increases",
        "e-waste": "If 10,000 users → heavy metal leakage risk"
    }.get(cat, "No data")


def what_if_simulator(cat):
    return {
        "plastic": "Reducing plastic by 30% → major landfill reduction",
        "battery": "Proper disposal → toxicity reduced by 60%",
        "food": "Composting → methane reduced by 40%",
        "glass": "Recycling → energy saved by 35%",
        "e-waste": "Safe recycling → pollution reduced by 70%"
    }.get(cat, "Behavior change improves environment")
