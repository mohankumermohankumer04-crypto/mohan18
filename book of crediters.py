import tkinter as tk
from tkinter import ttk, messagebox

total_balance = 0

def add_record():
    global total_balance

    name = entry_name.get()
    amount = entry_amount.get()
    tran_type = tran_var.get()

    if name == "" or amount == "":
        messagebox.showwarning("Error", "Please fill all fields")
        return

    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Error", "Enter valid amount")
        return

    if tran_type == "Credit":
        balance = amount
    else:
        balance = -amount

    total_balance += balance

    table.insert("", tk.END, values=(name, tran_type, amount, balance))
    update_total()

    clear_fields()

def delete_record():
    global total_balance
    selected = table.selection()

    if not selected:
        messagebox.showwarning("Error", "Select a record to delete")
        return

    for item in selected:
        bal = float(table.item(item, "values")[3])
        total_balance -= bal
        table.delete(item)

    update_total()

def clear_fields():
    entry_name.delete(0, tk.END)
    entry_amount.delete(0, tk.END)
    tran_var.set("Credit")

def update_total():
    total_label.config(text=f"Akida Balance: ₹ {total_balance:.2f}")

# Main window
root = tk.Tk()
root.title("BOOK OF CREDITORS")
root.geometry("800x500")

tk.Label(root, text="BOOK OF CREDITORS",
         font=("Arial", 16, "bold"), fg="darkblue").pack(pady=10)

# Input Frame
frame = tk.Frame(root, bd=2, relief="groove")
frame.pack(pady=5)

tk.Label(frame, text="Creditor Name").grid(row=0, column=0, padx=5, pady=5)
entry_name = tk.Entry(frame)
entry_name.grid(row=0, column=1)

tk.Label(frame, text="Amount").grid(row=1, column=0, padx=5, pady=5)
entry_amount = tk.Entry(frame)
entry_amount.grid(row=1, column=1)

tk.Label(frame, text="Transaction").grid(row=2, column=0, padx=5, pady=5)

tran_var = tk.StringVar(value="Credit")
tk.Radiobutton(frame, text="Credit", variable=tran_var, value="Credit").grid(row=2, column=1, sticky="w")
tk.Radiobutton(frame, text="Debit", variable=tran_var, value="Debit").grid(row=2, column=2, sticky="w")

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add Entry", width=15, command=add_record).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Delete Entry", width=15, command=delete_record).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Clear", width=15, command=clear_fields).grid(row=0, column=2, padx=5)

# Table
columns = ("Creditor Name", "Type", "Amount", "Balance")
table = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    table.heading(col, text=col)
    table.column(col, width=180)

table.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

# Bottom Balance
total_label = tk.Label(root, text="Akida Balance: ₹ 0.00",
                       font=("Arial", 13, "bold"), fg="green")
total_label.pack(pady=10)

root.mainloop()
