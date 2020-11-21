import tkinter
# import requests
# import json
#
# url = 'https://raw.githubusercontent.com/tijmenjoppe/AnalyticalSkills-student/master/project/data/steam.json'
#
# response = requests.get(url)
#
# content = json.loads(response.text)
#
# for rij in content:
#     print(rij['name'])
""""
Steam colour codes:
#171a21 donker donker blauw
#66c0f4 licht licht blauw
#1b2838 donker blauw
#2a475e licht blauw
#c7d5e0 grijswit

Label settings: bg = '#2a9df4',fg='white'
                bg = '#187bcd',fg='white'
                bg = '#0197CF',fg='white' (Favoriet)
"""

def startFrame():
    onlineScherm.forget()
    gamesScherm.forget()
    startScherm.pack()
    root.geometry('400x400')
    #optie scherm met wat je wilt zien

def onlineVriendenFrame():
    startScherm.forget()
    onlineScherm.pack()
    root.geometry('400x400')
    #vrienden die online zijn moeten getoond worden, ook wat je verwacht wat online komt.

def playedGamesFrame():
    startScherm.forget()
    gamesScherm.pack()
    root.geometry('400x400')
    #games die gespeeld worden en mogelijk nu gespeeld worden.

root = tkinter.Tk()
root.configure(background='#1b2838')
root.title('Steam AI')
#root.maxsize(600,400)


startScherm = tkinter.Frame(master=root,bg = '#1b2838')
startScherm.pack()
startSchermWelkomLabel = tkinter.Label(master=startScherm,text='Welkom!',bg = '#1b2838',fg='white',font=(30))
startSchermWelkomLabel.pack(pady=10)
startSchermOnline = tkinter.Button(master=startScherm,text='Online vrienden',command=onlineVriendenFrame,bg = '#2a475e',fg='#c7d5e0',
activebackground='green')
startSchermOnline.pack()
startSchermGames = tkinter.Button(master=startScherm,text='Games',command=playedGamesFrame,bg = '#2a475e',fg='#c7d5e0')
startSchermGames.pack()

onlineScherm = tkinter.Frame(master=root,bg = '#1b2838')
onlineScherm.pack()
onlineVrienden = tkinter.Label(master=onlineScherm,text='Momenteel online:',bg = '#0197CF',fg='white')
onlineVrienden.pack(pady=3)
mogelijkOnline = tkinter.Label(master=onlineScherm,text='Deze vrienden zijn nu vaak online:',bg = '#0197CF',fg='white')
mogelijkOnline.pack(pady=3)
terugButton = tkinter.Button(master=onlineScherm, text ='Terug',command=startFrame,bg = '#2a475e',fg='#c7d5e0')
terugButton.pack()

gamesScherm = tkinter.Frame(master=root,bg = '#1b2838')
gamesScherm.pack()
gamesNuGespeeld = tkinter.Label(master=gamesScherm,text='Games die nu gespeeld worden:',bg = '#0197CF',fg='white')
gamesNuGespeeld.pack(pady=3)

response = requests.get(url)
content = json.loads(response.text)
game1 = (content[220]["name"])
huidigegame = tkinter.Label(master=gamesScherm, text=game1,bg = '#0197CF',fg='white')
huidigegame.pack(pady=3)

gamesMogelijkGespeeld = tkinter.Label(master=gamesScherm,text='Games die nu mogelijk gespeeld worden:',bg = '#0197CF',fg='white')
gamesMogelijkGespeeld.pack(pady=3)
terugButton = tkinter.Button(master=gamesScherm, text ='Terug',command=startFrame,bg = '#2a475e',fg='#c7d5e0')
terugButton.pack()

startScherm.forget()
onlineScherm.forget()
gamesScherm.forget()

startFrame()

root.mainloop()
