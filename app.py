import streamlit as st
from agents import classification_agent, disposal_agent, impact_agent, education_agent, eco_score

st.set_page_config(page_title="EcoCycle AI", page_icon="🌱")

st.title("🌱 EcoCycle AI")
st.markdown("🌍 EcoCycle AI helps reduce waste mismanagement using AI-driven decision agents.")
st.markdown("---")
st.markdown("### Multi-Agent Smart Waste Management System")

user_input = st.text_input("Enter waste item (e.g., plastic bottle, battery, food waste)")

if st.button("Analyze Waste"):

    category = classification_agent(user_input)
    disposal = disposal_agent(category)
    impact = impact_agent(category)
    tip = education_agent(category)
    score = eco_score(category)

    st.markdown("## 🧠 AI Agent Flow")

    st.code(f"""
Planner Agent → understands input
Classification Agent → {category}
Decision Agent → disposal plan generated
Impact Agent → environmental impact analyzed
Education Agent → sustainability tip generated
""")

    st.markdown("## 📊 Eco Score")
    st.progress(score)
    st.write(f"Environmental Impact Score: {score}/100")

    st.markdown("## ♻ Result")
    st.success(f"Waste Type: {category.upper()}")
    st.info(disposal)
    st.warning(impact)
    st.write(tip)

st.markdown("---")
st.caption("Built for UN Sustainable Development Goals 🌍")
