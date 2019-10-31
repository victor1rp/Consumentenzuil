from tkinter import *
import json
lst = []
with open('tweetlijst.json') as json_file:
    d = json.load(json_file)
    for i in d:
        if i['Accepted'] == True:
         lst.append(i)

def bericht1():
    try:
        text = lst[-1]['Datum'] + '\n' + lst[-1]['Tweet']
    except:
        text = ''
    return text



def bericht2():
    try:
        text = lst[-2]['Datum'] + '\n' + lst[-2]['Tweet']
    except:
        text = ''
    return text


def bericht3():
    try:
        text =  lst[-3]['Datum'] + '\n' + lst[-3]['Tweet']
    except:
        text = ''
    return text



root = Tk()
root.geometry("768x382")
root.resizable(width=False, height=False)
root.title("Tweets Pagina")
root.iconbitmap('NS_icon.ico')

layout= Canvas(root, bg='#fcc63f')
afbeelding = PhotoImage(file='Appinterface_achtergrond.png')
achtergrond= Label(root, image=afbeelding, bg='#fcc63f')
achtergrond.pack()
layout.pack()



label1 = Label(root,
               text = 'NS Twitter berichten',
               bd = 1,
               relief = 'solid',
               font = 'times 20',
               background = '#fcc63f',
               foreground = '#212b5c',
               width = 18,
               height = 1,)


label2 = Label(root,
               text = bericht1(),
               bd = 1,
               relief = 'solid',
               font = 'times 12',
               background = '#fcc63f',
               foreground = '#212b5c',
               width = 40,
               height = 5,
               anchor = N,
               wraplength=250)
label3 = Label(root,
               text = bericht2(),
               bd = 1,
               relief = 'solid',
               font = 'times 12',
               background  = '#fcc63f',
               foreground = '#212b5c',
               width = 40,
               height = 5,
               anchor = N,
               wraplength=250)
label4 = Label(root,
               text = bericht3(),
               bd = 1,
               relief = 'solid',
               font = 'times 12',
               background = '#fcc63f',
               foreground = '#212b5c',
               width = 40,
               height = 5,
               anchor = N,
               wraplength=250)

label1.place(x=245, y=5)
label2.place(x=200, y=70)
label3.place(x=200, y=175)
label4.place(x=200, y=280)
root.mainloop()