import json
from datetime import datetime
import os

class ExpenseTracker:
    def __init__(self, filename='expenses.json'):
        self.filename = filename
        self.expenses = self.load_expenses()

    def load_expenses(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        return []

    def save_expenses(self):
        with open(self.filename, 'w') as f:
            json.dump(self.expenses, f, indent=4)

    def add_expense(self, amount, category, note):
        expense = {
            'amount': amount,
            'category': category,
            'note': note,
            'date': datetime.now().strftime("%Y-%m-%d")
        }
        self.expenses.append(expense)
        self.save_expenses()

    def get_summary(self):
        summary = {}
        for e in self.expenses:
            cat = e['category']
            summary[cat] = summary.get(cat, 0) + float(e['amount'])
        return summary

    def get_all_expenses(self):
        return self.expenses
