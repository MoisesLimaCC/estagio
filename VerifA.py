def count_letter_a(s):
    count = s.lower().count('a')
    if count > 0:
        return f"A letra 'a' aparece {count} vezes na string."
    else:
        return "A letra 'a' não aparece na string."


string = input("Informe uma string: ")
print(count_letter_a(string))
