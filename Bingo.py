from tkinter import *
from random import *
from time import *
class bingoGame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, bg = 'pink')
        self.master = master
        self.box_count = 0
        self.bingoCards = []
        self.cardNum = []
        self.picList = {}
        self.chosenImgs = []
        self.cardsLists = []
        self.imgLeft = 25
        self.duplicates = set()
        self.blackedOut = False
        self.init_bingoGame()
    def init_bingoGame(self):
        self.master.title("Animals Bingo Blackout")
        with open('pics/txtImages.txt') as f:
            for i, line in enumerate(f):
                self.picList[i + 1] = line.strip().split(',')[0]
        topFrame = Frame(self, bg = 'yellow') # TOP FRAME
        topFrame.grid(row=0, column=0, columnspan=10, pady=3)
        
        lblCardNo = Label(topFrame, text="Select Card No:", font='Times 11 bold', bg = 'yellow') 
        lblCardNo.grid(row=0, column=0, columnspan=3, pady=3)
        self.spnCardNo = Spinbox(topFrame, from_=1, to=4, width=8, bg = 'yellow',command=self.updateCards)
        self.spnCardNo.grid(row=0, column=5, padx=10)
        self.btnStart = Button(topFrame, text='START', font='Times 11 bold', width=7, bg = 'yellow', command = self.start)
        self.btnStart.grid(row=0, column=8)
        self.bottomFrame = Frame(self,bg = 'pink')
        self.bottomFrame.grid(row=2, column=0, columnspan=10, padx = 5, pady=3)
        self.cardNames = []
        self.cardsLeft = []
        self.updateCards()
        self.pack()
    def start(self):
        self.btnStart.config(text='RESTART', width=9, command=self.restartGame)
        self.genImage()

    def updateCards(self):
        self.selected_cardNo = int(self.spnCardNo.get())
        self.resetGame()
        self.cardsLists.clear()
        self.cardNames.clear()
        self.cardsLeft.clear()
        for x in range(self.selected_cardNo):
            self.insertCards(x+1)
    def insertCards(self, card_no):
        grid_count = 5  
        box_count = grid_count * grid_count
        selected_images = sample(list(self.picList.values()), box_count)
        shuffle(selected_images)
        middleFrame = Frame(self, borderwidth=2, relief="ridge")
        middleFrame.grid(row = 1, column = card_no-1, pady=3,padx=3)
        cards = []
        imgLeftLabel = Label(middleFrame, text=f'{self.imgLeft} left.', font='Times 10 bold')
        imgLeftLabel.grid(row=6, column=2)
        self.cardsLeft.append(self.imgLeft)
        self.cardNames.append(imgLeftLabel)
        for i in range(grid_count):  # row
            for o in range(grid_count):  # column
                self.img = PhotoImage(file=f"pics/{selected_images[i*grid_count+o]}.png")
                bingoImg = Label(
                    middleFrame,
                    image=self.img,
                    height=65, width=65,
                    relief='ridge') 
                bingoImg.grid(row=i, column=o)
                bingoImg.image = self.img   
                self.bingoCards.append(bingoImg)
                cards.append(bingoImg)
        self.bingoCards.append(middleFrame)
        self.cardsLists.append(cards)
        root.geometry(f"{355 * self.selected_cardNo}x490")
    def restartGame(self):
        self.resetGame()
        self.blackedOut = False
        self.start()
    def resetGame(self):
        for widget in self.chosenImgs + self.bingoCards:
            widget.destroy()
        self.bingoCards.clear()
        self.chosenImgs.clear()
        self.imgLeft = 25
    def createBingo(self, x):
        while True:
            img_fileName = choice(list(self.picList.values())) + '.png'
            if img_fileName not in self.duplicates:
                break
        self.duplicates.add(img_fileName)
        self.img = PhotoImage(file=f"pics/{img_fileName}")
        bingoImg = Label(
            self.bottomFrame,
            image=self.img,
            height=65, width=65,
            relief='flat', bg = 'pink') 
        bingoImg.grid(row=1, column=x, padx=1, pady=1)
        bingoImg.image = self.img
        self.chosenImgs.append(bingoImg)
        for cardsList in self.cardsLists:
            for card in cardsList:
                cardFile = card.image["file"]
                if cardFile == bingoImg.image["file"]:
                    self.imgLeft -= 1
                    cardIndex = self.cardsLists.index(cardsList)
                    self.cardsLeft[cardIndex] -= 1
                    self.cardNames[cardIndex].config(text=f'{self.cardsLeft[cardIndex]} left.')
                    card.config(bg="red")
                    if self.imgLeft == 0:
                        self.cardNames[cardIndex].config(text='Blacked out.')
                        return
                    break
    def genImage(self):
        self.selected_cardNo = int(self.spnCardNo.get())
        group_size = 10 if self.selected_cardNo == 2 else 5  
        for _ in range(76):
            img_index = len(self.chosenImgs)
            self.createBingo(img_index)         
            if len(self.chosenImgs) % (self.selected_cardNo * 5) == 0:
                for widget in self.chosenImgs[-group_size:]:
                    widget.destroy()
                self.chosenImgs = self.chosenImgs[-group_size:]    
            if self.blackedOut:
                for index, cardLeft in enumerate(self.cardsLeft):
                    if cardLeft == 0:
                        self.cardNames[index].config(text='Blacked out.')
                break  
            self.bottomFrame.update()
            sleep(0.1)
root = Tk()
root.geometry("355x490")
root.config(bg="pink")
app = bingoGame(root)
root.mainloop()