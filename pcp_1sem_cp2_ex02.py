#exercicio 2 - Lados de um Triangulo
ladoA= int(input("qual o valor do maior lado: "))
ladoB= int(input("qual o valor do lado medio: "))
ladoC= int(input("qual o valor do menor lado: "))
print(f"Maior lado: {ladoA}")
print(f"Lado Medio: {ladoB}")
print(f"Menor lado: {ladoC}")
if ladoA>=ladoB+ladoC:
    print("não forma triangulo!!!")
else:
    if ladoA**2==ladoB**2+ladoC**2:
        print("triangulo retangulo")
    if ladoA**2>ladoB**2 + ladoC**2:
        print("triangulo obtuso")
    if ladoA**2<ladoB**2 + ladoC**2:
        print("triangulo acutangulo")
    if ladoA==ladoB==ladoC:
         print("triangulo equilatero")
    elif ladoA==ladoB or ladoA==ladoC or ladoB==ladoC:
         print("triangulo isosceles ")


