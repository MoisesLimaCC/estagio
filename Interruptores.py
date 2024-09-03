import time

def descobrir_interruptores():
    # Inicializando os interruptores e lâmpadas
    interruptores = [False, False, False]
    lampadas = [False, False, False]
    temperaturas = ["fria", "fria", "fria"]

    # Passo 1: Ligar o primeiro interruptor e esperar
    interruptores[0] = True
    time.sleep(2)  # Simula esperar alguns minutos
    lampadas[0] = True
    temperaturas[0] = "quente"

    # Passo 2: Desligar o primeiro interruptor e ligar o segundo
    interruptores[0] = False
    interruptores[1] = True
    lampadas[0] = False
    lampadas[1] = True

    # Passo 3: Ir até a sala das lâmpadas
    # Verificar qual lâmpada está acesa e as temperaturas das lâmpadas apagadas
    for i in range(3):
        if lampadas[i]:
            print(f"A lâmpada {i+1} está acesa. Controlada pelo interruptor 2.")
        elif temperaturas[i] == "quente":
            print(f"A lâmpada {i+1} está quente. Controlada pelo interruptor 1.")
        else:
            print(f"A lâmpada {i+1} está fria. Controlada pelo interruptor 3.")

# Executar a função
descobrir_interruptores()
