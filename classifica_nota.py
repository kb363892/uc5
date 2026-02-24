nota = float(input("Digite a nota (0 a 10): "))

if 0 <= nota <= 10:
    if nota >= 8:
        print("otimo")
    elif nota >= 6:
        print("bom")
    elif nota >= 4:
        print("regular")
    else:
        print("insuficiente")
else:
    print("nota inválida, digite um valor entre 0 e 10.")

