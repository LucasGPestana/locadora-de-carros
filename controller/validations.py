import re

def verifyEmptyField(modelo, marca, preco, quantidade):

  return all([modelo, marca, preco, quantidade])

def validatePrice(preco):

  pricePattern = re.compile(r"[0-9]+[.|,]{0,1}[0-9]+")

  return pricePattern.fullmatch(preco) and float(preco.replace(",", ".")) > 0

def validateAmount(quantidade):

  return quantidade.isnumeric() and int(quantidade) > 0

def existCar(modelo, carros):

  return any([getattr(carro, "modelo") == modelo for carro in carros])