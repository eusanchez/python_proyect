#programa para imprimir una palabra a lo inverso.
#Ana Eugenia Sanchez V.

usuario = input("Digite una palabra: ")

lista = list(usuario)
lista.reverse()
print ("Esta es mi palabra en reversa: ", "".join(lista)) #palabra reversa

print("Esta es mi palabra original: ",usuario) #palabra original
