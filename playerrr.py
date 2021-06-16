import tkinter
from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
from PIL import *
import os, sys
import fnmatch
import simpleaudio as sa
import wave

#tamanho e titulo da area do player
raiz = Tk()
raiz.title('WAVE PLAYER')
raiz.geometry("800x600")
raiz.iconbitmap('D:/mone-/Área de Trabalho/monise/cursos/python/scripts/botoes/icon.ico')


# caixa da playlist
master_frame = Frame(raiz)
master_frame.pack(pady=40)

caixa_playlist = Listbox(master_frame, bg="#cf734f", fg="white", height= 20, width=80, selectbackground="white", selectforeground="green")
caixa_playlist.grid(row=0, column=0)

#função para abrir o explorador de arquivo
def add_song():
    song = filedialog.askopenfilename(initialdir='Downloads/', title="Escolha uma musica", filetypes=(("wav files", "*.wav"), ))
    caixa_playlist.insert(END, song)
    return song

def add_music():
    variosarq = filedialog.askopenfilenames(initialdir='Downloads/', title="Escolha uma musica", filetypes=(("wav files", "*.wav"), ))
    caixa_playlist.insert(END, variosarq)
    return song

# Create Menu
my_menu = Menu(raiz)
raiz.config(menu=my_menu)

# adicionar musicas
addmusica_menu = Menu(my_menu)
my_menu.add_cascade(label="Adicionar", menu=addmusica_menu)

addmusica_menu.add_command(label="Uma Música", command=add_song)
addmusica_menu.add_command(label="Varias Músicas", command=add_music)


def Sobre():
    tkinter.messagebox.showinfo('Sobre o APP', 'Player criado por alunos da UFBA')

Ajuda = Menu(my_menu)
my_menu.add_cascade(label="Ajuda", menu=Ajuda)
Ajuda.add_command(label="Sobre", command=Sobre)
Ajuda.add_command(label="Sair", command=raiz.destroy)

def conversao():
    signal, samplerate = sf.read(add_song)
    audiodata = audiodata.astype(float)
    d= audiodata.sum(axis=1) / 2


#def grafic():
#    signal, samplerate = sf.read(add_song)
#    time = np.arange(0, len(signal) * 1/samplerate, 1/samplerate)

#    plt.plot(time, signal)
#    plt.xlabel('Time (s)')
#    plt.ylabel('Amplitude (V)')
#    plt.show()


grafico = Menu(my_menu)
my_menu.add_cascade(label="Gráfico", menu=grafico)
grafico.add_command(label="Mostrar Gráfico")

def play():
    wave_read = wave.open(add_song, 'rb')
    wave_obj = sa.WaveObject.from_wave_read(wave_read)
    wave_obj = sa.WaveObject.from_wave_file(wave_obj)
    play_obj = wave_obj.play()

def parar():
    play_obj.stop()


# botes de controle
Rightframe = Frame(raiz)
Rightframe.pack(pady=1)

middleframe = Frame(Rightframe)
middleframe.pack(pady=5, padx=5)

parar_img = PhotoImage(file='botoes/parar.png')
pararBt = Button(middleframe, image=parar_img, borderwidth=0, command=parar)
pararBt.grid(row=10, column=0, padx=5)

pause_img = PhotoImage(file='botoes/pause.png')
pauseBt = Button(middleframe, image=pause_img, borderwidth=0)
pauseBt.grid(row=10, column=1, padx=5)

play_img = PhotoImage(file='botoes/play.png')
playBt = Button(middleframe, image=play_img, borderwidth=0, command=play)
playBt.grid(row=10, column=2, padx=5)

volume_img = PhotoImage(file='botoes/volume_max.png')
volumeBt = Button(middleframe, image=volume_img, borderwidth=0)
volumeBt.grid(row=10, column=3)

mudo_img = PhotoImage(file='botoes/mudo.png')
mudoBt = Button(middleframe, image=mudo_img, borderwidth=0)
mudoBt.grid(row=10, column=4, padx=5)

raiz.mainloop()
