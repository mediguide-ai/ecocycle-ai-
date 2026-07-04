def classification_agent(text):
    text = text.lower()

    if any(x in text for x in ["plastic", "bottle", "bag", "wrapper"]):
        return "plastic"
    elif any(x in text for x in ["battery", "charger", "cell"]):
        return "battery"
    elif any(x in text for x in ["food", "fruit", "leftover", "vegetable"]):
        return "food"
    elif any(x in text for x in ["glass", "jar"]):
        return "glass"
    elif any(x in text for x in ["phone", "laptop", "tv", "electronics", "e-waste"]):
        return "e-waste"
    else:
        return "other"


def disposal_agent(cat):
    return {
        "plastic": "♻ Recycle in dry waste bin",
        "battery": "⚠ Dispose at e-waste collection center",
        "food": "🌱 Compost organic waste",
        "glass": "♻ Send to glass recycling facility",
        "e-waste": "⚠ Hand over to certified e-waste recycler",
        "other": "📍 Follow local municipal guidelines"
    }.get(cat, "Unknown")


def impact_agent(cat):
    return {
        "plastic": "High pollution • 400+ years to decompose",
        "battery": "Toxic chemicals contaminate soil & water",
        "food": "Produces methane in landfills",
        "glass": "Non-biodegradable but recyclable",
        "e-waste": "Releases heavy metals & toxins",
        "other": "Moderate environmental impact"
    }.get(cat, "")


def education_agent(cat):
    return {
        "plastic": "Use reusable bags instead of plastic",
        "battery": "Switch to rechargeable batteries",
        "food": "Reduce food waste at source",
        "glass": "Reuse bottles before recycling",
        "e-waste": "Recycle electronics responsibly"
    }.get(cat, "Follow sustainable habits")


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


def eco_badge(score):
    if score >= 85:
        return "🟢 Green Hero"
    elif score >= 60:
        return "🟡 Waste Watcher"
    else:
        return "🔴 High Impact User"


def city_impact(cat):
    return {
        "plastic": "If 1000 users/day → 50kg plastic waste enters landfill",
        "battery": "If 1000 users/day → severe soil toxicity risk",
        "food": "If 1000 users/day → high methane emissions",
        "glass": "If 1000 users/day → high recycling energy demand",
        "e-waste": "If 1000 users/day → dangerous metal leakage risk"
    }.get(cat, "No simulation available")
