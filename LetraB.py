import math

def erro_obtido(ponto_y, ponto_x):
    erros = []
    for i in range(len(ponto_y)):
        erro = (0.42294772202393455 * ponto_x[i] + 2.385376863321436) - ponto_y[i]
        erro_quadrado = erro ** 2
        print(f"Erro = {erro}")
        print(f"Erro ao Quadrado = {erro_quadrado}")
        erros.append(float(erro_quadrado))
    return erros

def desvio_padrao(erros):
    erro_total = sum(erros)
    desvio_padrao = math.sqrt(erro_total)
    print(desvio_padrao)

if _name_ == "_main_":
    ponto_y = [1, 2, 2.4, 2.9, 3.5]
    ponto_x = [-3, -1.5, 0.3, 1.7, 2.2]
    
    print("===== ERRO OBTIDO POR PONTO =====")
    erros = erro_obtido(ponto_y, ponto_x)
    
    print("===== DESVIO PADRÃO DOS ERROS =====")
    desvio_padrao(erros)