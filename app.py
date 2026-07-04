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
st.set_page_config(page_title="EcoCycle AI", page_icon="🌱", layout="wide")

# ---------------- HEADER ----------------
st.markdown("<h1 style='text-align:center; color:#2ecc71;'>🌱 EcoCycle AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Smart Waste Intelligence System</p>", unsafe_allow_html=True)

st.markdown("---")

# ---------------- SIDEBAR ----------------
mode = st.sidebar.selectbox("Select Mode", ["Waste Analysis", "City Simulation"])

st.sidebar.info("AI-powered waste classification & sustainability insights")

# ======================================================
# 🌍 CITY SIMULATION
# ======================================================
if mode == "City Simulation":

    st.subheader("🌍 City Impact Simulation")

    city = city_simulator()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Daily Waste", city["daily_waste"])

    with col2:
        st.metric("Recycling Rate", city["recycling_rate"])

    with col3:
        st.metric("CO₂ Impact", city["co2_impact"])

    st.markdown("---")

    data = pd.DataFrame({
        "Category": ["Plastic", "Food", "E-Waste", "Glass"],
        "Percentage": [35, 30, 20, 15]
    })

    fig = px.pie(data, names="Category", values="Percentage", title="Waste Distribution")
    st.plotly_chart(fig, use_container_width=True)

    st.success("📊 Prediction: " + city["prediction"])

# ======================================================
# 🧾 WASTE ANALYSIS
# ======================================================
else:

    st.subheader("🧾 Waste Analysis Engine")

    user_input = st.text_input("Enter waste item (plastic, battery, food, glass)")

    if st.button("Analyze Waste"):

        if user_input.strip() == "":
            st.warning("Please enter a waste item")
        else:

            # ---------------- AI PIPELINE ----------------
            category = classification_agent(user_input)
            disposal = disposal_agent(category)
            impact = impact_agent(category)
            education = education_agent(category)
            score = eco_score(category)
            level = user_level(score)

            # ---------------- RESULTS ----------------
            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Waste Type", category.upper())

            with col2:
                st.metric("Eco Score", f"{score}/100")

            with col3:
                st.metric("User Level", level)

            st.markdown("---")

            st.subheader("♻ Disposal Guide")
            st.success(disposal)

            st.subheader("⚠ Environmental Impact")
            st.warning(impact)

            st.subheader("📘 Education Tip")
            st.info(education)

            # ---------------- CHART ----------------
            st.subheader("📊 Eco Score Visualization")

            fig = px.bar(
                x=["Eco Score", "Impact"],
                y=[score, 100 - score],
                color=["Eco Score", "Impact"]
            )

            st.plotly_chart(fig, use_container_width=True)

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("<p style='text-align:center; color:gray;'>Built for SDG 12 🌱</p>", unsafe_allow_html=True)
