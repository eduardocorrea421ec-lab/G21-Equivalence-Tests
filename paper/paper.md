---
title: "G21 Equivalence Tests"
tags: [python, statistics]
authors:
    - name: Eduardo Correa
    affiliation: 1
affiliations:
    - name: Independent Researcher
    index: 1
date: 12 November 2026
bibliography: paper.bib
---

# Summary

G21-Equivalence-Tests implements five experimental tests of the Weak Equivalence Principle in extreme regimes (pulsars, MICROSCOPE, GW170817) and the mathematical unification where 21 statistical tests collapse to dP=0.

# Statement of need

Tests of WEP are scattered across missions. Researchers need open software to test gravitational shielding (G21.1), GW velocity (G21.2) and matter equivalence against public LIGO data.

# State of the field

Existing libraries like SciPy implement isolated tests. No package unifies 21 tests under dP=0 nor provides WEP tests in strong-field regimes.

# Software design

Package is flat: codigo/ contains G21_shielding.py, G21_velocity.py, G21_materia.py. Each imports only NumPy. Function teste_blindagem(S) implements tau_G21 = tau_GR * (1 - S).

# Research impact statement

G21 enables statisticians to replace 21 tests with one and physicists to test WEP with public LIGO data.

# AI usage disclosure

No generative AI used for core algorithms.

# Acknowledgements

We acknowledge LIGO Scientific Collaboration for open data via GWOSC.

# References
