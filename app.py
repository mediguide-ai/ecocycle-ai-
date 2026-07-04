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
st.set_page_config(page_title="EcoCycle AI - Final Boss", page_icon="🌱", layout="wide")

# ---------------- HERO ----------------
st.markdown("""
<h1 style='text-align:center; color:#00ff99;'>🌱 EcoCycle AI - Final Boss</h1>
<p style='text-align:center; color:gray;'>AI-Powered Sustainability Intelligence Platform</p>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------------- SIDEBAR ----------------
mode = st.sidebar.selectbox("Select Mode", ["AI Waste Brain", "City Intelligence Engine"])

# =====================================================
# 🌍 CITY MODE (FINAL BOSS)
# =====================================================
if mode == "City Intelligence Engine":

    st.subheader("🌍 Smart City Command Center")

    city = city_simulator()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Daily Waste", city["daily_waste"])

    with col2:
        st.metric("Recycling Rate", city["recycling_rate"])

    with col3:
        st.metric("CO₂ Impact", city["co2_impact"])

    st.markdown("### 📊 City Waste Distribution")

    df = pd.DataFrame({
        "Category": ["Plastic", "Food", "E-Waste", "Glass", "Other"],
        "Value": [40, 25, 20, 10, 5]
    })

    fig = px.pie(df, names="Category", values="Value",
                 color_discrete_sequence=px.colors.sequential.Greens)

    st.plotly_chart(fig, use_container_width=True)

    st.success("📈 AI Forecast: " + city["prediction"])

# =====================================================
# 🧠 AI WASTE BRAIN (FINAL BOSS)
# =====================================================
else:

    st.subheader("🧠 AI Waste Intelligence Brain")

    user_input = st.text_input("Enter waste item")

    if st.button("Analyze Waste 🚀"):

        if not user_input.strip():
            st.warning("Enter a waste item")
        else:

            # ---------------- AI ENGINE ----------------
            category = classification_agent(user_input)
            disposal = disposal_agent(category)
            impact = impact_agent(category)
            education = education_agent(category)
            score = eco_score(category)
            level = user_level(score)

            # ---------------- METRICS ----------------
            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Waste Type", category.upper())

            with col2:
                st.metric("Eco Level", level)

            with col3:
                st.metric("Score", f"{score}/100")

            st.markdown("---")

            # ---------------- GAUGE (FINAL BOSS FEATURE) ----------------
            st.subheader("🌱 Sustainability Score Engine")

            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=score,
                title={'text': "Eco Score"},
                gauge={
                    'axis': {'range': [0, 100]},
                    'bar': {'color': "#00ff99"},
                    'steps': [
                        {'range': [0, 40], 'color': "red"},
                        {'range': [40, 70], 'color': "orange"},
                        {'range': [70, 100], 'color': "green"},
                    ],
                }
            ))

            st.plotly_chart(fig, use_container_width=True)

            # ---------------- INSIGHTS ----------------
            st.subheader("♻ Disposal Strategy")
            st.success(disposal)

            st.subheader("⚠ Environmental Impact")
            st.warning(impact)

            st.subheader("📘 Smart Recommendation")
            st.info(education)

            # ---------------- DOWNLOAD REPORT (WOW FEATURE) ----------------
            report = f"""
EcoCycle AI Report
------------------
Waste Type: {category}
Eco Score: {score}
Level: {level}
Disposal: {disposal}
Impact: {impact}
"""

            st.download_button("📄 Download Report", report, file_name="eco_report.txt")
