from expences import Expence
from storage import save_expences, load_expences
from utils import format_currency, get_today_date
import tkinter as tk
from tkinter import ttk, messagebox

expences = load_expences()

def update_expences_list():
  expence_list.delete(*expence_list.get_children())
  for idx, expence in enumerate(expences):
      expence_list.insert('','end', iid=idx, values=(
          expence.title,
          format_currency(expence.amount),
          expence.category,
          expence.date))
      #update_expences_list()

def update_total_label():
    total = sum( expence.amount for expence in expences)
    total_label.config(text=f"total costs: {format_currency(total)} ")

def add_expence():
    title = title_entry.get()
    amount = amount_entry.get()
    category = category_entry.get()
    date = date_entry.get() or get_today_date()

    if not title or not amount or not category:
        messagebox.showwarning("Error","You have to fill in all the fields.")
        return
    try:
     amount = float(amount)
    except ValueError:
        messagebox.showwarning("Error","The amount must be a number.")
        return

    new_expence = Expence(title, amount, category, date)
    expences.append(new_expence)
    save_expences(expences)
    update_expences_list()

    title_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)
    update_total_label()

def delete_expence():
    selected_item = expence_list.selection()
    if not selected_item:
        messagebox.showwarning("Error","No item selected.")
        return

    idx = int (selected_item[0])
    del expences[idx]
    save_expences(expences)
    update_expences_list()
    update_total_label()

root = tk.Tk()
root.title("Personal expense")
root.geometry("700x500")

form_frame = tk.Frame(root)
form_frame.pack(pady=10)

tk.Label(form_frame,text="Title").grid(row=0,column=0)
title_entry= tk.Entry(form_frame)
title_entry.grid(row=0,column=1)

tk.Label(form_frame,text="Amount").grid(row=0,column=2)
amount_entry= tk.Entry(form_frame)
amount_entry.grid(row=0,column=3)

tk.Label(form_frame,text="Category").grid(row=1,column=0)
category_entry= tk.Entry(form_frame)
category_entry.grid(row=1,column=1)

tk.Label(form_frame,text="Date").grid(row=1,column=2)
date_entry= tk.Entry(form_frame)
date_entry.grid(row=1,column=3)

add_btn = tk.Button(form_frame,text="Add cost",command= add_expence, bg="#4CAF50", fg="white")
add_btn.grid(row=2,column=0, columnspan=5, pady=10)

columns= ("title", "amount", "category", "date")
expence_list = ttk.Treeview(root, columns=columns, show="headings")
expence_list.heading("title", text="Title")
expence_list.heading("amount", text="Amount")
expence_list.heading("category", text="Category")
expence_list.heading("date", text="Date")
expence_list.pack(pady=10, fill= "x")

delete_btn= tk.Button(root, text = "Delete costs",command= delete_expence, bg = "#f44336", fg = "white")
delete_btn.pack(pady=5)

total_label= tk.Label(root, text = "", font=("Arial", 14, "bold") )
total_label.pack(pady=10)

update_expences_list()
update_total_label()

root.mainloop()