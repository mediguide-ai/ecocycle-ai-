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
import streamlit as st
from agents import *

st.set_page_config(page_title="EcoCycle AI", page_icon="🌱", layout="centered")

# HEADER
st.markdown("<h1 style='text-align:center;'>🌱 EcoCycle AI</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center;'>AI Waste Intelligence + City Impact Simulator</h4>", unsafe_allow_html=True)

st.markdown("---")

# INPUT
user_input = st.text_input("Enter waste item", placeholder="plastic bottle, battery, food waste...")

if st.button("Analyze Waste"):

    category = classification_agent(user_input)
    disposal = disposal_agent(category)
    impact = impact_agent(category)
    education = education_agent(category)
    score = eco_score(category)
    level = user_level(score)
    city = city_impact(category)
    whatif = what_if_simulator(category)

    # RESULTS
    st.markdown("## ♻ Waste Intelligence Report")

    col1, col2 = st.columns(2)

    with col1:
        st.success(f"Category: {category.upper()}")
        st.info(disposal)

    with col2:
        st.warning(impact)
        st.write(education)

    st.markdown("---")

    # SCORE
    st.markdown("## 📊 Eco Score")
    st.progress(score / 100)
    st.subheader(f"Score: {score}/100")

    # LEVEL (NEW WINNER FEATURE)
    st.markdown("## 🏅 Your Sustainability Level")
    st.success(level)

    st.markdown("---")

    # CITY IMPACT
    st.markdown("## 🌍 City Impact Simulation")
    st.info(city)

    st.markdown("---")

    # WHAT IF SIMULATOR (KEY WINNER FEATURE)
    st.markdown("## 🔥 What-If Simulator")
    st.success(whatif)

# FOOTER
st.markdown("---")
st.caption("Built for SDG 12 🌱 | EcoCycle AI | Hackathon Project")
