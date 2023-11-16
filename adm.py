import tkinter as tk
from tkinter import simpledialog, messagebox
from misc import auth, tools, prints

class AdmApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Administração")
        self.root.geometry("600x400")

        # Barra de menu
        menubar = tk.Menu(root)
        root.config(menu=menubar)

        # Menu de autenticação
        auth_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Autenticação", menu=auth_menu)
        auth_menu.add_command(label="Autenticar", command=self.authenticate_and_show_menu)

        # Componentes principais (inicialmente desativados)
        self.label = tk.Label(root, text="Escolha uma opção:")
        self.label.pack(pady=10)

        self.create_button = tk.Button(root, text="Criar Usuário", command=self.create_user, state=tk.DISABLED)
        self.create_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Deletar Usuário", command=self.delete_user, state=tk.DISABLED)
        self.delete_button.pack(pady=5)

        self.change_password_button = tk.Button(root, text="Alterar Senha", command=self.change_password, state=tk.DISABLED)
        self.change_password_button.pack(pady=5)

        self.view_users_button = tk.Button(root, text="Ver Usuários", command=self.view_users, state=tk.DISABLED)
        self.view_users_button.pack(pady=5)

        self.view_users_text = tk.Text(root, height=10, width=50)
        self.view_users_text.pack(pady=5)

    def create_user(self):
        username = simpledialog.askstring("Criar Usuário", "Insira o nome de usuário:")
        password = simpledialog.askstring("Criar Usuário", "Insira a senha:")
        if username and password:
            auth.newUser(user=username, password=password)
            messagebox.showinfo("Sucesso", f"Usuário {username} criado com sucesso!")

    def delete_user(self):
        username = simpledialog.askstring("Deletar Usuário", "Insira o nome de usuário a ser deletado:")
        if username:
            auth.delete(user=username)
            messagebox.showinfo("Sucesso", f"Usuário {username} deletado com sucesso!")

    def change_password(self):
        username = simpledialog.askstring("Alterar Senha", "Insira o nome de usuário:")
        new_password = simpledialog.askstring("Alterar Senha", "Insira a nova senha:")
        if username and new_password:
            auth.change_password(user=username, new_password=new_password)
            messagebox.showinfo("Sucesso", f"Senha do usuário {username} alterada com sucesso.")

    def view_users(self):
        user_data_list = auth.get_user_data_list()
        if user_data_list:
            users_str = "\n".join([f"Usuário: {user[0]}, Senha: {user[1]}" for user in user_data_list])
            self.view_users_text.delete(1.0, tk.END)
            self.view_users_text.insert(tk.END, users_str)
        else:
            self.view_users_text.delete(1.0, tk.END)
            self.view_users_text.insert(tk.END, "Nenhum usuário cadastrado.")

    def authenticate_and_show_menu(self):
        username = simpledialog.askstring("Autenticação de Administrador", "Insira o nome de usuário:")
        password = simpledialog.askstring("Autenticação de Administrador", "Insira a senha:")

        if username == "yyax" and auth.check(username, password) == "ADM":
            self.enable_menu_buttons()
        else:
            messagebox.showerror("Erro de Autenticação", "Credenciais de administrador inválidas.")

    def enable_menu_buttons(self):
        # Ativa os botões do menu após a autenticação
        self.label.config(text="Escolha uma opção:")
        self.create_button.config(state=tk.NORMAL)
        self.delete_button.config(state=tk.NORMAL)
        self.change_password_button.config(state=tk.NORMAL)
        self.view_users_button.config(state=tk.NORMAL)

    def show_admin_menu(self):
        tools.clear()
        prints.banner()

if __name__ == "__main__":
    root = tk.Tk()
    app = AdmApp(root)
    root.mainloop()
