
import streamlit as st
import numpy as np

# ==========================================
# PAGE CONFIG
# ==========================================
st.set_page_config(
    page_title="FitAura | Fitness Dashboard",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# CUSTOM CSS - CLOUD FRIENDLY
# ==========================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --background: #F8F6FC;
    --white: #FFFFFF;
    --purple: #8B70C9;
    --purple-dark: #694DA7;
    --lavender: #EEE7FA;
    --pink: #F8E8F1;
    --text: #30283F;
    --muted: #837B91;
    --border: #E8E0F2;
}

/* Main background */
.stApp {
    background: linear-gradient(135deg, #F8F6FC 0%, #FCF8FC 100%);
    color: var(--text);
    font-family: 'Inter', sans-serif;
}

[data-testid="stAppViewContainer"] {
    background: transparent;
}

[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 1150px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Typography */
h1, h2, h3, h4, p, label {
    font-family: 'Inter', sans-serif;
}

h1, h2, h3, h4 {
    color: var(--text);
}

/* Hero banner */
.hero {
    background: linear-gradient(120deg, #E9DFFC 0%, #FBEAF2 100%);
    border: 1px solid #FFFFFF;
    border-radius: 26px;
    padding: 34px;
    margin-bottom: 25px;
    box-shadow: 0 8px 28px rgba(95, 67, 137, 0.06);
}

.hero-label {
    color: #7658AC;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 3px;
    margin-bottom: 14px;
}

.hero-title {
    color: #30243F !important;
    font-size: clamp(30px, 4vw, 46px);
    font-weight: 800;
    line-height: 1.15;
    letter-spacing: -1.5px;
    margin: 0 0 14px 0;
}

.hero-description {
    color: #6F647F !important;
    font-size: 14px;
    line-height: 1.9;
    max-width: 620px;
    margin: 0;
}

/* Section headings */
.section-title {
    color: #40344F !important;
    font-size: 19px;
    font-weight: 800;
    margin: 25px 0 5px 0;
}

.section-description {
    color: var(--muted) !important;
    font-size: 13px;
    margin-bottom: 18px;
}

/* Cards - use Streamlit's public container border option */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background: #FFFFFF !important;
    border: 1px solid #E8E0F2 !important;
    border-radius: 20px !important;
    box-shadow: 0 5px 22px rgba(75, 52, 108, 0.045);
}

/* Card headings */
div[data-testid="stVerticalBlockBorderWrapper"] h3,
div[data-testid="stVerticalBlockBorderWrapper"] h4 {
    color: #4D3C65 !important;
}

/* Labels */
.stApp label,
.stApp [data-testid="stWidgetLabel"] p {
    color: #51485F !important;
    font-weight: 500;
    font-size: 13px;
}

/* Slider */
.stSlider [data-baseweb="slider"] [role="slider"] {
    background-color: #8B70C9 !important;
    border-color: #8B70C9 !important;
}

.stSlider [data-baseweb="slider"] > div > div {
    background-color: #8B70C9;
}

/* Toggle */
.stToggle label {
    color: #51485F !important;
}

/* Primary button */
.stButton > button {
    width: 100%;
    min-height: 52px;
    border-radius: 15px;
    border: 1px solid #8B70C9;
    background: linear-gradient(100deg, #8568C2, #AD8BDC);
    color: #FFFFFF !important;
    font-size: 15px;
    font-weight: 800;
    transition: all 0.2s ease;
    box-shadow: 0 7px 18px rgba(139, 112, 201, 0.20);
}

.stButton > button:hover {
    background: linear-gradient(100deg, #7355B1, #9B7ACD);
    border-color: #7355B1;
    color: #FFFFFF !important;
    transform: translateY(-1px);
}

/* Metrics */
div[data-testid="stMetric"] {
    background: #FFFFFF;
    border: 1px solid #E8E0F2;
    border-radius: 18px;
    padding: 20px;
}

div[data-testid="stMetricLabel"] {
    color: #837B91 !important;
}

div[data-testid="stMetricValue"] {
    color: #7558B3 !important;
    font-weight: 800;
}

/* Result panel */
.result-card {
    background: linear-gradient(135deg, #EEE6FC, #FBEAF2);
    border: 1px solid #E7DDF4;
    border-radius: 23px;
    padding: 28px 20px;
    text-align: center;
    margin: 8px 0 15px 0;
}

.result-label {
    color: #796A8B !important;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.result-number {
    color: #7354AD !important;
    font-size: clamp(38px, 6vw, 55px);
    font-weight: 800;
    letter-spacing: -2px;
    margin: 10px 0;
}

.result-message {
    color: #48375E !important;
    font-size: 16px;
    font-weight: 700;
}

/* Progress bar */
div[data-testid="stProgressBar"] > div {
    background: #E8DFF4;
    border-radius: 20px;
}

div[data-testid="stProgressBar"] > div > div {
    background: linear-gradient(90deg, #9275D0, #E6A7CA);
    border-radius: 20px;
}

/* Alert boxes */
div[data-testid="stAlert"] {
    border-radius: 15px;
}

/* Footer */
.footer {
    text-align: center;
    color: #A098B0 !important;
    font-size: 11px;
    letter-spacing: 2px;
    padding-top: 30px;
    padding-bottom: 10px;
}

/* Mobile responsive */
@media (max-width: 640px) {
    .block-container {
        padding: 1rem 1rem 2rem 1rem;
    }

    .hero {
        padding: 24px 20px;
        border-radius: 21px;
    }

    .hero-title {
        letter-spacing: -0.8px;
    }

    .result-card {
        padding: 23px 15px;
    }
}
</style>
""", unsafe_allow_html=True)


# ==========================================
# HERO
# ==========================================
st.markdown("""
<div class="hero">
    <div class="hero-label">✦ FITAURA STUDIO</div>
    <div class="hero-title">
        Small habits.<br>Stronger you.
    </div>
    <p class="hero-description">
        Your personal fitness dashboard. Explore how your daily
        habits, nutrition, activity, and recovery contribute
        to your fitness journey.
    </p>
</div>
""", unsafe_allow_html=True)


# ==========================================
# SECTION 01 - PERSONAL PROFILE
# ==========================================
st.markdown("""
<div class="section-title">01 — Your Profile</div>
<div class="section-description">
Start with your personal baseline.
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    with st.container(border=True):
        st.markdown("#### 🧍 Personal")
        age = st.slider("Age", 16, 60, 25)
        height_cm = st.slider("Height (cm)", 150, 200, 170)
        weight_kg = st.slider("Weight (kg)", 45, 140, 70)

with col2:
    with st.container(border=True):
        st.markdown("#### 🌙 Recovery")
        sleep_hours = st.slider("Sleep Hours", 3, 10, 7)
        stress_level = st.slider("Stress Level", 1, 10, 5)
        water_liters = st.slider(
            "Water (L/day)", 0.5, 7.0, 2.5, step=0.5
        )

with col3:
    with st.container(border=True):
        st.markdown("#### ⚡ Activity")
        steps_per_day = st.slider(
            "Steps per Day", 500, 25000, 8000, step=500
        )
        workout_days_per_week = st.slider(
            "Workout Days/Week", 0, 7, 3
        )
        cardio_days_per_week = st.slider(
            "Cardio Days/Week", 0, 7, 2
        )


# ==========================================
# SECTION 02 - LIFESTYLE
# ==========================================
st.markdown("""
<div class="section-title">02 — Your Lifestyle</div>
<div class="section-description">
Build your progress through everyday choices.
</div>
""", unsafe_allow_html=True)

col4, col5 = st.columns(2)

with col4:
    with st.container(border=True):
        st.markdown("#### 🥑 Nutrition")
        protein_grams = st.slider(
            "Protein (g/day)", 30, 260, 120
        )
        meal_quality = st.slider(
            "Meal Quality", 1, 10, 6
        )

with col5:
    with st.container(border=True):
        st.markdown("#### 🎯 Mindset")
        program_consistency = st.slider(
            "Program Consistency", 1, 10, 6
        )
        motivation_level = st.slider(
            "Motivation Level", 1, 10, 7
        )


# ==========================================
# SECTION 03 - ADDITIONAL FACTORS
# ==========================================
st.markdown("""
<div class="section-title">03 — Additional Factors</div>
<div class="section-description">
Include other lifestyle factors.
</div>
""", unsafe_allow_html=True)

col6, col7 = st.columns(2)

with col6:
    with st.container(border=True):
        smoker = st.toggle("🚬 Smoker")

with col7:
    with st.container(border=True):
        injury_last_3_months = st.toggle(
            "🩹 Injury in the last 3 months"
        )


# ==========================================
# PREDICTION
# ==========================================
st.markdown("---")

if st.button("✦  Calculate My Progress"):

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

    st.markdown("""
    <div class="section-title">04 — Your Results</div>
    <div class="section-description">
    Your personalized fitness score.
    </div>
    """, unsafe_allow_html=True)

    result_col1, result_col2 = st.columns([1.15, 1])

    with result_col1:
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
        st.caption("Score calculated using your selected lifestyle inputs.")

    with result_col2:
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
            "This is a rule-based estimate, not a medically "
            "validated prediction of actual body changes."
        )


# ==========================================
# FOOTER
# ==========================================
st.markdown("""
<div class="footer">
    FITAURA STUDIO &nbsp; ✦ &nbsp; BUILD YOUR BETTER SELF
</div>
""", unsafe_allow_html=True)