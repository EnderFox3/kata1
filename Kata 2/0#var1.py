"""
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es del día tiene un descuendo del 60%.
Escribe un programa que comience leyendo el número de barras vendidas que no son del día. Después tu programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste dinal total.
"""

precio = 3.49
descuento=0.4 
precio_con_descuento = precio*descuento

numero_de_barras = int(input("Introduce el numero de barras vendidas:")) #guarda lo que el usuario ingresa en variable

print("Precio habitual: " + str(precio))
print("Descuento: " + str(precio_con_descuento))
print("Coste final: " + str(numero_de_barras*precio_con_descuento))