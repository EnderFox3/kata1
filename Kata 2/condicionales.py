"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte la usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsuclas y minúsculas
"""

password="contraseña"

password_usuario = input ("Introduzca la contraseña: ")

if password==password_usuario.lower():
    print("El password es correcto")
else:
    print("El password no es correcto")