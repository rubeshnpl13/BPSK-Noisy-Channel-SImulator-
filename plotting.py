import matplotlib.pyplot as plt


def plot_ber(noise_levels, simulated_ber_results, expected_ber_results):
    fig, ax = plt.subplots(figsize=(7, 4))

    ax.plot(
        noise_levels,
        simulated_ber_results,
        marker="o",
        label="Simulated BER"
    )

    ax.plot(
        noise_levels,
        expected_ber_results,
        marker="x",
        linestyle="--",
        label="Expected BER"
    )

    ax.set_title("BPSK bit error rate vs. noise")
    ax.set_xlabel("Noise standard deviation")
    ax.set_ylabel("Bit error rate (BER)")
    ax.set_ylim(bottom=0)
    ax.grid(True)
    ax.legend()

    fig.tight_layout()
    fig.savefig("ber_simulated_vs_expected.png", dpi=150)
    plt.show()