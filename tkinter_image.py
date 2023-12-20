from tkinter import *
from utils import *

root = Tk()

root.title('Imagens')
root.iconbitmap('imagem.ico')

#adicona o menu
menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)

filemenu.add_command(
    label='Open',
    command=lambda: open_folder(root)
)

filemenu.add_command(label='Save')
filemenu.add_command(label='Exit')

menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)

load_images(root)

# Botao para mostrar a proxima imagem
btnprev = Button(root, text='PREV', command=lambda: prev_image(root), bg='#175728', fg='#ffffff')
btnprev.grid(row=1, column= 0, sticky=E+W )

btnsair = Button(root, text='CLOSE',command=root.quit, bg='#b01919', fg='#ffffff')
btnsair.grid(row=1, column=1, sticky=E+W)

btnnext = Button(root, text='NEXT', command=lambda:next_image(root), bg='#175728', fg='#ffffff', )
btnnext.grid(row=1, column=2, sticky=E+W)

root.bind('<Right>', lambda event: next_image(root))
root.bind('<Left>', lambda event: prev_image(root))
root.bind('<Escape>', lambda event: root.quit())

root.mainloop()