# G21-Equivalence-Tests
Code and data # Testes de Equivalência G21

Códigos em Python para testar os 5 teoremas de equivalência da Teoria G21 contra dados observacionais públicos.

**Artigo:** "Testando o Princípio da Equivalência Fraca em Regimes Extremos" 

## Como rodar os testes
-- G21_shielding.py ---
cole o código aqui
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
**Requisitos:** Python 3.8+ e numpy
```bash

pip install numpy
--- G21_velocity.py ---
cole o código aquiimport numpy as np

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
--- G21_accel.py ---
cole o código aqui
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
import numpy as np
--- G21_spin.py ---
cole o código aqui
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
    print(teste_spin(epsilon)
--- G21_materia.py ---
cole o código aqui
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

for f in [1.0, 0.999, 0.99, 0.9]:
    print(teste_velocidade(f * c))
