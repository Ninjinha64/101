import keyboard
import random

def roll_dice():
    """Simula o lançamento de um dado de seis lados."""
    return random.randint(1, 6)

while True:
    # Espera o usuário pressionar o botão "y"
    keyboard.wait('y')

    # Simula o lançamento do dado e imprime o resultado
    resultado = roll_dice()
    print("O resultado do lançamento do dado foi:", resultado)
