from tkinter import *
from tkinter import messagebox
from database import Database

class GerirVeiculos:
    def __init__(self, master):
        self.db = Database()
        self.master = master
        self.master.title("Gerir Veículos")
        
        # Labels e Entradas
        Label(master, text="Fabricante").grid(row=0, column=0)
        self.fabricante_entry = Entry(master)
        self.fabricante_entry.grid(row=0, column=1)
        
        Label(master, text="Modelo").grid(row=1, column=0)
        self.modelo_entry = Entry(master)
        self.modelo_entry.grid(row=1, column=1)
        
        Label(master, text="Tipo").grid(row=2, column=0)
        self.tipo_entry = Entry(master)
        self.tipo_entry.grid(row=2, column=1)
        
        # Botões
        Button(master, text="Salvar", command=self.cadastrar_veiculo).grid(row=3, column=0)
        Button(master, text="Listar Veículos", command=self.listar_veiculos).grid(row=3, column=1)
        Button(master, text="Deletar", command=self.deletar_veiculo).grid(row=3, column=2)
        
        # Listbox para Exibir Veículos
        self.veiculos_listbox = Listbox(master)
        self.veiculos_listbox.grid(row=4, column=0, columnspan=3)
    
    def cadastrar_veiculo(self):
        fabricante = self.fabricante_entry.get()
        modelo = self.modelo_entry.get()
        tipo = self.tipo_entry.get()
        
        if fabricante and modelo:
            self.db.cursor.execute("INSERT INTO Veiculos (fabricante, modelo, tipo) VALUES (?, ?, ?)", 
                                   (fabricante, modelo, tipo))
            self.db.conn.commit()
            messagebox.showinfo("Sucesso", "Veículo cadastrado com sucesso!")
            self.listar_veiculos()
        else:
            messagebox.showerror("Erro", "Todos os campos obrigatórios.")
    
    def listar_veiculos(self):
        self.veiculos_listbox.delete(0, END)
        self.db.cursor.execute("SELECT * FROM Veiculos")
        for row in self.db.cursor.fetchall():
            self.veiculos_listbox.insert(END, f"{row[1]} - {row[2]} - Tipo: {row[3]}")
    
    def deletar_veiculo(self):
        selected = self.veiculos_listbox.curselection()
        if selected:
            veiculo = self.veiculos_listbox.get(selected[0])
            modelo = veiculo.split(" - ")[1]
            confirm = messagebox.askyesno("Confirmação", "Tem certeza que deseja excluir este veículo?")
            if confirm:
                self.db.cursor.execute("DELETE FROM Veiculos WHERE modelo = ?", (modelo,))
                self.db.conn.commit()
                self.listar_veiculos()
                messagebox.showinfo("Sucesso", "Veículo excluído com sucesso.")
        else:
            messagebox.showerror("Erro", "Selecione um veículo para excluir.")
    
    def close(self):
        self.db.close()
