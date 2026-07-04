import plotly.express as px
import pandas as pd


# ---------------- WASTE DISTRIBUTION PIE CHART ----------------
def waste_pie_chart():
    data = pd.DataFrame({
        "Category": ["Plastic", "Food", "E-Waste", "Glass", "Others"],
        "Percentage": [35, 30, 15, 10, 10]
    })

    fig = px.pie(
        data,
        names="Category",
        values="Percentage",
        title="🌍 Waste Composition",
        color_discrete_sequence=px.colors.sequential.Greens
    )

    return fig


# ---------------- ECO SCORE BREAKDOWN ----------------
def eco_score_bar(score):
    data = pd.DataFrame({
        "Type": ["Eco Score", "Environmental Impact"],
        "Value": [score, 100 - score]
    })

    fig = px.bar(
        data,
        x="Type",
        y="Value",
        color="Type",
        title="📊 Sustainability Score Breakdown",
        color_discrete_sequence=["#2ecc71", "#e74c3c"]
    )

    return fig


# ---------------- CITY TREND SIMULATION ----------------
def city_trend_chart():
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    data = pd.DataFrame({
        "Day": days,
        "Waste": [100, 110, 120, 130, 125, 140, 150],
        "Recycling": [40, 42, 43, 41, 45, 47, 50]
    })

    fig = px.line(
        data,
        x="Day",
        y=["Waste", "Recycling"],
        title="📈 Weekly City Waste Trends",
        markers=True
    )

    return fig


# ---------------- CO2 IMPACT COMPARISON ----------------
def co2_impact_chart():
    data = pd.DataFrame({
        "Source": ["Plastic", "Battery", "Food", "E-Waste", "Glass"],
        "Impact": [80, 95, 60, 90, 50]
    })

    fig = px.bar(
        data,
        x="Source",
        y="Impact",
        title="⚠ Environmental CO₂ Impact",
        color="Impact",
        color_continuous_scale="Reds"
    )

    return fig
