import tkinter as tk
from tkinter import ttk
from random import randint
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


def jokenpo():
    app = tk.Tk()
    app.title('Jokenpô')
    app.geometry('280x200+300+300')
    app.resizable(width=False, height=False)
    style = ttk.Style('solar')

    """Sistema para gerar as três palavras de forma randomica"""
    sistema_alea = ['Pedra', 'Papel', 'Tesoura'][randint(0, 2)]

    """Labels/Textos"""
    label = ttk.Label(app, text='JOKENPÔ', font='Arial 12',
                      width=10, bootstyle='warning', anchor=tk.CENTER)
    label_2 = ttk.Label(app, text='Você:', font='Arial 12',
                        bootstyle='success', width=10, anchor=tk.CENTER)
    label_3 = ttk.Label(app, text='Sistema:', font='Arial 12',
                        bootstyle='info', width=10, anchor=tk.CENTER)
    label_4 = ttk.Label(app, text=' ', font='Arial 12',
                        foreground='#FFFFFF', width=10)
    label_v = ttk.Label(app, text='', font='Arial 12',
                        bootstyle='success', width=10, anchor=tk.CENTER)
    label_s = ttk.Label(app, text='', font='Arial 12',
                        bootstyle='info', width=10, anchor=tk.CENTER)
    label_r = ttk.Label(app, text="", font='Arial 12',
                        foreground='#FFFFFF', width=10, anchor=tk.CENTER)
    label_espaco = ttk.Label(app, text='')
    label_espaco_02 = ttk.Label(app, text='')

    """Labels/Textos Grid"""
    label.grid(row=0, column=1)
    label_2.grid(row=4, column=0)
    label_3.grid(row=4, column=1)
    label_4.grid(row=3, column=1)
    label_v.grid(row=5, column=0)
    label_s.grid(row=5, column=1)
    label_r.grid(row=5, column=2)
    label_espaco.grid(row=6, column=0)
    label_espaco_02.grid(row=1, column=0)

    """Definições"""

    def texto_pedra():
        label_v['text'] = 'Pedra'
        label_s['text'] = sistema_alea
        if sistema_alea == 'Pedra':
            label_r['text'] = 'Empate!'
        elif sistema_alea == 'Papel':
            label_r['text'] = 'Perdeu!'
        elif sistema_alea == 'Tesoura':
            label_r['text'] = 'Ganhou!'

    def texto_papel():
        label_v['text'] = 'Papel'
        label_s['text'] = sistema_alea
        if sistema_alea == 'Papel':
            label_r['text'] = 'Empate!'
        elif sistema_alea == 'Tesoura':
            label_r['text'] = 'Perdeu!'
        elif sistema_alea == 'Pedra':
            label_r['text'] = 'Ganhou!'

    def texto_tesoura():
        label_v['text'] = 'Tesoura'
        label_s['text'] = sistema_alea
        if sistema_alea == 'Tesoura':
            label_r['text'] = 'Empate!'
        elif sistema_alea == 'Pedra':
            label_r['text'] = 'Perdeu!'
        elif sistema_alea == 'Papel':
            label_r['text'] = 'Ganhou!'

    def finalizar():
        exit()

    def reinicio():
        jokenpo()

    """Botões"""
    cmd = ttk.Button(app, text='Pedra', bootstyle='dark', command=lambda: texto_pedra())
    cmd_2 = ttk.Button(app, text='Papel', bootstyle='info', command=lambda: texto_papel())
    cmd_3 = ttk.Button(app, text='Tesoura', bootstyle='secondary', command=lambda: texto_tesoura())
    cmd_4 = ttk.Button(app, text='Finalizar', bootstyle='warning-outline', command=lambda: finalizar())
    cmd_5 = ttk.Button(app, text='Jogar', bootstyle='warning-outline', command=lambda: reinicio())

    """Botões Grid"""
    cmd.grid(row=2, column=0)
    cmd_2.grid(row=2, column=1)
    cmd_3.grid(row=2, column=2)
    cmd_4.grid(row=7, column=2)
    cmd_5.grid(row=7, column=0)

    app.mainloop()


if __name__ == "__main__":
    jokenpo()