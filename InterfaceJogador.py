import tkinter as tk
from tkinter import messagebox
from tkinter.messagebox import showinfo
from Tabuleiro import Tabuleiro
from dog.dog_actor import DogActor
from dog.dog_interface import DogPlayerInterface

class InterfaceJogador(DogPlayerInterface):
    
    def __init__(self):
        self.tk = tk.Tk()
        self.tabuleiro = Tabuleiro(self.tk)
        self.dog_server_interface = DogActor()
        message = self.dog_server_interface.initialize("Tiago", self)
        messagebox.showinfo(message=message)
    
    def iniciar_partida(self):
        start_status = self.__dog_server_interface.start_match(2)
        message = start_status.get_message()
        messagebox.showinfo(message=message)
    
    def receber_inicio(self):
        self.__show_popup_message("Recebe início")

    def receive_start(self) -> None:
        pass  

    def __show_popup_message(self, msg: str) -> None:
        showinfo("Oxono", f"MENSAGEM: {msg}")

    def executar(self):
        self.tk.title("Oxono multiplayer")
        self.tk.configure(bg="#333")
        self.tk.mainloop()