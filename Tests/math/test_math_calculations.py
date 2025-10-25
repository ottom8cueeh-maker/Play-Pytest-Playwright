import re
from playwright.sync_api import Playwright, sync_playwright, expect
import pytest

# content of test_sample.py
def add(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def test_addition():
    assert add(1, 9) == 10

def test_subtraction():
    assert minus(10, 1) > 0

@pytest.mark.regression
def test_multiplication():
    assert multiply(4, 5) == 20

@pytest.mark.regression
def test_division():
    assert divide(28, 4) == 7



