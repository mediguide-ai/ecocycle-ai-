import streamlit as st
from agents import *

st.set_page_config(page_title="EcoCycle AI", page_icon="🌱")

st.title("🌱 EcoCycle AI")
st.markdown("### AI Multi-Agent Waste Intelligence System")
st.markdown("Built for SDG 12 🌍 Responsible Consumption & Production")

st.markdown("---")

# Input
user_input = st.text_input("Enter waste item", placeholder="plastic bottle, battery, food waste...")

if st.button("Analyze Waste"):

    category = classification_agent(user_input)
    disposal = disposal_agent(category)
    impact = impact_agent(category)
    education = education_agent(category)
    score = eco_score(category)
    badge = eco_badge(score)
    city = city_impact(category)

    st.markdown("## ♻ Results")

    col1, col2 = st.columns(2)

    with col1:
        st.success(f"Waste Type: {category.upper()}")
        st.info(disposal)

    with col2:
        st.warning(impact)
        st.write(education)

    st.markdown("## 📊 Eco Score")
    st.progress(score / 100)
    st.write(f"Score: {score}/100")

    st.markdown("## 🏅 Your Eco Badge")
    st.subheader(badge)

    st.markdown("## 🌍 City Impact Simulation")
    st.info(city)

    st.markdown("---")
    st.caption("EcoCycle AI • SDG 12 • Sustainable Future 🌱")
