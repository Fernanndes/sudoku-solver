# 🧩 Sudoku Solver Web

Este é um aplicativo web para resolver tabuleiros de Sudoku.  
Desenvolvido com **Python**, **Django** e **HTML/CSS**, este projeto recebe um tabuleiro do usuário e aplica um algoritmo de backtracking para encontrar a solução.

## 🔧 Funcionalidades

- ✅ Interface intuitiva para preenchimento do tabuleiro
- ✅ Algoritmo de backtracking em Python
- ✅ Células fixas destacadas visualmente
- ✅ Validação de entrada (1 a 9)
- ✅ Layout responsivo básico

## 🚀 Como rodar localmente

```bash
# Clone o repositório
git clone https://github.com/seunome/sudoku-solver.git
cd sudoku-solver

# Crie e ative o ambiente virtual
python -m venv .venv
source .venv/bin/activate  # ou .venv\Scripts\activate no Windows

# Instale as dependências
pip install -r requirements.txt

# Execute o servidor
python manage.py runserver
