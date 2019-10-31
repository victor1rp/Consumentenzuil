from tkinter import *
from TwitterAPI import TwitterAPI
import json
import datetime
api = TwitterAPI('xsKJiql07a9iTFcIzVAGxuSqZ',   #consumer key
                 'DonNCHPSVJpwPNBhVGGeSO2ZEJwoGyUyAtxgz1p5hryzBrM4BU',  #consumer secret key
                 '1188760815261933569-j5BtIGSXPUMl2cPDUkhdnMnKewVEnB',  #acces token key
                 '7okJrulDrjSBBwg6zJWsF9fNMyuuPaaoVUNRsrlwxCwe9')   #acces token secret key

def check(toBeChecked):
    global counter

    if next['text'] == 'begin':
        next['text'] = 'volgende'
        tweet['text'] = toBeChecked[counter]["Tweet"]

    elif counter < len(toBeChecked):
        if acceptTicked.get() == 0: #reject knop
            print(counter, toBeChecked[counter], 'rejected')
            toBeChecked[counter]["Accepted"] = False
            toBeChecked[counter]["DatumRejected"] = datetime.datetime.today().strftime("%X %d/%m/%Y")
        if acceptTicked.get() == 1: #accept knop
            print(counter, toBeChecked[counter], 'accepted')
            toBeChecked[counter]["Accepted"] = True
            toBeChecked[counter]["Tweeted"] = False
        counter += 1
    if counter != len(toBeChecked): #displayed volgende tweet die gekeurd moet worden
        tweet['text'] = toBeChecked[counter]["Tweet"]
    else:
        tweet['text'] = 'Alle tweets zijn gekeurd en gepost, je bent klaar.'
        updateJSON()
        tweetCheckedMessages()

def updateJSON(): #vervangt de entries in data met de nieuwe in toBeChecked, en plaatst deze vervolgens in de JSON file
    for checkedItem in toBeChecked:
        for item in data:
            if checkedItem["ID"] == item["ID"]:
                data.remove(item)
                data.append(checkedItem)
    with open('tweetlijst.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)

def tweetCheckedMessages(): #tweet de berichten in data met "Accepted" == True en "Tweeted" == False
    for item in data:
        if item["Accepted"] == True and item["Tweeted"] == False:
            r = api.request('statuses/update', {'status': item["Tweet"]})
            print(r.status_code)
            item["Tweeted"] = True
            with open('tweetlijst.json', 'w') as outfile:   #update de "Tweeted" key in de JSON file
                json.dump(data, outfile, indent=4)

counter = 0

with open('tweetlijst.json', 'r') as infile:    #zet tweets uit json file in een lijst
    data = json.load(infile)
toBeChecked = list()

for message in data:    #haalt nog niet gekeurde tweets uit data lijst
    if "Accepted" not in message:
        toBeChecked.append(message)

root = Tk()
root.state('zoomed')
acceptTicked = IntVar()

mainFrame = Frame(master=root)
mainFrame.place(relx=0.5, rely=0.5, anchor=CENTER)

tweet = Label(master=mainFrame, background='#ffcc18', font=("Helvetica", 20, ), fg='#00016c', height=10, width=50, wraplength=800)
tweet.pack(pady=10, padx=10)

buttonFrame = Frame(master=mainFrame)
buttonFrame.pack()

accept = Radiobutton(master=buttonFrame, text='goedgekeuren', variable=acceptTicked, value=1, height=5, width=15, font=("Helvetica", 15))
accept.pack(side=RIGHT, padx=10)
reject = Radiobutton(master=buttonFrame, text='afkeuren', variable=acceptTicked, value=0, height=5, width=15, font=("Helvetica", 15))
reject.pack(side=LEFT, padx=10)
next = Button(master = buttonFrame, text='begin', command=lambda: check(toBeChecked), height=5, width=15, font=("Helvetica", 15))
next.pack()

mainloop()