from tkinter import *
from tkinter import messagebox
from database import Database

class GerirPecas:
    def __init__(self, master):
        self.db = Database()
        self.master = master
        self.master.title("Gerir Peças")
        
        # Labels e Entradas
        Label(master, text="Código").grid(row=0, column=0)
        self.codigo_entry = Entry(master)
        self.codigo_entry.grid(row=0, column=1)
        
        Label(master, text="Descrição").grid(row=1, column=0)
        self.descricao_entry = Entry(master)
        self.descricao_entry.grid(row=1, column=1)
        
        Label(master, text="Fabricante").grid(row=2, column=0)
        self.fabricante_entry = Entry(master)
        self.fabricante_entry.grid(row=2, column=1)
        
        Label(master, text="Fornecedor").grid(row=3, column=0)
        self.fornecedor_entry = Entry(master)
        self.fornecedor_entry.grid(row=3, column=1)
        
        Label(master, text="Quantidade").grid(row=4, column=0)
        self.quantidade_entry = Entry(master)
        self.quantidade_entry.grid(row=4, column=1)
        
        Label(master, text="Preço de Venda").grid(row=5, column=0)
        self.preco_venda_entry = Entry(master)
        self.preco_venda_entry.grid(row=5, column=1)
        
        # Botões
        Button(master, text="Salvar", command=self.cadastrar_peca).grid(row=6, column=0)
        Button(master, text="Listar Peças", command=self.listar_pecas).grid(row=6, column=1)
        Button(master, text="Deletar", command=self.deletar_peca).grid(row=6, column=2)
        
        # Listbox para Exibir Peças
        self.pecas_listbox = Listbox(master)
        self.pecas_listbox.grid(row=7, column=0, columnspan=3)
    
    def cadastrar_peca(self):
        codigo = self.codigo_entry.get()
        descricao = self.descricao_entry.get()
        fabricante = self.fabricante_entry.get()
        fornecedor = self.fornecedor_entry.get()
        quantidade = self.quantidade_entry.get()
        preco_venda = self.preco_venda_entry.get()
        
        if codigo and descricao:
            try:
                self.db.cursor.execute('''INSERT INTO Pecas (codigo, descricao, fabricante, fornecedor, quantidade, preco_venda) 
                                          VALUES (?, ?, ?, ?, ?, ?)''', 
                                          (codigo, descricao, fabricante, fornecedor, quantidade, preco_venda))
                self.db.conn.commit()
                messagebox.showinfo("Sucesso", "Peça cadastrada com sucesso!")
                self.listar_pecas()
            except sqlite3.IntegrityError:
                messagebox.showerror("Erro", "Código da peça já cadastrado.")
        else:
            messagebox.showerror("Erro", "Todos os campos obrigatórios.")
    
    def listar_pecas(self):
        self.pecas_listbox.delete(0, END)
        self.db.cursor.execute("SELECT * FROM Pecas")
        for row in self.db.cursor.fetchall():
            self.pecas_listbox.insert(END, f"{row[1]} - {row[2]} - Quantidade: {row[4]} - Preço: {row[5]}")
    
    def deletar_peca(self):
        selected = self.pecas_listbox.curselection()
        if selected:
            peca = self.pecas_listbox.get(selected[0])
            codigo = peca.split(" - ")[0]
            confirm = messagebox.askyesno("Confirmação", "Tem certeza que deseja excluir esta peça?")
            if confirm:
                self.db.cursor.execute("DELETE FROM Pecas WHERE codigo = ?", (codigo,))
                self.db.conn.commit()
                self.listar_pecas()
                messagebox.showinfo("Sucesso", "Peça excluída com sucesso.")
        else:
            messagebox.showerror("Erro", "Selecione uma peça para excluir.")
    
    def close(self):
        self.db.close()
