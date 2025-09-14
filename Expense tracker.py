import tkinter as tk
from tkinter import messagebox
import json
import os

# File to save expenses
FILE_NAME = "expenses.json"

# Load expenses if file exists


def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

# Save expenses to file


def save_expenses():
    with open(FILE_NAME, "w") as f:
        json.dump(expenses, f)

# Add new expense


def add_expense():
    desc = entry_desc.get()
    try:
        amount = float(entry_amount.get())
    except ValueError:
        messagebox.showerror("Error", "Amount must be a number")
        return

    if desc == "":
        messagebox.showerror("Error", "Description cannot be empty")
        return

    expenses.append({"description": desc, "amount": amount})
    listbox.insert(tk.END, f"{desc} - ₦{amount}")
    save_expenses()

    entry_desc.delete(0, tk.END)
    entry_amount.delete(0, tk.END)

# Calculate total


def show_total():
    total = sum(item["amount"] for item in expenses)
    messagebox.showinfo("Total Expenses", f"Total: ₦{total}")


# Initialize window
root = tk.Tk()
root.title("Expense Tracker")

# Input fields
tk.Label(root, text="Description:").grid(row=0, column=0, padx=5, pady=5)
entry_desc = tk.Entry(root)
entry_desc.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Amount (₦):").grid(row=1, column=0, padx=5, pady=5)
entry_amount = tk.Entry(root)
entry_amount.grid(row=1, column=1, padx=5, pady=5)

# Buttons
tk.Button(root, text="Add Expense", command=add_expense).grid(
    row=2, column=0, columnspan=2, pady=10)
tk.Button(root, text="Show Total", command=show_total).grid(
    row=3, column=0, columnspan=2, pady=5)

# Listbox to show expenses
listbox = tk.Listbox(root, width=40, height=10)
listbox.grid(row=4, column=0, columnspan=2, pady=10)

# Load saved expenses
expenses = load_expenses()
for item in expenses:
    listbox.insert(tk.END, f"{item['description']} - ₦{item['amount']}")

root.mainloop()
