# *args = Convensão para argumentos
# **kwargs = argumentos nomeados
# sep -> Separador

# def func(*args):  # Se liga no *args
#     print(args[2])
#     print(args[-3])
#     print(len(args))

#
# def func2(*args):  # Se liga no *args
#     print(args)
#
#
# lista1 = [1, 2, 3, 4, 5, 6]
# lista2 = [15, 25, 35, 45, 55, 65]
# func2(lista1, 'Gusavo')
# func2(*lista1, *lista2)

# def func3(*args, **kwargs):  # Se liga no *args
#     print(args)
#     print(kwargs)
#
#
# lista1 = [1, 2, 3, 4, 5, 6]
# lista2 = [15, 25, 35, 45, 55, 65]
# func3(*lista1, *lista2, nome='Gustavo', sobrenome='Hammes')

# def func4(*args, **kwargs):  # Se liga no *args
#     print(args)
#     print(kwargs['nome'], kwargs['sobrenome'])
#
#
# lista1 = [1, 2, 3, 4, 5, 6]
# lista2 = [15, 25, 35, 45, 55, 65]
# func4(*lista1, *lista2, nome='Gustavo', sobrenome='Hammes')

def func5(*args, **kwargs):  # Se liga no (*args) e no (**kwargs)
    print(f'\n args: {args}')
    print(
        f'\n kwargs["nome"], kwargs["sobrenome"]: {kwargs["nome"], kwargs["sobrenome"]}')
    # Este trecho é para receber qualquer argumento para a função sem declara-lo
    # EXCELENTE!!!
    idade = kwargs.get('idade')  # recebo esse argumento
    if idade is not None:  # Testo se o argumento é nenhum (none)
        print(f'\n idade: {idade}')


lista1 = [1, 2, 3, 4, 5, 6]
lista2 = [15, 25, 35, 45, 55, 65]
func5(*lista1, *lista2, idade=44, nome='Gustavo', sobrenome='Hammes')

n1, n2, *n = lista1  # Se liga no (*n)
print(f'\n lista1: {lista1}')
print(f'\n *lista1:', *lista1)  # Se liga no (*lista)
print(f'\n *lista2, sep= "@":', *lista2, sep=' @ ')  # Se liga no (*lista)
print(f'\n {n1, n2, n} \n')
