"""
Reescriba el programa del salario para pagarle
al empleado 15 veces la tarifa para las horas extras
(por encima de 40)

Ingrese horas: 45
Ingrese tarifa: 10
Pago: 475.0

475 = 40*10+5*15
"""

horas = int(input("Ingrese las horas: "))
tarifa = int(input("Ingrese la tarifa: "))

pago = 40 * tarifa + horas * 15

print(pago)
