import numpy as np


number_of_bits = 20
rng = np.random.default_rng(seed=42)

transmitted_bits = rng.integers(0, 2, size=number_of_bits)

print("Transmitted bits:", transmitted_bits)
print("Number of bits:", len(transmitted_bits))

transmitted_symbols = 2 * transmitted_bits - 1

print("BPSK symbols:", transmitted_symbols)
print("Number of symbols:", len(transmitted_symbols))

noise_std = 0.5

noise = rng.normal(
    loc=0.0,
    scale=noise_std,
    size=number_of_bits
)

received_symbols = transmitted_symbols + noise

print("Noise:", np.round(noise, 2))
print("Received symbols:", np.round(received_symbols, 2))