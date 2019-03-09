def is_palindrome(palindrome):
    # Por si nos pasan un número lo pasamos a string, luego minúsculas y finalmente quitamos espacios
    standard = str(palindrome).lower().replace(" ", "")
    # En string [::-1] da la vuelta a la cadena de texto
    return standard == standard[::-1]


palindromes = [
    "is not palindrome",
    "radar",
    "this is pallap si siht",
    1234321,
    1221,
    "na",
    1,
    4251651
]

for p in palindromes:
    if is_palindrome(p):
        print(str(p) + " is palindrome.")
    else:
        print(str(p) + " is NOT palindrome.")
