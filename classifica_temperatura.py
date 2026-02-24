temperatura = float(input("Digite a temperatura atual: "))
if  temperatura < 15:
    print(" Hoje Está Frio.")
elif temperatura >= 15 and temperatura <= 25:
    print(" Hoje Está Agradável.")
else:
    print("Está Quente.")