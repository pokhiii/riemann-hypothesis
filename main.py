from mpmath import zetazero, zeta, mp

# Set precision for mpmath (in decimal places)
mp.dps = 50  # You can adjust this for higher precision

print("Finding zeros of the zeta function on the critical line:")
for n in range(1, 21):  # First 20 non-trivial zeros
    zero = zetazero(n)  # Get the nth zero of the zeta function
    print(f"Zero {n}: 0.5 + {zero.imag}i")
