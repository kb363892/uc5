print ("menu de opçoes")
print ("se voce quiser pagar no pix digite 1 ")
print ("se voce quiser pagar no credito digite 2")
print ("se voce quiser pagar no debito digite 3")
valor = float(input("Digite o valor da sua compra: R$ ")
opçao = int(input)("Digite a opçao de pagamento:") 

match(opçao):
    case1:
        desconto = valor_compra * 0.05
    case2:
        desconto = valor_compra * 0
    case3:
        desconto = valor_compra * 0.03

valor_final = valor_compra - desconto

print("Desconto:", desconto)
print("Valor final: ", valor_final)
    
        
    
        