def ceaser_cipher():
    str_to_encrypt = input("Wpisz frazę do zaszyfrowania: ")
    result = ""
    offset = 1
    for char in str_to_encrypt:
        print(f'Szyfrowany znak - {char}, obece przesunięcie: {offset}')
        if 65 <= ord(char) <= 90:  # char is upper letter
            result += (chr((ord(char) + offset - 65) % 26 + 65))  # to ensure new value will be from scope
            # 65 - 90
        elif 97 <= ord(char) <= 122:  # char is lower letter
            result += (chr((ord(char) + offset - 97) % 26 + 97))  # to ensure new value will be from scope
            # 97 - 122
        else:  # char is NOT a letter
            result += char
        offset += 1
    print(result)


ceaser_cipher()


