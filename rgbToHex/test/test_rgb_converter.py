# test_rgb_converter.py

from app.rgb_converter import is_in_range, rgbToHex

def test_is_in_range_valid_values():
    assert is_in_range([100, 150, 200]) == True

def test_is_in_range_invalid_values():
    assert is_in_range([-50, 256, 120]) == False

def test_rgbToHex_valid_values():
    hex_string = rgbToHex(100, 150, 200)
    assert hex_string == "6496C8"

def test_rgbToHex_invalid_values():
    hex_string = rgbToHex(-50, 256, 120)
    assert hex_string == ""