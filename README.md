🏏 IPL Win Predictor 2025
Live Match Outcome Predictor for IPL Matches — Built with Machine Learning & Streamlit

📌 About the Project
Cricket is unpredictable, but data can bring us closer to the odds. The IPL Win Predictor 2025 uses historical match data, real-time game conditions, and machine learning to estimate the winning probabilities of both teams during an ongoing IPL match.

With just a few live match inputs — current score, target, overs, and wickets — the app computes the probability of winning for the batting and bowling teams.

🚀 Features
📊 Real-time prediction of match outcome

🧠 ML model trained on historical IPL data

📍 City-based venue impact incorporated

🎯 Uses inputs like target, current score, wickets, and overs

📈 Calculates and displays:

Win/Loss probabilities

Required Run Rate (RRR)

Current Run Rate (CRR)

💻 Interactive UI with Streamlit

🧮 Clean visuals and probability metrics

🛠️ Tech Stack
Python 3.9+

Pandas

Pickle (for model loading)

Scikit-learn (model trained separately)

Streamlit (web UI framework)

📂 How to Use
Clone the repo:

bash
Copy
Edit
git clone https://github.com/shahpriyansh9/Win_Predictor.git
cd Win_Predictor
Install dependencies (if needed):

bash
Copy
Edit
pip install -r requirements.txt
Run the app:

bash
Copy
Edit
streamlit run app.py
Enter:

Batting & bowling teams

Venue

Match situation (score, overs, wickets, target)

Hit “Predict Now” — see live win probabilities and match stats!

🎯 Example
"Mumbai Indians need 50 runs in 30 balls with 6 wickets in hand..."
This app tells you the probability of MI winning right now based on the situation!

📈 Behind the Scenes
The machine learning model was trained on IPL match data (deliveries, outcomes, match metadata).

Core logic handles:

Run & ball calculations

CRR vs RRR comparison

Input transformation for the model

Model training code and datasets are available in the Match_Winner.ipynb notebook.
