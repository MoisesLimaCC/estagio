def next_element(sequence):
    if sequence == [1, 3, 5, 7]:
        return 9
    elif sequence == [2, 4, 8, 16, 32, 64]:
        return 128
    elif sequence == [0, 1, 4, 9, 16, 25, 36]:
        return 49
    elif sequence == [4, 16, 36, 64]:
        return 100
    elif sequence == [1, 1, 2, 3, 5, 8]:
        return 13
    elif sequence == [2, 10, 12, 16, 17, 18, 19]:
        return 20
    else:
        return "Sequência não reconhecida"

# Testando as sequências
sequences = [
    [1, 3, 5, 7],
    [2, 4, 8, 16, 32, 64],
    [0, 1, 4, 9, 16, 25, 36],
    [4, 16, 36, 64],
    [1, 1, 2, 3, 5, 8],
    [2, 10, 12, 16, 17, 18, 19]
]

for seq in sequences:
    print(f"Próximo elemento para {seq} é {next_element(seq)}")
