from mpmath import zetazero, zeta, mp
import matplotlib.pyplot as plt

# Set precision for mpmath (in decimal places)
mp.dps = 50  # Adjust this for higher precision

# Collect zeros
real_parts = []
imag_parts = []

print("Finding zeros of the zeta function on the critical line:")
for n in range(1, 21):  # First 20 non-trivial zeros
    zero = zetazero(n)  # Get the nth zero of the zeta function
    print(f"Zero {n}: 0.5 + {zero.imag}i")
    real_parts.append(zero.real)  # Real part should be 0.5 for all points
    imag_parts.append(zero.imag)  # Imaginary part

# Plot the zeros
plt.figure(figsize=(10, 6))
plt.scatter(real_parts, imag_parts, color='blue', marker='o')
plt.axvline(x=0.5, color='red', linestyle='--', label='Critical Line (Re(s) = 0.5)')
plt.xlabel('Real Part')
plt.ylabel('Imaginary Part')
plt.title('Zeros of the Riemann Zeta Function on the Critical Line')
plt.legend()
plt.grid(True)
plt.show()
