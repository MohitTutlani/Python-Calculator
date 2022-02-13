from tkinter import *
from tkinter import messagebox

#Tkinter layout
window = Tk()
window.geometry("390x415")
window.resizable(0, 0)
window.title("Calculator")

# ---------------------------- Calculator functions ------------------------------- #

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

# 'bt_clear' function :This is used to clear 
# the input field

def bt_clear(): 
    global expression 
    expression = "" 
    input_text.set("")
 
# 'bt_equal':This method calculates the expression 
# present in input field
 
def bt_equal():
    global expression
    if (len(expression) != 0):
        result = str(eval(expression)) # 'eval':This function is used to evaluates the string expression directly
        input_text.set(result)
    else:
        messagebox.showerror(title="Error", message="Please Insert value")
expression = ""
 
# 'StringVar()' :It is used to get the instance of input field
 
input_text = StringVar()
 
# ---------------------------- UI LAYOUT ------------------------------- #

input_frame = Frame(window, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="white", highlightthickness=2)
 
input_frame.pack(side=TOP)
 

input_field = Entry(input_frame, font=('arial', 18, 'bold'),textvariable=input_text, width=50, bg="black", fg="#e8e8e8", bd=0, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=25)
# ---------------------------- Buttons ------------------------------- #
btns_frame = Frame(window, width=312, height=272.5, bg="black")
btns_frame.pack()
 
# first row
# clear
clear = Button(btns_frame, text = "C", fg = "#e8e8e8", width = 32, height = 3, bd = 0, bg = "#a5a5a5", cursor = "hand2", font=("bold"),command = lambda: bt_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
 # divide
divide = Button(btns_frame, text = "÷", fg = "#d6d6d6", width = 10, height = 3, bd = 0, bg = "#fe9505", cursor = "hand2", font=("bold"), command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)
 
# second row
# 7
seven = Button(btns_frame, text = "7", fg = "#d6d6d6", width = 10, height = 3, bd = 0, bg = "#333333", cursor = "hand2", font=("bold"), command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
# 8
eight = Button(btns_frame, text = "8", fg = "#d6d6d6", width = 10, height = 3, bd = 0, bg = "#333333", cursor = "hand2", font=("bold"), command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
# 9
nine = Button(btns_frame, text = "9", fg = "#d6d6d6", width = 10, height = 3, bd = 0, bg = "#333333", cursor = "hand2", font=("bold"), command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
# multiply
multiply = Button(btns_frame, text = "*", fg = "#d6d6d6", width = 10, height = 3, bd = 0, bg = "#fe9505", cursor = "hand2", font=("bold"), command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
 
# third row
 # 4
four = Button(btns_frame, text = "4", fg = "#d6d6d6", width = 10, height = 3, bd = 0, bg = "#333333", cursor = "hand2", font=("bold"), command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
 # 5
five = Button(btns_frame, text = "5", fg = "#d6d6d6", width = 10, height = 3, bd = 0, bg = "#333333", cursor = "hand2", font=("bold"), command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
 # 6
six = Button(btns_frame, text = "6", fg = "#d6d6d6", width = 10, height = 3, bd = 0, bg = "#333333", cursor = "hand2", font=("bold"), command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
 # minus
minus = Button(btns_frame, text = "-", fg = "#d6d6d6", width = 10, height = 3, bd = 0, bg = "#fe9505", cursor = "hand2", font=("bold"), command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
 
# fourth row
 # 1
one = Button(btns_frame, text = "1", fg = "#d6d6d6", width = 10, height = 3, bd = 0, bg = "#333333", cursor = "hand2", font=("bold"), command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
# 2
two = Button(btns_frame, text = "2", fg = "#d6d6d6", width = 10, height = 3, bd = 0, bg = "#333333", cursor = "hand2", font=("bold"), command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
# 3
three = Button(btns_frame, text = "3", fg = "#d6d6d6", width = 10, height = 3, bd = 0, bg = "#333333", cursor = "hand2", font=("bold"), command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
 # plus
plus = Button(btns_frame, text = "+", fg = "#d6d6d6", width = 10, height = 3, bd = 0, bg = "#fe9505", cursor = "hand2", font=("bold"), command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
 
# fifth row
 # 0
zero = Button(btns_frame, text = "0", fg = "#d6d6d6", width = 21, height = 3, bd = 0, bg = "#333333", cursor = "hand2", font=("bold"), command = lambda: btn_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
 # .
point = Button(btns_frame, text = ".", fg = "#d6d6d6", width = 10, height = 3, bd = 0, bg = "#333333", cursor = "hand2", font=("bold"), command = lambda: btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
 # =
equals = Button(btns_frame, text = "=", fg = "#d6d6d6", width = 10, height = 3, bd = 0, bg = "#fe9505", cursor = "hand2", font=("bold"), command = lambda: bt_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)

window.mainloop()
