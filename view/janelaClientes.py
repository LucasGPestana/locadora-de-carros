import tkinter as tk
from model.constants import CORES

def rodarTelaClientes():

  telaClientes = tk.Tk()
  telaClientes.title("Tela dos Clientes")
  telaClientes.geometry("600x400")
  telaClientes.config(background=CORES["Preto"])

  tituloPagina = tk.Label(master=telaClientes,
                        text="Login do Cliente",
                        font=("Arial", 25, "bold"),
                        fg=CORES["Branco"],
                        bg=CORES["Preto"])
  tituloPagina.pack(pady=5)

  labelCpf = tk.Label(master=telaClientes, 
                      text="CPF", 
                      bg=CORES["Preto"],
                      fg=CORES["Branco"])
  labelCpf.pack(pady=5)

  inputCpf = tk.Entry(master=telaClientes)
  inputCpf.pack(padx=5)

  labelSenha = tk.Label(master=telaClientes, 
                      text="Senha", 
                      bg=CORES["Preto"],
                      fg=CORES["Branco"])
  labelSenha.pack(pady=5)

  inputSenha = tk.Entry(master=telaClientes, show="*")
  inputSenha.pack(pady=5)

  botaoLogin = tk.Button(master=telaClientes, text="Logar")
  botaoLogin.pack(pady=5)

  telaClientes.mainloop()