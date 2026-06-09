import numpy as np

# G21.1 - Teste de Blindagem Gravitacional em Campo Forte
# Dados GW150914
M_remanescente = 62  # massas solares
tau_GR = 4.0  # ms, previsão GR
tau_obs = 4.0  # ms, observado LIGO
erro_tau = 0.3  # ms

def teste_blindagem(S):
    tau_G21 = tau_GR * (1 - S)
    desvio = abs(tau_G21 - tau_obs)
    sigma = desvio / erro_tau
    if sigma > 2:
        return f"G21.1 REFUTADA: S={S:.2f}, Desvio={sigma:.1f}σ"
    else:
        return f"G21.1 COMPATÍVEL: S={S:.2f}, Desvio={sigma:.1f}σ"

for S in [0, 0.05, 0.10, 0.20]:
    print(teste_blindagem(S))
