import tkinter as tk
from tkinter import FALSE, Menu, messagebox, simpledialog
from tkinter.messagebox import showinfo
from Tabuleiro import Tabuleiro
from dog.dog_actor import DogActor
from dog.dog_interface import DogPlayerInterface

class InterfaceJogador(DogPlayerInterface):
    def __init__(self):
        self.tk = tk.Tk()
        self.menubar = Menu(self.tk)
        self.arquivo = Menu(self.menubar, tearoff=0)
        self.arquivo.add_command(label='Iniciar jogo', command=self.iniciar_partida)
        self.arquivo.add_command(label='Restaurar estado inicial', command=self.start_game)
        self.menubar.add_cascade(label='Arquivo', menu=self.arquivo)
        self.tk.config(menu=self.menubar) 
        self.tabuleiro = Tabuleiro(self.tk)
        nome_jogador = simpledialog.askstring("Nome do Jogador", "Digite seu nome:")
        self.dog_server_interface = DogActor()
        mensagem = self.dog_server_interface.initialize(nome_jogador, self)
        messagebox.showinfo(message=mensagem)
    
    def iniciar_partida(self):
        start_status = self.dog_server_interface.start_match(2)
        menssagem = start_status.get_message()
        messagebox.showinfo(message=menssagem)
        '''status_partida = self.tabuleiro.get_status_partida()
        if status_partida == 1:
            resposta = messagebox.askyesno("START", "Deseja iniciar uma nova partida?")
            if resposta:
                start_status = self.dog_server_interface.start_match(2)
                codigo = start_status.get_code()
                menssagem = start_status.get_message()
                if codigo == "0" or codigo == "1":
                    messagebox.showinfo(message=menssagem)
                else:  #    (code=='2')
                    jogadores = start_status.get_players()
                    jogadore_local_id = start_status.get_local_id()
                    self.tabuleiro.iniciar_partida(jogadores, jogadore_local_id)
                    game_state = self.tabuleiro.get_status()
                    self.update_gui(game_state)
                    messagebox.showinfo(message=start_status.get_message())'''
    
    def receber_inicio(self, start_status):
        message = start_status.get_message()
        messagebox.showinfo(message=message)

    def start_game(self):
        print("Iniciando jogo...")
 

    def __show_popup_message(self, msg: str) -> None:
        showinfo("Oxono", f"MENSAGEM: {msg}")

    def executar(self):
        self.tk.title("Oxono multiplayer")
        self.tk.configure(bg="#333")
        self.tk.mainloop()