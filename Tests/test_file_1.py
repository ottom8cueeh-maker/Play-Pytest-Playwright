import re
from playwright.sync_api import Playwright, sync_playwright, expect
import pytest

# content of test_sample.py
def func(x):
    return x + 1

def add(a, b):
    return a + b


def test_answer():
    assert func(4) == 5


def test_addition():
    assert add(1, 9) == 10