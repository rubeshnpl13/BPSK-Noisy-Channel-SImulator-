import numpy as np


class BPSKTransmitter:
    def __init__(self, rng):
        self.rng = rng

    def generate_bits(self, number_of_bits):
        return self.rng.integers(0, 2, size=number_of_bits)

    def modulate(self, bits):
        return 2 * bits - 1


class NoisyChannel:
    def __init__(self, noise_std, rng):
        self.noise_std = noise_std
        self.rng = rng

    def transmit(self, symbols):
        noise = self.rng.normal(
            loc=0.0,
            scale=self.noise_std,
            size=len(symbols)
        )
        received_symbols = symbols + noise
        return received_symbols, noise


class BPSKReceiver:
    def decode(self, received_symbols):
        return (received_symbols >= 0).astype(int)