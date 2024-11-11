from tkinter import *
from tkinter import messagebox
from database import Database

class GerirFabricantes:
    def __init__(self, master):
        self.db = Database()
        self.master = master
        self.master.title("Gerir Fabricantes")
        
        # Labels e Entradas
        Label(master, text="Razão Social").grid(row=0, column=0)
        self.razao_social_entry = Entry(master)
        self.razao_social_entry.grid(row=0, column=1)
        
        Label(master, text="CNPJ").grid(row=1, column=0)
        self.cnpj_entry = Entry(master)
        self.cnpj_entry.grid(row=1, column=1)
        
        # Botões
        Button(master, text="Salvar", command=self.cadastrar_fabricante).grid(row=2, column=0)
        Button(master, text="Listar Fabricantes", command=self.listar_fabricantes).grid(row=2, column=1)
        Button(master, text="Deletar", command=self.deletar_fabricante).grid(row=2, column=2)
        
        # Listbox para Exibir Fabricantes
        self.fabricante_listbox = Listbox(master)
        self.fabricante_listbox.grid(row=3, column=0, columnspan=3)
    
    def cadastrar_fabricante(self):
        razao_social = self.razao_social_entry.get()
        cnpj = self.cnpj_entry.get()
        
        if razao_social and cnpj:
            try:
                self.db.cursor.execute("INSERT INTO Fabricantes (razao_social, cnpj) VALUES (?, ?)", (razao_social, cnpj))
                self.db.conn.commit()
                messagebox.showinfo("Sucesso", "Fabricante cadastrado com sucesso!")
                self.listar_fabricantes()
            except sqlite3.IntegrityError:
                messagebox.showerror("Erro", "CNPJ já cadastrado.")
        else:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios.")
    
    def listar_fabricantes(self):
        self.fabricante_listbox.delete(0, END)
        self.db.cursor.execute("SELECT * FROM Fabricantes")
        for row in self.db.cursor.fetchall():
            self.fabricante_listbox.insert(END, f"{row[1]} - {row[2]}")
    
    def deletar_fabricante(self):
        selected = self.fabricante_listbox.curselection()
        if selected:
            fabricante = self.fabricante_listbox.get(selected[0])
            cnpj = fabricante.split(" - ")[1]
            confirm = messagebox.askyesno("Confirmação", "Tem certeza que deseja excluir este fabricante?")
            if confirm:
                self.db.cursor.execute("DELETE FROM Fabricantes WHERE cnpj = ?", (cnpj,))
                self.db.conn.commit()
                self.listar_fabricantes()
                messagebox.showinfo("Sucesso", "Fabricante excluído com sucesso.")
        else:
            messagebox.showerror("Erro", "Selecione um fabricante para excluir.")
    
    def close(self):
        self.db.close()
