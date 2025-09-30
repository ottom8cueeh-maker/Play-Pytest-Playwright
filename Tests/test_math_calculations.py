import re
from playwright.sync_api import Playwright, sync_playwright, expect
import pytest

# content of test_sample.py
def add(a, b):
    return a + b

def minus(a, b):
    return a - b

def test_addition():
    assert add(1, 9) == 10

def test_subtraction():
    assert add(10, 1) > 0

