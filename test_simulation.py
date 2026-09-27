import unittest

import numpy as np

from simulation import BPSKTransmitter, NoisyChannel, BPSKReceiver


class TestBPSKSimulation(unittest.TestCase):
    def test_generate_bits_has_requested_length_and_binary_values(self):
        rng = np.random.default_rng(seed=42)
        transmitter = BPSKTransmitter(rng)

        bits = transmitter.generate_bits(100)

        self.assertEqual(len(bits), 100)
        self.assertTrue(np.all((bits == 0) | (bits == 1)))

    def test_modulate_maps_bits_to_bpsk_symbols(self):
        rng = np.random.default_rng(seed=42)
        transmitter = BPSKTransmitter(rng)
        bits = np.array([0, 1, 1, 0])

        symbols = transmitter.modulate(bits)

        np.testing.assert_array_equal(symbols, [-1, 1, 1, -1])

    def test_zero_noise_preserves_symbols(self):
        rng = np.random.default_rng(seed=42)
        channel = NoisyChannel(noise_std=0.0, rng=rng)
        symbols = np.array([-1, 1, -1, 1])

        received_symbols, noise = channel.transmit(symbols)

        np.testing.assert_array_equal(noise, [0, 0, 0, 0])
        np.testing.assert_array_equal(received_symbols, symbols)

    def test_receiver_decodes_using_zero_threshold(self):
        receiver = BPSKReceiver()
        received_symbols = np.array([-0.2, 0.0, 0.2])

        bits = receiver.decode(received_symbols)

        np.testing.assert_array_equal(bits, [0, 1, 1])


if __name__ == "__main__":
    unittest.main()