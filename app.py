import streamlit as st
from agents import classification_agent, disposal_agent, impact_agent, education_agent

st.set_page_config(page_title="EcoCycle AI", page_icon="🌱")

st.title("🌱 EcoCycle AI")
st.subheader("Multi-Agent Smart Waste Management System")

user_input = st.text_input("Enter waste item (e.g., plastic bottle, battery, food waste)")

if st.button("Analyze Waste"):

    category = classification_agent(user_input)
    disposal = disposal_agent(category)
    impact = impact_agent(category)
    tip = education_agent(category)

    st.markdown("## 🧠 Analysis Report")

    st.success(f"🏷 Waste Type: {category.upper()}")

    st.markdown("### ♻ Disposal")
    st.info(disposal)

    st.markdown("### 🌍 Impact")
    st.warning(impact)

    st.markdown("### 📘 Eco Tip")
    st.write(tip)

st.markdown("---")
st.caption("Built for Sustainable Development Goals 🌍")
