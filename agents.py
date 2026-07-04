def classification_agent(text):
    text = text.lower()

    if any(x in text for x in ["plastic", "bottle", "bag", "wrapper"]):
        return "plastic"
    if any(x in text for x in ["battery", "charger", "cell"]):
        return "battery"
    if any(x in text for x in ["food", "fruit", "leftover"]):
        return "food"
    if any(x in text for x in ["glass", "jar"]):
        return "glass"
    if any(x in text for x in ["phone", "laptop", "tv", "electronics", "e-waste"]):
        return "e-waste"
    return "other"


def disposal_agent(cat):
    return {
        "plastic": "♻ Recycle in dry waste bin",
        "battery": "⚠ E-waste facility required",
        "food": "🌱 Compost organic waste",
        "glass": "♻ Glass recycling plant",
        "e-waste": "⚠ Certified e-waste recycler",
        "other": "📍 Follow municipal guidelines"
    }.get(cat, "")


def impact_agent(cat):
    return {
        "plastic": "High pollution • 400+ years decomposition",
        "battery": "Toxic soil + water contamination",
        "food": "Methane emissions in landfills",
        "glass": "Energy intensive recycling",
        "e-waste": "Heavy metal leakage risk",
        "other": "Moderate impact"
    }.get(cat, "")


def education_agent(cat):
    return {
        "plastic": "Avoid single-use plastics",
        "battery": "Switch to rechargeable options",
        "food": "Reduce food waste",
        "glass": "Reuse before recycling",
        "e-waste": "Recycle responsibly"
    }.get(cat, "Follow sustainable habits")


# 🌍 ECO SCORE
def eco_score(cat):
    return {
        "plastic": 70,
        "battery": 95,
        "food": 50,
        "glass": 40,
        "e-waste": 90,
        "other": 60
    }.get(cat, 50)


# 🏅 BEHAVIOR ENGINE (NEW WINNER FEATURE)
def user_level(score):
    if score >= 85:
        return "🌳 Sustainability Leader"
    elif score >= 60:
        return "🌿 Responsible Citizen"
    else:
        return "🌱 Eco Beginner"


# 🌍 CITY IMPACT (UPGRADED)
def city_impact(cat):
    return {
        "plastic": "If 10,000 users → severe landfill pressure increase",
        "battery": "If 10,000 users → toxic contamination risk rises sharply",
        "food": "If 10,000 users → high methane emission surge",
        "glass": "If 10,000 users → energy demand increases",
        "e-waste": "If 10,000 users → heavy metal leakage risk"
    }.get(cat, "No simulation available")


# 🔥 WHAT-IF SIMULATOR (WINNING FEATURE)
def what_if_simulator(cat):
    return {
        "plastic": "Reducing plastic by 30% → landfill load ↓ 25%",
        "battery": "Proper disposal → toxicity risk ↓ 60%",
        "food": "Composting → methane emissions ↓ 40%",
        "glass": "Recycling reuse → energy savings ↑ 35%",
        "e-waste": "Safe recycling → pollution ↓ 70%"
    }.get(cat, "Behavior improvement reduces environmental impact")
