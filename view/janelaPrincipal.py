import sys, os

# Adiciona o diretório do projeto no PYTHONPATH para procurar pelos módulos
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# Instala automaticamente as dependências necessárias para rodar o código
os.chdir(os.path.dirname(os.path.dirname(__file__)))
os.system("pip install -r requirements.txt")

import tkinter as tk
from model.constants import CORES
from view.janelaClientes import rodarTelaClientes
from view.janelaFuncionarios import rodarTelaFuncionarios

principal = tk.Tk()

principal.title("Locadora de Carros")
principal.geometry("600x400")
principal.config(background=CORES["Preto"])

tituloPagina = tk.Label(master=principal,
                        text="Locadora de Carros",
                        font=("Arial", 25, "bold"),
                        fg=CORES["Branco"],
                        bg=CORES["Preto"])
tituloPagina.pack(padx=10, pady=10)

botaoClientes = tk.Button(master=principal,
                          text="Sistema Clientes",
                          command=rodarTelaClientes)
botaoClientes.pack(padx=10, pady=30)

botaoFuncionarios = tk.Button(master=principal,
                          text="Sistema Funcionarios",
                          command=rodarTelaFuncionarios)
botaoFuncionarios.pack(padx=10, pady=30)

principal.mainloop()