import streamlit as st
from agents import *

# ---------------- UI SETUP ----------------
st.set_page_config(page_title="EcoCycle AI", page_icon="🌱", layout="centered")

# ---------------- HEADER ----------------
st.markdown("<h1 style='text-align:center;'>🌱 EcoCycle AI</h1>", unsafe_allow_html=True)

st.markdown(
    "<h4 style='text-align:center; color:gray;'>AI Multi-Agent Waste Intelligence System</h4>",
    unsafe_allow_html=True
)

st.markdown("---")

# ---------------- HERO SECTION ----------------
st.markdown("### 🌍 About the System")
st.info("EcoCycle AI analyzes waste, predicts environmental impact, and guides sustainable disposal using a multi-agent system aligned with SDG 12.")

st.markdown("---")

# ---------------- INPUT ----------------
st.markdown("### 🧾 Enter Waste Item")
user_input = st.text_input("", placeholder="e.g., plastic bottle, battery, food waste")

# ---------------- BUTTON ----------------
if st.button("🚀 Analyze Waste"):

    if user_input.strip() == "":
        st.warning("Please enter a waste item")
    else:

        # Agents
        category = classification_agent(user_input)
        disposal = disposal_agent(category)
        impact = impact_agent(category)
        education = education_agent(category)
        score = eco_score(category)
        badge = eco_badge(score)
        city = city_impact(category)

        # ---------------- RESULTS ----------------
        st.markdown("## ♻ Results Dashboard")

        col1, col2 = st.columns(2)

        with col1:
            st.success("🧠 Waste Category")
            st.subheader(category.upper())

            st.info("♻ Disposal Guide")
            st.write(disposal)

        with col2:
            st.warning("⚠ Environmental Impact")
            st.write(impact)

            st.info("📘 Sustainability Tip")
            st.write(education)

        st.markdown("---")

        # ---------------- ECO SCORE ----------------
        st.markdown("## 📊 Eco Impact Score")

        st.progress(score / 100)

        if score >= 85:
            st.error(f"{score}/100 — High Environmental Risk")
        elif score >= 60:
            st.warning(f"{score}/100 — Moderate Environmental Risk")
        else:
            st.success(f"{score}/100 — Low Environmental Risk")

        st.markdown("---")

        # ---------------- BADGE ----------------
        st.markdown("## 🏅 Your Eco Badge")
        st.subheader(badge)

        st.markdown("---")

        # ---------------- CITY IMPACT ----------------
        st.markdown("## 🌍 City-Level Impact Simulation")
        st.info(city)

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("Built for UN SDG 12 🌱 | EcoCycle AI | Hackathon Project")
