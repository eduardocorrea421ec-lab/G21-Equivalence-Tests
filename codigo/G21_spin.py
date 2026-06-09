import numpy as np

# G21.4 - Precessão de Spin em Pulsares Binários
# Dados PSR J0737-3039
Omega_GR = 16.90  # graus/ano, previsão GR
Omega_obs = 16.90  # graus/ano, observado
erro_Omega = 0.05  # graus/ano

def teste_spin(epsilon):
    Omega_G21 = Omega_GR * (1 + epsilon)
    desvio = abs(Omega_G21 - Omega_obs)
    sigma = desvio / erro_Omega
    if sigma > 2:
        return f"G21.4 REFUTADA: epsilon={epsilon:.3f}, Desvio={sigma:.1f}σ"
    else:
        return f"G21.4 COMPATÍVEL: epsilon={epsilon:.3f}, Desvio={sigma:.1f}σ"

for epsilon in [0, 0.01, 0.05, 0.10]:
    print(teste_spin(epsilon))
