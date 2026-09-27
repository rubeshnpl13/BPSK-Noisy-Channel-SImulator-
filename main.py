import numpy as np

from plotting import plot_ber
from simulation import BPSKTransmitter, NoisyChannel, BPSKReceiver


# Small demonstration: inspect individual bits, symbols, and noise values.
number_of_bits = 20
rng = np.random.default_rng(seed=42)

transmitter = BPSKTransmitter(rng)
receiver = BPSKReceiver()

transmitted_bits = transmitter.generate_bits(number_of_bits)
print("Transmitted bits:", transmitted_bits)
print("Number of bits:", len(transmitted_bits))

transmitted_symbols = transmitter.modulate(transmitted_bits)
print("BPSK symbols:", transmitted_symbols)
print("Number of symbols:", len(transmitted_symbols))

noise_std = 1.5
channel = NoisyChannel(noise_std, rng)
received_symbols, noise = channel.transmit(transmitted_symbols)

print("Noise:", np.round(noise, 2))
print("Received symbols:", np.round(received_symbols, 2))

received_bits = receiver.decode(received_symbols)
print("Received bits:", received_bits)
print("Number of received bits:", len(received_bits))

bit_errors = transmitted_bits != received_bits
number_of_errors = np.count_nonzero(bit_errors)
ber = number_of_errors / number_of_bits

print("Bit errors:", bit_errors)
print("Number of errors:", number_of_errors)
print("Bit error rate:", ber)


# Larger experiment: measure BER at several noise levels.
print("\n--- BER experiment across noise levels ---")

experiment_bits = 10_000
experiment_rng = np.random.default_rng(seed=123)

experiment_transmitter = BPSKTransmitter(experiment_rng)
experiment_receiver = BPSKReceiver()

bits = experiment_transmitter.generate_bits(experiment_bits)
symbols = experiment_transmitter.modulate(bits)

noise_levels = [0.2, 0.5, 1.0, 1.5, 2.0]
ber_results = []

for noise_level in noise_levels:
    experiment_channel = NoisyChannel(noise_level, experiment_rng)
    noisy_symbols, _ = experiment_channel.transmit(symbols)
    decoded_bits = experiment_receiver.decode(noisy_symbols)

    errors = np.count_nonzero(bits != decoded_bits)
    error_rate = errors / experiment_bits
    ber_results.append(error_rate)

    print(
        f"Noise std: {noise_level:.1f} | "
        f"Errors: {errors} | "
        f"BER: {error_rate:.4f}"
    )

plot_ber(noise_levels, ber_results)