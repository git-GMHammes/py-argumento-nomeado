# 
# *args = Convenção para argumentos
# **kwargs = argumentos nomeados
# 
def func5(*args, **kwargs):  # Se liga no (*args) e no (**kwargs)
    print(f'\n func5(*args, **kwargs):')
    print
    print(f'\n args: {args}')
    print(
        f'\n kwargs["nome"], kwargs["sobrenome"]: {kwargs["nome"], kwargs["sobrenome"]}')
    # Este trecho é para receber qualquer argumento para a função sem declara-lo
    # EXCELENTE!!!
    idade = kwargs.get('idade')  # recebo esse argumento
    if idade is not None:  # Texto se o argumento é nenhum (none)
        print(f'\n idade: {idade} \n')


lista1 = [1, 2, 3, 4, 5, 6]
lista2 = [15, 25, 35, 45, 55, 65]
func5(*lista1, *lista2, idade=44, nome='Gustavo', sobrenome='Hammes')
