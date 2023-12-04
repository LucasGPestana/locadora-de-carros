import tkinter as tk
from model.constants import CORES
from controller.events import logarFuncionario
from view.janelaCarros import telaCadastroCarros, telaRemoveCarros, telaConsultaCarros, telaAlteraCarros

def rodarTelaFuncionarios():
  
  telaFuncionarios = tk.Tk()
  telaFuncionarios.title("Sistema dos Funcionários")
  telaFuncionarios.geometry("600x400")
  telaFuncionarios.config(background=CORES["Preto"])

  tituloPagina = tk.Label(master=telaFuncionarios,
                        text="Login do Funcionário",
                        font=("Arial", 25, "bold"),
                        fg=CORES["Branco"],
                        bg=CORES["Preto"])
  tituloPagina.pack(pady=5)

  labelCpf = tk.Label(master=telaFuncionarios, 
                      text="CPF", 
                      bg=CORES["Preto"],
                      fg=CORES["Branco"])
  labelCpf.pack(pady=5)

  inputCpf = tk.Entry(master=telaFuncionarios)
  inputCpf.pack(padx=5)

  labelSenha = tk.Label(master=telaFuncionarios, 
                      text="Senha", 
                      bg=CORES["Preto"],
                      fg=CORES["Branco"])
  labelSenha.pack(pady=5)

  inputSenha = tk.Entry(master=telaFuncionarios, show="*")
  inputSenha.pack(pady=5)

  botaoLogin = tk.Button(master=telaFuncionarios, 
                         text="Logar", 
                         command=lambda: logarFuncionario(inputCpf.get(), 
                                                          inputSenha.get(), 
                                                          telaFuncionarioLogado,
                                                          respostaLogin))
  botaoLogin.pack(pady=5)

  respostaLogin = tk.Label(master=telaFuncionarios, 
                           text="", 
                           bg=CORES["Preto"], 
                           fg=CORES["Branco"])
  respostaLogin.pack(pady=5)

  telaFuncionarios.mainloop()

# Essa tela será chamada apenas se o funcionário estiver logado
def telaFuncionarioLogado(funcionario):

  telaFuncLogado = tk.Tk()
  telaFuncLogado.title("Opções de Funcionário")
  telaFuncLogado.geometry("600x400")
  telaFuncLogado.config(background=CORES["Preto"])

  saudacoes = tk.Label(master=telaFuncLogado, 
                       text=f"Olá, {getattr(funcionario, 'nome')}!", 
                       bg=CORES["Preto"], 
                       fg=CORES["Branco"])
  saudacoes.pack(pady=20)

  botaoCadastrar = tk.Button(master=telaFuncLogado, 
                             text="Cadastrar Carro", 
                             command=lambda: telaCadastroCarros(funcionario))
  botaoCadastrar.pack(pady=5)

  botaoConsultar = tk.Button(master=telaFuncLogado, 
                             text="Consultar Carros", 
                             command=lambda: telaConsultaCarros(funcionario))
  botaoConsultar.pack(pady=5)

  botaoAlterar = tk.Button(master=telaFuncLogado,
                           text="Alterar Dados do Carro",
                           command=lambda: telaAlteraCarros(funcionario))
  botaoAlterar.pack(pady=5)

  botaoRemover = tk.Button(master=telaFuncLogado, 
                           text="Remover Carro", 
                           command=lambda: telaRemoveCarros(funcionario))
  botaoRemover.pack(pady=5)

  botaoSair = tk.Button(master=telaFuncLogado, 
                        text="Sair", 
                        command=telaFuncLogado.destroy)
  botaoSair.pack(pady=20)

  telaFuncLogado.mainloop()
