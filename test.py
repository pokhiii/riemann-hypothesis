from mpmath import zeta, mp

mp.dps = 50  # High precision

for t in range(1, 21):  # Test points on the critical line
    s = 0.5 + t * 1j
    zeta_value = zeta(s)
    print(f"t = {t}, zeta(0.5 + {t}i) = {zeta_value}")
