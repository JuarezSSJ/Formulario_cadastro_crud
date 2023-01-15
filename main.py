# importando tkinter
from tkinter import *

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

frame_superior = Frame(janela, width=310, height=403, bg=co1, relief='flat')
frame_superior.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

frame_esq = Frame(janela, width=588, height=403, bg=co1, relief='flat')
frame_esq.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)


janela.mainloop()
