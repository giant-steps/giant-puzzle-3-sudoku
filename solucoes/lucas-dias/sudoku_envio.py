import numpy as np
import numba as nb
import re
import pickle
import os

# Tabuleiro, incluindo os divisores nas bordas
board = np.array(
    [
        [0, 4, 0, 2, 0, 0, 11, 127, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [125, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [29, 0, 0, 0, 0, 0, 0, 0, 0, 0, 79],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 257, 0, 17, 0, 0, 5, 877, 0, 0, 0],
    ]
)

# Quadrado mágico 3x3
magic = np.array([[8, 1, 6], [3, 5, 7], [4, 9, 2],])

solucoes = []


def fase1(bo):
    """ Fase 1: testa rotações 90º do quadrado mágico """
    for i in range(4):
        bo[4:7, 4:7] = np.rot90(magic, i)

        if fase2(bo):
            print("Achou solução")
            return True

    print("Não achou")
    return False


def fase2(bo):
    """ Fase 2: testa espelhamentos do quadrado mágico """
    for i in range(2):
        if i == 1:
            bo[4:7, 4:7] = np.flip(bo[4:7, 4:7], 0)

        if fase3(bo):
            return True

    return False


def fase3(bo):
    """ Fase 3: preenche linhas/colunas com múltiplos das bordas """

    max_val, max_pos = busca_maior_divisor(bo)

    if max_val == 0:
        if fase4(bo):
            return True

        return False

    borda, slc, oposto = dados_borda(max_pos)

    mult = resgata_multiplos(max_val, bo[oposto], arr_to_str(bo[slc]), borda)

    for m in mult:
        test = int_to_arr(m)

        valido = True
        for i in range(len(test)):
            if borda == "t" or borda == "b":
                if not valida_sudoku(bo, test[i], (i + 1, slc[1])):
                    valido = False
            else:
                if not valida_sudoku(bo, test[i], (slc[0], i + 1)):
                    valido = False

        if not valido:
            continue

        old_slc = np.copy(bo[slc])
        bo[slc] = test
        bo[max_pos] = -max_val
        bo[oposto] = -bo[oposto]

        if fase3(bo):
            return True

        bo[slc] = old_slc
        bo[max_pos] = max_val
        bo[oposto] = -bo[oposto]

    return False


def fase4(bo):
    """ Fase 4: termina resolução do Sudoku """

    find = busca_vazio(bo)
    if not find:
        solucoes.append(board[1:10, 1:10].copy())
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valida_sudoku(bo, i, (row, col)):
            bo[row, col] = i

            if fase4(bo):
                return True

            bo[row, col] = 0

    return False


def busca_vazio(bo):
    for i in range(1, 10):
        for j in range(1, 10):
            if bo[i, j] == 0:
                return (i, j)

    return None


def busca_maior_divisor(bo):
    max_val = 0
    max_pos = (0, 0)
    for i in range(0, 11):
        for j in [0, 10]:
            if bo[i, j] > max_val:
                max_val = bo[i, j]
                max_pos = (i, j)
            elif bo[j, i] > max_val:
                max_val = bo[j, i]
                max_pos = (j, i)

    return max_val, max_pos


def valida_sudoku(bo, num, pos):
    """ Verifica se sudoku é válido """

    # Checa linha
    for i in range(1, 10):
        if bo[pos[0], i] == num and pos[1] != i:
            return False

    # Checa coluna
    for i in range(1, 10):
        if bo[i, pos[1]] == num and pos[0] != i:
            return False

    # Checa box
    box_x = (pos[1] - 1) // 3
    box_y = (pos[0] - 1) // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i + 1, j + 1] == num and (i + 1, j + 1) != pos:
                return False

    return True


def arr_to_str(x):
    return "".join([str(i) for i in x]).zfill(9)


def int_to_arr(x):
    return [int(i.zfill(9)) for i in str(x)]


def dados_borda(max_pos):
    """ Busca informações dos pares de divisores da borda """

    if max_pos[0] == 0:
        borda = "t"
    if max_pos[0] == 10:
        borda = "b"
    if max_pos[1] == 0:
        borda = "l"
    if max_pos[1] == 10:
        borda = "r"

    if borda == "t":
        slc = (slice(1, 10), max_pos[1])
        oposto = (10, max_pos[1])
    elif borda == "b":
        slc = (slice(1, 10), max_pos[1])
        oposto = (0, max_pos[1])
    elif borda == "l":
        slc = (max_pos[0], slice(1, 10))
        oposto = (max_pos[0], 10)
    elif borda == "r":
        slc = (max_pos[0], slice(1, 10))
        oposto = (max_pos[0], 0)

    return borda, slc, oposto


def resgata_multiplos(n1, n2, mascara, borda):
    """ Busca múltiplos salvos em arquivo """

    mult2 = []
    if borda == "b" or borda == "r":
        mascara = mascara[::-1]
    pat = re.compile(mascara.replace("0", "."))

    with open("%s@%s" % (n1, n2), "rb") as f:
        mult = pickle.load(f)

    for i in mult:
        si = str(i)
        if not pat.match(si):  # encaixa no board
            continue

        if borda == "b" or borda == "r":
            i = int(si[::-1])

        mult2.append(i)

    return mult2


def salva_multiplos(bo):
    """ Salva em arquivo os múltiplos de uma dupla de divisores,
    pois isso economiza tempo na resolução """

    max_val, max_pos = busca_maior_divisor(bo)

    if max_val == 0:
        return True

    borda, slc, oposto = dados_borda(max_pos)

    # print(max_val, bo[oposto])

    # não precisa pegar o oposto quando é negativo
    if bo[oposto] >= 0:
        mult = salva_multiplos_aux(max_val, bo[oposto])
        with open("%s@%s" % (max_val, bo[oposto]), "wb") as f:
            pickle.dump(mult, f)

    bo[max_pos] = -max_val
    bo[oposto] = -bo[oposto]

    if salva_multiplos(bo):
        return True


@nb.njit(cache=True, nogil=True)
def salva_multiplos_aux(n1, n2):
    """ Auxiliar da rotina dos múltiplos, para filtrar
    os números que funcionam para um dado par de divisores n1, n2 """
    mult = []

    for i in range(n1, int(1e9), n1): # busca candidato a múltiplo
        if i < 123456789: # filtra números pequenos
            continue
        if tem_digito(i, 0):  # não pode ter dígito zero
            continue
        if tem_digitos_duplicados(i):  # não pode ter dígitos duplicados
            continue
        if n2 > 0 and reverter_int(i) % n2 != 0: # divisível pelo oposto
            continue

        mult.append(i)

    return mult


@nb.njit(cache=True, nogil=True)
def tem_digito(x, d):
    while x > 0:
        if x % 10 == d:
            return True
        x = x // 10

    return False


@nb.njit(cache=True, nogil=True)
def tem_digitos_duplicados(x):
    digitos = []
    while x > 0:
        d = x % 10
        for i in digitos:
            if i == d:
                return True
        digitos.append(d)
        x = x // 10

    return False


@nb.njit(cache=True, nogil=True)
def reverter_int(x):
    rev = 0
    while x > 0:
        rev = (10 * rev) + x % 10
        x //= 10
    return rev


def main():
    print("Salvando múltiplos previamente...")
    salva_multiplos(board.copy())
    print("Resolvendo...")
    fase1(board)
    print(solucoes)


if __name__ == "__main__":
    main()
