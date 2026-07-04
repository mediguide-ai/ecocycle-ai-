def classification_agent(text):
    text = text.lower()

    if any(x in text for x in ["plastic", "bottle", "bag"]):
        return "plastic"
    if any(x in text for x in ["battery", "charger", "cell"]):
        return "battery"
    if any(x in text for x in ["food", "fruit", "leftover"]):
        return "food"
    if any(x in text for x in ["glass"]):
        return "glass"
    if any(x in text for x in ["phone", "laptop", "electronics", "e-waste"]):
        return "e-waste"
    return "other"


def disposal_agent(cat):
    return {
        "plastic": "Recycle in dry waste bin",
        "battery": "Dispose at e-waste center",
        "food": "Compost organic waste",
        "glass": "Send to glass recycling facility",
        "e-waste": "Hand over to certified recycler",
        "other": "Follow local municipal rules"
    }.get(cat, "Unknown")


def impact_agent(cat):
    return {
        "plastic": "High pollution, 400+ years to decompose",
        "battery": "Toxic chemicals contaminate soil & water",
        "food": "Produces methane gas in landfill",
        "glass": "Non-biodegradable but recyclable",
        "e-waste": "Releases heavy metals into environment",
        "other": "Moderate environmental impact"
    }.get(cat, "")


def education_agent(cat):
    return {
        "plastic": "Avoid single-use plastics",
        "battery": "Use rechargeable alternatives",
        "food": "Reduce food waste",
        "glass": "Reuse before recycling",
        "e-waste": "Recycle electronics responsibly"
    }.get(cat, "Follow sustainable habits")


# 🌍 NEW FEATURE 1: CITY IMPACT SIMULATOR
def city_impact(cat):
    impact = {
        "plastic": "If 1000 users dispose daily → ~50kg plastic waste/day",
        "battery": "If 1000 users dispose daily → toxic contamination risk increases 5x",
        "food": "If 1000 users dispose daily → high methane emission increase",
        "glass": "If 1000 users dispose daily → high recycling energy demand",
        "e-waste": "If 1000 users dispose daily → dangerous heavy metal leakage",
    }
    return impact.get(cat, "No major simulation data available")


# 🏆 NEW FEATURE 2: ECO SCORE
def eco_score(cat):
    scores = {
        "plastic": 70,
        "battery": 95,
        "food": 50,
        "glass": 40,
        "e-waste": 90,
        "other": 60
    }
    return scores.get(cat, 50)


# 🏅 NEW FEATURE 3: BADGE SYSTEM
def eco_badge(score):
    if score >= 85:
        return "🟢 Green Hero"
    elif score >= 60:
        return "🟡 Waste Watcher"
    else:
        return "🔴 High Impact User"


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
