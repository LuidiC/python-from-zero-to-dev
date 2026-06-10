frase = 'Curso em Vídeo Python'

print(frase[9])
print(frase[15:21]) #Sempre o carcter do último não será considerado, nesse caso imprimirá até o 20
print(frase[9:21:2]) #O último número representa quando os caracteres serão considerados, nesse caso específico de 2 em 2 
print(frase[:5]) #Do início até a o caracter terminado 
print(frase[9:]) #Do caracter do início até o último caracter 
print(frase[9::3]) #Do caracter do início até o último caracter, de 3 em 3  
print(len(frase))
print(frase.count('o'))
print(frase.count('o', 0, 14)) #Quantas vezes determinado caracter apareceu nesse intervalo
print(frase.find('deo'))
print('Curso' in frase)
frase = frase.replace('Python', "Java")
print(frase)
#Parei no tempo 20:49 da aula 09