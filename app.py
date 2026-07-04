import streamlit as st
from agents import (
    classification_agent,
    disposal_agent,
    impact_agent,
    education_agent,
    eco_score,
    user_level,
    city_impact,
    what_if_simulator
)

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="EcoCycle AI",
    page_icon="🌱",
    layout="wide"
)

# ---------------- HEADER ----------------
st.markdown("""
    <h1 style='text-align:center; color:#2ecc71;'>🌱 EcoCycle AI</h1>
    <h4 style='text-align:center; color:gray;'>
    AI-Powered Waste Intelligence + City Impact Simulator
    </h4>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------------- INPUT SECTION ----------------
col1, col2 = st.columns([2, 1])

with col1:
    user_input = st.text_input(
        "Enter Waste Item",
        placeholder="e.g., plastic bottle, battery, food waste..."
    )

with col2:
    st.markdown("### 🔥 Examples")
    st.write("• plastic bottle")
    st.write("• battery charger")
    st.write("• food waste")
    st.write("• broken phone")

# ---------------- ANALYZE BUTTON ----------------
if st.button("🚀 Analyze Waste"):

    if not user_input.strip():
        st.warning("Please enter a waste item")
    else:

        # ---------------- AGENTS ----------------
        category = classification_agent(user_input)
        disposal = disposal_agent(category)
        impact = impact_agent(category)
        education = education_agent(category)
        score = eco_score(category)
        level = user_level(score)
        city = city_impact(category)
        whatif = what_if_simulator(category)

        # ---------------- DASHBOARD TITLE ----------------
        st.markdown("## 📊 Waste Intelligence Dashboard")

        # ---------------- METRICS ----------------
        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric("♻ Waste Type", category.upper())

        with c2:
            st.metric("📊 Eco Score", f"{score}/100")

        with c3:
            st.metric("🏅 User Level", level)

        st.markdown("---")

        # ---------------- MAIN CONTENT ----------------
        left, right = st.columns(2)

        with left:
            st.markdown("### ♻ Disposal Recommendation")
            st.success(disposal)

            st.markdown("### 📘 Sustainability
