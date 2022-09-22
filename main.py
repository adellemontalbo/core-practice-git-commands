import pytest


def always_returns_true():
    return True
    print("This returns change")


def test_always_returns_true():
    assert always_returns_true()
