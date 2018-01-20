from tkinter import *
import tkinter.messagebox
from hangman import hangman
import sys
import os

class GUIhman():
    def exitGame(self):
        root.destroy()

    root = Tk()
    root.wm_title('Hangman')

    menu = Menu(root)
    root.config(menu=menu)

    subMenu = Menu(menu)
    # Adds a drop down when "File" is clicked
    menu.add_cascade(label="File", menu=subMenu)
    subMenu.add_command(label="New Project...")
    subMenu.add_command(label="Restart")
    subMenu.add_separator()
    subMenu.add_command(label="Exit", command=exitGame)

    instanceGame = hangman('HundingsRage')

    unique_letters = instanceGame.get_unique_letters()
    correct_guesses = []
    incorrect_guesses = 0
    guess_word = instanceGame.update_template(instanceGame.word, correct_guesses)

    def buttonPress(self,guess):
        global unique_letters
        global prompt
        if (guess in unique_letters):
            prompt.set(instanceGame.correct_prompt())

            global correct_guesses
            if (guess not in correct_guesses):
                correct_guesses.append(guess)
        else:
            prompt.set(instanceGame.incorrect_prompt())

            global incorrect_guesses
            incorrect_guesses += 1

        global guess_word
        guess_word = instanceGame.update_template(instanceGame.word, correct_guesses)
        global tv
        tv.set(instanceGame.display(guess_word))
        global ic
        ic.set('Incorrect Guesses: ' + str(incorrect_guesses))
        createHangman()

        if (incorrect_guesses > 5):
            tkinter.messagebox.showinfo('Hangman', 'Game Over! You Lose!')
        elif (winCondition()):
            tkinter.messagebox.showinfo('Hangman', 'Congratulations! You Won!')

    def winCondition(self):
        x = len(unique_letters)
        y = 0
        for i in range(len(correct_guesses)):
            if correct_guesses[i] in unique_letters:
                y += 1

        if (y == x):
            return True
        else:
            return False

    topFrame = Frame(root)
    topFrame.pack()
    canvas = Canvas(topFrame, width=225, height=200)
    canvas.pack()

    def hangman_stand(self):
        stand = []
        stand.append(canvas.create_line(100, 20, 100, 40, width=2))
        stand.append(canvas.create_line(100, 20, 150, 20, width=2))
        stand.append(canvas.create_line(150, 20, 150, 170, width=2))
        stand.append(canvas.create_line(130, 170, 170, 170, width=2))

    hangman_stand(self)

    def createHangman(self):
        global incorrect_guesses
        if (incorrect_guesses == 1):
            head = canvas.create_oval(90, 40, 110, 60, width=2)
        elif (incorrect_guesses == 2):
            body = canvas.create_line(100, 60, 100, 100, width=2)
        elif (incorrect_guesses == 3):
            leftHand = canvas.create_line(100, 70, 80, 80, width=2)
        elif (incorrect_guesses == 3):
            rightHand = canvas.create_line(100, 70, 120, 80, width=2)
        elif (incorrect_guesses == 3):
            leftFeet = canvas.create_line(100, 100, 80, 130, width=2)
        elif (incorrect_guesses == 3):
            rightFeet = canvas.create_line(100, 100, 120, 130, width=2)

    middleFrame = Frame(root, width=225, height=50)

    tv = StringVar()
    tv.set(instanceGame.display(guess_word))
    display = Label(middleFrame, bg='lightblue', textvariable=tv, font=("Helvetica", 14, "bold"))
    display.pack()

    prompt = StringVar()
    prompt.set('Guess A Letter!')
    promptDisplay = Label(middleFrame, textvariable=prompt, font=("Arial", 10))
    promptDisplay.pack()

    ic = StringVar()
    ic.set('Incorrect Guesses: ' + str(incorrect_guesses))
    incorrect = Label(middleFrame, fg='red', textvariable=ic, font=("Helvetica", 10, "bold"))
    incorrect.pack()

    middleFrame.pack()

    bottomFrame = Frame(root, width=225, height=275)
    letters = []
    lettersAtoI = Frame(bottomFrame, width=225, height=90)
    lettersJtoR = Frame(bottomFrame, width=225, height=90)
    lettersStoZ = Frame(bottomFrame, width=225, height=90)

    def renderKeys(self):
        A = (Button(self.lettersAtoI, text='A', fg="cyan", bg='black', width=2, height=1,
                    command=lambda: self.buttonPress(A.cget('text'))))
        A.pack(side=LEFT)

        B = (Button(self.lettersAtoI, text='B', fg="cyan", bg='black', width=2, height=1,
                    command=lambda: self.buttonPress(B.cget('text'))))
        B.pack(side=LEFT)

        C = (Button(self.lettersAtoI, text='C', fg="cyan", bg='black', width=2, height=1,
                    command=lambda: self.buttonPress(C.cget('text'))))
        C.pack(side=LEFT)

        D = (Button(self.lettersAtoI, text='D', fg="cyan", bg='black', width=2, height=1,
                    command=lambda: self.buttonPress(D.cget('text'))))
        D.pack(side=LEFT)

        E = (Button(self.lettersAtoI, text='E', fg="cyan", bg='black', width=2, height=1,
                    command=lambda: self.buttonPress(E.cget('text'))))
        E.pack(side=LEFT)

        F = (Button(self.lettersAtoI, text='F', fg="cyan", bg='black', width=2, height=1,
                    command=lambda: self.buttonPress(F.cget('text'))))
        F.pack(side=LEFT)

        G = (Button(self.lettersAtoI, text='G', fg="cyan", bg='black', width=2, height=1,
                    command=lambda: self.buttonPress(G.cget('text'))))
        G.pack(side=LEFT)

        H = (Button(self.lettersAtoI, text='H', fg="cyan", bg='black', width=2, height=1,
                    command=lambda: self.buttonPress(H.cget('text'))))
        H.pack(side=LEFT)

        I = (Button(self.lettersAtoI, text='I', fg="cyan", bg='black', width=2, height=1,
                    command=lambda: self.buttonPress(I.cget('text'))))
        I.pack(side=LEFT)
        #######################
        J = (Button(self.lettersJtoR, text='J', fg="cyan", bg='black', width=2, height=1,
                    command=lambda: self.buttonPress(J.cget('text'))))
        J.pack(side=LEFT)

        K = (Button(self.lettersJtoR, text='K', fg="cyan", bg='black', width=2, height=1,
                    command=lambda: self.buttonPress(K.cget('text'))))
        K.pack(side=LEFT)

        L = (Button(self.lettersJtoR, text='L', fg="cyan", bg='black', width=2, height=1,
                    command=lambda: self.buttonPress(L.cget('text'))))
        L.pack(side=LEFT)

        M = (Button(self.lettersJtoR, text='M', fg="cyan", bg='black', width=2, height=1,
                    command=lambda: self.buttonPress(M.cget('text'))))
        M.pack(side=LEFT)

        N = (Button(self.lettersJtoR, text='N', fg="cyan", bg='black', width=2, height=1,
                    command=lambda: self.buttonPress(N.cget('text'))))
        N.pack(side=LEFT)

        O = (Button(self.lettersJtoR, text='O', fg="cyan", bg='black', width=2, height=1,
                    command=lambda: self.buttonPress(O.cget('text'))))
        O.pack(side=LEFT)

        P = (Button(self.lettersJtoR, text='P', fg="cyan", bg='black', width=2, height=1,
                    command=lambda: self.buttonPress(P.cget('text'))))
        P.pack(side=LEFT)

        Q = (Button(self.lettersJtoR, text='Q', fg="cyan", bg='black', width=2, height=1,
                    command=lambda: self.buttonPress(Q.cget('text'))))
        Q.pack(side=LEFT)

        R = (Button(self.lettersJtoR, text='R', fg="cyan", bg='black', width=2, height=1,
                    command=lambda: self.buttonPress(R.cget('text'))))
        R.pack(side=LEFT)

        #############################

        S = (Button(self.lettersStoZ, text='S', fg="cyan", bg='black', width=2, height=1,
                    command=lambda: self.buttonPress(S.cget('text'))))
        S.pack(side=LEFT)

        T = (Button(self.lettersStoZ, text='T', fg="cyan", bg='black', width=2, height=1,
                    command=lambda: self.buttonPress(T.cget('text'))))
        T.pack(side=LEFT)

        U = (Button(self.lettersStoZ, text='U', fg="cyan", bg='black', width=2, height=1,
                    command=lambda: self.buttonPress(U.cget('text'))))
        U.pack(side=LEFT)

        V = (Button(self.lettersStoZ, text='V', fg="cyan", bg='black', width=2, height=1,
                    command=lambda: self.buttonPress(V.cget('text'))))
        V.pack(side=LEFT)

        W = (Button(self.lettersStoZ, text='W', fg="cyan", bg='black', width=2, height=1,
                    command=lambda: self.buttonPress(W.cget('text'))))
        W.pack(side=LEFT)

        X = (Button(self.lettersStoZ, text='X', fg="cyan", bg='black', width=2, height=1,
                    command=lambda: self.buttonPress(X.cget('text'))))
        X.pack(side=LEFT)

        Y = (Button(self.lettersStoZ, text='Y', fg="cyan", bg='black', width=2, height=1,
                    command=lambda: self.buttonPress(Y.cget('text'))))
        Y.pack(side=LEFT)

        Z = (Button(self.lettersStoZ, text='Z', fg="cyan", bg='black', width=2, height=1,
                    command=lambda: self.buttonPress(Z.cget('text'))))
        Z.pack(side=LEFT)

        self.lettersAtoI.grid(row=0)
        self.lettersJtoR.grid(row=1)
        self.lettersStoZ.grid(row=2)

    renderKeys()
    bottomFrame.pack(side=BOTTOM, padx=5, pady=5)

    root.mainloop()

