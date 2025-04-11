from tkinter import Canvas
from Peca import Peca


class Tabuleiro:
    def __init__(self, root, grid_size=5):
        self.grid_size = grid_size
        self.board_margin = 50
        self.canvas_width = 500
        self.canvas_height = 500
        self.cell_size = (self.canvas_width - 2 * self.board_margin) / self.grid_size
        self.pieces = []

        self.canvas = Canvas(root, width=self.canvas_width, height=self.canvas_height, bg="#333", highlightthickness=0)
        self.canvas.pack(padx=20, pady=20)

        self.draw_board()
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

