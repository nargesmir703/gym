import streamlit as st
import numpy as np

# -------------------------
# Page Configuration
# -------------------------
st.set_page_config(
    page_title="FitAura | Progress Predictor",
    page_icon="✦",
    layout="wide"
)

# -------------------------
# Custom CSS
# -------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --bg: #F8F6FC;
    --card: #FFFFFF;
    --purple: #8B70C9;
    --purple-dark: #62459B;
    --lavender: #EDE6FA;
    --pink: #F8E5EF;
    --text: #29243A;
    --muted: #898397;
}

.stApp {
    background: linear-gradient(135deg, #F8F6FC, #FDF8FB);
    font-family: 'Inter', sans-serif;
    color: var(--text);
}

.block-container {
    max-width: 1180px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

#MainMenu, footer, header {
    visibility: hidden;
}

.hero {
    background: linear-gradient(120deg, #E9DFFC, #FBEAF2);
    padding: 36px;
    border-radius: 28px;
    margin-bottom: 28px;
    border: 1px solid #FFFFFF;
}

.eyebrow {
    color: #765AAE;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 3px;
    text-transform: uppercase;
}

.hero h1 {
    font-size: clamp(30px, 4vw, 46px);
    font-weight: 800;
    color: #302546;
    margin: 12px 0;
    letter-spacing: -1.5px;
}

.hero p {
    color: #746783;
    font-size: 15px;
    line-height: 1.8;
    max-width: 600px;
}

.section-title {
    font-size: 19px;
    font-weight: 800;
    color: #39304B;
    margin: 26px 0 5px 0;
}

.section-subtitle {
    color: #91899F;
    font-size: 13px;
    margin-bottom: 20px;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(255,255,255,0.88);
    border: 1px solid #EDE7F5;
    border-radius: 22px;
    padding: 20px;
    box-shadow: 0 8px 28px rgba(76, 54, 117, 0.045);
}

div[data-testid="stSlider"] {
    padding-top: 5px;
    padding-bottom: 5px;
}

.stSlider [data-baseweb="slider"] div[role="slider"] {
    background-color: #8B70C9;
    border-color: #8B70C9;
}

.stSlider [data-testid="stTickBar"] {
    background: #E9E0F6;
}

.stButton > button {
    width: 100%;
    min-height: 54px;
    border-radius: 16px;
    border: none;
    color: white;
    background: linear-gradient(100deg, #8B70C9, #AD8BDC);
    font-weight: 800;
    font-size: 16px;
    transition: 0.25s ease;
    box-shadow: 0 8px 18px rgba(139,112,201,0.22);
}

.stButton > button:hover {
    color: white;
    border: none;
    transform: translateY(-2px);
    box-shadow: 0 12px 25px rgba(139,112,201,0.3);
}

div[data-testid="stMetric"] {
    background: white;
    border: 1px solid #EDE7F5;
    border-radius: 20px;
    padding: 22px;
}

div[data-testid="stMetricLabel"] {
    color: #81768F;
    font-weight: 600;
}

div[data-testid="stMetricValue"] {
    color: #7054AC;
    font-weight: 800;
}

.result-card {
    background: linear-gradient(135deg, #EEE6FC, #FCEBF3);
    border: 1px solid #E7DDF4;
    border-radius: 24px;
    padding: 28px;
    text-align: center;
    margin-top: 16px;
}

.result-number {
    font-size: 54px;
    font-weight: 800;
    letter-spacing: -2px;
    color: #7355AE;
}

.result-label {
    font-size: 12px;
    letter-spacing: 2px;
    color: #81718F;
    font-weight: 700;
    text-transform: uppercase;
}

.result-message {
    font-size: 18px;
    font-weight: 800;
    color: #46375F;
    margin-top: 8px;
}

.footer {
    text-align: center;
    color: #A39AAF;
    font-size: 12px;
    padding-top: 35px;
    letter-spacing: 1px;
}

[data-testid="stProgressBar"] > div > div {
    background: linear-gradient(90deg, #9275D0, #E6A7CA);
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# Hero
# -------------------------
st.markdown("""
<div class="hero">
    <div class="eyebrow">✦ YOUR PERSONAL FITNESS SPACE</div>
    <h1>Small habits.<br>Stronger you.</h1>
    <p>
        A personalized fitness dashboard to explore how your
        daily habits, recovery, and consistency contribute
        to your fitness journey.
    </p>
</div>
""", unsafe_allow_html=True)

# -------------------------
# Input Sections
# -------------------------
st.markdown(
    '<div class="section-title">01 — Your Profile</div>'
    '<div class="section-subtitle">Start with your personal baseline.</div>',
    unsafe_allow_html=True
)

c1, c2, c3 = st.columns(3)

with c1:
    with st.container(border=True):
        st.markdown("#### 🧍 Personal")
        age = st.slider("Age", 16, 60, 25)
        height_cm = st.slider("Height (cm)", 150, 200, 170)
        weight_kg = st.slider("Weight (kg)", 45, 140, 70)

with c2:
    with st.container(border=True):
        st.markdown("#### 🌙 Recovery")
        sleep_hours = st.slider("Sleep Hours", 3, 10, 7)
        stress_level = st.slider("Stress Level", 1, 10, 5)
        water_liters = st.slider("Water (L/day)", 0.5, 7.0, 2.5, 0.5)

with c3:
    with st.container(border=True):
        st.markdown("#### ⚡ Daily Activity")
        steps_per_day = st.slider("Steps per Day", 500, 25000, 8000, 500)
        workout_days_per_week = st.slider("Workout Days", 0, 7, 3)
        cardio_days_per_week = st.slider("Cardio Days", 0, 7, 2)

st.markdown(
    '<div class="section-title">02 — Your Lifestyle</div>'
    '<div class="section-subtitle">Consistency is built one decision at a time.</div>',
    unsafe_allow_html=True
)

c4, c5 = st.columns(2)

with c4:
    with st.container(border=True):
        st.markdown("#### 🥑 Nutrition")
        protein_grams = st.slider("Protein (g/day)", 30, 260, 120)
        meal_quality = st.slider("Meal Quality", 1, 10, 6)

with c5:
    with st.container(border=True):
        st.markdown("#### 🎯 Mindset")
        program_consistency = st.slider("Program Consistency", 1, 10, 6)
        motivation_level = st.slider("Motivation Level", 1, 10, 7)

st.markdown(
    '<div class="section-title">03 — Additional Factors</div>'
    '<div class="section-subtitle">A few more details for your prediction.</div>',
    unsafe_allow_html=True
)

c6, c7 = st.columns(2)

with c6:
    smoker = st.toggle("🚬 Smoker")

with c7:
    injury_last_3_months = st.toggle("🩹 Injury in the last 3 months")

# -------------------------
# Prediction
# -------------------------
st.markdown("---")

if st.button("✦  Calculate My Progress", use_container_width=True):

    body_progress = (
        program_consistency * 4
        + meal_quality * 3
        + motivation_level * 2.5
        + sleep_hours * 2
        + workout_days_per_week * 2.5
        + cardio_days_per_week * 1.5
        + protein_grams * 0.05
        + water_liters * 1.5
        + steps_per_day * 0.0003
        - stress_level * 3
        - int(smoker) * 8
        - int(injury_last_3_months) * 10
    )

    body_progress = float(np.clip(body_progress, 0, 100))
    goal_achieved = body_progress >= 70

    st.markdown(
        '<div class="section-title">04 — Your Results</div>'
        '<div class="section-subtitle">Your personalized progress overview.</div>',
        unsafe_allow_html=True
    )

    r1, r2 = st.columns([1.1, 1])

    with r1:
        st.markdown(f"""
        <div class="result-card">
            <div class="result-label">Estimated Progress Score</div>
            <div class="result-number">{body_progress:.1f}%</div>
            <div class="result-message">
                {"You're on your way ✨" if goal_achieved else "Keep building your habits 🌱"}
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.progress(int(body_progress))
        st.caption("Progress score generated by the current rule-based formula.")

    with r2:
        st.metric(
            "Goal Threshold",
            "70%",
            delta=f"{body_progress - 70:+.1f} points"
        )

        if goal_achieved:
            st.success("✦ Score target reached!")
        else:
            st.info("✦ Keep focusing on consistency.")

        st.caption(
            "This is a heuristic score, not a medically "
            "validated prediction of actual body changes."
        )

# -------------------------
# Footer
# -------------------------
st.markdown("""
<div class="footer">
    FITAURA STUDIO &nbsp; ✦ &nbsp; BUILD YOUR BETTER SELF
</div>
""", unsafe_allow_html=True)