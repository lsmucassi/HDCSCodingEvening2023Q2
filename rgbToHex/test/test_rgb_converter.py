# test_rgb_converter.py

from app.rgb_converter import is_in_range, rgbToHex

def test_is_in_range_valid_values():
    assert is_in_range([100, 150, 200]) == True
    assert is_in_range([-50, 256, 120]) == True
    assert is_in_range([-10, 128, 260]) == True  
    assert is_in_range([300, 200, -5]) == True  


def test_is_in_range_invalid_values():
    assert is_in_range(["", 256, 120]) == False
    assert is_in_range(["-90", 256, 120]) == False
    assert is_in_range([90, "56", 120]) == False
    assert is_in_range([45, 256, "Linda"]) == False



def test_rgbToHex_valid_values():
    hex_string = rgbToHex(100, 150, 200)
    assert hex_string == "6496C8"
    assert rgbToHex(255, 255, 255) == "FFFFFF"
    assert rgbToHex(0, 0, 0) == "000000"
    assert rgbToHex(148, 0, 211) == "9400D3"
    assert rgbToHex(-10, 128, 200) == "0080C8" 
    assert rgbToHex(255, 128, 260) == "FF80FF"  
    assert rgbToHex(100, 150, 200) == "6496C8"
    assert rgbToHex(-10, 128, 260) == "0080FF" 
    assert rgbToHex(300, 200, -5) == "FFC800" 
    assert rgbToHex(255, 255, 300) == "FFFFFF"  


def test_rgbToHex_invalid_values():
    assert rgbToHex("", 256, 120) == ""
    assert rgbToHex("-90", 256, 120) == ""
    assert rgbToHex(90, "56", 120) == ""
    assert rgbToHex(45, 256, "Linda") == ""
    

