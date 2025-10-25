import re
from playwright.sync_api import Playwright, sync_playwright, expect
import pytest

# content of test_sample.py
def rectangle_area(l, w):
    return l * w

def rectangle_perimeter(l, w):
    return 2*l + 2*w

def triangle_area(b, h):
    return 0.5*b*h

def triangle_perimeter(a, b, c):
    return a+b+c

def circle_circumference(r):
    return 2*3.142*r

def test_rectangle_area():
    assert rectangle_area(1, 1) == 1

def test_rectangle_perimeter():
    assert rectangle_perimeter(2, 2) == 8

def test_triangle_area():
    assert triangle_area(1, 2) == 1

def test_triangle_perimeter():
    assert triangle_perimeter(1, 2,3) == 6

def test_circle_circumference():
    assert circle_circumference(1) == 6.284
