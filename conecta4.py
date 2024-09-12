import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

plt.ion()
board = np.zeros((6, 7))

def draw_board(board, winner=None, message=None, turn_message=None):
    fig, ax = plt.subplots(figsize=(8, 7))
    ax.clear()
    for row in range(6):
        for col in range(7):
            ax.add_patch(patches.Circle((col + 0.5, 5.5 - row), 0.45, color='blue'))
            if board[row, col] == 1:
                ax.add_patch(patches.Circle((col + 0.5, 5.5 - row), 0.45, color='red'))
            elif board[row, col] == 2:
                ax.add_patch(patches.Circle((col + 0.5, 5.5 - row), 0.45, color='green'))
    ax.set_xlim(0, 7)
    ax.set_ylim(0, 6)
    ax.axis('off')
    for col in range(7):
        ax.text(col + 0.5, -0.3, str(col + 1), ha='center', va='center', size=20)
    if winner is not None:
        ax.text(3.5, 6.2, "Jugador {} gana!".format(winner), ha='center', fontsize=24)
    if message is not None:
        ax.text(3.5, 6.5, message, ha='center', fontsize=18)
    if turn_message is not None:
        ax.text(3.5, 6.2, turn_message, ha='center', va='center', fontsize=18)
    plt.draw()
    plt.pause(0.1)

def drop_disc(board, col, player):
    for row in range(6):
        if board[5 - row, col] == 0:
            board[5 - row, col] = player
            return True
    return False

def check_win(board):
    # Verificar victoria en horizontal
    for row in range(6):
        for col in range(7 - 3):  # Ajustar el rango para evitar índices fuera de rango
            if np.all([board[row, col + i] == board[row, col] for i in range(4)]) and board[row, col] != 0:
                return True

    # Verificar victoria en vertical
    for row in range(6 - 3):  # Ajustar el rango para evitar índices fuera de rango
        for col in range(7):
            if np.all([board[row + i, col] == board[row, col] for i in range(4)]) and board[row, col] != 0:
                return True

    # Verificar victoria en diagonal (de arriba a abajo)
    for row in range(6 - 3):  # Ajustar el rango para evitar índices fuera de rango
        for col in range(7 - 3):  # Ajustar el rango para evitar índices fuera de rango
            if np.all([board[row + i, col + i] == board[row, col] for i in range(4)]) and board[row, col] != 0:
                return True

    # Verificar victoria en diagonal (de abajo a arriba)
    for row in range(3, 6):  # Ajustar el rango para evitar índices fuera de rango
        for col in range(7 - 3):  # Ajustar el rango para evitar índices fuera de rango
            if np.all([board[row - i, col + i] == board[row, col] for i in range(4)]) and board[row, col] != 0:
                return True

    return False

def jugar_de_nuevo():
    respuesta = input("¿Quieres jugar de nuevo? (y/n): ")
    if respuesta.lower() == "y":
        return True
    else:
        return False

def juego_conecta4():
    print("Bienvenido al juego de Conecta 4!")
    print("El objetivo es conectar 4 discos del mismo color en horizontal, vertical o diagonal.")
    board = np.zeros((6, 7))
    player = 1
    turn_message = ""
    while True:
        turn_message = "Turno jugador {}".format(player)
        draw_board(board, message="Bienvenido al juego de Conecta 4!", turn_message=turn_message)
        col = int(input("Elige columna (1-7): ".format(player))) - 1
        if 0 <= col < 7 and drop_disc(board, col, player):
            if check_win(board):
                draw_board(board, winner=player)
                if not jugar_de_nuevo():
                    draw_board(board, message="Gracias por jugar!")
                    break
                else:
                    board = np.zeros((6, 7))
                    player = 1
            else:
                player = 3 - player
        else:
            draw_board(board, message="Columna llena o fuera de rango. Intenta de nuevo.", turn_message=turn_message)

juego_conecta4()