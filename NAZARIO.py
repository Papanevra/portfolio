import tkinter as tk
from tkinter import messagebox

# Инициализация приложения
root = tk.Tk()
root.title("Трекер бюджета")
root.geometry("600x600")

total_budget = 0
expenses = []

def update_budget_label():
    budget_label.config(text=f"Общий бюджет: {total_budget}")

def update_expenses_listbox():
    expenses_listbox.delete(0, tk.END)
    for expense in expenses:
        expenses_listbox.insert(tk.END, f"{expense[0]} - {expense[1]}")

def add_expense():
    global total_budget
    try:
        amount = float(amount_entry.get())
        description = desc_entry.get()

        if amount <= 0:
            raise ValueError

        expenses.append((amount, description))
        total_budget -= amount

        update_budget_label()
        update_expenses_listbox()

        amount_entry.delete(0, tk.END)
        desc_entry.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите действительную сумму и описание.")

def remove_expense():
    global total_budget
    try:
        selected_idx = expenses_listbox.curselection()[0]
        expense = expenses[selected_idx]

        expenses.pop(selected_idx)
        total_budget += expense[0]

        update_budget_label()
        update_expenses_listbox()

    except IndexError:
        messagebox.showerror("Ошибка", "Пожалуйста, выберите расход для удаления.")

# Виджеты интерфейса
budget_label = tk.Label(root, text="Общий бюджет: 0")
budget_label.pack(pady=10)

amount_label = tk.Label(root, text="Сумма: ")
amount_label.pack(pady=5)

amount_entry = tk.Entry(root)
amount_entry.pack(pady=5)

desc_label = tk.Label(root, text="Описание: ")
desc_label.pack(pady=5)

desc_entry = tk.Entry(root)
desc_entry.pack(pady=5)

add_button = tk.Button(root, text="Добавить расход", command=add_expense)
add_button.pack(pady=10)

expenses_listbox = tk.Listbox(root, width=50, height=20)
expenses_listbox.pack(pady=10)

remove_button = tk.Button(root, text="Удалить расход", command=remove_expense)
remove_button.pack(pady=10)

#Запуск главного цикла
root.mainloop()