import matplotlib.pyplot as plt


def plot_ber(noise_levels, ber_results):
    fig, ax = plt.subplots(figsize=(7, 4))

    ax.plot(noise_levels, ber_results, marker="o")
    ax.set_title("BPSK bit error rate vs. noise")
    ax.set_xlabel("Noise standard deviation")
    ax.set_ylabel("Bit error rate (BER)")
    ax.set_ylim(bottom=0)
    ax.grid(True)

    fig.tight_layout()
    plt.show()