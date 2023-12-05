from localStoragePy import localStoragePy
from model.constants import CORES
import json
from model.objects import Funcionario, Carro
from controller.validations import verifyEmptyField, validatePrice, validateAmount, existCar

localStorage = localStoragePy("./banco", storage_backend="json")

carros = json.loads(localStorage.getItem("carrosCadastrados")) if localStorage.getItem("carrosCadastrados") else []
funcionarios = json.loads(localStorage.getItem("funcionariosCadastrados")) if localStorage.getItem("funcionariosCadastrados") else [vars(Funcionario("Roberto", "11111111111", "abcd1"))]

Carro.qtdCarros = json.loads(localStorage.getItem("contIdentificador"))[0] if localStorage.getItem("contIdentificador") else 0

# Converte as listas com dicionários para listas de objeto Carro e Funcionario
carros = [Carro(**atributosCarro) for atributosCarro in carros]
funcionarios = [Funcionario(**atributosFuncionario) for atributosFuncionario in funcionarios]

# Retorna o objeto Funcionario correspondente ao cpf e senha passados como argumento (Ou None, caso não tenha um correspondente)
def buscarFuncionario(cpf, senha):
  
  for funcionario in funcionarios:

    if getattr(funcionario, "cpf") == cpf.replace(".", "", 3).replace("-", "") and getattr(funcionario, "senha") == senha:

      return funcionario

  return None

# Realiza a intermediação entre o buscarFuncionario e a tela de login do funcionário
# Chama a tela do funcionário logado o valor de funcionario não seja None
def logarFuncionario(cpf, senha, callback, respLabel):

  funcionario = buscarFuncionario(cpf, senha)

  # Abre as opções do funcionário
  if funcionario:
    callback(funcionario)
  else:
    respLabel.config(fg=CORES["Vermelho"])
    respLabel["text"] = "CPF e/ou senha incorreto(s)! Por favor, verifique se você está no sistema correto (Atual: Funcionário)"

def limparCampos(**kwargs):

  for key in kwargs:
    kwargs[key].delete(0, len(kwargs[key].get()))

# Intermedia a tela de cadastro de carros e o método de inserirCarro da classe Funcionario
# Valida as informações digitadas pelo usuário
def inserirCarro(funcionario, modelo, marca, precoAlugel, qtdEstoque, respLabel):

  global carros

  if verifyEmptyField(modelo.get(), marca.get(), precoAlugel.get(), qtdEstoque.get()):

    if validatePrice(precoAlugel.get()):

      if validateAmount(qtdEstoque.get()):

        if not existCar(modelo.get(), carros):

          Carro.qtdCarros += 1

          # vars converte o objeto Carro em um dicionário cujas chaves são os atributos e os valores são os valores dos atributos associados
          funcionario.inserirCarro(modelo.get(), marca.get(), float(precoAlugel.get().replace(",", ".")), int(qtdEstoque.get()), carros)
          localStorage.setItem("carrosCadastrados", json.dumps([vars(carro) for carro in carros]))
          localStorage.setItem("contIdentificador", json.dumps([Carro.qtdCarros]))

          limparCampos(modelo=modelo, 
                      marca=marca, 
                      preco=precoAlugel, 
                      qtdEstoque=qtdEstoque)
          
          respLabel.config(fg=CORES["Verde"])
          respLabel["text"] = "Carro cadastrado com sucesso!"

          modelo.focus()
        
        else:

          respLabel.config(fg=CORES["Vermelho"])
          respLabel["text"] = "Já existe um carro desse modelo cadastrado!"
        
      else:

        respLabel.config(fg=CORES["Vermelho"])
        respLabel["text"] = "A quantidade em estoque estipulada é inválida!"

    else:

      respLabel.config(fg=CORES["Vermelho"])
      respLabel["text"] = "O preço estipulado é inválido!"
  
  else:

    respLabel.config(fg=CORES["Vermelho"])
    respLabel["text"] = "Algum(ns) campo(s) não foi(foram) preenchido(s)!"

# Intermedia a tela de consulta de carros e o método de consultarCarros da classe Usuario (herdado para Cliente e Funcionario)
# Mostra as informações do carro com um filtro definido (Marca). Caso esse filtro não seja passado (Entrada vazia), vai ser mostrado todos os carros cadastrados
def consultarCarros(funcionario, filtro, valorFiltro, respLabel):

  global carros

  if carros:

    carrosEncontrados = funcionario.consultarCarros(carros, filtro, valorFiltro)

    # Primeira condição (antes do 'or') serve para os casos em que o valor do filtro foi definido, mas nenhum carro com esse filtro for encontrado em pesquisar por carro
    # Segunda condição (depois do 'or')serve para a tela de remoção de carros, no qual é obrigatório que o valor do filtro (identificador, nese caso) seja definido. Caso contrário, uma mensagem de erro é lançada
    if (carrosEncontrados == "" and valorFiltro != "") or (filtro == "identificador" and valorFiltro == ""):
      
      respLabel.config(fg=CORES["Vermelho"])
      respLabel["text"] = "Não foi encontrado nenhum carro com essas especificações!"
      
    else:
      
      respLabel.config(fg=CORES["Branco"])
      respLabel["text"] = "ID | Modelo | Marca | Preço(R$) | Qtd. Estoque\n" + carrosEncontrados
  
  else:

    respLabel.config(fg=CORES["Vermelho"])
    respLabel["text"] = "Nenhum carro foi cadastrado ainda!"

# Intermedia a tela de remoção de carros e o método de removerCarro da classe Funcionario
# Remove um determinado carro dentro dos carros cadastrados, a partir do identificador
def removerCarro(funcionario, ident, consulta, respLabel):

  global carros

  if carros:

    if consulta["text"] != "" and consulta["fg"] != CORES["Vermelho"]:

      funcionario.removerCarro(ident, carros)
      localStorage.setItem("carrosCadastrados", json.dumps([vars(carro) for carro in carros]))

      respLabel.config(fg=CORES["Verde"])
      respLabel["text"] =  "Carro removido!"
    else:

      respLabel.config(fg=CORES["Vermelho"])
      respLabel["text"] = "Não foi selecionado um carro específico para remover!"
  
  else:

    respLabel.config(fg=CORES["Vermelho"])
    respLabel["text"] = "Nenhum carro foi cadastrado ainda!"

def pegarInfoCarro(identificador, respLabel, **kwargs):

  global carros

  limparCampos(**kwargs)

  if carros:

    carroEscolhido = Funcionario.buscarPorId(identificador.get(), carros)

    if carroEscolhido:

      for key in kwargs:
          
        kwargs[key].insert(0, getattr(carroEscolhido, key))
    
    else:

      respLabel.config(fg=CORES["Vermelho"])
      respLabel["text"] = "Não existe um carro com esse identificador!"
  
  else:

    respLabel.config(fg=CORES["Vermelho"])
    respLabel["text"] = "Nenhum carro foi cadastrado ainda!"

def alterarCarro(funcionario, identificador, modelo, marca, precoAlugel, quantidadeEstoque, respLabel):
  
  global carros

  if verifyEmptyField(modelo.get(), marca.get(), precoAlugel.get(), quantidadeEstoque.get()):

    if validatePrice(precoAlugel.get()):

      if validateAmount(quantidadeEstoque.get()):

        funcionario.alterarCarro(identificador=identificador.get(), 
                          modelo=modelo.get(), 
                          marca=marca.get(), 
                          precoAlugel=float(precoAlugel.get().replace(",", ".")), 
                          quantidadeEstoque=int(quantidadeEstoque.get()), 
                          carros=carros)
        localStorage.setItem("carrosCadastrados", json.dumps([vars(carro) for carro in carros]))

        limparCampos(modelo=modelo, 
                    marca=marca, 
                    preco=precoAlugel, 
                    quantidadeEstoque=quantidadeEstoque)
          
        respLabel.config(fg=CORES["Verde"])
        respLabel["text"] = "Informações do carro alteradas com sucesso!"
        
      else:

        respLabel.config(fg=CORES["Vermelho"])
        respLabel["text"] = "A quantidade em estoque estipulada é inválida!"

    else:

      respLabel.config(fg=CORES["Vermelho"])
      respLabel["text"] = "O preço estipulado é inválido!"
  
  else:

    respLabel.config(fg=CORES["Vermelho"])
    respLabel["text"] = "Algum(ns) campo(s) não foi(foram) preenchido(s)!"

