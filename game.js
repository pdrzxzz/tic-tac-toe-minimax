import math

# Verifica se há um vencedor ou empate
# Caso haja, retorna o 'X', 'O' ou 'Empate'
# Caso contrário, retorna None
def checar_vencedor(tabuleiro):
    linhas = tabuleiro
    colunas = [list(col) for col in zip(*tabuleiro)]
    diagonais = [[tabuleiro[i][i] for i in range(3)],
                 [tabuleiro[i][2 - i] for i in range(3)]]

    for linha in linhas + colunas + diagonais:
        if linha == ['X'] * 3:
            return 'X'
        elif linha == ['O'] * 3:
            return 'O'

    # Se todos as posições não estiverem vazias, o tabuleiro está cheio (Empate).
    if all(position != ' ' for linha in tabuleiro for position in linha):
        return 'Empate'

    return None

# Retorna as posições disponíveis no tabuleiro como tuplas (i, j)
def movimentos_possiveis(tabuleiro):
    # Checa se a posição está vazia, caso sim, a inclui na lista de retorno.
    return [(i, j) for i in range(3) for j in range(3) if tabuleiro[i][j] == ' ']

# Algoritmo Minimax com poda alpha-beta, essa função é chamada por melhor_jogada
def minimax(tabuleiro, maximizando, alpha, beta):
    # Checa vencedor, importante pois o algoritmo é recursivo
    resultado = checar_vencedor(tabuleiro)
    if resultado == 'X':
        return 1
    elif resultado == 'O':
        return -1
    elif resultado == 'Empate':
        return 0

    if maximizando:
        # Começamos com o pior valor possível para alpha (ele quer maximizar isso)
        valor_maximo = -math.inf
        # Percorre todas as jogadas possíveis
        for (i, j) in movimentos_possiveis(tabuleiro):
            # Simula a jogada
            tabuleiro[i][j] = 'X'
            # Chama recursivamente o minimax para o oponente (maximizando = False)
            valor = minimax(tabuleiro, False, alpha, beta)
            # Desfaz a simulação (backtracking)
            tabuleiro[i][j] = ' '
            valor_maximo = max(valor_maximo, valor)
            alpha = max(alpha, valor)
            # Esse ramo pode ser ignorado
            if beta <= alpha:
                break
        return valor_maximo
    else:
        # Começamos com o pior valor possível para beta (ele quer minimizar isso)
        valor_minimo = math.inf
        for (i, j) in movimentos_possiveis(tabuleiro):
            # Simula a jogada
            tabuleiro[i][j] = 'O'
            # Chama recursivamente o minimax para o oponente (maximizando = True)
            valor = minimax(tabuleiro, True, alpha, beta)
            # Desfaz a simulação (backtracking)
            tabuleiro[i][j] = ' '
            valor_minimo = min(valor_minimo, valor)
            beta = min(beta, valor)
            # Esse ramo pode ser ignorado
            if beta <= alpha:
                break
        return valor_minimo

# Retorna a melhor jogada da IA
def melhor_jogada(tabuleiro, ia):
    valor_maximo = -math.inf
    jogada = None
    for (i, j) in movimentos_possiveis(tabuleiro):
        tabuleiro[i][j] = ia
        valor = minimax(tabuleiro, ia == 'X', -math.inf, math.inf)
        tabuleiro[i][j] = ' '
        if valor > valor_maximo:
            valor_maximo = valor
            jogada = (i, j)
    return jogada

# Função para imprimir o tabuleiro
def mostrar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 10)

# Jogo interativo
def jogar():
    tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
    jogador = input("Você quer ser X ou O? ").upper()
    ia = 'O' if jogador == 'X' else 'X'

    turno = 'X'  # X sempre começa

    while True:
        # Estado atual do tabuleiro
        mostrar_tabuleiro(tabuleiro)

        # Teste de término
        vencedor = checar_vencedor(tabuleiro)
        if vencedor:
            if vencedor == 'Empate':
                print("Empate!")
            else:
                print(f"{vencedor} venceu!")
            break

        if turno == jogador:
            try:
                i, j = map(int, input("Sua jogada (linha e coluna, de 0 a 2): ").split())
                if tabuleiro[i][j] == ' ':
                    tabuleiro[i][j] = jogador
                    turno = ia
                else:
                    print("Posição ocupada. Tente novamente.")
            except:
                print("Entrada inválida. Digite dois números de 0 a 2.")
        else:
            print("IA está pensando...")
            i, j = melhor_jogada(tabuleiro, ia)
            tabuleiro[i][j] = ia
            turno = jogador

# Iniciar o jogo
if __name__ == "__main__":
    jogar()
