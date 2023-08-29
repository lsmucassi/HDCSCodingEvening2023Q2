def is_in_range(r_g_b: list) -> bool:
    '''
        takes in  a number and check if it's in the range 0 - 255 and if the values are numeric(int)
    '''
    results = []

    for num in r_g_b:
        # check if the value is a number
        if isinstance(num, (int)):
            # check if values are within range 0 - 255
            # if a number is less than 0, treat it as a zero
            if num < 0:
                num = 0
            elif num > 255:
                num = 255
            
            results.append(True if 0 <= num <= 255 else False)
        else:
            # if at east one value is not a number(int), return false
            return False
        
    return all(results)


def rgbToHex(r: int, g: int, b: int) -> str:
    hex_string = ""
    # check if RGB values are between 0 and 255
    if is_in_range([r, g, b]):
        hex_string = format(abs(r), '02X') + format(abs(g), '02X') + format(abs(b), '02X') 

    return hex_string

