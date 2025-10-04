import streamlit as st
from expense_tracker import ExpenseTracker
import pandas as pd

# Initialize the tracker
tracker = ExpenseTracker()

# Streamlit UI setup
st.set_page_config(page_title="Simple Expense Tracker", page_icon="💰", layout="centered")
st.title("💰 Simple Expense Tracker")

# Input section
amount = st.number_input("Amount", min_value=0.0, step=0.01)
category = st.text_input("Category (food, travel, etc.)")
note = st.text_input("Note")

col1, col2 = st.columns(2)

with col1:
    if st.button("Add Expense"):
        if amount > 0 and category:
            tracker.add_expense(amount, category, note)
            st.success(f"✅ Added: ₹{amount} for {category}")
        else:
            st.error("Please enter both amount and category.")

with col2:
    if st.button("View Summary"):
        summary = tracker.get_summary()
        if summary:
            st.subheader("📊 Summary by Category")
            df = pd.DataFrame(summary.items(), columns=["Category", "Total (₹)"])
            st.table(df)
            st.bar_chart(df.set_index("Category"))
        else:
            st.info("No expenses yet. Add one first!")

# Display all expenses below
st.divider()
st.subheader("📋 All Expenses")
expenses = tracker.get_all_expenses()
if expenses:
    df_exp = pd.DataFrame(expenses)
    st.dataframe(df_exp)
else:
    st.info("No expenses recorded yet.")
