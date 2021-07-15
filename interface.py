import tkinter


class Interface(tkinter.Frame):

    def __init__(self, window):
        tkinter.Frame.__init__(self, window)
        self.login()
        self.pack(expand=True)

    def login(self):
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

        remember = tkinter.Checkbutton(frame, text="Garder sa Session ouverte")
        remember.place(x=50, y=250)

        tkinter.Button(frame, text="S'Inscrire", font=('Courrier', 10),
                       width=10).place(x=30, y=350)

        tkinter.Button(frame, text="Se Connecter", font=('Courrier', 10),
                       width=10).place(x=300, y=350)


        frame.pack(expand=True)
