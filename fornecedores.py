from tkinter import *
from tkinter import messagebox
from database import Database

class GerirFornecedores:
    def __init__(self, master):
        self.db = Database()
        self.master = master
        self.master.title("Gerir Fornecedores")
        
        # Labels e Entradas
        Label(master, text="Razão Social").grid(row=0, column=0)
        self.razao_social_entry = Entry(master)
        self.razao_social_entry.grid(row=0, column=1)
        
        Label(master, text="CNPJ").grid(row=1, column=0)
        self.cnpj_entry = Entry(master)
        self.cnpj_entry.grid(row=1, column=1)
        
        # Botões
        Button(master, text="Salvar", command=self.cadastrar_fornecedor).grid(row=2, column=0)
        Button(master, text="Listar Fornecedores", command=self.listar_fornecedores).grid(row=2, column=1)
        Button(master, text="Deletar", command=self.deletar_fornecedor).grid(row=2, column=2)
        
        # Listbox para Exibir Fornecedores
        self.fornecedor_listbox = Listbox(master)
        self.fornecedor_listbox.grid(row=3, column=0, columnspan=3)
    
    def cadastrar_fornecedor(self):
        razao_social = self.razao_social_entry.get()
        cnpj = self.cnpj_entry.get()
        
        if razao_social and cnpj:
            try:
                self.db.cursor.execute("INSERT INTO Fornecedores (razao_social, cnpj) VALUES (?, ?)", (razao_social, cnpj))
                self.db.conn.commit()
                messagebox.showinfo("Sucesso", "Fornecedor cadastrado com sucesso!")
                self.listar_fornecedores()
            except sqlite3.IntegrityError:
                messagebox.showerror("Erro", "CNPJ já cadastrado.")
        else:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios.")
    
    def listar_fornecedores(self):
        self.fornecedor_listbox.delete(0, END)
        self.db.cursor.execute("SELECT * FROM Fornecedores")
        for row in self.db.cursor.fetchall():
            self.fornecedor_listbox.insert(END, f"{row[1]} - {row[2]}")
    
    def deletar_fornecedor(self):
        selected = self.fornecedor_listbox.curselection()
        if selected:
            fornecedor = self.fornecedor_listbox.get(selected[0])
            cnpj = fornecedor.split(" - ")[1]
            confirm = messagebox.askyesno("Confirmação", "Tem certeza que deseja excluir este fornecedor?")
            if confirm:
                self.db.cursor.execute("DELETE FROM Fornecedores WHERE cnpj = ?", (cnpj,))
                self.db.conn.commit()
                self.listar_fornecedores()
                messagebox.showinfo("Sucesso", "Fornecedor excluído com sucesso.")
        else:
            messagebox.showerror("Erro", "Selecione um fornecedor para excluir.")
    
    def close(self):
        self.db.close()
