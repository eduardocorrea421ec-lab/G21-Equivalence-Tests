import numpy as np

# G21.2 - Velocidade das Ondas Gravitacionais
# Dados GW170817 + GRB170817A
c = 299792458  # m/s
delta_t = 1.7  # s, atraso GRB
D = 40e6 * 9.461e15  # 40 Mpc em metros
erro_delta_t = 0.1  # s

def teste_velocidade(v_gw):
    delta_t_G21 = D * (c - v_gw) / (c * v_gw)
    desvio = abs(delta_t_G21 - delta_t)
    sigma = desvio / erro_delta_t
    if sigma > 2:
        return f"G21.2 REFUTADA: v_gw={v_gw/c:.9f}c, Desvio={sigma:.1f}σ"
    else:
        return f"G21.2 COMPATÍVEL: v_gw={v_gw/c:.9f}c, Desvio={sigma:.1f}σ"

for f in [1.0, 0.999, 0.99, 0.9]:
    print(teste_velocidade(f * c))
