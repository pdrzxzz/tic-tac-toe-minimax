# 🎮 Tic-Tac-Toe with AI (Minimax Algorithm)

Um simples jogo da velha no terminal escrito em Python, onde um jogador humano compete contra uma IA.  

## 🧠 Sobre a IA

- ✅ IA imbatível usando Minimax com poda Alpha-Beta  
- 🎯 Prioriza vitórias rápidas e evita derrotas  
- ♻️ Lógica de backtracking para simular todas as possibilidades do jogo  


## 🎮 Como Jogar

Clone este repositório:

	git clone https://github.com/yourusername/tic-tac-toe-ai.git

Execute o jogo:

	python game.py

1. Escolha jogar como **X** ou **O**  
2. **X sempre joga primeiro**  
3. Informe suas jogadas com os índices da linha e coluna (de 0 a 2), por exemplo:

```
Your move (row and column, from 0 to 2): 0 1
```

## 🧾 Estrutura do Código

- play() – Inicia e gerencia o loop do jogo  
- minimax() – Algoritmo recursivo principal para decisões ideais  
- best_move() – Encontra a melhor jogada para a IA usando o Minimax  
- isGameOver() – Verifica vitória ou empate  
- possible_moves() – Retorna as jogadas disponíveis no tabuleiro  
- show_board() – Exibe o tabuleiro no console  

## 🛠 Requisitos

- Python 3.6 ou superior  
- Nenhuma biblioteca externa necessária  

---

## 📷 Exemplo de Saída

```
AI is thinking...
 X | O | O
-----------
   | O | X
-----------
 O | X | X
-----------
O wins!

```

## 📄 Licença

Este projeto é **open-source** e gratuito para uso.

Made by [pdrzxzz](https://github.com/pdrzxzz) | Computer Science Student 🎓

![MuaKissGIF (2)](https://github.com/user-attachments/assets/2bc84399-8890-47c4-bca9-74546d5d07a6)


