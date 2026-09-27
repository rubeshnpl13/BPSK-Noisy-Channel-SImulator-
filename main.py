import numpy as np


number_of_bits = 20
rng = np.random.default_rng(seed=42)

transmitted_bits = rng.integers(0, 2, size=number_of_bits)

print("Transmitted bits:", transmitted_bits)
print("Number of bits:", len(transmitted_bits))

transmitted_symbols = 2 * transmitted_bits - 1

print("BPSK symbols:", transmitted_symbols)
print("Number of symbols:", len(transmitted_symbols))

noise_std = 1.5

noise = rng.normal(
    loc=0.0,
    scale=noise_std,
    size=number_of_bits
)

received_symbols = transmitted_symbols + noise

print("Noise:", np.round(noise, 2))
print("Received symbols:", np.round(received_symbols, 2))

received_bits = (received_symbols >= 0).astype(int)

print("Received bits:", received_bits)
print("Number of received bits:", len(received_bits))


bit_errors = transmitted_bits != received_bits
number_of_errors = np.count_nonzero(bit_errors)
ber = number_of_errors / number_of_bits

print("Bit errors:", bit_errors)
print("Number of errors:", number_of_errors)
print("Bit error rate:", ber)

print("\n--- BER experiment across noise levels ---")

experiment_bits = 10_000
experiment_rng = np.random.default_rng(seed=123)

bits = experiment_rng.integers(0, 2, size=experiment_bits)
symbols = 2 * bits - 1

noise_levels = [0.2, 0.5, 1.0, 1.5, 2.0]
ber_results = []

for noise_level in noise_levels:
    noise = experiment_rng.normal(
        loc=0.0,
        scale=noise_level,
        size=experiment_bits
    )

    noisy_symbols = symbols + noise
    decoded_bits = (noisy_symbols >= 0).astype(int)

    errors = np.count_nonzero(bits != decoded_bits)
    error_rate = errors / experiment_bits

    ber_results.append(error_rate)

    print(
        f"Noise std: {noise_level:.1f} | "
        f"Errors: {errors} | "
        f"BER: {error_rate:.4f}"
    )