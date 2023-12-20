from tkinter import *
from PIL import ImageTk, Image, ImageOps
import os 
from tkinter import messagebox
from tkinter import filedialog

#Variavel para guardar as imagens
imagens= []

#variável de controle da imagem atual
imagem_atual = 0

#variavel para arrumar o label da imagm
img_label = None

#variavel para armazenar o caminho para a pasta de imagens
img_folder = ""

# Função para carregar as imagens
def load_images(root):
    global img_folder
    global imagens
    global img_label
    # Se existe uma pasta de imagens
    if img_folder:
        # Limpa a lista de imagens
        imagens.clear()
        # Lista os arquivos da pasta imagens
        arquivos = os.listdir(img_folder)
        # Percorre a lista de arquivos
        for arquivo in arquivos:
            try:
                # Abre a imagem
                img = Image.open(os.path.join(img_folder, arquivo))

            except Exception as e:
                pass 
            else:
                # Redimensiona a imagem
                img = ImageOps.contain(img, (500, 500))
                # Adiciona a imagem na lista
                imagens.append(ImageTk.PhotoImage(img))
    # Se não existe uma pasta de imagem
    else:
       #cria uma imagem em branco
       img = Image.new("RGB", (500,500),)
       # Adiciona a imagem na lista
       imagens.append(ImageTk.PhotoImage(img))

    # Carrega a primeira imagem no Label
    img_label = Label(root, image=imagens[0])
    # Exibe a imagem
    img_label.grid(row=0, column=0, columnspan=3)

#função para abrir a pasta de imagens
def open_folder(root):
    folder_path = filedialog.askdirectory()
    
    if  folder_path:
        load_images(root)
        global img_folder
        img_folder = folder_path
        messagebox.showinfo(
            title='Abrindo diretório...',
            message=f'O diretório selecionado foi: {folder_path}'
        )
    else:
        messagebox.showerror(
            title='Abrindo diretório...',
            message='Nenhum diretório foi selecionado'
        ) 

def prev_image(root):
    global imagem_atual
    global img_label
    global imagens

    #verifica se é a primeira imagem, se sim volta para a úttima
    if imagem_atual == 0:
        imagem_atual= len(imagens) - 1
    else:
        imagem_atual -= 1

    #apaga a imagem atual
    img_label.grid_forget()

    #Exibe a nova imagem
    img_label = Label(root, image=imagens [imagem_atual])
    img_label.grid( column=0, row=0, columnspan=3)

def next_image(root):
    global imagem_atual
    global img_label
    global imagens

    #verifica se é a primeira imagem, se sim volta para a úttima
    if imagem_atual == len(imagens) - 1:
        imagem_atual =0
        
    else:
        imagem_atual += 1

    #apaga a imagem atual
    img_label.grid_forget()

    #Exibe a nova imagem
    img_label = Label(root, image=imagens [imagem_atual])
    img_label.grid( column=0, row=0, columnspan=3)
