from tkinter import Tk
from fabricantes import GerirFabricantes

def main():
    root = Tk()
    app = GerirFabricantes(root)
    root.mainloop()

if __name__ == "__main__":
    main()
