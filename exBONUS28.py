# Crie um decorador que limite o número de vezes que uma função pode ser chamada.
# O decorador deve receber um parâmetro que define o número máximo de chamadas permitidas.
# Se a função for chamada mais vezes do que o limite permitido,
# o decorador deve imprimir uma mensagem de erro e não chamar a função.

def maximo_de_vezes(numero_maximo):
    def decorador(func):
      aux = 0
      def nova_func(*args, **kwargs):
          nonlocal aux
          if aux >= numero_maximo:
              print('Numero de chamadas ultrapassado')
              return None
          else:
              aux += 1
              return func(*args, **kwargs)
      return nova_func
    return decorador




@maximo_de_vezes(2)
def somar(n1, n2):
    print(n1 + n2)

@maximo_de_vezes(2)
def subtrair(n1, n2):
    if n1 < n2:
        n1, n2 = n2, n1
    print(n1 - n2)

@maximo_de_vezes(2)
def multiplicar(n1, n2):
    print(n1 * n2)


multiplicar(4, 3)
multiplicar(2, 3)
multiplicar(4, 2)




