def roman_conversion(rom):
    rom_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    rom = rom[::-1]
    num = 0
    current_value = 0
    for r in rom:
        value = rom_dict[r]
        if value > current_value:
            num = num + value
            current_value = value
        else:
            num = num - value
    return num


print(roman_conversion('DV'))
