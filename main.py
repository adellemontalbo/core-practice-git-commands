import pytest


def always_returns_true():
    return "True"


def test_always_returns_true():
    assert not always_returns_true()
