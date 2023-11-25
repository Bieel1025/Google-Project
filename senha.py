import string
from random import choice
tamanho = 8
valores = string.ascii_letters + string.digits + string.punctuation
senha = ''
for i in range(tamanho):
  senha += choice(valores)

print(senha)
