AI-Powered Expense Tracker

A simple and smart Expense Tracker App built using Python and Streamlit, designed to help users manage and analyze their daily expenses effortlessly.
This project was created as part of an internship assessment to demonstrate problem-solving, resourcefulness, and documentation skills.

# About the Project

The Expense Tracker allows users to:
Add daily expenses (food, travel, rent, etc.)
View and filter weekly/monthly summaries
Automatically analyze spending patterns using simple AI logic
Store data locally (CSV-based)
The goal was to create a minimal but functional AI-powered app that helps users understand their spending behavior.

# Features

> Add daily expenses (category, amount, date, note)
> Visualize spending with charts (powered by Streamlit)
> View total and category-wise summaries
> AI-based text insight on spending trend (simple rule-based or model call)
> Data saved locally — no database needed
>  Clean UI built using Streamlit

# Tech Stack
Tool	Purpose
Python 3	Core logic
Streamlit	Interactive web UI
Pandas	Data handling
Matplotlib / Plotly	Charts & graphs
# Installation & Setup
1️ Clone the Repository
git clone https://github.com/VAIBHAVVARORA/Expense_Tracker.git
cd Expense_Tracker

2️ Create a Virtual Environment
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate  # On Mac/Linux

3️ Install Dependencies
pip install -r requirements.txt

4️ Run the App
streamlit run app.py

#   ----------Example Usage ------------

Click “Add Expense” to enter new spending.

Choose a category (Food, Travel, Rent, etc.)

# The app shows:

Total expenses
Top spending category
Daily/weekly summaries

# Deployment

The app is deployed on Streamlit Cloud:
# ----- Live Demo -------
https://trackyourexpensess.streamlit.app/

# Documentation

Every step, from setup to deployment, was documented during development:

Installed Python + Streamlit.

Built a CLI version first.

Upgraded to Streamlit UI.

Debugged CSV handling and visualization.

Deployed on Streamlit Cloud.

All progress was committed and documented in this repo.


# Learnings

Basics of Streamlit web apps.

Using Pandas for simple data analysis.

Structuring and deploying a small AI project.

Documenting each step clearly for review.