import numpy as np

# G21.3 - Aceleração de Galáxias Satélite
# Dados Anãs de Andrômeda
a_N = 1e-10  # m/s^2, aceleração Newtoniana típica
a_obs = 2e-10  # m/s^2, observada
erro_a = 0.3e-10  # m/s^2
a_0 = 1.2e-10  # m/s^2, escala MOND

def teste_aceleracao():
    a_G21 = a_N * np.sqrt(1 + (a_N/a_0)**2)
    desvio = abs(a_G21 - a_obs)
    sigma = desvio / erro_a
    if sigma > 2:
        return f"G21.3 REFUTADA: Desvio={sigma:.1f}σ"
    else:
        return f"G21.3 COMPATÍVEL: Desvio={sigma:.1f}σ"

print(teste_aceleracao())
