from tkinter import *
from tkinter import ttk
import tkinter as tk

root = Tk()
root.title("Calculator")
root.geometry("515x615")
root.iconbitmap(default = "calc_icon.ico")

def close_app(): root.destroy()

exit_button = tk.Button(
    root,
    text="⏼",
    borderwidth=0,
    highlightthickness=0,
    bg="#DAD5B9",
    activebackground="#DAD5B9",
    font="helvetica 30",
    command=close_app
)
exit_button.place(height=50, width=50,x=4, y=53)

root.configure(bg='#DAD5B9')

ttk.Style().configure(".",  font="helvetica 18", foreground="#004D40", padding=8, background="#B2DFDB")

math = ttk.Label(font="helvetica 30", background="#C7B599", foreground="#484538", padding=20)
math.place(height=100, width=415, x=60, y=30)

def click_1():
    current_text = math.cget("text")
    math.config(text=current_text + "1")

btn1 = ttk.Button(root, text="1", command=click_1)
btn1.place(height=100, width=100, x=60, y=150)


def click_2():
    current_text = math.cget("text")
    math.config(text=current_text + "2")

btn2 = ttk.Button(text="2", command=click_2)
btn2.place(height=100, width=100, x=165, y=150)


def click_3():
    current_text = math.cget("text")
    math.config(text=current_text + "3")

btn3 = ttk.Button(text="3", command=click_3)
btn3.place(height=100, width=100, x=270, y=150)


def click_plus():
    current_text = math.cget("text")
    math.config(text=current_text + "+")

btn_plus = ttk.Button(text="+", command=click_plus)
btn_plus.place(height=100, width=100, x=375, y=150)


def click_4():
    current_text = math.cget("text")
    math.config(text=current_text + "4")

btn4 = ttk.Button(text="4", command=click_4)
btn4.place(height=100, width=100, x=60, y=255)


def click_5():
    current_text = math.cget("text")
    math.config(text=current_text + "5")

btn5 = ttk.Button(text="5", command=click_5)
btn5.place(height=100, width=100, x=165, y=255)


def click_6():
    current_text = math.cget("text")
    math.config(text=current_text + "6")

btn6 = ttk.Button(text="6", command=click_6)
btn6.place(height=100, width=100, x=270, y=255)


def click_min():
    current_text = math.cget("text")
    math.config(text=current_text + "-")

btn_min = ttk.Button(text="-", command=click_min)
btn_min.place(height=100, width=100, x=375, y=255)


def click_7():
    current_text = math.cget("text")
    math.config(text=current_text + "7")

btn7 = ttk.Button(text="7", command=click_7)
btn7.place(height=100, width=100, x=60, y=360)


def click_8():
    current_text = math.cget("text")
    math.config(text=current_text + "8")

btn8 = ttk.Button(text="8", command=click_8)
btn8.place(height=100, width=100, x=165, y=360)


def click_9():
    current_text = math.cget("text")
    math.config(text=current_text + "9")

btn9 = ttk.Button(text="9", command=click_9)
btn9.place(height=100, width=100, x=270, y=360)


def click_mult():
    current_text = math.cget("text")
    math.config(text=current_text + "×")

btn_mult = ttk.Button(text="×", command=click_mult)
btn_mult.place(height=100, width=100, x=375, y=360)


def click_enter():
    new_text = ""
    current_text = math.cget("text")
    if current_text == "1984":
        print("Старший брат следит за тобой!")
        exit()
    else:
        for i in current_text:
            if i == ":" or "×":
                new_text = current_text.replace(":", "/").replace("×", "*")
                result = eval(new_text)
                return math.config(text=result)
            else:
                result = eval(current_text)
                return math.config(text=result)

btn_enter = ttk.Button(text="=", command=click_enter)
btn_enter.place(height=100, width=100, x=375, y=465)


def click_c():
    current_text = math.cget("text")
    math.config(text="")

btn_del = ttk.Button(text="C", command=click_c)
btn_del.place(height=100, width=100, x=60, y=465)


def click_0():
    current_text = math.cget("text")
    math.config(text=current_text + "0")

btn0 = ttk.Button(text="0", command=click_0)
btn0.place(height=100, width=100, x=165, y=465)


def click_two():
    current_text = math.cget("text")
    math.config(text=current_text + ":")

btn_share = ttk.Button(text=":", command=click_two)
btn_share.place(height=100, width=100, x=270, y=465)

root.mainloop()