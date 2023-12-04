class Usuario():

  def __init__(self, nome, cpf, senha):

    self.nome = nome
    self.cpf = cpf
    self.senha = senha
  
  def __str__(self):

    return f"{self.nome} | {self.cpf}"


  def consultarCarros(self, carros, filtro, valorFiltro):

    carrosMarca = list()

    # carros corresponde a uma lista com objetos Carro
    # carro é um objeto da classe Carro

    if valorFiltro != "":

      for carro in carros:

        if str(getattr(carro, filtro)) == valorFiltro:

          carrosMarca.append(carro)

    else:

      carrosMarca = carros.copy()

    info_carros = [f"{getattr(carro, 'identificador')} | {getattr(carro, 'modelo')} | {getattr(carro, 'marca')} | {str(round(getattr(carro, 'precoAlugel'), 2)).replace('.', ',')} | {getattr(carro, 'quantidadeEstoque')}" for carro in carrosMarca]

    return "\n".join(info_carros)
  
  # Retorna o objeto (ou lista de objetos) referente ao valor associado a chave (id, modelo e marca)

  @staticmethod
  def buscarPorId(ident, carros):

    for carro in carros:

      if str(getattr(carro, "identificador")) == ident:

        return carro

class Cliente(Usuario):

  def __init__(self, nome, cpf, senha):

    super().__init__(nome, cpf, senha)
  
  def __str__(self):

    return super().__str__()
  
  def alugarCarro():
    pass

class Funcionario(Usuario):

  def __init__(self, nome, cpf, senha):

    super().__init__(nome, cpf, senha)
  
  def __str__(self):

    return super().__str__()
  
  def inserirCarro(self, modelo, marca, precoAlugel, quantidadeEstoque, carros):

    novoCarro = Carro(modelo, marca, precoAlugel, quantidadeEstoque)
    carros.append(novoCarro)
  
  def removerCarro(self, identificador, carros):

    carroEscolhido = Funcionario.buscarPorId(ident=identificador, carros=carros)

    carros.pop(carros.index(carroEscolhido))
  
  def alterarCarro(self, identificador, carros, **kwargs):

    carroEscolhido = Funcionario.buscarPorId(ident=identificador, carros=carros)
    posicaoCarro = carros.index(carroEscolhido)

    for key in kwargs:

      setattr(carroEscolhido, key, kwargs[key])
    
    carros[posicaoCarro] = carroEscolhido
  
class Carro():

  qtdCarros = 0

  def __init__(self, modelo, marca, precoAlugel, quantidadeEstoque, identificador=0):

    Carro.qtdCarros += 1

    self.identificador = identificador or Carro.qtdCarros
    self.modelo = modelo
    self.marca = marca
    self.precoAlugel = precoAlugel
    self.quantidadeEstoque = quantidadeEstoque
  
  def __str__(self):

    return f"{self.modelo} | {self.marca}"