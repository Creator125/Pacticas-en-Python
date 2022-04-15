"""
Reescriba el código el código que pagabas unas horas extras
y cree una función llamada “pagocomputado” que reciba dos
argumentos (hora y tarifa).

Ingrese horas: 45
Ingrese tarifa: 10
Pago: 475.0

475 = 40*10+5*15
"""

def pagocomputaodor(horas, tarifa):
    pago = 40 * tarifa + horas * 15
    print(pago)

pagocomputaodor(int(input("hora: ")), int(input("tarifa: ")))