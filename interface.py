import mysql.connector

import tkinter as tk
import tkinter.font as tkFont
from tkinter import PhotoImage
from tkinter import ttk
from mainsql import *
import mainsql

# Passo 1: Em criar a canvas/janela "a tela de trabalho"

colors = "#edf6f9", "#025930", "#D91A2A", "#2E2C70", "#FFFFFF"
# 0 = cinza, 1 = verde , 2 = vermelho, 3 roxo, 4 branco

formulario = tk.Tk()
formulario.geometry("700x500") #valor_widthvalor_height
formulario.resizable(width = False,height= False)
formulario.title("Sistema de Cadastro de Pacientes - RHP")
formulario.iconbitmap("logo_app.ico")
formulario.config(bg=colors[1])
roboto15 = tkFont.Font(family="Roboto", size=15)
roboto13 = tkFont.Font(family="Roboto", size=13, weight="bold")
roboto12 = tkFont.Font(family="Roboto", size=10)
roboto8 = tkFont.Font(family="Roboto", size=10, weight="bold")
roboto8n = tkFont.Font(family="Roboto", size=10, )

# Passo 2: Colocar os elementos gráficos
# Nome Completo, Idade, Gênero, Morada, Número do Cartão do Cidadão
# Número de Contribuinte, Email, Telemóvel

quadro = tk.Frame(formulario, padx=10, pady= 20)
quadro.grid(row=0, column=0, columnspan = 2)
quadro.config(bg=colors[4])
quadro.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

imagem1= PhotoImage(file="logo2.png")
imagem1 = imagem1.subsample(6,6)
label_logo = tk.Label(quadro, image=imagem1,background=colors[4])
label_logo.grid(row=0, column = 0)

txt=tk.Label(quadro, text="Cadastro de Pacientes \n RHP Real Hostipal Português", background=colors[4], foreground=colors[2], font= roboto15)
txt.place(x=10, y=10, width=100, height=20,)
txt.grid(row=0, column=1)

#Nome Completo
lbl_nome = tk.Label(quadro, text= "Nome Completo: ", background=colors[4], foreground=colors[3], font = roboto8)
lbl_nome.grid(row=1, column=0)
ent_nome = tk.Entry(quadro, width="60", font = roboto8n, background=colors[0])
ent_nome.grid(row=1,column=1)

#Idade
age = tk.StringVar()
age.set("Selecione")
lbl_idade = tk.Label(quadro, text= "Idade: ", background=colors[4],font = roboto8, foreground=colors[3])
lbl_idade.grid(row=2, column=0)

ent_idade = tk.OptionMenu(quadro, age, *[str(i) for i in range(0,123)])
ent_idade.grid(row=2, column=1)
ent_idade.config(width=63, bg=colors[0])


""" lbl_idade = tk.Label(quadro, text= "Idade: ", background=colors[4],font = roboto8, foreground=colors[3])
lbl_idade.grid(row=2, column=0)
ent_idade = tk.Entry(quadro, width="70", background=colors[0])
ent_idade.grid(row=2,column=1) """

#Gênero
lbl_genero = tk.Label(quadro, text= "Gênero: ", font = roboto8, background=colors[4], foreground=colors[3])
lbl_genero.grid(row=3, column=0)
options = ["Masculino", "Feminino", "Prefiro não declarar"]
sex = tk.StringVar(quadro)
sex.set("Selecione")

ent_genero = tk.OptionMenu(quadro, sex, *options)
ent_genero.config(width=63, bg=colors[0])
ent_genero.grid(row=3, column=1)

#Morada
lbl_morada = tk.Label(quadro, text= "Morada: ", font = roboto8, background=colors[4], foreground=colors[3])
lbl_morada.grid(row=4, column=0)
ent_morada = tk.Entry(quadro, width="60", font = roboto8n, background=colors[0])
ent_morada.grid(row=4,column=1)

#Número de identidade
lbl_identidade = tk.Label(quadro, text= "NIF: ", font = roboto8, background=colors[4], foreground=colors[3])
lbl_identidade.grid(row=5, column=0)
ent_identidade = tk.Entry(quadro, width="60", font = roboto8n, background=colors[0])
ent_identidade.grid(row=5,column=1)

#Email
lbl_email = tk.Label(quadro, text= "Email: ", font = roboto8, background=colors[4], foreground=colors[3])
lbl_email.grid(row=6, column=0)
ent_email = tk.Entry(quadro, width="60", font = roboto8n, background=colors[0])
ent_email.grid(row=6,column=1)

#Telemóvel
lbl_telefone = tk.Label(quadro, text= "Telemóvel: ", font = roboto8, background=colors[4], foreground=colors[3])
lbl_telefone.grid(row=7, column=0)
ent_telefone = tk.Entry(quadro, width="60", font = roboto8n, background=colors[0])
ent_telefone.grid(row=7,column=1)


'''def submit_callback():
    # Armazenando as informações dos campos de entrada em variáveis
    nome = ent_nome.get()
    idade = age.get()
    # genero = sex.get()
    # morada = ent_morada.get()
    # identidade = ent_identidade.get()
    # email = ent_email.get()
    # telefone = ent_telefone.get()
    
'''

    

submit_button = tk.Button(formulario, text="Submeter",font = roboto13, background=colors[4], foreground=colors[3])
submit_button.grid(row=8, column=1)
submit_button.place(x=350, y=450, anchor="center")
submit_button.config(bg=colors[0])

# Passo 3: Execução em loop
formulario.mainloop()
#