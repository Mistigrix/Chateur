from functools import partial
import tkinter
from database import DataBase
from functions import *

class Interface(tkinter.Frame):

    def __init__(self, window):
        tkinter.Frame.__init__(self, window)

        self.user = get_user()
        self.database = DataBase('database.db')
        self.pack(expand=True)

        if not self.user.connect:
            self.login()
        else:
            self.home()

    def clean(self):
        """Methode permettant de nettoyer la fenetre en supprimant tout les widget de celle ci"""

        for c in self.winfo_children():
            c.destroy()

    def home(self):
        """Interface d'acceuil uniquement accessible aux utilisateurs connectés"""

        # nettoyer la fenetre
        self.clean()

        frame = tkinter.Frame(self, bg='#f3f3f6', width=700, height=450, borderwidth=1)

        tkinter.Label(frame, text=f"Bienvenue sur Chateur {self.user.username}", bg='#f3f3f6', font=('Courriel', 20)).place(x=200, y=200)

        frame.pack()

    def login(self):

        self.clean()

        frame = tkinter.Frame(self, bg='#f3f3f6', width=400, height=450, borderwidth=1)

        tkinter.Label(frame, text="Connectez Vous à votre compte Chateur", bg='#f3f3f6',
                      font=('Helvetica', 15)).place(x=20, y=20)

        # afficher le label et l'entrer du nom de l'user
        tkinter.Label(frame, text='Username: ', bg='#f3f3f6',
                      font=('Courrier', 10)).place(x=20, y=100)
        entry_username = tkinter.Entry(frame, width=35, font=('Courrier', 10))
        entry_username.place(x=100, y=100)

        # afficher le label et l'entrer du password de l'user
        tkinter.Label(frame, text='Password: ', bg='#f3f3f6',
                      font=('Courrier', 10)).place(x=20, y=200)
        entry_password = tkinter.Entry(frame, width=35, font=('Courrier', 10))
        entry_password.place(x=100, y=200)

        self.var_case = tkinter.BooleanVar()
        remember = tkinter.Checkbutton(frame, text="Garder sa Session ouverte", variable=self.var_case)
        remember.place(x=50, y=250)

        tkinter.Button(frame, text="S'Inscrire", font=('Courrier', 10),
                       width=10, command=self.register).place(x=30, y=350)

        tkinter.Button(frame, text="Se Connecter", font=('Courrier', 10),
                       width=10, command=partial(self.__get_data, entry_username, entry_password)).place(x=300, y=350)

        frame.pack()

    def register(self):

        self.clean()

        frame = tkinter.Frame(self, bg='#f3f3f6', width=400, height=450, borderwidth=1)

        tkinter.Label(frame, text="Creer un nouveau compte Chateur", bg='#f3f3f6',
                      font=('Helvetica', 15)).place(x=20, y=20)

        # afficher le label et l'entrer du nom de l'user
        tkinter.Label(frame, text='Username: ', bg='#f3f3f6',
                      font=('Courrier', 10)).place(x=20, y=100)
        entry_username = tkinter.Entry(frame, width=35, font=('Courrier', 10))
        entry_username.place(x=100, y=100)

        # afficher le label et l'entrer du password de l'user
        tkinter.Label(frame, text='Password: ', bg='#f3f3f6',
                      font=('Courrier', 10)).place(x=20, y=150)
        entry_password = tkinter.Entry(frame, width=35, font=('Courrier', 10))
        entry_password.place(x=100, y=150)

        # afficher le label et l'entrer pour la confirmation du password de l'user
        tkinter.Label(frame, text='Confirm: ', bg='#f3f3f6',
                      font=('Courrier', 10)).place(x=20, y=200)
        entry_confirm = tkinter.Entry(frame, width=35, font=('Courrier', 10))
        entry_confirm.place(x=100, y=200)

        self.var_case = tkinter.BooleanVar()
        remember = tkinter.Checkbutton(frame, text="Garder sa Session ouverte", variable=self.var_case)
        remember.place(x=50, y=250)

        tkinter.Button(frame, text="Se connecter", font=('Courrier', 10),
                       width=10, command=self.login).place(x=30, y=350)

        tkinter.Button(frame, text="S'Inscrire", font=('Courrier', 10),
                       width=10, command=partial(self.__get_data, entry_username, entry_password, entry_confirm)).place(x=300, y=350)

        frame.pack()

    def __get_data(self, entry_username, entry_password, entry_confirm=None):
        username = entry_username.get()
        password = entry_password.get()

        if entry_confirm:
            confirm = entry_confirm.get()
            if password == confirm:
                self.user = self.database.create_user(username, password)
                self.user.connect = True
                # verifier si l'utilisateur souhaite enregistrer ses données
                if self.var_case.get():
                    set_user(self.user)
                self.home()
        else:
            # verifier le client est un membre
            if self.database.check_member(username, password):
                # redirection vers la page d'acceuil
                self.user = self.database.check_member(username, password)
                self.user.connect = True
                # verifier si l'utilisateur souhaite enregistrer ses données
                if self.var_case.get():
                    set_user(self.user)
                self.home()
            else:
                print("Le client n'existe pas")
