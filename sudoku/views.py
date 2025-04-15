from django.shortcuts import render
from .solver import solve  # importa o algoritmo de resolução
import copy

def index(request):
    board = [[0]*9 for _ in range(9)]
    fixed_cells = []

    if request.method == "POST":
        # Monta a matriz 9x9 com os valores do formulário e marca células fixas
        for i in range(9):
            for j in range(9):
                val = request.POST.get(f'cell_{i}_{j}')
                if val and val.isdigit():
                    num = int(val)
                    if 1 <= num <= 9:
                        board[i][j] = num
                        fixed_cells.append(f"{i},{j}")
                    else:
                        board[i][j] = 0  # ignora valores fora de 1-9
                else:
                    board[i][j] = 0

        # Copia o tabuleiro para resolver
        solved_board = copy.deepcopy(board)
        solve(solved_board)

        return render(request, 'sudoku/index.html', {
            'board': solved_board,
            'range_9': range(9),
            'fixed_cells': fixed_cells
        })

    # Se for GET, renderiza o tabuleiro vazio
    return render(request, 'sudoku/index.html', {
        'board': board,
        'range_9': range(9),
        'fixed_cells': []
    })
