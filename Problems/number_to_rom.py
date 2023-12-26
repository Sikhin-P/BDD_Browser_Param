def num_to_rom(num):
    number = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
    rom = ""
    i = 12

    while num:
        div = num // number[i]
        num = num % number[i]
        while div:
            rom = rom + sym[i]
            div = div - 1
        i = i - 1
    return rom


print(num_to_rom(505))
