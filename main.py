# importando tkinter
from tkinter import *
from tkinter import ttk

# importar calendario
from tkcalendar import Calendar, DateEntry


################# cores ###############
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # sky blue

lista_urgencia = ["Normal", "Urgência"]

# criando janela
janela = Tk()
janela.title("")
janela.geometry('1043x453')
janela.configure(background=co9)
# bloquear tamanho da janela
janela.resizable(width=False, height=False)

# dividindo a janela por freme
frame_superior = Frame(janela, width=310, height=50, bg=co2, relief='flat')
frame_superior.grid(row=0, column=0)

frame_inferior = Frame(janela, width=310, height=403, bg=co1, relief='flat')
frame_inferior.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

frame_esq = Frame(janela, width=588, height=403, bg=co1, relief='flat')
frame_esq.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)

# criando o 1 label

nome_app = Label(frame_superior, text="Formulário de Cadastro",
                 anchor=NW, font=("Ivy 13 bold"), bg=co2, fg=co1, relief='flat')
nome_app.place(x=10, y=20)

# configurando frame_inferior

#área de nome do paciente
label_nome = Label(frame_inferior, text="Nome *", anchor=NW,
                   font=("Ivy 10 bold"), bg=co1, fg=co4, relief='flat')
label_nome.place(x=10, y=10)

campo_nome = Entry(frame_inferior, width=45, justify="left", relief='solid')
campo_nome.place(x=15, y=40)


#área de e-mail
label_email = Label(frame_inferior, text="e-mail *", anchor=NW,
                    font=("Ivy 10 bold"), bg=co1, fg=co4, relief='flat')
label_email.place(x=10, y=70)

campo_email = Entry(frame_inferior, width=45, justify="left", relief='solid')
campo_email.place(x=15, y=100)


#área de telefone
label_telefone = Label(frame_inferior, text="Telefone *", anchor=NW,
                       font=("Ivy 10 bold"), bg=co1, fg=co4, relief='flat')
label_telefone.place(x=10, y=130)

campo_telefone = Entry(frame_inferior, width=45,
                       justify="left", relief='solid')
campo_telefone.place(x=15, y=160)


#área de data da consulta
label_data_consulta = Label(frame_inferior, text="Data da Consulta *",
                            anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4, relief='flat')
label_data_consulta.place(x=10, y=190)

campo_data_consulta = DateEntry(
    frame_inferior, width=12, bg="blue", fg="white", borderwidth=2, year=2023)
campo_data_consulta.place(x=15, y=220)


#área de classificação de urgência
label_grau_urgencia = Label(frame_inferior, text="Grau de Urgência *",
                            anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4, relief='flat')
label_grau_urgencia.place(x=165, y=190)

#incluir uma lista suspensa para evitar erros
campo_grau_urgencia = ttk.Combobox(frame_inferior, values=lista_urgencia, width=15)
campo_grau_urgencia.place(x=170, y=220)


#área de observação
label_obs = Label(frame_inferior, text="Observação *", anchor=NW,
                       font=("Ivy 10 bold"), bg=co1, fg=co4, relief='flat')
label_obs.place(x=10, y=250)

campo_obs = Entry(frame_inferior, width=45,
                       justify="left", relief='solid')
campo_obs.place(x=15, y=280)


janela.mainloop()
