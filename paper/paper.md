---
title: 'G21 Equivalence Tests: Weak Equivalence Principle in Extreme Regimes and dP=0 Unification'
tags:
    - python
    - statistics
    - equivalence-principle
    - gravitational-physics
    - gvg-theory
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

`G21-Equivalence-Tests` implements five experimental tests of the Weak Equivalence Principle (WEP) in extreme regimes (pulsars, MICROSCOPE, GW170817) and the mathematical unification where 21 statistical tests collapse to `dP = 0`. The codes `G21_shielding.py`, `G21_velocity.py` and `G21_materia.py` provide reproducible tests for GVG theory predictions.

# Statement of need

Tests of WEP are scattered across different missions and formalisms. Researchers need an open, unified software to test gravitational shielding (G21.1), GW velocity (G21.2) and matter equivalence against public LIGO/Virgo and pulsar data. `G21` provides pip-installable Python tests with public data (GW150914 tau = 4.0 ms).

# State of the field

Existing libraries (e.g., SciPy) implement isolated statistical tests. No package unifies the 21 tests under `dP=0` nor provides WEP tests in strong-field regimes linking pulsars, MICROSCOPE and GW observations.

# Mathematics

Core: `tau_G21 = tau_GR * (1 - S)` for shielding, where `S` is shielding parameter. Compatibility: `sigma = |tau_G21 - tau_obs| / erro_tau`. If `sigma > 2`, refuted.

# References
