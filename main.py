import tkinter as tk 

janela = tk.Tk()
janela.geometry("600x600")
janela.title("AcheAqui")
janela.grid_columnconfigure((0,1), weight=1)
janela.grid_rowconfigure((2,1), weight=1)
janela.configure(bg="#0b0f14")

titulo = tk.Label(
    janela,
    text="🖥\nMenu Principal",
    font=("Arial", 30, "bold"),
    bg="#1e293b",
    fg="#9ca3af",
    pady=20
)

titulo.grid(row=0, column=0, columnspan=2, sticky="nsew")

#Botões 

#Botão Usuários
bt_user = tk.Button(
    janela,
    text="USUÁRIOS\nConsultar Usuários",
    font=("Arial", 18, "bold"),
    fg="#9ca3af",
    bg="#0b1220",
    activebackground="#1a2f5a",
    activeforeground="#9ca3af",
    relief="flat",
    bd=0,
)

bt_user.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

#Botão Avaliações

bt_assen = tk.Button(
    janela,
    text="Avaliações\n Consultar Avaliações",
    font=("Arial", 18, "bold"),
    fg="#9ca3af",
    bg="#150b1f",
    activebackground="#3a1d5c",
    activeforeground="#9ca3af",
    relief="flat",
    bd=0
)

bt_assen.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)

#Botão Serviços 

bt_serv = tk.Button(
    janela,
    text="SERVIÇOS\nCadastro e consulta",
    font=("Arial", 18, "bold"),
    fg="#9ca3af",
    bg="#06150f",
    activebackground="#0f3d2b",
    activeforeground="#9ca3af",
    relief="flat",
    bd=0
)
bt_serv.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

#Botão Denúncias

bt_den = tk.Button(
    janela,
    text="DENÚNCIAS\nConsultar Denúncias",
    font=("Arial", 18, "bold"),
    fg="#9ca3af",
    bg="#1f1305",
    activebackground="#5a3410",
    activeforeground="#9ca3af",
    relief="flat",
    bd=0
)

bt_den.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)


janela.mainloop()