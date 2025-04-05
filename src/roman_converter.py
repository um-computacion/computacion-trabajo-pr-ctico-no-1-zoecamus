def decimal_to_roman(numero):
    valores = {
        1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC",
        100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"
    }
    result = ""
    for valor in sorted(valores.keys(), reverse=True):
        while numero >= valor:
            result += valores[valor]
            numero -= valor
    return result
numero = int(input("Ingrese un número entero: "))
if 1 <= numero <= 3999:
    romano = decimal_to_roman(numero)
    print("Número romano:", romano)
else:
    print("Ingrese un número entre 1 y 3999.")

