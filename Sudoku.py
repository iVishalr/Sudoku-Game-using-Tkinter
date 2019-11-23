import tkinter as tk
from tkinter import ttk
import time
import copy
import multiprocessing
import random
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
style.use("ggplot")
time1 = time.time()
LARGE_FONT = ("Verdana",20)
diff = []
entries=[]
pro=""
choices=0
print(choices)

f = Figure(figsize=(4,4),dpi=100)
a = f.add_subplot(111)

def animate(i):
    file=open("Control.txt","r")
    choice = int(file.read())
    file.close()
    if(choice==1):
        pulldata = open("easyAnsSet.txt","r").read()
        dataList = pulldata.split("\n")
        xList = []
        for eachLine in dataList:
            if len(eachLine) >= 1:
                xList.append(int(eachLine))

        a.clear()
        a.bar("Your Score", xList[len(xList) - 1], width=0.8)
        avg = sum(xList) / len(xList)
        a.bar("Average Score", avg, width=0.8)
    elif(choice==2):
        pulldata = open("mediumAnsSet.txt", "r").read()
        dataList = pulldata.split("\n")
        xList = []
        for eachLine in dataList:
            if len(eachLine) >= 1:
                xList.append(int(eachLine))

        a.clear()
        a.bar("Your Score", xList[len(xList) - 1], width=0.8)
        avg = sum(xList) / len(xList)
        a.bar("Average Score", avg, width=0.8)
    elif (choice == 3):
        pulldata = open("hardAnsSet.txt", "r").read()
        dataList = pulldata.split("\n")
        xList = []
        for eachLine in dataList:
            if len(eachLine) >= 1:
                xList.append(int(eachLine))

        a.clear()
        a.bar("Your Score", xList[len(xList) - 1], width=0.8)
        avg = sum(xList) / len(xList)
        a.bar("Average Score", avg, width=0.8)
    elif (choice == 4):
        pulldata = open("insaneAnsSet.txt", "r").read()
        dataList = pulldata.split("\n")
        xList = []
        for eachLine in dataList:
            if len(eachLine) >= 1:
                xList.append(int(eachLine))

        a.clear()
        a.bar("Your Score", xList[len(xList) - 1], width=0.8)
        avg = sum(xList) / len(xList)
        a.bar("Average Score", avg, width=0.8)



class SudokuApp(tk.Tk):

    '''This is the main class. It creates window for Sudoku Game'''
    #*args is any number of arguments
    #**kwargs are keyword arguments such as dictionaries

    def __init__(self,*args,**kwargs):
        self.problem_Set =0
        tk.Tk.__init__(self,*args,**kwargs)
        #tk.Tk.iconbitmap(self, default="sudoku.ico")
        tk.Tk.wm_title(self,"Sudoku Game")

        container = tk.Frame(self)
        container.pack(side="top", fill="both",expand=True)

        #Fill will fill in the space we allowed for the pack
        #expand - if there are any more whitespaces in the window it expands the frame to fill it.

        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        #0 sets the minimum size
        # weight gives the priority
        self.selected_choice=""
        self.name=""

        self.frames = dict()

        for F in (StartPage,PageOne,PageTwo,SudokuUIPage,resultPage):

            frame = F(container,self)
            self.frames[F] = frame

            frame.grid(row=0,column=0,sticky="nsew")

        #grid is used to place the frame in the window in the specified row number and column number
        # sticky is used for alignment. nsew stands for North South East West.

        self.show_frame(StartPage)


    def show_frame(self,cont):

        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    """This class creates a new frame in the app."""
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        #parent is the main class

        label = tk.Label(self, text="Welcome to Sudoku Game", font=("Verdana",40))
        label.pack(pady=10, padx=10)

        #to print an image on the main screen
        label1=tk.Label(self,command=self.showImg())
        label1.pack()
        label2 = ttk.Label(self,text="Sudoku is considered highly addictive\nbut since there aren’t any harmful side effects\ngo right ahead and get addicted!",font=("Bold",20))
        label2.place(x=600,y=300)
        button1 = ttk.Button(self,text="Let's Play", command=lambda: controller.show_frame(PageOne))
        button1.place(x=600,y=400)

        #Button to quit the game
        button2 = ttk.Button(self,text="Exit", command=lambda :self.close())
        button2.place(x=600,y=430)

    def close(self):
        file = open("Control.txt","w")
        file.write("0")
        file.close()
        file = open("ControlFile.txt", "w")
        file.write('0')
        file.close()
        app.quit()

    def showImg(self):
        render = tk.PhotoImage(file="sudoku.jpeg")
        img = tk.Label(self,image=render)
        img.Image=render
        img.place(x=50,y=115)

class PageOne(tk.Frame):
    """This class creates a new frame in the app."""
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        width_value = PageOne.winfo_screenwidth(self)
        height_value = PageOne.winfo_screenheight(self)

        label = ttk.Label(self,text="Hey There!",font=("Bold",30))
        label.place(x=50,y=30)

        label1 = ttk.Label(self,text="Enter your Name :",font=LARGE_FONT,style="BW.TLabel")
        label1.place(x=50,y=height_value//8)

        entry_name = ttk.Entry(self)
        entry_name.place(x=260,y=height_value//8+4)

        choice = tk.IntVar()
        self.selected_choice = 0

        difficulty = [("  Easy",1),("  Medium",2),("  Hard",3),("  Insane",4)]

        label2 = ttk.Label(self,text="Please select the level of difficulty :",font=("Verdana",20),style="BW.TLabel")
        label2.place(x=50,y=height_value//8+70)

        rad_y = height_value//8+120
        choice_button1 = ttk.Radiobutton(self,text=difficulty[0][0],variable=choice,command=lambda :ShowChoice(),value=difficulty[0][1])
        choice_button1.place(x=50,y=rad_y)

        choice_button2 = ttk.Radiobutton(self, text=difficulty[1][0], variable=choice,command=lambda: ShowChoice(), value=difficulty[1][1])
        choice_button2.place(x=50, y=rad_y+35)

        choice_button3 = ttk.Radiobutton(self, text=difficulty[2][0], variable=choice,command=lambda: ShowChoice(), value=difficulty[2][1])
        choice_button3.place(x=50, y=rad_y + 70)

        choice_button4 = ttk.Radiobutton(self, text=difficulty[3][0], variable=choice,command=lambda: ShowChoice(), value=difficulty[3][1])
        choice_button4.place(x=50, y=rad_y + 105)

        button3 = ttk.Button(self, text="Submit", command=lambda: getInfo())
        button3.place(x=50, y=height_value // 8 + 270)

        button1 = ttk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        button1.place(x=50, y=height_value // 8 + 305)


        def ShowChoice():
            global choices
            control = 1
            app.selected_choice = choice.get()
            choices = app.selected_choice
            file = open("Control.txt","w")
            file.write(str(app.selected_choice))
            file.close()
            print(app.selected_choice,"You selected")

        def getInfo():


            processes = []
            process2 = multiprocessing.Process(target=multiprocess)
            processes.append(process2)
            process2.start()

            process3 = multiprocessing.Process(target=controller.show_frame(PageTwo))
            process3.start()
            process3.append(processes)
            for process in processes:
                process.join()
class PageTwo(tk.Frame):
    """This class creates a new frame in the app."""
    def __init__(self,parent,controller):

        tk.Frame.__init__(self,parent)
        #display the question to the user
        label = tk.Label(self,text="Rules Of Sudoku",font=("Bold",30))
        label.place(x=50,y=30)
        label1 = ttk.Label(self,text="While solving Sudoku puzzles can be significant challenge, the rules for traditional solution finding are quite straight forward.\n\n1. Each row, column, and nonet can contain each number (typically 1 to 9) exactly once.\n\n2. For traditional Sudoku puzzles featuring the numbers 1 to 9, this sum is equal to 45.\n\n3. In order to solve Sudoku puzzles reliably,you must be disciplined, focused, and patient.",font=("Bold",20))
        label1.place(x=50,y=100)

        label2=ttk.Label(self,text="4. If you enter more than one number then only the first number will be considered for evaluation.",font=("Bold",20))
        label2.place(x=50,y=275)
        choice = 0
        button1 = ttk.Button(self,text=" Back ",command=lambda: controller.show_frame(PageOne))
        button1.place(x=50,y=330)

        button_entry = ttk.Button(self,text=" Next ",command=lambda:go())
        button_entry.place(x=150,y=330)


        def go():

            controller.show_frame(SudokuUIPage)


class SudokuUIPage(tk.Frame):
    """This class creates a new frame in the app. This class is responsible for generating the sudoku grid."""
    time_taken=time.time()
    global pro

    def __init__(self,parent,controller):

        tk.Frame.__init__(self, parent)
        width_value1 = self.winfo_screenwidth()
        height_value1 = self.winfo_screenheight()
        self.createCan()
        self.updater1()
        label = ttk.Label(self,text="How's Scoring done?",font=("Bold",30))
        label.place(x=600,y=100)
        label1 = ttk.Label(self, text="Maximum Marks: 100", font=("Bold", 20))
        label1.place(x=600, y=150)
        label2 = ttk.Label(self, text="If the puzzle remains unsolved or the solved puzzle is incorrect\none mark will be given to each valid entry.\n\n\nRemember, if you enter more than one number\nonly the first entry will be considered for evaluation.", font=("Bold", 20))
        label2.place(x=600, y=190)
        button = ttk.Button(self, text="Submit", command=lambda:readVal())
        button.place(x=600,y=350)

        button1 = ttk.Button(self, text="Exit", command=lambda:self.onExit())
        button1.place(x=600,y=380)

        def readVal():

            global pro

            temp = pro
            file = open("TempProb.txt","w")
            file.write(str(temp))
            file.close()
            del temp
            entValues = []
            user_solution = []
            for i in entries:
                entValues.append(i.get())

            count = 0
            for i in range(9):
                x = []
                for j in range(9):
                    if (pro[i][j] == 0 and entValues[count] != ''):
                        x.append(int(entValues[count][0]))
                        count += 1
                    elif (pro[i][j] == 0 and entValues[count] == ''):
                        x.append(0)
                        count += 1
                    else:
                        x.append(pro[i][j])
                user_solution.append(x)

            print(user_solution)
            compSol = compSolveSudoku()
            print(compSol)

            file = open("TempProb.txt","r")
            s= file.read()

            prob_stat = []
            row = []
            i = 0
            while (True):
                count = 0
                for j in s:
                    if (count < 9):
                        if (j != "["):
                            if (j != "]"):
                                if (j != "," and j != " "):
                                    row.append(int(j))
                                    count += 1
                    else:
                        prob_stat.append(row)
                        row = []
                        i += 1
                        count = 0
                if (i == 9):
                    break

            score = 0

            validating_list=[]
            test_list=[]
            for i in range(9):
                for j in range(9):
                    if(prob_stat[i][j]==0):
                        validating_list.append(user_solution[i][j])
                        test_list.append(compSol[i][j])

            for i in range(0,len(validating_list)):

                if validating_list[i]==test_list[i]:
                    score+=1
            if(user_solution==compSol):
                score=100
            else:
                pass
            if app.selected_choice == 1:
                file = open("easyAnsSet.txt","a")
                file.write(str(score)+"\n")
                file.close()
                print(SudokuUIPage.time_taken)
            elif app.selected_choice == 2:
                file = open("mediumAnsSet.txt", "a")
                file.write((str(score)+"\n"))
                file.close()
            elif app.selected_choice == 3:
                file = open("hardAnsSet.txt", "a")
                file.write((str(score)+"\n"))
                file.close()
            elif app.selected_choice == 4:
                file = open("insaneAnsSet.txt", "a")
                file.write((str(score)+"\n"))
                file.close()


            controller.show_frame(resultPage)

    def updater1(self):
        file = open("Control.txt", "r")
        choices = int(file.read())
        file.close()
        file=open("ControlFile.txt","r")
        control = int(file.read())
        file.close()
        if(choices==0):
            try:
                self.createCan()
            except Exception as e:
                pass
        elif(choices!=0 and control<1):
            file=open("ControlFile.txt","w")
            file.write(str(control+1))
            file.close()
            self.createCan()
        self.after(5000,self.updater1)

    def createCan(self):

        canvas = tk.Canvas(self, height=510, width=510)
        x = 5
        y = 56
        p = 500
        q = 56
        for i in range(10):
            if i == 0:
                line = canvas.create_line(5, 5, 500, 5, width=5)
            elif (i == 1 or i == 2):
                line = canvas.create_line(x, y, p, q, width=1)
                y += 56
                q += 56
            elif (i == 3):
                line = canvas.create_line(x, y, p, q, width=5)
                y += 56
                q += 56
            elif (i == 4 or i == 5):
                line = canvas.create_line(x, y, p, q, width=1)
                y += 56
                q += 56
            elif (i == 6):
                line = canvas.create_line(x, y, p, q, width=5)
                y += 56
                q += 56
            elif (i == 7 or i == 8):
                line = canvas.create_line(x, y, p, q, width=1)
                y += 56
                q += 56
            elif (i == 9):
                line = canvas.create_line(x, y, p, q, width=5)
                y += 56
                q += 56
        x1 = 56
        y1 = 0
        p1 = 56
        q1 = 506
        for i in range(10):
            if i == 0:
                line = canvas.create_line(5, 0, 5, 506, width=5)
            elif (i == 1 or i == 2):
                line = canvas.create_line(x1, y1, p1, q1, width=1)
                x1 += 56
                p1 += 56
            elif (i == 3):
                line = canvas.create_line(x1, y1, p1, q1, width=5)
                x1 += 56
                p1 += 56
            elif (i == 4 or i == 5):
                line = canvas.create_line(x1, y1, p1, q1, width=1)
                x1 += 56
                p1 += 56
            elif (i == 6):
                line = canvas.create_line(x1, y1, p1, q1, width=5)
                x1 += 56
                p1 += 56
            elif (i == 7 or i == 8):
                line = canvas.create_line(x1, y1, p1, q1, width=1)
                x1 += 56
                p1 += 56
            elif (i == 9):
                line = canvas.create_line(x1 - 5, y1, p1 - 5, q1, width=5)
                x1 += 56
                p1 += 56
        canvas.place(x=50, y=120)
        c=0
        p, q = 65, 137
        for i in range(9):
            x=0
            for k in range(9):
                if(i==0 and k==0):
                    c=0
                    x=loadVal(i,k,c)
                else:
                    c=1
                    x=loadVal(i,k,c)
                if(x!='0'):
                    E = tk.Label(self,text=x,font=("Bold",20))
                    E.grid_slaves(row=i, column=k)
                    E.place(x=p, y=q)
                    p += 56.0
                else:
                    entry = tk.Entry(self,width=3,font=("BOLD",20))
                    entry.grid_slaves(row=i, column=k)
                    entry.place(x=p, y=q+0.5, height=25, width=25)
                    entries.append(entry)
                    p += 56.0
            q += 55
            p = 65

    def onExit(self):
        file = open("Control.txt","w")
        file.write(str(0))
        file.close()
        file = open("ControlFile.txt", "w")
        file.write(str(0))
        file.close()
        app.quit()

class resultPage(tk.Frame):

    def __init__(self,parent,controller):

        tk.Frame.__init__(self,parent)
        self.score = tk.IntVar()
        self.winmessage=tk.StringVar()
        self.readScore()
        self.updater()
        self.width_value = self.winfo_screenwidth()
        self.height_value = self.winfo_screenheight()
        if(self.score==100):
            labelx = ttk.Label(self,textvariable=self.winmessage,font=("Bold",30))
            labelx.place(x=50,y=18)
        else:
            labelx = ttk.Label(self, textvariable=self.winmessage, font=("Bold", 30))
            labelx.place(x=50, y=18)
        label1 = ttk.Label(self, text="You Scored : ",font=("Bold",25))
        label1.place(x=50,y=55)
        label2 = ttk.Label(self, textvariable=self.score ,font=("Bold",25))
        label2.place(x=190,y=56)
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack()

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()


        canvas._tkcanvas.place(x=0,y=85,height=600,width=1300)
        button1 = tk.Button(self, text="Exit", command=lambda: self.onExit())
        button1.place(x=1000,y=60)
        button1.configure(height=3,width=15)
    def updater(self):
        self.readScore()
        self.after(1000,self.updater)
    def onExit(self):
        file = open("Control.txt", "w")
        file.write(str(0))
        file.close()
        file = open("ControlFile.txt", "w")
        file.write(str(0))
        file.close()
        app.quit()

    def readScore(self):

        file = open("Control.txt", "r")
        c = int(file.read())
        file.close()
        if (c == 1):
            file1 = open("easyAnsSet.txt", "r")
            data = file1.read().split("\n")
            x = []
            for eachLine in data:
                if (len(eachLine) >= 1):
                    x.append(int(eachLine))
            file1.close()
            self.score.set(x[len(x)-1])
            if(x[len(x)-1]==100):
                self.winmessage.set("Congratulations!")
            else:
                self.winmessage.set("Better Luck Next Time!")

        elif (c == 2):
            file1 = open("mediumAnsSet.txt", "r")
            data = file1.read().split("\n")
            x = []
            for eachLine in data:
                if (len(eachLine) >= 1):
                    x.append(int(eachLine))
            file1.close()
            self.score.set(x[len(x)-1])
            if (x[len(x) - 1] == 100):
                self.winmessage.set("Congratulations!")
            else:
                self.winmessage.set("Better Luck Next Time!")
        elif(c==3):
            file1 = open("hardAnsSet.txt", "r")
            data = file1.read().split("\n")
            x = []
            for eachLine in data:
                if (len(eachLine) >= 1):
                    x.append(int(eachLine))
            file1.close()
            self.score.set(x[len(x)-1])
            if (x[len(x) - 1] == 100):
                self.winmessage.set("Congratulations!")
            else:
                self.winmessage.set("Better Luck Next Time!")
        elif (c == 4):
            file1 = open("insaneAnsSet.txt", "r")
            data = file1.read().split("\n")
            x = []
            for eachLine in data:
                if (len(eachLine) >= 1):
                    x.append(int(eachLine))
            file1.close()
            self.score.set(x[len(x)-1])
            if (x[len(x) - 1] == 100):
                self.winmessage.set("Congratulations!")
            else:
                self.winmessage.set("Better Luck Next Time!")

def loadVal(a,b,c):
    global pro
    global choices

    file = open("Control.txt", "r")
    choices = int(file.read())
    file.close()
    if (choices != 0):
        if (c == 0):
            if (choices == 1):
                file = open("EasyProbSet.csv", "r")
                data = file.read().split("\n")
                random.shuffle(data)
                x = data.index("")
                del data[x]
                # print(data)
                s = random.choice(data)
                prob = []
                row = []
                i = 0
                while (True):
                    count = 0
                    for j in s:
                        if (count < 9):
                            if (j != "["):
                                if (j != "]"):
                                    if (j != "," and j != " "):
                                        row.append(int(j))
                                        count += 1
                        else:
                            prob.append(row)
                            row = []
                            i += 1
                            count = 0
                    if (i == 9):
                        break
                pro = prob
                file.close()
            elif (choices == 2):
                file = open("MediumProbSet.csv", "r")
                data = file.read().split("\n")
                random.shuffle(data)
                x = data.index("")
                del data[x]
                s = random.choice(data)
                prob = []
                row = []
                i = 0
                while (True):
                    count = 0
                    for j in s:
                        if (count < 9):
                            if (j != "["):
                                if (j != "]"):
                                    if (j != "," and j != " "):
                                        row.append(int(j))
                                        count += 1
                        else:
                            prob.append(row)
                            row = []
                            i += 1
                            count = 0
                    if (i == 9):
                        break
                pro = prob
                file.close()
            elif (choices == 3):
                file = open("HardProbSet.csv", "r")
                data = file.read().split("\n")
                random.shuffle(data)
                x = data.index("")
                del data[x]
                s = random.choice(data)
                prob = []
                row = []
                i = 0
                while (True):
                    count = 0
                    for j in s:
                        if (count < 9):
                            if (j != "["):
                                if (j != "]"):
                                    if (j != "," and j != " "):
                                        row.append(int(j))
                                        count += 1
                        else:
                            prob.append(row)
                            row = []
                            i += 1
                            count = 0
                    if (i == 9):
                        break
                pro = prob
                file.close()
            elif (choices == 4):
                file = open("InsaneProbSet.csv", "r")
                data = file.read().split("\n")
                random.shuffle(data)
                x = data.index("")
                del data[x]
                s = random.choice(data)
                prob = []
                row = []
                i = 0
                while (True):
                    count = 0
                    for j in s:
                        if (count < 9):
                            if (j != "["):
                                if (j != "]"):
                                    if (j != "," and j != " "):
                                        row.append(int(j))
                                        count += 1
                        else:
                            prob.append(row)
                            row = []
                            i += 1
                            count = 0
                    if (i == 9):
                        break
                pro = prob
                file.close()
        if (c == 0):
            print(str(pro))
        return str(pro[a][b])

    else:
        pass

def shownum():

    if (not app.selected_choice==""):
        user_choice = app.selected_choice

        print(user_choice, "hi")
        if (user_choice == 1):
            print("one")
        elif (user_choice == 2):
            print("two")
        elif (user_choice == 3):
            print("three")
        elif (user_choice == 4):
            print("four")
def multiprocess():


    level=""
    if(app.selected_choice==1):
        level = "Easy"
    elif(app.selected_choice==2):
        level="Medium"
    elif(app.selected_choice==3):
        level = "Hard"
    elif(app.selected_choice==4):
        level="Insane"

    processes = []

    process1 = multiprocessing.Process(target=main,args=[level])
    process1.start()
    processes.append((process1))

    for process in processes:
        process.join()

def compSolveSudoku():

    SIZE = 9
    #sudoku problem
    #cells with value 0 are vacant cells
    matrix = pro
    print(pro)
    #function to print sudoku
    def print_sudoku1():
        comp_sol=[]
        for i in matrix:
            comp_sol.append(i)
        return comp_sol

    #function to check if all cells are assigned or not
    #if there is any unassigned cell
    #then this function will change the values of
    #row and col accordingly
    def number_unassigned1(row, col):
        num_unassign = 0
        for i in range(0,SIZE):
            for j in range (0,SIZE):
                #cell is unassigned
                if matrix[i][j] == 0:
                    row = i
                    col = j
                    num_unassign = 1
                    a = [row, col, num_unassign]
                    return a
        a = [-1, -1, num_unassign]
        return a
    #function to check if we can put a
    #value in a paticular cell or not
    def is_safe1(n, r, c):
        #checking in row
        for i in range(0,SIZE):
            #there is a cell with same value
            if matrix[r][i] == n:
                return False
        #checking in column
        for i in range(0,SIZE):
            #there is a cell with same value
            if matrix[i][c] == n:
                return False
        row_start = (r//3)*3
        col_start = (c//3)*3;
        #checking submatrix
        for i in range(row_start,row_start+3):
            for j in range(col_start,col_start+3):
                if matrix[i][j]==n:
                    return False
        return True

    #function to check if we can put a
    #value in a paticular cell or not
    def solve_sudoku1():
        row = 0
        col = 0
        #if all cells are assigned then the sudoku is already solved
        #pass by reference because number_unassigned will change the values of row and col
        a = number_unassigned1(row, col)
        if a[2] == 0:
            return True
        row = a[0]
        col = a[1]
        #number between 1 to 9
        for i in range(1,10):
            #if we can assign i to the cell or not
            #the cell is matrix[row][col]
            if is_safe1(i, row, col):
                matrix[row][col] = i
                #backtracking
                if solve_sudoku1():
                    return True
                #f we can't proceed with this solution
                #reassign the cell
                matrix[row][col]=0
        return False

    if solve_sudoku1():
        print("HellowWorld")
        x=print_sudoku1()
        return x
    else:
        print("No solution")

""" [Level of Difficulty] = Input the level of difficulty of the sudoku puzzle. Difficulty levels
        include ‘Easy’ ‘Medium’ ‘Hard’ and ‘Insane’. Outputs a sudoku of desired
        difficulty."""
class cell():
    """ Initilalizes cell object. A cell is a single box of a sudoku puzzle. 81 cells make up the body of a
        sudoku puzzle. Initializes puzzle with all possible answers available, solved to false, and position of cell within the
        sudoku puzzle"""

    def __init__(self, position):
        self.possibleAnswers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.answer = None
        self.position = position
        self.solved = False

    def remove(self, num):
        """Removes num from list of possible anwers in cell object."""
        if num in self.possibleAnswers and self.solved == False:
            self.possibleAnswers.remove(num)
            if len(self.possibleAnswers) == 1:
                self.answer = self.possibleAnswers[0]
                self.solved = True
        if num in self.possibleAnswers and self.solved == True:
            self.answer = 0

    def solvedMethod(self):
        """ Returns whether or not a cell has been solved"""
        return self.solved

    def checkPosition(self):
        """ Returns the position of a cell within a sudoku puzzle. x = row; y = col; z = box number"""
        return self.position

    def returnPossible(self):
        """ Returns a list of possible answers that a cell can still use"""
        return self.possibleAnswers

    def lenOfPossible(self):
        """ Returns an integer of the length of the possible answers list"""
        return len(self.possibleAnswers)

    def returnSolved(self):
        """ Returns whether or not a cell has been solved"""
        if self.solved == True:
            return self.possibleAnswers[0]
        else:
            return 0

    def setAnswer(self, num):
        """ Sets an answer of a puzzle and sets a cell's solved method to true. This
            method also eliminates all other possible numbers"""
        if num in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            self.solved = True
            self.answer = num
            self.possibleAnswers = [num]
        else:
            raise (ValueError)

    def reset(self):
        """ Resets all attributes of a cell to the original conditions"""
        self.possibleAnswers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.answer = None
        self.solved = False


def emptySudoku():
    ''' Creates an empty sudoku in row major form. Sets up all of the x, y, and z
        coordinates for the sudoku cells'''
    ans = []
    for x in range(1, 10):
        if x in [7, 8, 9]:
            intz = 7
            z = 7
        if x in [4, 5, 6]:
            intz = 4
            z = 4
        if x in [1, 2, 3]:
            intz = 1
            z = 1
        for y in range(1, 10):
            z = intz
            if y in [7, 8, 9]:
                z += 2
            if y in [4, 5, 6]:
                z += 1
            if y in [1, 2, 3]:
                z += 0
            c = cell((x, y, z))
            ans.append(c)
    return ans


def printSudoku(sudoku):
    '''Prints out a sudoku in a format that is easy for a human to read'''
    row1 = []
    row2 = []
    row3 = []
    row4 = []
    row5 = []
    row6 = []
    row7 = []
    row8 = []
    row9 = []
    for i in range(81):
        if i in range(0, 9):
            row1.append(sudoku[i].returnSolved())
        if i in range(9, 18):
            row2.append(sudoku[i].returnSolved())
        if i in range(18, 27):
            row3.append(sudoku[i].returnSolved())
        if i in range(27, 36):
            row4.append(sudoku[i].returnSolved())
        if i in range(36, 45):
            row5.append(sudoku[i].returnSolved())
        if i in range(45, 54):
            row6.append(sudoku[i].returnSolved())
        if i in range(54, 63):
            row7.append(sudoku[i].returnSolved())
        if i in range(63, 72):
            row8.append(sudoku[i].returnSolved())
        if i in range(72, 81):
            row9.append(sudoku[i].returnSolved())
    print(row1[0:3], row1[3:6], row1[6:10])
    print(row2[0:3], row2[3:6], row2[6:10])
    print(row3[0:3], row3[3:6], row3[6:10])
    print('')
    print(row4[0:3], row4[3:6], row4[6:10])
    print(row5[0:3], row5[3:6], row5[6:10])
    print(row6[0:3], row6[3:6], row6[6:10])
    print('')
    print(row7[0:3], row7[3:6], row7[6:10])
    print(row8[0:3], row8[3:6], row8[6:10])
    print(row9[0:3], row9[3:6], row9[6:10])

    file = open("Control.txt","r")
    level = file.read()
    file.close()

    prob = [row1,row2,row3,row4,row5,row6,row7,row8,row9]
    if(level=='4'):
        file1 = open("InsaneProbSet.csv","r")
        data = file1.read().split("\n")
        file1.close()
        if(not str(prob) in data):
            file2=open("InsaneProbSet.csv","a")
            file2.write(str(prob))
            file2.write("\n")
            file2.close()
        else:
            print("Problem already exists!")
            main("Insane")
    elif(level=='1'):
        file1 = open("EasyProbSet.csv", "r")
        data = file1.read().split("\n")
        file1.close()
        if (not str(prob) in data):
            file2 = open("EasyProbSet.csv", "a")
            file2.write(str(prob))
            file2.write("\n")
            file2.close()
        else:
            print("Problem already exists!")
            main("Easy")
    elif(level=='2'):
        file1 = open("MediumProbSet.csv", "r")
        data = file1.read().split("\n")
        file1.close()
        if (not str(prob) in data):
            file2 = open("MediumProbSet.csv", "a")
            file2.write(str(prob))
            file2.write("\n")
            file2.close()
        else:
            print("Problem already exists!")
            main("Medium")
    elif(level=='3'):
        file1 = open("HardProbSet.csv", "r")
        data = file1.read().split("\n")
        file1.close()
        if (not str(prob) in data):
            file2 = open("HardProbSet.csv", "a")
            file2.write(str(prob))
            file2.write("\n")
            file2.close()
        else:
            print("Problem already exists!")
            main("Hard")

    else:
        print("NotFoundError")

def sudokuGen():
    '''Generates a completed sudoku. Sudoku is completly random'''
    cells = [i for i in range(81)]  ## our cells is the positions of cells not currently set
    sudoku = emptySudoku()
    while len(cells) != 0:
        lowestNum = []
        Lowest = []
        for i in cells:
            lowestNum.append(
                sudoku[i].lenOfPossible())  ## finds all the lengths of of possible answers for each remaining cell
        m = min(lowestNum)  ## finds the minimum of those
        '''Puts all of the cells with the lowest number of possible answers in a list titled Lowest'''
        for i in cells:
            if sudoku[i].lenOfPossible() == m:
                Lowest.append(sudoku[i])
        '''Now we randomly choose a possible answer and set it to the cell'''
        choiceElement = random.choice(Lowest)
        choiceIndex = sudoku.index(choiceElement)
        cells.remove(choiceIndex)
        position1 = choiceElement.checkPosition()
        if choiceElement.solvedMethod() == False:  ##the actual setting of the cell
            possibleValues = choiceElement.returnPossible()
            finalValue = random.choice(possibleValues)
            choiceElement.setAnswer(finalValue)
            for i in cells:  ##now we iterate through the remaining unset cells and remove the input if it's in the same row, col, or box
                position2 = sudoku[i].checkPosition()
                if position1[0] == position2[0]:
                    sudoku[i].remove(finalValue)
                if position1[1] == position2[1]:
                    sudoku[i].remove(finalValue)
                if position1[2] == position2[2]:
                    sudoku[i].remove(finalValue)

        else:
            finalValue = choiceElement.returnSolved()
            for i in cells:  ##now we iterate through the remaining unset cells and remove the input if it's in the same row, col, or box
                position2 = sudoku[i].checkPosition()
                if position1[0] == position2[0]:
                    sudoku[i].remove(finalValue)
                if position1[1] == position2[1]:
                    sudoku[i].remove(finalValue)
                if position1[2] == position2[2]:
                    sudoku[i].remove(finalValue)
    return sudoku


def sudokuChecker(sudoku):
    """ Checks to see if an input a completed sudoku puzzle is of the correct format and abides by all
        of the rules of a sudoku puzzle. Returns True if the puzzle is correct. False if otherwise"""
    for i in range(len(sudoku)):
        for n in range(len(sudoku)):
            if i != n:
                position1 = sudoku[i].checkPosition()
                position2 = sudoku[n].checkPosition()
                if position1[0] == position2[0] or position1[1] == position2[1] or position1[2] == position2[2]:
                    num1 = sudoku[i].returnSolved()
                    num2 = sudoku[n].returnSolved()
                    if num1 == num2:
                        return False
    return True


def perfectSudoku():
    '''Generates a completed sudoku. Sudoku is in the correct format and is completly random'''
    result = False
    while result == False:
        s = sudokuGen()
        result = sudokuChecker(s)
    return s


def solver(sudoku, f=0):
    """ Input an incomplete Sudoku puzzle and solver method will return the solution to the puzzle. First checks to see if any obvious answers can be set
        then checks the rows columns and boxes for obvious solutions. Lastly the solver 'guesses' a random possible answer from a random cell and checks to see if that is a
        possible answer. If the 'guessed' answer is incorrect, then it removes the guess and tries a different answer in a different cell and checks for a solution. It does this until
        all of the cells have been solved. Returns a printed solution to the puzzle and the number of guesses that it took to complete the puzzle. The number of guesses is
        a measure of the difficulty of the puzzle. The more guesses that it takes to solve a given puzzle the more challenging it is to solve the puzzle"""
    if f > 900:
        return False
    guesses = 0
    copy_s = copy.deepcopy(sudoku)
    cells = [i for i in range(81)]  ## our cells is the positions of cells not currently set
    solvedCells = []
    for i in cells:
        if copy_s[i].lenOfPossible() == 1:
            solvedCells.append(i)
    while solvedCells != []:
        for n in solvedCells:
            cell = copy_s[n]
            position1 = cell.checkPosition()
            finalValue = copy_s[n].returnSolved()
            for i in cells:  ##now we itterate through the remaing unset cells and remove the input if it's in the same row, col, or box
                position2 = copy_s[i].checkPosition()
                if position1[0] == position2[0]:
                    copy_s[i].remove(finalValue)
                if position1[1] == position2[1]:
                    copy_s[i].remove(finalValue)
                if position1[2] == position2[2]:
                    copy_s[i].remove(finalValue)
                if copy_s[i].lenOfPossible() == 1 and i not in solvedCells and i in cells:
                    solvedCells.append(i)
                ##print(n)
            solvedCells.remove(n)
            cells.remove(n)
        if cells != [] and solvedCells == []:
            lowestNum = []
            lowest = []
            for i in cells:
                lowestNum.append(copy_s[i].lenOfPossible())
            m = min(lowestNum)
            for i in cells:
                if copy_s[i].lenOfPossible() == m:
                    lowest.append(copy_s[i])
            randomChoice = random.choice(lowest)
            randCell = copy_s.index(randomChoice)
            randGuess = random.choice(copy_s[randCell].returnPossible())
            copy_s[randCell].setAnswer(randGuess)
            solvedCells.append(randCell)
            guesses += 1
    if sudokuChecker(copy_s):
        if guesses == 0:
            level = 'Easy'
        elif guesses <= 2:
            level = 'Medium'
        elif guesses <= 7:
            level = 'Hard'
        else:
            level = 'Insane'
        return copy_s, guesses, level
    else:
        return solver(sudoku, f + 1)


def solve(sudoku, n=0):
    """ Uses the solver method to solve a puzzle. This method was built in order to avoid recursion depth errors. Returns True if the puzzle is solvable and
        false if otherwise"""
    if n < 30:
        s = solver(sudoku)
        if s != False:
            return s
        else:
            solve(sudoku, n + 1)
    else:
        return False


def puzzleGen(sudoku):
    """ Generates a puzzle with a unique solution. """
    cells = [i for i in range(81)]
    while cells != []:
        copy_s = copy.deepcopy(sudoku)
        randIndex = random.choice(cells)
        cells.remove(randIndex)
        copy_s[randIndex].reset()
        s = solve(copy_s)
        if s[0] == False:
            f = solve(sudoku)
            print("Guesses: " + str(f[1]))
            print("Level: " + str(f[2]))
            return printSudoku(sudoku)
        elif equalChecker(s[0], solve(copy_s)[0]):
            if equalChecker(s[0], solve(copy_s)[0]):
                sudoku[randIndex].reset()
        else:
            f = solve(sudoku)
            ##            print("Guesses: " + str(f[1]))
            ##            print("Level: " + str(f[2]))
            return sudoku, f[1], f[2]


def equalChecker(s1, s2):
    """ Checks to see if two puzzles are the same"""
    for i in range(len(s1)):
        if s1[i].returnSolved() != s2[i].returnSolved():
            return False
    return True


def main(level):
    """ Input the level of difficulty of the sudoku puzzle. Difficulty levels
        include ‘Easy’ ‘Medium’ ‘Hard’ and ‘Insane’. Outputs a sudoku of desired
        difficulty."""
    t1 = time.time()
    n = 0
    if level == 'Easy':
        p = perfectSudoku()
        s = puzzleGen(p)
        if s[2] != 'Easy':
            return main(level)
        t2 = time.time()
        t3 = t2 - t1
        print("Runtime is " + str(t3) + " seconds")
        print("Guesses: " + str(s[1]))
        print("Level: " + str(s[2]))
        return printSudoku(s[0])
    if level == 'Medium':
        p = perfectSudoku()
        s = puzzleGen(p)
        while s[2] == 'Easy':
            n += 1
            s = puzzleGen(p)
            if n > 50:
                return main(level)
        if s[2] != 'Medium':
            return main(level)
        t2 = time.time()
        t3 = t2 - t1
        print("Runtime is " + str(t3) + " seconds")
        print("Guesses: " + str(s[1]))
        print("Level: " + str(s[2]))
        return printSudoku(s[0])
    if level == 'Hard':
        p = perfectSudoku()
        s = puzzleGen(p)
        while s[2] == 'Easy':
            n += 1
            s = puzzleGen(p)
            if n > 50:
                return main(level)
        while s[2] == 'Medium':
            n += 1
            s = puzzleGen(p)
            if n > 50:
                return main(level)
        if s[2] != 'Hard':
            return main(level)
        t2 = time.time()
        t3 = t2 - t1
        print("Runtime is " + str(t3) + " seconds")
        print("Guesses: " + str(s[1]))
        print("Level: " + str(s[2]))
        return printSudoku(s[0])
    if level == 'Insane':
        p = perfectSudoku()
        s = puzzleGen(p)
        while s[2] != 'Insane':
            n += 1
            s = puzzleGen(p)
            if n > 50:
                return main(level)
        t2 = time.time()
        t3 = t2 - t1
        print("Runtime is " + str(t3) + " seconds")
        print("Guesses: " + str(s[1]))
        print("Level: " + str(s[2]))
        return printSudoku(s[0])
    else:
        raise (ValueError)

app = SudokuApp()
width_value = app.winfo_screenwidth()
height_value = app.winfo_screenheight()
app.geometry("%dx%d+0+0" %(width_value,height_value))
ani = animation.FuncAnimation(f,animate,interval=500)
app.mainloop()