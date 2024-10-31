import streamlit as st
import pickle
import pandas as pd

# Load model
pipe = pickle.load(open('pipe.pkl', 'rb'))

# Data
teams = [
    'Sunrisers Hyderabad', 'Mumbai Indians', 'Royal Challengers Bangalore',
    'Kolkata Knight Riders', 'Kings XI Punjab', 'Chennai Super Kings',
    'Rajasthan Royals', 'Delhi Capitals'
]

cities = sorted([
    'Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
    'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
    'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
    'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
    'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
    'Sharjah', 'Mohali', 'Bengaluru'
])

# App Config
st.set_page_config(page_title="IPL Win Predictor", page_icon="🏏", layout="centered")

# Custom CSS for background and styling
st.markdown("""
    <style>
        body {
            background: linear-gradient(to right, #ffe259, #ffa751);
        }
        .big-font {
            font-size: 24px !important;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>🏆 IPL Win Predictor 2025</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Predict the outcome of any IPL match live during play!</p>", unsafe_allow_html=True)
st.markdown("---")

# Input: Teams
col1, col2 = st.columns(2)
with col1:
    batting_team = st.selectbox('🟢 Batting Team', sorted(teams))
with col2:
    bowling_team = st.selectbox('🔵 Bowling Team', sorted(teams))

# Input: City and target
st.subheader("📍 Match Details")
selected_city = st.selectbox('🏟️ Match Venue', cities)
target = st.number_input('🎯 Target Score', min_value=1)

# Input: Live match data
st.subheader("📈 Live Match Stats")
col3, col4, col5 = st.columns(3)
with col3:
    score = st.number_input('🏏 Current Score', min_value=0)
with col4:
    overs = st.number_input('⏱️ Overs Completed', min_value=0.0, max_value=20.0, step=0.1)
with col5:
    wickets = st.number_input('❌ Wickets Lost', min_value=0, max_value=10)

# Prediction button
st.markdown("### 🔮 Predict the Outcome")
if st.button("⚡ Predict Now"):

    try:
        # Calculations
        runs_left = target - score
        balls_left = 120 - (overs * 6)
        remaining_wickets = 10 - wickets
        crr = score / overs if overs > 0 else 0
        rrr = (runs_left * 6) / balls_left if balls_left > 0 else 0

        # Input dataframe
        input_df = pd.DataFrame({
            'batting_team': [batting_team],
            'bowling_team': [bowling_team],
            'city': [selected_city],
            'runs_left': [runs_left],
            'balls_left': [balls_left],
            'wickets': [remaining_wickets],
            'total_runs_x': [target],
            'crr': [crr],
            'rrr': [rrr]
        })

        # Prediction
        result = pipe.predict_proba(input_df)
        loss = result[0][0]
        win = result[0][1]

        # Result Display
        st.markdown("---")
        st.subheader("📊 Probability of Winning")
        st.metric(label=f"{batting_team}", value=f"{round(win * 100)}%", delta_color="normal")
        st.metric(label=f"{bowling_team}", value=f"{round(loss * 100)}%", delta_color="inverse")

        st.progress(win)

        st.markdown("### 🧮 Match Summary")
        st.markdown(f"**Runs Needed:** {runs_left} | **Balls Left:** {int(balls_left)} | **Wickets in Hand:** {remaining_wickets}")
        st.markdown(f"**Current Run Rate (CRR):** {round(crr, 2)} | **Required Run Rate (RRR):** {round(rrr, 2)}")

    except Exception as e:
        st.error("⚠️ Could not predict. Please check the input values.")

st.markdown("---")
st.markdown("<h6 style='text-align: center; color: gray;'>Built with ❤️ using Streamlit - 2025 Edition</h6>", unsafe_allow_html=True)
