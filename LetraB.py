import math

def erro_obtido(ponto_y, ponto_x):
    erros = []
    for i in range(len(ponto_y)):
        erro = ponto_y[i] - (0.42294772 * ponto_x[i] + 2.38537686)
        print("Erros obtidos por ponto: ", erro)
        erros.append(erro)
    return erros

def desvio_padrao(erros):
    erro_quadratico = sum(x**2 for x in erros)
    desvio_padrao = math.sqrt(erro_quadratico)
    print("Desvio Padrão: ", desvio_padrao)

def main():
    ponto_y = [1, 2, 2.4, 2.9, 3.5]
    ponto_x = [-3, -1.5, 0.3, 1.7, 2.2]

    erros = erro_obtido(ponto_y, ponto_x)
    desvio_padrao(erros)

if __name__ == "__main__":
    main()