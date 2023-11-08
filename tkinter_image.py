from tkinter import *
from PIL import ImageTk, Image

root = Tk()


img = Image.open('gato.jpg')
img_tk = ImageTk.PhotoImage(img)


img_label = Label(root, image=img_tk)

img_label.pack()

root.mainloop()