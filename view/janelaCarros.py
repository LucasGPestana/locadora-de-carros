import tkinter as tk
from model.constants import CORES
from controller.events import inserirCarro, consultarCarros, removerCarro, pegarInfoCarro, alterarCarro

def telaCadastroCarros(funcionario):

  telaCadastroCarros = tk.Tk()
  telaCadastroCarros.title("Cadastro de Carro")
  telaCadastroCarros.geometry("600x400")
  telaCadastroCarros.config(background=CORES["Preto"])

  labelModelo = tk.Label(master=telaCadastroCarros, 
                       text="Modelo", 
                       bg=CORES["Preto"],
                       fg=CORES["Branco"])
  labelModelo.pack(pady=5)

  inputModelo = tk.Entry(master=telaCadastroCarros)
  inputModelo.pack(pady=5)

  labelMarca = tk.Label(master=telaCadastroCarros, 
                       text="Marca", 
                       bg=CORES["Preto"],
                       fg=CORES["Branco"])
  labelMarca.pack(pady=5)

  inputMarca = tk.Entry(master=telaCadastroCarros)
  inputMarca.pack(pady=5)

  labelPreco = tk.Label(master=telaCadastroCarros, 
                       text="Preço (R$)", 
                       bg=CORES["Preto"],
                       fg=CORES["Branco"])
  labelPreco.pack(pady=5)

  inputPreco = tk.Entry(master=telaCadastroCarros)
  inputPreco.pack(pady=5)

  labelEstoque = tk.Label(master=telaCadastroCarros, 
                       text="Qtd. Estoque", 
                       bg=CORES["Preto"],
                       fg=CORES["Branco"])
  labelEstoque.pack(pady=5)

  inputEstoque = tk.Entry(master=telaCadastroCarros)
  inputEstoque.pack(pady=5)

  botaoCadastrar = tk.Button(master=telaCadastroCarros, 
                             text="Cadastrar", 
                             command=lambda: inserirCarro(funcionario, inputModelo, inputMarca, inputPreco, inputEstoque, respostaCadastro))
  botaoCadastrar.pack(pady=5)

  respostaCadastro = tk.Label(master=telaCadastroCarros, 
                              text="", 
                              bg=CORES["Preto"], 
                              fg=CORES["Branco"])
  respostaCadastro.pack(pady=5)

  botaoSair = tk.Button(master=telaCadastroCarros, 
                        text="Sair", 
                        command=telaCadastroCarros.destroy)
  botaoSair.pack(pady=5)

  telaCadastroCarros.mainloop()

def telaRemoveCarros(funcionario):
  
  telaRemoveCarros = tk.Tk()
  telaRemoveCarros.title("Pesquisa por Carro")
  telaRemoveCarros.geometry("600x400")
  telaRemoveCarros.config(background=CORES["Preto"])

  labelId = tk.Label(master=telaRemoveCarros, 
                        text="ID", 
                        bg=CORES["Preto"], 
                        fg=CORES["Branco"])
  labelId.pack(pady=5)

  inputId = tk.Entry(master=telaRemoveCarros)
  inputId.pack(pady=5)

  botaoPesquisar = tk.Button(master=telaRemoveCarros, 
                             text="Pesquisar", 
                             command=lambda: consultarCarros(funcionario, "identificador", inputId.get(), textoConsulta))
  botaoPesquisar.pack(pady=5)

  textoConsulta = tk.Label(master=telaRemoveCarros, 
                           text="", 
                           bg=CORES["Preto"], 
                           fg=CORES["Branco"])
  textoConsulta.pack(pady=5)

  botaoRemover = tk.Button(master=telaRemoveCarros, 
                           text="Remover", 
                           command=lambda: removerCarro(funcionario, inputId.get(), textoConsulta, respostaRemocao))
  botaoRemover.pack(pady=5)

  respostaRemocao = tk.Label(master=telaRemoveCarros, 
                             text="", 
                             bg=CORES["Preto"], 
                             fg=CORES["Branco"])
  respostaRemocao.pack(pady=5)

  botaoSair = tk.Button(master=telaRemoveCarros, 
                        text="Sair", 
                        command=telaRemoveCarros.destroy)
  botaoSair.pack(pady=5)

  telaRemoveCarros.mainloop()

def telaConsultaCarros(funcionario):
  
  telaConsultaCarros = tk.Tk()
  telaConsultaCarros.title("Pesquisa por Carro")
  telaConsultaCarros.geometry("600x400")
  telaConsultaCarros.config(background=CORES["Preto"])

  labelMarca = tk.Label(master=telaConsultaCarros, 
                        text="Marca", 
                        bg=CORES["Preto"], 
                        fg=CORES["Branco"])
  labelMarca.pack(pady=5)

  inputMarca = tk.Entry(master=telaConsultaCarros)
  inputMarca.pack(pady=5)

  botaoPesquisar = tk.Button(master=telaConsultaCarros, 
                             text="Pesquisar", 
                             command=lambda: consultarCarros(funcionario, "marca", inputMarca.get(), textoConsulta))
  botaoPesquisar.pack(pady=5)

  textoConsulta = tk.Label(master=telaConsultaCarros, 
                           text="", 
                           bg=CORES["Preto"], 
                           fg=CORES["Branco"])
  textoConsulta.pack(pady=5)

  botaoSair = tk.Button(master=telaConsultaCarros, 
                        text="Sair", 
                        command=telaConsultaCarros.destroy)
  botaoSair.pack(pady=5)

  telaConsultaCarros.mainloop()

def telaAlteraCarros(funcionario):

  telaAlteraCarros = tk.Tk()
  telaAlteraCarros.title("Cadastro de Carro")
  telaAlteraCarros.geometry("600x500")
  telaAlteraCarros.config(background=CORES["Preto"])

  labelId = tk.Label(master=telaAlteraCarros, 
                        text="ID", 
                        bg=CORES["Preto"], 
                        fg=CORES["Branco"])
  labelId.pack(pady=5)

  inputId = tk.Entry(master=telaAlteraCarros)
  inputId.pack(pady=5)

  botaoPesquisar = tk.Button(master=telaAlteraCarros, 
                             text="Pesquisar", 
                             command=lambda: pegarInfoCarro(identificador=inputId, 
                                                            modelo=inputModelo, 
                                                            marca=inputMarca, 
                                                            precoAlugel=inputPreco, 
                                                            quantidadeEstoque=inputEstoque,
                                                            respLabel=textoConsulta))
  botaoPesquisar.pack(pady=5)

  textoConsulta = tk.Label(master=telaAlteraCarros, 
                           text="", 
                           bg=CORES["Preto"], 
                           fg=CORES["Branco"])
  textoConsulta.pack(pady=5)

  labelModelo = tk.Label(master=telaAlteraCarros, 
                       text="Modelo", 
                       bg=CORES["Preto"],
                       fg=CORES["Branco"])
  labelModelo.pack(pady=5)

  inputModelo = tk.Entry(master=telaAlteraCarros)
  inputModelo.pack(pady=5)

  labelMarca = tk.Label(master=telaAlteraCarros, 
                       text="Marca", 
                       bg=CORES["Preto"],
                       fg=CORES["Branco"])
  labelMarca.pack(pady=5)

  inputMarca = tk.Entry(master=telaAlteraCarros)
  inputMarca.pack(pady=5)

  labelPreco = tk.Label(master=telaAlteraCarros, 
                       text="Preço (R$)", 
                       bg=CORES["Preto"],
                       fg=CORES["Branco"])
  labelPreco.pack(pady=5)

  inputPreco = tk.Entry(master=telaAlteraCarros)
  inputPreco.pack(pady=5)

  labelEstoque = tk.Label(master=telaAlteraCarros, 
                       text="Qtd. Estoque", 
                       bg=CORES["Preto"],
                       fg=CORES["Branco"])
  labelEstoque.pack(pady=5)

  inputEstoque = tk.Entry(master=telaAlteraCarros)
  inputEstoque.pack(pady=5)

  botaoAlterar = tk.Button(master=telaAlteraCarros, 
                             text="Cadastrar", 
                             command=lambda: alterarCarro(funcionario, inputId, inputModelo, inputMarca, inputPreco, inputEstoque, respostaAlteracao))
  botaoAlterar.pack(pady=5)

  respostaAlteracao = tk.Label(master=telaAlteraCarros, 
                              text="", 
                              bg=CORES["Preto"], 
                              fg=CORES["Branco"])
  respostaAlteracao.pack(pady=5)

  botaoSair = tk.Button(master=telaAlteraCarros, 
                        text="Sair", 
                        command=telaAlteraCarros.destroy)
  botaoSair.pack(pady=5)

  telaAlteraCarros.mainloop()