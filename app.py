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
if st.button("🚀 Analyze Waste", key="analyze_btn"):
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
        city_data = city_simulator()

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
        st.markdown("## 🌍 EcoCity Intelligence Dashboard")

col1, col2, col3 = st.columns(3)

with col1:
import streamlit as st
import plotly.express as px
import pandas as pd

from agents import (
    classification_agent,
    disposal_agent,
    impact_agent,
    education_agent,
    eco_score,
    user_level,
    city_simulator
)

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="EcoCycle AI",
    page_icon="🌱",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.main {
    background-color: #0e1117;
}
h1, h2, h3 {
    color: #2ecc71;
}
.stMetric {
    background-color: #1c1f26;
    padding: 15px;
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("<h1 style='text-align:center;'>🌱 EcoCycle AI v3.0</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:gray;'>Smart Waste Intelligence & City Impact System</p>", unsafe_allow_html=True)

st.markdown("---")

# ---------------- SIDEBAR ----------------
st.sidebar.title("🌍 Control Panel")
mode = st.sidebar.selectbox("Choose Mode", ["Single Analysis", "City Dashboard"])

st.sidebar.info("EcoCycle AI helps analyze waste and simulate environmental impact.")

# ---------------- CITY MODE ----------------
if mode == "City Dashboard":

    st.markdown("## 🌍 Smart City Simulation")

    city = city_simulator()

    col1, col2, col3 = st.columns(3)

    col1.metric("Daily Waste", city["daily_waste"])
    col2.metric("Recycling Rate", city["recycling_rate"])
    col3.metric("CO₂ Impact", city["co2_impact"])

    data = pd.DataFrame({
        "Category": ["Plastic", "Food", "E-Waste", "Glass"],
        "Percentage": [35, 30, 20, 15]
    })

    fig = px.pie(data, names="Category", values="Percentage", title="Waste Distribution")
    st.plotly_chart(fig, use_container_width=True)

    st.success("📈 Prediction: " + city["prediction"])

# ---------------- SINGLE ANALYSIS MODE ----------------
else:

    st.markdown("## 🧾 Waste Analysis Engine")

    user_input = st.text_input("Enter waste item", placeholder="plastic bottle, battery, food waste...")

    if st.button("🚀 Analyze", key="analyze"):

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

            # ---------------- DASHBOARD ----------------
            col1, col2, col3 = st.columns(3)

            col1.metric("Waste Type", category.upper())
            col2.metric("Eco Score", f"{score}/100")
            col3.metric("User Level", level)

            st.markdown("---")

            # ---------------- DETAILS ----------------
            st.subheader("♻ Disposal Guide")
            st.success(disposal)

            st.subheader("⚠ Environmental Impact")
            st.warning(impact)

            st.subheader("📘 Education Tip")
            st.info(education)

            # ---------------- SCORE CHART ----------------
            st.subheader("📊 Eco Score Visualization")

            fig = px.bar(
                x=["Eco Score", "Remaining Impact"],
                y=[score, 100 - score],
                color=["Eco Score", "Remaining Impact"],
                title="Sustainability Breakdown"
            )

            st.plotly_chart(fig, use_container_width=True)

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("<p style='text-align:center;color:gray;'>Built for SDG 12 🌱 | EcoCycle AI</p>", unsafe_allow_html=True)
