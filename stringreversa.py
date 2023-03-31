texto = "Exemplo de string"
lista_caracteres = list(texto)
lista_invertida = []

for i in range(len(lista_caracteres)-1, -1, -1):
    lista_invertida.append(lista_caracteres[i])


    texto_invertido = "".join(lista_invertida)

    print(texto_invertido)
