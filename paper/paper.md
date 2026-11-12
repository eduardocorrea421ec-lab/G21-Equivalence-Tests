---
title: 'G21 Equivalence Tests: Weak Equivalence Principle in Extreme Regimes and dP=0 Unification'
tags:
    - python
    - statistics
    - equivalence-principle
    - gravitational-physics
    - open-science
authors:
    - name: Eduardo Correa
    affiliation: 1
affiliations:
    - name: Independent Researcher, Itatinga, Brazil
    index: 1
date: 12 November 2026
bibliography: paper.bib
---

# Summary

The Weak Equivalence Principle (WEP) is a cornerstone of General Relativity, yet its tests remain fragmented across missions: MICROSCOPE in low Earth orbit, binary pulsars in strong-field regimes, and gravitational-wave events like GW150914 and GW170817. `G21-Equivalence-Tests` is an open-source Python toolkit that unifies these tests under a single statistical framework. We implement five experimental tests: gravitational shielding (G21.1), velocity of gravitational waves (G21.2), matter equivalence, inertial mass equivalence, and time-dilation equivalence.

The central theoretical contribution is the demonstration that 21 commonly used statistical tests (Student t-test, Mann-Whitney U, Kolmogorov-Smirnov, Anderson-Darling, etc.) collapse to a single condition `dP = 0`, where `dP = |P_A - P_B|` is the empirical probability difference. This reduces computational complexity from $O(n^2)$ to $O(n)$ and provides a unified decision rule for equivalence.

The software is designed for non-specialist use: `G21_shielding.py`, `G21_velocity.py`, and `G21_materia.py` are standalone scripts requiring only NumPy. Public LIGO data are used, for example GW150914 remnant $M = 62 M_{\odot}$, GR prediction $\tau_{GR} = 4.0$ ms, observed $\tau_{obs} = 4.0$ ms with error $0.3$ ms. Compatibility is assessed via $\sigma = |\tau_{G21} - \tau_{obs}| / \sigma_{\tau}$.

# Statement of need

Researchers testing alternative gravity theories like GVG need reproducible, open tools. Currently, testing WEP requires combining data from disparate sources without a common statistical language. A physicist testing shielding must write custom code, a statistician comparing groups must choose among 21 tests without knowing they are redundant, and an astrophysicist analyzing GW150914 must re-implement GR predictions. `G21` solves this by providing: (1) a unified Python implementation with MIT license, (2) direct use of public LIGO-Virgo-KAGRA data via GWOSC, (3) a falsifiable criterion: if $\sigma > 2$, G21.1 is refuted for shielding parameter $S$.

This directly supports the GVG theory development by providing the observational testbed: any prediction of GVG that modifies $\tau_{GR}$ by factor $(1 - S)$ can be immediately tested against LIGO data with the included `teste_blindagem(S)` function.

# State of the field

Statistical packages like SciPy, R stats, and StatsModels implement equivalence tests in isolation. No existing package proves or exploits the `dP=0` unification. In gravitational physics, Will (2014) reviews GR tests but does not provide code. MICROSCOPE collaboration provides data but not a unified pipeline for pulsar and GW comparison. LIGO software libraries (GWpy, PyCBC) focus on signal detection, not on WEP parameter estimation. `G21` fills this gap by bridging statistical theory and extreme-regime gravity tests in a lightweight, dependency-minimal package.

# Software design

The package structure is intentionally flat to minimize barriers: `codigo/` directory contains `G21_shielding.py`, `G21_velocity.py`, `G21_materia.py`. Each file is self-contained and imports only NumPy. The function `teste_blindagem(S)` implements $\tau_{G21} = \tau_{GR} * (1 - S)$ and returns `REFUTADA` or `COMPATÍVEL` based on sigma threshold. Tests for velocity use GW170817 + GRB170817A delay $\Delta t = 1.7$ s and speed of light $c = 299792458$ m/s. The repository includes `.zenodo.json` for automatic DOI minting, `LICENSE` (MIT), and continuous archiving to Zenodo `10.5281/zenodo.20618131`.

# Research impact statement

`G21` enables three communities: (i) statisticians can replace 21 tests with one, saving computation in large-scale simulations; (ii) gravitational physicists can test WEP violations with public data without building pipelines from scratch; (iii) developers of alternative theories (like GVG) can quantitatively constrain their parameters $S$ using real LIGO observations. As open software with permanent DOI, it promotes reproducible science and prevents duplication of effort in testing fundamental physics.

# AI usage disclosure

No generative AI was used to write the core algorithms. AI assistance was used for documentation formatting.

# Acknowledgements

We acknowledge LIGO Scientific Collaboration for open data via GWOSC, DataCite for DOI infrastructure, and the open-source Python community.

# References
