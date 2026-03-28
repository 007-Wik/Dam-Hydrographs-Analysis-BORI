"""
plot_config.py
Kurnur (BORI) Dam – Breach & Hydrograph Analysis
Shared plotting configuration for all notebooks.

Usage:
    from src.utils.plot_config import apply_engineering_style, COLORS

Author: Satwik Udupi
"""

import matplotlib.pyplot as plt
import matplotlib as mpl

# ── Color palette ──────────────────────────────────────────────────────────────
COLORS = {
    "headwater":        "#1f77b4",   # Blue      – upstream water surface
    "tailwater":        "#17becf",   # Cyan      – downstream water surface
    "total_discharge":  "#d62728",   # Red       – total outflow
    "breach_discharge": "#ff7f0e",   # Orange    – breach flow
    "breach_width":     "#9467bd",   # Purple    – breach opening width
    "breach_velocity":  "#2ca02c",   # Green     – breach mean velocity
    "grid":             "#e0e0e0",   # Light grey – background grid
    "peak_marker":      "#e377c2",   # Pink      – peak annotation
}

# ── Figure dimensions ──────────────────────────────────────────────────────────
FIG_WIDTH  = 14    # inches
FIG_HEIGHT = 6     # inches
DPI_SCREEN = 100   # screen rendering
DPI_EXPORT = 300   # regulatory submission export


def apply_engineering_style():
    """Apply engineering-grade matplotlib style settings."""
    mpl.rcParams.update({
        "figure.facecolor":   "white",
        "axes.facecolor":     "white",
        "axes.grid":          True,
        "grid.color":         COLORS["grid"],
        "grid.linestyle":     "--",
        "grid.linewidth":     0.6,
        "axes.spines.top":    False,
        "axes.spines.right":  False,
        "font.family":        "DejaVu Sans",
        "font.size":          11,
        "axes.titlesize":     13,
        "axes.labelsize":     12,
        "legend.fontsize":    10,
        "legend.framealpha":  0.85,
        "legend.edgecolor":   "#cccccc",
        "xtick.direction":    "out",
        "ytick.direction":    "out",
        "figure.dpi":         DPI_SCREEN,
        "savefig.dpi":        DPI_EXPORT,
        "savefig.bbox":       "tight",
        "lines.linewidth":    2.0,
    })


def add_peak_annotation(ax, time_series, discharge_series, label="Q_peak"):
    """Annotate the peak discharge on a given axis."""
    idx_peak = discharge_series.idxmax()
    q_peak   = discharge_series.max()
    t_peak   = time_series[idx_peak]

    ax.axvline(t_peak, color=COLORS["peak_marker"], linestyle=":", linewidth=1.2, alpha=0.8)
    ax.annotate(
        f"{label} = {q_peak:.1f} m³/s\n@ T = {t_peak:.2f} hr",
        xy=(t_peak, q_peak),
        xytext=(t_peak + 0.5, q_peak * 0.9),
        fontsize=9,
        color=COLORS["peak_marker"],
        arrowprops=dict(arrowstyle="->", color=COLORS["peak_marker"], lw=1.0),
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor=COLORS["peak_marker"], alpha=0.8),
    )


def add_breach_initiation_line(ax, t_breach, label="Breach Initiation"):
    """Mark breach initiation time with a vertical dashed line."""
    ax.axvline(t_breach, color="#555555", linestyle="--", linewidth=1.0, alpha=0.7, label=label)


def save_figure(fig, filepath, dpi=DPI_EXPORT):
    """Save figure at regulatory-grade resolution."""
    fig.savefig(filepath, dpi=dpi, bbox_inches="tight", facecolor="white")
    print(f"Figure saved: {filepath} at {dpi} DPI")
