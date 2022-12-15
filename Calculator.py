from tkinter import *

class Theme:
    fore = "#ffffff"
    btnColor = "#0a0b0d"
    bgColor = "#1b1b21"
    colorHover = "#131417"
    actColor = "#131420"
    opColor = "#0c0f14"

class Btn:
    height = 3
    width = 7

    def onChange(btn, colorE, colorL):
        btn.bind("<Enter>", func = lambda e : btn.config(background = colorE))
        btn.bind("<Leave>", func = lambda e : btn.config(background = colorL))
        

class Main:
    def __init__(self, root):
        root.title("Calculator")
        root.geometry("320x450+100+100")
        root.resizable(0, 0)
        root.config(bg = "#1b1b21")

        inputFrame = Frame(root, background = Theme.bgColor)
        inputFrame.place(x = 0, y = 5)

        inputLabel = Label(
            inputFrame,
            width = 36,
            height = 2,
            font = ("arial", 12),
            background = "#131417",
            foreground = "#ffffff"
        )
        inputLabel.pack()

        outputLabel = Label(
            inputFrame,
            width = 32,
            height = 2,
            font = ("arial", 12, "bold"),
            background = "#131417",
            foreground = "#ffffff"
        )
        outputLabel.pack()
        
        btnGrid = Frame(root, width = 320, height = 360, background = Theme.bgColor)
        btnGrid.place(x = 0, y = 95)

        #buttons

        Main.txt = ""

        def clickAC():
            if(Main.txt == ""):
                outputLabel.config(text = "")
                outputLabel.config(text = Main.txt)
            else:
                Main.txt = ""
                inputLabel.config(text = Main.txt)
                outputLabel.config(text = Main.txt)
        btnAC = Button(
            btnGrid,
            text = "AC",
            height = Btn.height,
            width = Btn.width,
            border = 0,
            activebackground = Theme.actColor,
            activeforeground = "#ff0000",
            background = "#4d0b0b",
            foreground = Theme.fore,
            font = ("arial", 12, "bold"),
            command = clickAC
        )
        btnAC.grid(row = 0, column = 0, padx = 2, pady = 2)
        Btn.onChange(btnAC, "#630f0f", "#4d0b0b")

        def clickC():
            length = len(Main.txt)
            if(length > 0):
                Main.txt = Main.txt[0:length - 1]
            else:
                Main.txt = ""
            inputLabel.config(text = Main.txt)
        btnC = Button(
            btnGrid,
            text = "C",
            height = Btn.height,
            width = Btn.width,
            border = 0,
            activebackground = Theme.actColor,
            activeforeground = "#ff0033",
            background = "#4d0b0b",
            foreground = Theme.fore,
            font = ("arial", 12, "bold"),
            command = clickC
        )
        btnC.grid(row = 0, column = 1, padx = 2, pady = 2)
        Btn.onChange(btnC, "#630f0f", "#4d0b0b")

        def clickOpenBr():
            Main.txt += "("
            inputLabel.config(text = Main.txt)
        btnOpenBr = Button(
            btnGrid,
            text = "(",
            height = Btn.height,
            width = Btn.width,
            border = 0,
            activebackground = Theme.actColor,
            activeforeground = "#ffffff",
            background = Theme.opColor,
            foreground = Theme.fore,
            font = ("arial", 12, "bold"),
            command = clickOpenBr
        )
        btnOpenBr.grid(row = 0, column = 2, padx = 2, pady = 2)
        Btn.onChange(btnOpenBr, Theme.colorHover, Theme.opColor)

        def clickCloseBr():
            Main.txt += ")"
            inputLabel.config(text = Main.txt)
        btnCloseBr = Button(
            btnGrid,
            text = ")",
            height = Btn.height,
            width = Btn.width,
            border = 0,
            activebackground = Theme.actColor,
            activeforeground = "#ffffff",
            background = Theme.opColor,
            foreground = Theme.fore,
            font = ("arial", 12, "bold"),
            command = clickCloseBr
        )
        btnCloseBr.grid(row = 0, column = 3, padx = 2, pady = 2)
        Btn.onChange(btnCloseBr, Theme.colorHover, Theme.opColor)

        def click7():
            Main.txt += "7"
            inputLabel.config(text = Main.txt)
        btn7 = Button(
            btnGrid,
            text = "7",
            height = Btn.height,
            width = Btn.width,
            border = 0,
            activebackground = Theme.actColor,
            activeforeground = "#ffffff",
            background = Theme.btnColor,
            foreground = Theme.fore,
            font = ("arial", 12, "bold"),
            command = click7
        )
        btn7.grid(row = 1, column = 0, padx = 2, pady = 2)
        Btn.onChange(btn7, Theme.colorHover, Theme.btnColor)

        def click8():
            Main.txt += "8"
            inputLabel.config(text = Main.txt)
        btn8 = Button(
            btnGrid,
            text = "8",
            height = Btn.height,
            width = Btn.width,
            border = 0,
            activebackground = Theme.actColor,
            activeforeground = "#ffffff",
            background = Theme.btnColor,
            foreground = Theme.fore,
            font = ("arial", 12, "bold"),
            command = click8
        )
        btn8.grid(row = 1, column = 1, padx = 2, pady = 2)
        Btn.onChange(btn8, Theme.colorHover, Theme.btnColor)

        def click9():
            Main.txt += "9"
            inputLabel.config(text = Main.txt)
        btn9 = Button(
            btnGrid,
            text = "9",
            height = Btn.height,
            width = Btn.width,
            border = 0,
            activebackground = Theme.actColor,
            activeforeground = "#ffffff",
            background = Theme.btnColor,
            foreground = Theme.fore,
            font = ("arial", 12, "bold"),
            command = click9
        )
        btn9.grid(row = 1, column = 2, padx = 2, pady = 2)
        Btn.onChange(btn9, Theme.colorHover, Theme.btnColor)

        def clickDiv():
            Main.txt += "/"
            inputLabel.config(text = Main.txt)
        btnDiv = Button(
            btnGrid,
            text = "/",
            height = Btn.height,
            width = Btn.width,
            border = 0,
            activebackground = Theme.actColor,
            activeforeground = "#ffffff",
            background = Theme.opColor,
            foreground = Theme.fore,
            font = ("arial", 12, "bold"),
            command = clickDiv
        )
        btnDiv.grid(row = 1, column = 3, padx = 2, pady = 2)
        Btn.onChange(btnDiv, Theme.colorHover, Theme.opColor)

        def click4():
            Main.txt += "4"
            inputLabel.config(text = Main.txt)
        btn4 = Button(
            btnGrid,
            text = "4",
            height = Btn.height,
            width = Btn.width,
            border = 0,
            activebackground = Theme.actColor,
            activeforeground = "#ffffff",
            background = Theme.btnColor,
            foreground = Theme.fore,
            font = ("arial", 12, "bold"),
            command = click4
        )
        btn4.grid(row = 2, column = 0, padx = 2, pady = 2)
        Btn.onChange(btn4, Theme.colorHover, Theme.btnColor)

        def click5():
            Main.txt += "5"
            inputLabel.config(text = Main.txt)
        btn5 = Button(
            btnGrid,
            text = "5",
            height = Btn.height,
            width = Btn.width,
            border = 0,
            activebackground = Theme.actColor,
            activeforeground = "#ffffff",
            background = Theme.btnColor,
            foreground = Theme.fore,
            font = ("arial", 12, "bold"),
            command = click5
        )
        btn5.grid(row = 2, column = 1, padx = 2, pady = 2)
        Btn.onChange(btn5, Theme.colorHover, Theme.btnColor)

        def click6():
            Main.txt += "6"
            inputLabel.config(text = Main.txt)
        btn6 = Button(
            btnGrid,
            text = "6",
            height = Btn.height,
            width = Btn.width,
            border = 0,
            activebackground = Theme.actColor,
            activeforeground = "#ffffff",
            background = Theme.btnColor,
            foreground = Theme.fore,
            font = ("arial", 12, "bold"),
            command = click6
        )
        btn6.grid(row = 2, column = 2, padx = 2, pady = 2)
        Btn.onChange(btn6, Theme.colorHover, Theme.btnColor)

        def clickMul():
            Main.txt += "*"
            inputLabel.config(text = Main.txt)
        btnMul = Button(
            btnGrid,
            text = "*",
            height = Btn.height,
            width = Btn.width,
            border = 0,
            activebackground = Theme.actColor,
            activeforeground = "#ffffff",
            background = Theme.opColor,
            foreground = Theme.fore,
            font = ("arial", 12, "bold"),
            command = clickMul
        )
        btnMul.grid(row = 2, column = 3, padx = 2, pady = 2)
        Btn.onChange(btnMul, Theme.colorHover, Theme.opColor)

        def click1():
            Main.txt += "1"
            inputLabel.config(text = Main.txt)
        btn1 = Button(
            btnGrid,
            text = "1",
            height = Btn.height,
            width = Btn.width,
            border = 0,
            activebackground = Theme.actColor,
            activeforeground = "#ffffff",
            background = Theme.btnColor,
            foreground = Theme.fore,
            font = ("arial", 12, "bold"),
            command = click1
        )
        btn1.grid(row = 3, column = 0, padx = 2, pady = 2)
        Btn.onChange(btn1, Theme.colorHover, Theme.btnColor)

        def click2():
            Main.txt += "2"
            inputLabel.config(text = Main.txt)
        btn2 = Button(
            btnGrid,
            text = "2",
            height = Btn.height,
            width = Btn.width,
            border = 0,
            activebackground = Theme.actColor,
            activeforeground = "#ffffff",
            background = Theme.btnColor,
            foreground = Theme.fore,
            font = ("arial", 12, "bold"),
            command = click2
        )
        btn2.grid(row = 3, column = 1, padx = 2, pady = 2)
        Btn.onChange(btn2, Theme.colorHover, Theme.btnColor)

        def click3():
            Main.txt += "3"
            inputLabel.config(text = Main.txt)
        btn3 = Button(
            btnGrid,
            text = "3",
            height = Btn.height,
            width = Btn.width,
            border = 0,
            activebackground = Theme.actColor,
            activeforeground = "#ffffff",
            background = Theme.btnColor,
            foreground = Theme.fore,
            font = ("arial", 12, "bold"),
            command = click3
        )
        btn3.grid(row = 3, column = 2, padx = 2, pady = 2)
        Btn.onChange(btn3, Theme.colorHover, Theme.btnColor)

        def clickAdd():
            Main.txt += "+"
            inputLabel.config(text = Main.txt)
        btnAdd = Button(
            btnGrid,
            text = "+",
            height = Btn.height,
            width = Btn.width,
            border = 0,
            activebackground = Theme.actColor,
            activeforeground = "#ffffff",
            background = Theme.opColor,
            foreground = Theme.fore,
            font = ("arial", 12, "bold"),
            command = clickAdd
        )
        btnAdd.grid(row = 3, column = 3, padx = 2, pady = 2)
        Btn.onChange(btnAdd, Theme.colorHover, Theme.opColor)

        def clickDot():
            Main.txt += "."
            inputLabel.config(text = Main.txt)
        btnDot = Button(
            btnGrid,
            text = ".",
            height = Btn.height,
            width = Btn.width,
            border = 0,
            activebackground = Theme.actColor,
            activeforeground = "#ffffff",
            background = Theme.btnColor,
            foreground = Theme.fore,
            font = ("arial", 12, "bold"),
            command = clickDot
        )
        btnDot.grid(row = 4, column = 0, padx = 2, pady = 2)
        Btn.onChange(btnDot, Theme.colorHover, Theme.btnColor)

        def click0():
            Main.txt += "0"
            inputLabel.config(text = Main.txt)
        btn0 = Button(
            btnGrid,
            text = "0",
            height = Btn.height,
            width = Btn.width,
            border = 0,
            activebackground = Theme.actColor,
            activeforeground = "#ffffff",
            background = Theme.btnColor,
            foreground = Theme.fore,
            font = ("arial", 12, "bold"),
            command = click0
        )
        btn0.grid(row = 4, column = 1, padx = 2, pady = 2)
        Btn.onChange(btn0, Theme.colorHover, Theme.btnColor)

        def clickEqu():
            total = eval(Main.txt)
            total = "{:,}".format(total)
            outputLabel.config(text = total)
        btnEqu = Button(
            btnGrid,
            text = "=",
            height = Btn.height,
            width = Btn.width,
            border = 0,
            activebackground = Theme.actColor,
            activeforeground = "#ffffff",
            background = "#0a0a24",
            foreground = Theme.fore,
            font = ("arial", 12, "bold"),
            command = clickEqu
        )
        btnEqu.grid(row = 4, column = 2, padx = 2, pady = 2)
        Btn.onChange(btnEqu, Theme.colorHover, "#0a0a24")

        def clickSub():
            Main.txt += "-"
            inputLabel.config(text = Main.txt)
        btnSub = Button(
            btnGrid,
            text = "-",
            height = Btn.height,
            width = Btn.width,
            border = 0,
            activebackground = Theme.actColor,
            activeforeground = "#ffffff",
            background = Theme.opColor,
            foreground = Theme.fore,
            font = ("arial", 12, "bold"),
            command = clickSub
        )
        btnSub.grid(row = 4, column = 3, padx = 2, pady = 2)
        Btn.onChange(btnSub, Theme.colorHover, Theme.opColor)

window = Tk()
myApp = Main(window)
window.mainloop()