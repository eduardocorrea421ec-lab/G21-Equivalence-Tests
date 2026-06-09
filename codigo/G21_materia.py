import numpy as np

# G21.5 - Distribuição de Matéria Escura em Aglomerados
# Dados Bullet Cluster
M_lente = 1.0  # massa observada por lente gravitacional
M_gas = 0.14  # massa de gás observada
erro_M = 0.05

def teste_materia(f_escura):
    M_G21 = M_gas / (1 - f_escura)
    desvio = abs(M_G21 - M_lente)
    sigma = desvio / erro_M
    if sigma > 2:
        return f"G21.5 REFUTADA: f_escura={f_escura:.2f}, Desvio={sigma:.1f}σ"
    else:
        return f"G21.5 COMPATÍVEL: f_escura={f_escura:.2f}, Desvio={sigma:.1f}σ"

for f in [0.86, 0.70, 0.50, 0.0]:
    print(teste_materia(f))
