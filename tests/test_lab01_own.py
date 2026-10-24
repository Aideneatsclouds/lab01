"""Custom tests for Lab 1 covering boundary cases, zero totals, and invalid inputs."""
import pytest
from src.basics import gc_percent, parse_counts


def test_gc_percent_boundary_all_gc():
    """Boundary case: 100% GC content (only G and C counts provided)."""
    assert gc_percent(0, 25, 25, 0) == pytest.approx(100.0)


def test_gc_percent_zero_total():
    """Zero-total case: all counts are zero should raise ValueError."""
    with pytest.raises(ValueError):
        gc_percent(0, 0, 0, 0)


def test_parse_counts_invalid_format():
    """Invalid-input case: incorrect number of tokens or negative values."""
    with pytest.raises(ValueError):
        parse_counts("10 20 30")  # Only three values instead of four

    with pytest.raises(ValueError):
        parse_counts("10, -5, 20, 15")  # Negative value