import tkinter as tk 

janela = tk.Tk()
janela.geometry("600x600")
janela.title("Menu Principal")

titulo = tk.Label(
    janela,
    text="Menu Principal",
    font=("Arial", 28, "bold"),
    bg="#0F172A",
    fg="white",
    pady=20
)

titulo.grid(row=0, column=0, columnspan=3, sticky="nsew")

#Containers 

#Conteiner Usuários
bt_user = tk.Button(
    janela,
    text="USUÁRIOS",
    font=("Arial", 28, "bold")
)

bt_user.grid(row=1, column=1, columnspan=2, sticky="sew")

#Container Avaliações
bt_assen = tk.Button(
    janela,
    text="AVALIAÇÕES",
    font=("Arial", 28, "bold"),
    padx=20
)

sub_assen = tk.Label(
    bt_assen,
    text="Consultar Avaliações",
    font=("Arial", 12)
)

bt_assen.grid(row=2, column=1, sticky="sew")
# sub_assen.grid(row=3, column=0)



janela.mainloop()