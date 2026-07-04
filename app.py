import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
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

# ---------------- CONFIG ----------------
st.set_page_config(page_title="EcoCycle AI v4", page_icon="🌱", layout="wide")

# ---------------- HERO HEADER ----------------
st.markdown("""
<h1 style='text-align:center; color:#00ff88;'>🌱 EcoCycle AI v4</h1>
<p style='text-align:center; color:gray;'>AI-Powered Sustainability Intelligence System</p>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------------- SIDEBAR ----------------
mode = st.sidebar.selectbox("Select Mode", ["Waste Intelligence", "City Command Center"])

# =====================================================
# 🌍 CITY MODE (UPGRADED)
# =====================================================
if mode == "City Command Center":

    st.subheader("🌍 Smart City Control Dashboard")

    city = city_simulator()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Daily Waste", city["daily_waste"])

    with col2:
        st.metric("Recycling Rate", city["recycling_rate"])

    with col3:
        st.metric("CO₂ Impact", city["co2_impact"])

    st.markdown("### 📊 City Waste Composition")

    df = pd.DataFrame({
        "Type": ["Plastic", "Food", "E-Waste", "Glass", "Other"],
        "Value": [35, 30, 20, 10, 5]
    })

    fig = px.pie(df, names="Type", values="Value", hole=0.4,
                 color_discrete_sequence=px.colors.sequential.Greens)

    st.plotly_chart(fig, use_container_width=True)

    st.success("📈 Forecast: " + city["prediction"])

# =====================================================
# 🧠 WASTE INTELLIGENCE MODE
# =====================================================
else:

    st.subheader("🧠 AI Waste Intelligence Engine")

    user_input = st.text_input("Enter waste item")

    if st.button("Analyze Now 🚀"):

        if not user_input.strip():
            st.warning("Please enter waste item")
        else:

            # ---------------- AI PIPELINE ----------------
            category = classification_agent(user_input)
            disposal = disposal_agent(category)
            impact = impact_agent(category)
            education = education_agent(category)
            score = eco_score(category)
            level = user_level(score)

            # ---------------- TOP METRICS ----------------
            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Waste Type", category.upper())

            with col2:
                st.metric("Eco Level", level)

            with col3:
                st.metric("Score", f"{score}/100")

            st.markdown("---")

            # ---------------- GAUGE (WINNER FEATURE) ----------------
            st.subheader("🌱 Sustainability Score Meter")

            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=score,
                title={'text': "Eco Score"},
                gauge={
                    'axis': {'range': [0, 100]},
                    'bar': {'color': "green"},
                    'steps': [
                        {'range': [0, 40], 'color': "red"},
                        {'range': [40, 70], 'color': "yellow"},
                        {'range': [70, 100], 'color': "green"},
                    ],
                }
            ))

            st.plotly_chart(fig, use_container_width=True)

            # ---------------- INSIGHTS ----------------
            st.subheader("♻ Disposal Guidance")
            st.success(disposal)

            st.subheader("⚠ Environmental Impact")
            st.warning(impact)

            st.subheader("📘 Sustainability Tip")
            st.info(education)
