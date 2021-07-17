import tkinter

from interface import Interface

window = tkinter.Tk()
window.title('Chateur')
window.iconbitmap('icon.ico')
window.config(bg='#b0b2d3')

screen_x = int(window.winfo_screenwidth())
screen_y = int(window.winfo_screenheight())
window_x = 900
window_y = 600

posX = (screen_x // 2) - (window_x // 2)
posY = (screen_y // 2) - (window_y // 2)

geo = f"{window_x}x{window_y}+{posX}+{posY}"

window.geometry(geo)

interface = Interface(window)

window.mainloop()

interface.database.close()
