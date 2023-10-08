def verificaSeTriangulo(valor1, valor2, valor3):
    if (valor1 + valor2) >= valor3 and (valor3 + valor2) >= valor1 and (valor1 + valor3) >= valor2:
        return 1
    return 0

if verificaSeTriangulo(1, 1, 1) == 1:
    print("É um triangulo")
else:
    print("Não é um triangulo")

print()

def defineTipoTriangulo(valor1, valor2, valor3):
    if verificaSeTriangulo(valor1, valor2, valor3) == 1:
        if valor1 == valor2 == valor3:
           print("Triangulo equilatero")
        elif valor1 != valor2 and valor1 != valor3 and valor2 != valor3:
            print("Triangulo escaleno")
        else:
            print("Triangulo isoceles")
    else:
        print("Não é um triangulo")

lado1 = 30
lado2 = 30
lado3 = 40

defineTipoTriangulo(lado1, lado2, lado3)











