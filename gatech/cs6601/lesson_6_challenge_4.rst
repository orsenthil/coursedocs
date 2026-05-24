Challenge: Bayes Net Calculation
=================================

Given a Bayes network with variables: Lung Disease (LD), Cold (C), Cough (Co), Fever (F).

Problem 1: P(LD=T | Cough=T)
------------------------------

Using Bayes' rule:

::

    P(LD=T | Cough=T) = P(Cough=T | LD=T) * P(LD=T)
                        ---------------------------
                                P(Cough=T)

    Numerator:
    P(Co=T|LD=T) = P(Co=T|LD=T,C=T)*P(C=T) + P(Co=T|LD=T,C=F)*P(C=F)
                 = (0.80 * 0.30 + 0.75 * 0.70) = 0.765

    P(Co=T|LD=T) * P(LD=T) = 0.765 * 0.10 = 0.0765

    Denominator (total probability):
    = (0.80*0.30*0.10) + (0.30*0.30*0.90) + (0.75*0.70*0.10) + (0.05*0.70*0.90)
    = 0.189

    Result: 0.0765 / 0.189 ≈ 0.405

Problem 2: P(LD=T | Cough=T, Fever=T)
---------------------------------------

Enumerate over hidden variable Cold:

::

    P(Co=T,F=T | LD=T) * P(LD=T)
    = P(LD=T) * Σ_cold [P(Co=T|LD=T,cold) * P(F=T|cold) * P(cold)]
    = 0.10 * [(0.80 * 0.65 * 0.30) + (0.75 * 0.25 * 0.70)]
    = 0.028725

    P(Co=T,F=T | LD=F) * P(LD=F)
    = 0.90 * [(0.30 * 0.65 * 0.30) + (0.05 * 0.25 * 0.70)]
    = 0.060525

    P(LD=T | Co=T,F=T) = 0.028725 / (0.028725 + 0.060525) ≈ 0.322

References
----------
