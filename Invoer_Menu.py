import datetime
import json
from tkinter import *

def tweet_opslaan():
    verzonden_tweet = tweet.get()
    if len(verzonden_tweet) == 0:
        bericht = Label(text='Heb je echt niks te zeggen over ons?',font=("Times", 12, "bold"), bg="#fcc63f",
                        fg="#212b5c")
        bericht.place(x=255, y=340)
        return bericht
    elif len(verzonden_tweet) <= 140:
        jason_append()
        bericht = Label(text='Uw Tweet is succevol verzonden!\nVolg ons op Twitter @jhasjfgdsjg',
                        font=("Times", 12, "bold"), bg="#fcc63f", fg="#212b5c")
        bericht.place(x=268, y=320)
        return bericht
    elif len(verzonden_tweet) >= 141:
        bericht = Label(text='We vinden het altijd leuk dat u veel van ons houdt maar dat is een heel lang verhaal '
                             'daar.\nProbeer opnieuw en korter <3!', font=("Times", 12, "bold"), bg="#fcc63f",
                        fg="#212b5c")
        bericht.place(x=90, y=320)
        return bericht
    else:
        bericht = Label(text='Er is iets mis gegaan :(\n Probeer opnieuw!', font=("Times", 12, "bold"),
                        bg="#fcc63f", fg="#212b5c")
        bericht.place(x=255, y=320)
        return bericht


def jason_append(): #Functie om de Tweet, met zijn ID en Datum naar een JASON File opslaan
    verzonden_tweet = tweet.get()+'\n'
    datum = datetime.datetime.now()
    current_date = '{}:{}:{} {}/{}/{}'.format(datum.hour, datum.minute, datum.second, datum.day, datum.month,
                                              datum.year)

    with open('tweetlijst.json', 'r', encoding="utf-8") as json_file:
        tweetlijst = json.load(json_file)
        nieuwe_tweet = {}
        nieuwe_tweet['ID'] = len(tweetlijst)
        nieuwe_tweet['Tweet'] = verzonden_tweet
        nieuwe_tweet['Datum'] = current_date
        tweetlijst.append(nieuwe_tweet)

        with open('tweetlijst.json', 'w', encoding="utf-8") as json_file:
            json.dump(tweetlijst, json_file, indent=len(tweetlijst), ensure_ascii=False)
            json_file.close()
    tweet_invullen.delete(0, END)


#Layout
appinterface = Tk()
appinterface.geometry("768x382")
appinterface.resizable(width=False, height=False)
appinterface.title("Tweet Invoer Pagina")
appinterface.iconbitmap('NS_icon.ico')

layout= Canvas(appinterface, bg='#fcc63f')
afbeelding = PhotoImage(file='Appinterface_achtergrond.png')
achtergrond= Label(appinterface, image=afbeelding, bg='#fcc63f')
achtergrond.pack()
layout.pack()


top_titel = Label(text="Stuur je opmerkingen/meningen over onze diensten met behulp van deze applicatie", bg="#fcc63f",
                  fg="#212b5c", font=("Times", 14, "bold"))
top_titel.place(x=45, y=10)

tweet_text = Label(text="Hieronder je Tweet invullen", bg="#fcc63f",
                  fg="#212b5c", font=("Times", 12, "bold"))
tweet_text.place(x=280, y=120)

tweet = StringVar()

tweet_invullen = Entry(textvariable=tweet, width="31")
tweet_invullen.place(x=280, y=150)

send = Button(appinterface, text="Verzenden", width="15", height="2", font=("Times", 10, "bold"),
              command=tweet_opslaan, bg='#212b5c',
              fg='#fcc63f')
send.place(x=320, y=200)

appinterface.mainloop()