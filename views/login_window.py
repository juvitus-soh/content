import tkinter as tk
from tkinter import messagebox

class LoginWindow:
    def __init__(self, root, auth_controller):
        self.root = root
        self.root.title("Login")
        self.auth_controller = auth_controller

        self.label_user_code = tk.Label(root, text="User Code")
        self.label_user_code.pack(pady=10)

        self.entry_user_code = tk.Entry(root)
        self.entry_user_code.pack(pady=5)

        self.label_password = tk.Label(root, text="Password")
        self.label_password.pack(pady=10)

        self.entry_password = tk.Entry(root, show="*")
        self.entry_password.pack(pady=5)

        self.button_login = tk.Button(root, text="Login", command=self.login)
        self.button_login.pack(pady=20)

    def login(self):
        user_code = self.entry_user_code.get()
        password = self.entry_password.get()

        if self.auth_controller.authenticate(user_code, password):
            messagebox.showinfo("Login Successful", "Welcome!")
            self.root.destroy()
        else:
            messagebox.showerror("Login Failed", "Invalid User Code or Password")
