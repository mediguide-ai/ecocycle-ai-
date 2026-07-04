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
    <div style="text-align:center;">
        <h1 style="color:#2ecc71;">🌱 EcoCycle AI</h1>
        <h4 style="color:gray;">AI Waste Intelligence + Environmental Impact Simulator</h4>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------------- SIDEBAR ----------------
st.sidebar.title("🌍 EcoCycle Dashboard")
st.sidebar.info("This system analyzes waste, predicts environmental impact, and gives sustainability guidance.")

st.sidebar.markdown("### 🔥 Example Inputs")
st.sidebar.write("• plastic bottle")
st.sidebar.write("• battery charger")
st.sidebar.write("• food waste")
st.sidebar.write("• broken phone")

# ---------------- INPUT ----------------
st.markdown("## 🧾 Enter Waste Item")

user_input = st.text_input(
    "",
    placeholder="Type waste item here..."
)

# ---------------- BUTTON ----------------
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

        # ---------------- TITLE ----------------
        st.markdown("## 📊 Waste Analysis Dashboard")

        # ---------------- METRICS ----------------
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("♻ Waste Type", category.upper())

        with col2:
            st.metric("📊 Eco Score", f"{score}/100")

        with col3:
            st.metric("🏅 User Level", level)

        st.markdown("---")

        # ---------------- MAIN LAYOUT ----------------
        left, right = st.columns(2)

        with left:
            st.markdown("### ♻ Disposal Guide")
            st.success(disposal)

            st.markdown("### 📘 Sustainability Tip")
            st.info(education)

        with right:
            st.markdown("### ⚠ Environmental Impact")
            st.warning(impact)

            st.markdown("### 🌍 City Impact Simulation")
            st.error(city)

        st.markdown("---")

        # ---------------- ECO SCORE ----------------
        st.markdown("## 🌱 Environmental Impact Score")

        st.progress(score / 100)

        if score >= 85:
            st.error("🔴 High Environmental Risk")
        elif score >= 60:
            st.warning("🟠 Moderate Environmental Risk")
        else:
            st.success("🟢 Low Environmental Risk")

        st.markdown("---")

        # ---------------- WHAT IF ----------------
        st.markdown("## 🔥 What-If Simulation Engine")

        st.success(whatif)

        st.markdown("---")

        # ---------------- AI FLOW ----------------
        st.markdown("## 🧠 AI Multi-Agent Flow")

        st.code(f"""
Input → Classification Agent → {category}
       → Disposal Agent → {disposal}
       → Impact Agent → {impact}
       → Education Agent → {education}
       → Eco Score Engine → {score}
       → Behavior Engine → {level}
""")

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown(
    "<div style='text-align:center; color:gray;'>🌱 Built for UN SDG 12 | EcoCycle AI | Hackathon Project</div>",
    unsafe_allow_html=True
)
        # ---------------- METRICS ----------------
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("♻ Waste Type", category.upper())

        with col2:
            st.metric("📊 Eco Score", f"{score}/100")

        with col3:
            st.metric("🏅 User Level", level)

        st.markdown("---")

        # ---------------- MAIN LAYOUT ----------------
        left, right = st.columns(2)

        with left:
            st.markdown("### ♻ Disposal Guide")
            st.success(disposal)

            st.markdown("### 📘 Sustainability Tip")
            st.info(education)

        with right:
            st.markdown("### ⚠ Environmental Impact")
            st.warning(impact)

            st.markdown("### 🌍 City Impact Simulation")
            st.error(city)

        st.markdown("---")

        # ---------------- ECO SCORE ----------------
        st.markdown("## 🌱 Environmental Impact Score")

        st.progress(score / 100)

        if score >= 85:
            st.error("🔴 High Environmental Risk")
        elif score >= 60:
            st.warning("🟠 Moderate Environmental Risk")
        else:
            st.success("🟢 Low Environmental Risk")

        st.markdown("---")

        # ---------------- WHAT IF ----------------
        st.markdown("## 🔥 What-If Simulation Engine")

        st.success(whatif)

        st.markdown("---")

        # ---------------- AI FLOW ----------------
        st.markdown("## 🧠 AI Multi-Agent Flow")

        st.code(f"""
Input → Classification Agent → {category}
       → Disposal Agent → {disposal}
       → Impact Agent → {impact}
       → Education Agent → {education}
       → Eco Score Engine → {score}
       → Behavior Engine → {level}
""")

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown(
    "<div style='text-align:center; color:gray;'>🌱 Built for UN SDG 12 | EcoCycle AI | Hackathon Project</div>",
    unsafe_allow_html=True
)
