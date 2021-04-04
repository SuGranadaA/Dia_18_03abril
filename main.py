#Importamos nuestra libreria String
import string

#Abrimos y leemos nuestro archivo en modo lectura
f = open('abcd.txt', 'r')

#Cargamos los datos del archivo en una variable
fileContent = f.readlines()

#Realizamos operaciones propias del str
festivo = 'Hoy es un dìa festivo, no habràn clases'

c = open('dias.txt', 'r')

for p in list(string.punctuation):
    festivo = festivo.replace(p, '')

lineas = festivo.lower().split(' ')

abcd = 0
dias = 0

for word in lineas:
    if word in f:
        abcd += 1
        dias += 2
    if word in c:
        dias += 1
        abcd += 2
resultado = (abcd / (dias + 1))
if (resultado < -5):
    print('No tienes tiempo en tu vida')
elif (resultado < -0, 5):
    print('Tienes poco tiempo en tu vida')
elif (resultado < 0):
    print('Tienes tiempo en tu vida')
else:
    print('Tienes muy buen tiempo en tu vida')

print("Todos los dígitos del sistema:", string.digits, "\n")
print("Todos los signos de puntuación del sistema:", string.punctuation, "\n")
print("Todas las letras ascii:", string.ascii_letters, "\n")
print("Todas las letras ASCII en minúsculas:", string.ascii_lowercase, "\n")
print("Todas las letras ASCII en mayúsculas:", string.ascii_uppercase, "\n")
print("Todas los caracteres ASCII imprimibles:", string.printable, "\n")

f.close()

fileContent.reverse()

#Abrimos y leemos nuestro archivo 1 en modo escritura
archivo1 = open('Archivo1.txt', 'w+')

#Escribimos en nuestro archivo 1 los datos procesado
archivo1.writelines(fileContent)

archivo1.close()

c = open('dias.txt', 'r')

#Cargamos los datos del archivo en una variable
fileContent = c.readlines()
c.close()

fileContent.reverse()

#Abrimos y leemos nuestro archivo2 en modo escritura
archivo2 = open('Archivo2.txt', 'w+')

#Escribimos en nuestro archivo 2 los datos procesado
archivo2.writelines(fileContent)
archivo2.close()
