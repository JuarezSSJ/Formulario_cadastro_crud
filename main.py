# importando tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
# importar calendario
from tkcalendar import Calendar, DateEntry

#importando VIEW
from view import *


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

frame_dir = Frame(janela, width=588, height=403, bg=co1, relief='flat')
frame_dir.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)

# criando o 1 label

nome_app = Label(frame_superior, text="Formulário de Cadastro",
                  font=("Ivy 13 bold"), bg=co2, fg=co1, relief='flat', wraplength=310)
nome_app.place(x=10, y=20)


#função inserir / cadastrar

def cadastrar():
    nome = campo_nome.get()
    email = campo_email.get()
    telefone = campo_telefone.get()
    data = campo_data_consulta.get()
    situacao = campo_grau_urgencia.get()
    obs = campo_obs.get()
    
    lista_cadastro = [nome, email, telefone, data, situacao, obs]

    if nome == '':
        messagebox.showerror('Erro', 'O nome não pode está vazio')
    else:
        cadastrar_info(lista_cadastro)
        messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')
        #ira limpa os entry da posição 0 até o final de cada
        campo_nome.delete(0, 'end')
        campo_email.delete(0, 'end')
        campo_telefone.delete(0, 'end')
        campo_data_consulta.delete(0, 'end')
        campo_grau_urgencia.delete(0, 'end')
        campo_obs.delete(0, 'end')

    for campos in frame_dir.winfo_children():
        campos.destroy()
    
    apresentar()
    

# configurando frame_inferior

# área de nome do paciente
label_nome = Label(frame_inferior, text="Nome *", anchor=NW,
                   font=("Ivy 10 bold"), bg=co1, fg=co4, relief='flat')
label_nome.place(x=10, y=10)

campo_nome = Entry(frame_inferior, width=45, justify="left", relief='solid')
campo_nome.place(x=15, y=40)


# área de e-mail
label_email = Label(frame_inferior, text="e-mail *", anchor=NW,
                    font=("Ivy 10 bold"), bg=co1, fg=co4, relief='flat')
label_email.place(x=10, y=70)

campo_email = Entry(frame_inferior, width=45, justify="left", relief='solid')
campo_email.place(x=15, y=100)


# área de telefone
label_telefone = Label(frame_inferior, text="Telefone *", anchor=NW,
                       font=("Ivy 10 bold"), bg=co1, fg=co4, relief='flat')
label_telefone.place(x=10, y=130)

campo_telefone = Entry(frame_inferior, width=45,
                       justify="left", relief='solid')
campo_telefone.place(x=15, y=160)


# área de data da consulta
label_data_consulta = Label(frame_inferior, text="Data da Consulta *",
                            anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4, relief='flat')
label_data_consulta.place(x=10, y=190)

campo_data_consulta = DateEntry(
    frame_inferior, width=12, bg="blue", fg="white", borderwidth=2, year=2023)
campo_data_consulta.place(x=15, y=220)


# área de classificação de urgência
label_grau_urgencia = Label(frame_inferior, text="Grau de Urgência *",
                            anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4, relief='flat')
label_grau_urgencia.place(x=165, y=190)

# incluir uma lista suspensa para evitar erros
campo_grau_urgencia = ttk.Combobox(
    frame_inferior, values=lista_urgencia, width=15)
campo_grau_urgencia.place(x=170, y=220)


# área de observação
label_obs = Label(frame_inferior, text="Observação *", anchor=NW,
                  font=("Ivy 10 bold"), bg=co1, fg=co4, relief='flat')
label_obs.place(x=10, y=250)

campo_obs = Entry(frame_inferior, width=45,
                  justify="left", relief='solid')
campo_obs.place(x=15, y=280)


#cadastro dos botões

#botão Cadastrar
botao_cadastrar = Button (text="Cadastrar", command=cadastrar, borderwidth=2, relief="raised", overrelief="ridge", width=10, bg=co2, fg=co1)
botao_cadastrar.place(x=20, y=370)

#botão Editar
botao_cadastrar = Button (text="Editar", borderwidth=2, relief="raised", overrelief="ridge", width=10, bg=co6, fg=co1)
botao_cadastrar.place(x=110, y=370)

#botão Deletar
botao_cadastrar = Button (text="Deletar", borderwidth=2, relief="raised", overrelief="ridge", width=10, bg=co7, fg=co1)
botao_cadastrar.place(x=200, y=370)

#construindo a função para apresentar a tabela

def apresentar():

    # codigo para tabela
    lista = apresentar_info()

    # lista para cabecario
    tabela_head = ['ID','Nome',  'e-mail','Telefone', 'Data', 'Situação','Observação']


    # criando a tabela
    tree = ttk.Treeview(frame_dir, selectmode="extended", columns=tabela_head, show="headings")

    # rolagem vertical - tem de ser colocar dentro do mesmo freme para funcionar ex.: frame_dir o mesmo que está a tabela tree
    rolagem_lateral = ttk.Scrollbar(frame_dir, orient="vertical", command=tree.yview)

    # rolagem horizontal - tem de ser colocar dentro do mesmo freme para funcionar ex.: frame_dir o mesmo que está a tabela tree
    rolagem_inferior = ttk.Scrollbar( frame_dir, orient="horizontal", command=tree.xview)

    #aplicação da rolagem
    tree.configure(yscrollcommand=rolagem_lateral.set, xscrollcommand=rolagem_inferior.set)


    tree.grid(column=0, row=0, sticky='nsew')
    rolagem_lateral.grid(column=1, row=0, sticky='ns')
    rolagem_inferior.grid(column=0, row=1, sticky='ew')

    frame_dir.grid_rowconfigure(0, weight=12)


    hd=["nw","nw","nw","center","center","center","center"]
    h=[30,170,140,100,90,60,120]
    n=0

    #criei um laço de repetição para realizar toda a configuração da tabela
    for coluna in tabela_head:
        tree.heading(coluna, text=coluna.title(), anchor=CENTER)
        #ajusta a largura da coluna pelo tamanho do cabeçalho
        tree.column(coluna, width=h[n],anchor=hd[n])
        
        n+=1

    for item in lista:
        tree.insert('', 'end', values=item)
        #end - sig que os valores serão inseridos no final de uma tabela
        #values - é o que o for está percorrendo, e com o insert será inserido no final da lista
        #insert serve para inserir os itens em uma tabela Treeview

#chamando a função apresentar
apresentar()



janela.mainloop()
