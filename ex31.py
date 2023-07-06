# 1) Faça o debug a partir da primeira linha (x = 1) com o próprio Pycharm ou
# método pdb (Breakpoint) do seguinte código e anote os valores das variáveis em
# cada linha como resposta.

x = 1
y = 10
z = 100
x = x + (y + z) //2
y = y ** 2 + z * x
z = (z ** 2) + z + x
soma = x + y + z
print(soma)
