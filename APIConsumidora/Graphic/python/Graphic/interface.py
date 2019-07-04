from tkinter import *
import requests
import json
import os


#Get/Post
def post(nome):
        if nome != '':
                if requests.post('http://localhost:8000/api/reis', data = {'name':nome}):
                        labelFeed['text'] = "Rei indicado com sucesso!"
                        labelFeed['fg'] = "white"
                        labelFeed['bg'] = 'green'
                        frame2['bg'] = 'green'
                
                        labelFeed['font'] = 'none 12 bold'
                else :
                        labelFeed['text'] = "Não foi possível indicar esse bastardo"
                        labelFeed['bg'] = 'red'
                        labelFeed['fg'] = "white"
                        labelFeed['font'] = 'none 12 bold'
                        frame2['bg'] = 'red'
        else:
                labelFeed['text'] = "Estamos sem rei!!!!"
                labelFeed['bg'] = '#ff531a'
                labelFeed['fg'] = "white"
                labelFeed['font'] = 'none 12 bold'
                frame2['bg'] = '#ff531a'
def get():
    data = requests.get('http://localhost:8000/api/reis')
    binary = data.content
    output = json.loads(binary)
    for item in output['data']:
        labelList['text'] = "Saudem o Rei " + item['name']
#Window Configuration
window = Tk()
window.title("Game Of Python 3.0")
canvas = Canvas(window, height='500', width='500')
canvas.pack()
#Background
background = PhotoImage(file='teste.png')
backgroundLabel = Label(window, image=background)
backgroundLabel.place(relwidth=1, relheight=1)
#Frames
frameList = Frame(window, bg='#f0f0f5', bd=10)
frameList.place(relx=0.5, rely=0.50, relwidth=0.75, relheight=0.4, anchor='center')

frameList2 = Frame(window, bg='#f0f0f5', bd=10)
frameList2.place(relx=0.5, rely=0.9, relwidth=0.75, relheight=0.1, anchor='center')

frame = Frame(window, bg='#f0f0f5', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='center')

frame2 = Frame(window, bg='#f0f0f5', bd=5)
frame2.place(relx=0.5, rely=0.23, relwidth=0.75, relheight=0.1, anchor='center')
#Entry inputs
entry = Entry(frame, font=20)
entry.place(relwidth=0.65, relheight=1)
#Buttons
button = Button(frame, text="King Name",command=lambda : post(entry.get()))
button.place(relx=0.7, relwidth=0.30, relheight=1)

button2 = Button(frameList2, text="Saudação",command=lambda : get())
button2.place(relwidth=1, relheight=1)
#Labels
labelList = Label(frameList)
labelList.place(relwidth=1, relheight=1)

labelFeed = Label(frame2, text='')
labelFeed.place(relwidth=1, relheight=1)
window.mainloop()