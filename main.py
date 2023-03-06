from tkinter import *

calc_font = ("Arial", 20, "bold")


def button_click(b_number):
    current = calc_display.cget("text")
    calc_display.configure(text=current + str(b_number))


def calc_compute(to_compute):
    try:
        result = eval(to_compute)
        calc_display.configure(text=str(result))
    except:
        calc_display.configure(text='')


def calc_reset():
    calc_display.configure(text='')


class CalcButton:
    def __init__(self, master, posx, posy, number):
        self.number = number
        self.numericButton = Button(master,
                                    text=number,
                                    height=1,
                                    width=2,
                                    font=calc_font,
                                    command=lambda: button_click(self.number))

        self.numericButton.place(x=posx, y=posy)


root = Tk()
root.title("Calculator")
root.geometry("280x370")
root.configure(background='#f5f5f5')
root.resizable(False, False)


myx = 45
x_value = [myx, myx + 50, myx + 100, myx + 150]
y_value = [100, 160, 220, 280]

# Number Buttons
button1 = CalcButton(root, x_value[0], y_value[0], 7)
button2 = CalcButton(root, x_value[1], y_value[0], 8)
button3 = CalcButton(root, x_value[2], y_value[0], 9)
button4 = CalcButton(root, x_value[0], y_value[1], 4)
button5 = CalcButton(root, x_value[1], y_value[1], 5)
button6 = CalcButton(root, x_value[2], y_value[1], 6)
button7 = CalcButton(root, x_value[0], y_value[2], 1)
button8 = CalcButton(root, x_value[1], y_value[2], 2)
button9 = CalcButton(root, x_value[2], y_value[2], 3)
button0 = CalcButton(root, x_value[1], y_value[3], 0)

# Function Buttons
addition_button = CalcButton(root, x_value[3], y_value[0], "+")
subtraction_button = CalcButton(root, x_value[3], y_value[1], "-")
multiplication_button = CalcButton(root, x_value[3], y_value[2], "*")
division_button = CalcButton(root, x_value[3], y_value[3], "/")

equate_button = Button(root,
                       text="=",
                       height=1,
                       width=2,
                       font=calc_font,
                       command=lambda: calc_compute(calc_display.cget("text")))
equate_button.place(x=x_value[2], y=y_value[3])

reset_button = Button(root,
                      text="C",
                      height=1,
                      width=2,
                      font=calc_font,
                      command=lambda: calc_reset())
reset_button.place(x=x_value[0], y=y_value[3])

calc_display = Label(root, text="", bg='white', height=1, width=11, anchor="e", font=calc_font)
calc_display.place(x=45, y=50)

root.mainloop()
