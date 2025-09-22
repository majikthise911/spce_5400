"""
visualizations.py

Starter module for plotting and visual analytics related to the spce_5400 project.
Add your plotting functions here. Example usage provided at the bottom guard.
"""

from __future__ import annotations

from typing import Iterable, Optional

import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd


def plot_time_series(
    data: pd.DataFrame | pd.Series,
    *,
    title: str = "Time Series",
    x_label: str = "Date",
    y_label: str = "Value",
    legend: bool = True,
    figsize: tuple[int, int] = (10, 5),
    grid: bool = True,
    colors: Optional[Iterable[str]] = None,
) -> plt.Axes:
    """Plot a simple time series from a pandas Series or DataFrame.

    Parameters
    ----------
    data: DataFrame | Series
        Index should ideally be datetime-like. If a DataFrame is provided,
        each column will be plotted as a separate line.
    title: str
        Figure title.
    x_label: str
        X-axis label.
    y_label: str
        Y-axis label.
    legend: bool
        Whether to show legend for DataFrame columns.
    figsize: tuple[int, int]
        Figure size in inches.
    grid: bool
        Whether to show grid.
    colors: Optional[Iterable[str]]
        Optional list/iterable of colors to use for lines.

    Returns
    -------
    matplotlib.axes.Axes
        The axes containing the plot for further customization.
    """
    fig, ax = plt.subplots(figsize=figsize)

    if isinstance(data, pd.Series):
        ax.plot(data.index, data.values, color=None if colors is None else list(colors)[0])
    else:
        # If colors are provided, cycle them; otherwise let Matplotlib decide
        if colors is not None:
            for color, (col_name, series) in zip(colors, data.items()):
                ax.plot(series.index, series.values, label=str(col_name), color=color)
        else:
            for col_name, series in data.items():
                ax.plot(series.index, series.values, label=str(col_name))

    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    if grid:
        ax.grid(True, linestyle="--", alpha=0.4)

    if legend and isinstance(data, pd.DataFrame) and data.shape[1] > 1:
        ax.legend()

    fig.tight_layout()
    return ax


if __name__ == "__main__":
    ebno_db = np.linspace(0, 15, 200)  # Eb/No range in dB
    ebno = 10 ** (ebno_db / 10)  # Linear Eb/No

    # BER approximations (simple exponentials for quick visualization)
    ber_bpsk = 0.5 * np.exp(-ebno)
    ber_qpsk = 0.5 * np.exp(-ebno)  # QPSK same theoretical BER as BPSK per bit
    # 16-QAM approximate per-bit BER (loose exponential fit for quick viz)
    # Note: For accurate results, use Q-function-based expressions
    k = 0.75  # shaping factor to loosely reflect higher BER of 16-QAM
    ber_16qam = k * np.exp(-0.2 * ebno)

    plt.figure(figsize=(9, 5))
    plt.semilogy(ebno_db, ber_bpsk, label="BPSK")
    plt.semilogy(ebno_db, ber_qpsk, label="QPSK")
    plt.semilogy(ebno_db, ber_16qam, label="16-QAM")

    plt.xlabel("Eb/No (dB)")
    plt.ylabel("BER")
    plt.grid(True, which="both", linestyle="--", alpha=0.4)
    plt.legend()
    plt.title("BER vs Eb/No (Quick Approximations)")

    # Save to figures folder
    figures_dir = os.path.join(os.path.dirname(__file__), "figures")
    os.makedirs(figures_dir, exist_ok=True)
    out_path = os.path.join(figures_dir, "ber_vs_ebno.png")
    plt.tight_layout()
    plt.savefig(out_path, dpi=150)

    # Also show if a display is available
    try:
        plt.show()
    except Exception:
        pass

    print(f"Saved BER plot to: {out_path}")
