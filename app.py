import streamlit as st
import streamlit as st
from agents import classification_agent, disposal_agent, impact_agent, education_agent, eco_score

st.set_page_config(page_title="EcoCycle AI", page_icon="🌱", layout="centered")

# Header
st.title("🌱 EcoCycle AI")
st.markdown("### Multi-Agent Smart Waste Management System")
st.markdown("🌍 AI-powered waste classification aligned with SDG 12 (Responsible Consumption & Production)")
st.markdown("---")

# Examples section
st.markdown("### 🔥 Try Examples")
st.write("• plastic bottle")
st.write("• battery charger")
st.write("• food waste")
st.write("• broken phone")
st.markdown("---")

# Input
user_input = st.text_input(
    "Enter waste item",
    placeholder="e.g., plastic bottle, battery, food waste"
)

# Button
if st.button("Analyze Waste"):

    if not user_input.strip():
        st.warning("⚠ Please enter a waste item")
    else:

        # Agents pipeline
        category = classification_agent(user_input)
        disposal = disposal_agent(category)
        impact = impact_agent(category)
        education = education_agent(category)
        score = eco_score(category)

        # Results section
        st.markdown("## ♻ Results")

        col1, col2 = st.columns(2)

        with col1:
            st.success(f"🧠 Waste Type: {category.upper()}")
            st.info(f"♻ Disposal: {disposal}")

        with col2:
            st.warning(f"⚠ Impact: {impact}")
            st.write(f"📘 Tip: {education}")

        # Eco score
        st.markdown("## 📊 Eco Score")

        st.progress(score / 100)

        if score >= 80:
            st.error(f"🔴 High Environmental Impact: {score}/100")
        elif score >= 50:
            st.warning(f"🟠 Moderate Environmental Impact: {score}/100")
        else:
            st.success(f"🟢 Low Environmental Impact: {score}/100")

# Footer
st.markdown("---")
st.caption("Built for UN Sustainable Development Goal 12 🌱 | EcoCycle AI")
