# 1 - Crie uma pasta, uma subpasta e em seguida um módulo na subpasta
# contendo uma função qualquer.
# Acesse o módulo no programa principal e execute a função.
# Obs.: No módulo criado, estabeleça uma condição para a função ser acessada
# apenas se o módulo for importado e executado em outro. Ou seja, quando o
# módulo em questão não é o principal (main)
from biblioteca.pacote1 import arquivo1

print(arquivo1.somar(484847, 38474))
