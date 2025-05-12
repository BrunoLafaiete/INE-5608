from tkinter import Canvas
from Peca import Peca
import Jogador as jogador

# 	Board matchStatus
# 1 - no match (initial state)
# 2 - finished match (game with winner - no tied game)
# 3 - your turn, match in progress AND NOT move occurring (waiting first action)
# 4 - your turn, match in progress AND move occurring (waiting second action)
# 5 - NOT your turn, match in progress - waiting move
# 6 - match abandoned by opponent


class Tabuleiro:
    def __init__(self, root, grid_size=5):
        self.jogador_local = jogador.Jogador()
        self.jogador_remoto = jogador.Jogador()
        self.jogador_local.inicializar(1, "Red player", "Red player")
        self.jogador_remoto.inicializar(2, "Blue player", "Blue player")
        self.status_partida = 1
        self.grid_size = grid_size
        self.board_margin = 50
        self.canvas_width = 500
        self.canvas_height = 500
        self.cell_size = (self.canvas_width - 2 * self.board_margin) / self.grid_size
        self.pieces = []
        self.status_partida = 1

        self.canvas = Canvas(root, width=self.canvas_width, height=self.canvas_height, bg="#333", highlightthickness=0)
        self.canvas.pack(padx=20, pady=20)

        self.draw_board() # preciso colocar isso no diagrama de sequencia como uma self message de Tabuleiro???
        self.canvas.bind("<Button-1>", self.on_click)

        self.current_symbol = "X"
        self.current_color = "#cc0000"

    def draw_board(self):
        board_size = self.canvas_width - (2 * self.board_margin)
        self.canvas.create_rectangle(
            self.board_margin, self.board_margin,
            self.board_margin + board_size, self.board_margin + board_size,
            fill="#663399", outline="white", width=2
        )

        for i in range(1, self.grid_size):
            self.canvas.create_line(
                self.board_margin, self.board_margin + i * self.cell_size,
                self.board_margin + board_size, self.board_margin + i * self.cell_size,
                fill="white", width=1
            )
            self.canvas.create_line(
                self.board_margin + i * self.cell_size, self.board_margin,
                self.board_margin + i * self.cell_size, self.board_margin + board_size,
                fill="white", width=1
            )

    def iniciar_partida(self, jogadores, local_id):
        playerA_name = jogadores[0][0]
        playerA_id = jogadores[0][1]
        playerA_order = jogadores[0][2]
        playerB_name = jogadores[1][0]
        playerB_id = jogadores[1][1]
        self.jogador_local.reset()
        self.jogador_remoto.reset()
        self.jogador_local.inicializar(1, playerA_id, playerA_name)
        self.jogador_remoto.inicializar(2, playerB_id, playerB_name)
        if playerA_order == "1":
            self.jogador_local.alternar_turno()
            self.status_partida = 3  #    waiting piece or origin selection (first action)
        else:
            self.jogador_remoto.alternar_turno()
            self.status_partida = 5  #    waiting remote action

    def add_piece(self, peca: Peca):
        self.pieces.append(peca)
        x, y = peca.x, peca.y

        self.canvas.create_oval(
            self.board_margin + x * self.cell_size + 5,
            self.board_margin + y * self.cell_size + 5,
            self.board_margin + (x + 1) * self.cell_size - 5,
            self.board_margin + (y + 1) * self.cell_size - 5,
            fill=peca.color, outline="black", width=1
        )

        self.canvas.create_text(
            self.board_margin + (x + 0.5) * self.cell_size,
            self.board_margin + (y + 0.5) * self.cell_size,
            text=peca.symbol, fill="white", font=("Arial", 16, "bold")
        )

    def on_click(self, event):
        x = int((event.x - self.board_margin) // self.cell_size)
        y = int((event.y - self.board_margin) // self.cell_size)

        if 0 <= x < self.grid_size and 0 <= y < self.grid_size:
            if not any(p.x == x and p.y == y for p in self.pieces):
                self.add_piece(Peca(x, y, self.current_color, self.current_symbol))
                self.toggle_player()

    def toggle_player(self):
        if self.current_symbol == "X":
            self.current_symbol = "O"
            self.current_color = "blue"
        else:
            self.current_symbol = "X"
            self.current_color = "#cc0000"

    def get_status_partida(self):
        return self.status_partida
    
    def atualizar_interface(self, status_jogo):
        pass

