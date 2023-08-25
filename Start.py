import tkinter as tk
import sqlite3


connection = sqlite3.connect("data.csv")
cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users (name TEXT)""")
connection.commit()


def add_user(name):
    cursor.execute("""INSERT INTO users (name) VALUES (?)""", [name])
    connection.commit()

def get_users():
    cursor.execute("""SELECT name FROM users""")
    return cursor.fetchall()


def add_letter(letter):
    text = text_var.get()
    text += letter
    text_var.set(text)

def register():
    name = text_var.get()
    add_user(name)
    label.config(text=f"Команда «{name}» зарегистрирована.\nПроходите к следующей локации.")
    text_var.set("")

def delete_last_letter():
    text = text_var.get()
    text = text[:-1]
    text_var.set(text)


root = tk.Tk()
root.title("Регистрация команды")
root.geometry("600x450")

text_label = tk.Label(root, text="Введите название команды:", font=('Arial', 16))
text_label.pack()

text_var = tk.StringVar()
text_entry = tk.Entry(root, textvariable=text_var, width=30)
text_entry.pack(pady=10)
label = tk.Label(root, text="", font=("Arial", 16))
label.pack(pady=10)

letters = [
    "Ё1234567890-",
    "ЙЦУКЕНГШЩЗХЪ", 
    "ФЫВАПРОЛДЖЭ", 
    "ЯЧСМИТЬБЮ",
]

letters_frame = tk.Frame(root)
letters_frame.pack()

for row in letters:
    row_frame = tk.Frame(letters_frame)
    row_frame.pack()
    for letter in row:
        button = tk.Button(row_frame, text=letter.upper(), width=4, height=2, 
                           command=lambda l=letter: add_letter(l))
        button.pack(side="left", padx=2, pady=2)


delete_button = tk.Button(root, text="Удалить", width=10, height=2, command=delete_last_letter)
delete_button.pack(pady=10)


register_button = tk.Button(root, text="Зарегистрироваться", width=20, height=2, command=register)
register_button.pack(pady=10)

root.update_idletasks()
width = root.winfo_width()
height = root.winfo_height()
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry("{}x{}+{}+{}".format(width, height, x, y))

def show_users():
    all_users = get_users()
    users_text = "\n".join([f"{i + 1}. {user[0]}" for i, user in enumerate(all_users)])
    users_label.config(text=users_text)

users_label = tk.Label(root, text="", font=("Arial", 12))
users_label.pack(pady=10)

show_users_button = tk.Button(root, text="Показать пользователей", width=20, height=2, command=show_users)
show_users_button.pack(pady=10)

root.mainloop()

connection.close()