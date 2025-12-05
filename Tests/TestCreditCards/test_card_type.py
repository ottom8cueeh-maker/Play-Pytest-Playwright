import re
from playwright.sync_api import Playwright, sync_playwright, expect
import pytest

def get_card_type(cardno):
    match cardno:
        case '4242424242424242':
            return "Visa"
        case '5555555555554444':
            return "MasterCard"
        case _:
            return "Unknown Number"


def test_visa_card(cn='4242424242424242'):
    assert get_card_type(cn) == "Visa"