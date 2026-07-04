# ---------------- WASTE CLASSIFICATION AGENT ----------------
def classification_agent(text):
    text = text.lower()

    if "plastic" in text or "bottle" in text:
        return "plastic"
    elif "battery" in text or "cell" in text:
        return "battery"
    elif "food" in text or "leftover" in text:
        return "food"
    elif "glass" in text:
        return "glass"
    elif "phone" in text or "laptop" in text or "electronic" in text:
        return "e-waste"
    else:
        return "general waste"


# ---------------- DISPOSAL AGENT ----------------
def disposal_agent(category):
    return {
        "plastic": "♻ Recycle in dry waste bin or recycling center",
        "battery": "⚠ Dispose at certified e-waste facility",
        "food": "🌱 Compost or organic waste bin",
        "glass": "♻ Send to glass recycling unit",
        "e-waste": "🔌 Hand over to authorized e-waste recycler",
        "general waste": "🗑 Follow local municipal guidelines"
    }.get(category, "No guideline available")


# ---------------- IMPACT AGENT ----------------
def impact_agent(category):
    return {
        "plastic": "High pollution risk, takes 100+ years to decompose",
        "battery": "Toxic chemicals can contaminate soil & water",
        "food": "Produces methane gas in landfills",
        "glass": "Energy-intensive recycling but reusable",
        "e-waste": "Releases heavy metals like lead & mercury",
        "general waste": "Mixed environmental impact"
    }.get(category, "")


# ---------------- EDUCATION AGENT ----------------
def education_agent(category):
    return {
        "plastic": "Use reusable bags and bottles",
        "battery": "Switch to rechargeable batteries",
        "food": "Plan meals to reduce food waste",
        "glass": "Reuse jars and containers",
        "e-waste": "Donate or recycle electronics responsibly",
        "general waste": "
