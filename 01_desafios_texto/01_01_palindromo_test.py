def palindromo(text):

    text_lower = text.lower()
    text_min = text_lower.replace(" ", "")
    return text_min == text_min[::-1]


frase_1 = "Dabale arroz a la zorra el abad"
frase_2 = 'Cualquier cosa loco'
# palindromo(frase_1)
print(palindromo(frase_1))
print(palindromo(frase_2))
