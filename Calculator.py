from tkinter import *
import math
import tkinter.font as font
from tkmacosx import Button

root = Tk()
root.title("Scientific  Calculator - CVM")
root.geometry("575x475")

entered_value = Entry(root, font=("Times New Roman",  25), width = 43, borderwidth = 5, justify=RIGHT)
entered_value.pack()
entered_value.grid(row = 0, column = 0, columnspan = 43, padx = 0, pady = 20)

def button_click(number):
    
    current = entered_value.get()
    if current == str(math.pi) or current == str(math.e):
        entered_value.delete(0, END)
        entered_value.insert(0, "Error")
    elif current == "Error":
        entered_value.delete(0, END)
        entered_value.insert(0, str(number))
    elif current == "= ∞":
        entered_value.delete(0, END)
        entered_value.insert(0, str(number))
    elif current.startswith("= ") and current[-1].isdigit() and\
        "+"  not in current and "–"not in current and\
        "×" not in current and "÷" not in current and\
        "(" not in current and ")" not in current and "^" not in current or 'e+' in current or 'e-' in current:
        entered_value.delete(0, END)
        entered_value.insert(0, str(number))
    else:
        entered_value.delete(0, END)
        entered_value.insert(0, str(current) + str(number))


def button_allclear():
    
    try:
        entered_value.delete(0, END)
    except IndexError:
        pass


def button_clear():
    
    try:
        current = entered_value.get()
        entered_value.delete(0, END)
        if current.endswith("+ ") or current.endswith("– ") or current.endswith("× ") or current.endswith("÷ ") or current.endswith("( ") or current.endswith(") "):
            current = current.rstrip(current[-1 : -3 : -1][: : -1])
        elif current.startswith("= ") and current.lstrip("= ").isdigit() or 'e+' in current or 'e-' in current:
            current = ''
        elif current == 'Error':
            current = ''
        else:
            current = current[:-1]
        entered_value.insert(0, str(current))
    except IndexError:
        pass

    
def button_plus():
    
    try:
        current = entered_value.get()
        if current.endswith(" – "):
            current = current.rstrip(" – ")
            entered_value.delete(0, END)
            entered_value.insert(0, str(current) + " + ")
        elif current.endswith(" × "):
            current = current.rstrip(" × ")
            entered_value.delete(0, END)
            entered_value.insert(0, str(current) + " + ")
        elif current.endswith(" ÷ "):
            current = current.rstrip(" ÷ ")
            entered_value.delete(0, END)
            entered_value.insert(0, str(current) + " + ")
        elif current.endswith(" ^ "):
            current = current.rstrip(" ^ ")
            entered_value.delete(0, END)
            entered_value.insert(0, str(current) + " + ")
        elif current.endswith(" + "):
            current = current.rstrip(" + ")
            entered_value.delete(0, END)
            entered_value.insert(0, str(current) + " + ")
        else:
            entered_value.delete(0, END)
            entered_value.insert(0, str(current) + " + ")
    except ValueError:
        entered_value.insert(0, "Error")


def button_minus():
    
    try:
        current = entered_value.get()
        if current.endswith(" + "):
            current = current.rstrip(" + ")
            entered_value.delete(0, END)
            entered_value.insert(0, str(current) + " – ")
        elif current.endswith(" × "):
            current = current.rstrip(" × ")
            entered_value.delete(0, END)
            entered_value.insert(0, str(current) + " – ")
        elif current.endswith(" ÷ "):
            current = current.rstrip(" ÷ ")
            entered_value.delete(0, END)
            entered_value.insert(0, str(current) + " – ")
        elif current.endswith(" ^ "):
            current = current.rstrip(" ^ ")
            entered_value.delete(0, END)
            entered_value.insert(0, str(current) + " – ")
        elif current.endswith(" – "):
            current = current.rstrip(" – ")
            entered_value.delete(0, END)
            entered_value.insert(0, str(current) + " – ")
        else:
            entered_value.delete(0, END)
            entered_value.insert(0, str(current) + " – ")
    except ValueError:
        entered_value.insert(0, "Error")


def button_multiply():
    
    try:
        current = entered_value.get()
        if current.endswith(" + "):
            current = current.rstrip(" + ")
            entered_value.delete(0, END)
            entered_value.insert(0, str(current) + " × ")
        elif current.endswith(" – "):
            current = current.rstrip(" – ")
            entered_value.delete(0, END)
            entered_value.insert(0, str(current) + " × ")
        elif current.endswith(" ÷ "):
            current = current.rstrip(" ÷ ")
            entered_value.delete(0, END)
            entered_value.insert(0, str(current) + " × ")
        elif current.endswith(" ^ "):
            current = current.rstrip(" ^ ")
            entered_value.delete(0, END)
            entered_value.insert(0, str(current) + " × ")
        elif current.endswith(" × "):
            current = current.rstrip(" × ")
            entered_value.delete(0, END)
            entered_value.insert(0, str(current) + " × ")
        else:
            entered_value.delete(0, END)
            entered_value.insert(0, str(current) + " × ")
    except ValueError:
        entered_value.insert(0, "Error")


def button_divide():
    
    try:
        current = entered_value.get()
        if current.endswith(" + "):
            current = current.rstrip(" + ")
            entered_value.delete(0, END)
            entered_value.insert(0, str(current) + " ÷ ")
        elif current.endswith(" – "):
            current = current.rstrip(" – ")
            entered_value.delete(0, END)
            entered_value.insert(0, str(current) + " ÷ ")
        elif current.endswith(" × "):
            current = current.rstrip(" × ")
            entered_value.delete(0, END)
            entered_value.insert(0, str(current) + " ÷ ")
        elif current.endswith(" ^ "):
            current = current.rstrip(" ^ ")
            entered_value.delete(0, END)
            entered_value.insert(0, str(current) + " ÷ ")
        elif current.endswith(" ÷ "):
            current = current.rstrip(" ÷ ")
            entered_value.delete(0, END)
            entered_value.insert(0, str(current) + " ÷ ")
        else:
            entered_value.delete(0, END)
            entered_value.insert(0, str(current) + " ÷ ")
    except ValueError:
        entered_value.insert(0, "Error")


def button_equal():
    
    try:
        current = entered_value.get()
        current = current.lstrip("= ")
        entered_value.delete(0, END)
        current = current.replace(r" ^ ", " ** ")
        current = current.replace(r" – ", " - ")
        current = current.replace(r" × ", " * ")
        current = current.replace(r" ÷ ", " / ")

        value = eval(current)
        if str(value).endswith(".0"):
            entered_value.insert(0, "= " + str(int(value)))
        elif  len(str(value)) > 30:
            entered_value.insert(0, "= " + str(value)[0] + "." + str(value)[1:17] + "e+" + str(len(str(value)[17:]) + 16))
        else:
            entered_value.insert(0, "= " + str(value))
    except SyntaxError:
        entered_value.insert(0, "Error")
    except ZeroDivisionError:
        entered_value.insert(0, "Error")
    except TypeError:
        entered_value.insert(0, "Error")
    except ValueError:
        entered_value.insert(0, "= " + "∞")
    except OverflowError:
        entered_value.insert(0, "= " + "∞")


def button_leftbrk():
    
    current = entered_value.get()
    entered_value.delete(0, END)
    entered_value.insert(0, str(current) + " (")


def button_rightbrk():
    
    current = entered_value.get()
    entered_value.delete(0, END)
    entered_value.insert(0, str(current) + ") ")


def button_percent():
    
    try:
        current = entered_value.get()
        current = current.lstrip("= ")
        entered_value.delete(0, END)
        entered_value.insert(0, "= " + str(float(current) / 100))
    except ValueError:
        entered_value.insert(0, "Error")


def button_dot():
    
    current = entered_value.get()
    if current.endswith("."):
        entered_value.delete(0, END)
        entered_value.insert(0, str(current))
    else:
        entered_value.delete(0, END)
        entered_value.insert(0, str(current) + ".")


def button_fact():
    
    try:
        current = entered_value.get()
        current = current.lstrip("= ")
        entered_value.delete(0, END)
        entered_value.insert(0, "= " + str(math.factorial(int(current))))
    except ValueError:
        entered_value.insert(0, "Error")
    except OverflowError:
        entered_value.insert(0, "= " + "∞")
        

def button_sin(buttonsin, buttondeg):

    if buttondeg['text'] == 'deg' and buttonsin['text'] != 'sin⁻¹':
        try:
            current = entered_value.get()
            current = current.lstrip("= ")
            entered_value.delete(0, END)
            if math.sin(math.radians(float(current))) == 0.0:
                entered_value.insert(0, "= " + '0')
            elif math.sin(math.radians(float(current))) == 1.0:
                entered_value.insert(0, "= " + '1')
            elif math.sin(math.radians(float(current))) == 0.49999999999999994:
                entered_value.insert(0, "= " + '0.5')
            else:
                entered_value.insert(0, "= " + str(math.sin(math.radians(float(current)))))
        except ValueError:
            entered_value.insert(0, "Error")
    elif buttonsin['text'] == 'sin⁻¹':
        try:
            current = entered_value.get()
            current = current.lstrip("= ")
            entered_value.delete(0, END)
            if math.degrees(math.asin(float(current))) == 29.999999999999996:
                entered_value.insert(0, "= " + '30')
            elif math.degrees(math.asin(float(current))) == 59.99999999999999:
                entered_value.insert(0, "= " + '60')
            elif math.degrees(math.asin(float(current))) == 44.99999999999999:
                entered_value.insert(0, "= " + '45')
            else:
                entered_value.insert(0, "= " + str(int(math.degrees(math.asin(float(current))))))
        except ValueError:
            entered_value.insert(0, "Error")
    else:
        try:
            current = entered_value.get()
            current = current.lstrip("= ")
            entered_value.delete(0, END)
            entered_value.insert(0, "= " + str(math.sin((float(current)))))
        except ValueError:
            entered_value.insert(0, "Error")


def button_cos(buttoncos, buttondeg):
    
    if buttondeg['text'] == 'deg' and buttoncos['text'] != 'cos⁻¹':
        try:
            current = entered_value.get()
            current = current.lstrip("= ")
            entered_value.delete(0, END)
            if math.cos(math.radians(float(current))) == 6.123233995736766e-17:
                entered_value.insert(0, "= " + '0')
            elif math.cos(math.radians(float(current))) == 1.0:
                entered_value.insert(0, "= " + '1')
            elif math.cos(math.radians(float(current))) == 0.5000000000000001:
                entered_value.insert(0, "= " + '0.5')
            else:    
                entered_value.insert(0, "= " + str(math.cos(math.radians(float(current)))))
        except ValueError:
            entered_value.insert(0, "Error")
    elif buttoncos['text'] == 'cos⁻¹':
        try:
            current = entered_value.get()
            current = current.lstrip("= ")
            entered_value.delete(0, END)
            entered_value.insert(0, "= " + str(int(math.degrees(math.acos(float(current))))))
        except ValueError:
            entered_value.insert(0, "Error")
    else:
        try:
            current = entered_value.get()
            current = current.lstrip("= ")
            entered_value.delete(0, END)
            entered_value.insert(0, "= " + str(math.cos((float(current)))))
        except ValueError:
            entered_value.insert(0, "Error")


def button_tan(buttontan, buttondeg):

    if buttondeg['text'] == 'deg' and buttontan['text'] != 'tan⁻¹':
        try:
            current = entered_value.get()
            current = current.lstrip("= ")
            entered_value.delete(0, END)
            if math.tan(math.radians(float(current))) == 0.0:
                entered_value.insert(0, "= " + '0')
            elif math.tan(math.radians(float(current))) == 0.9999999999999999:
                entered_value.insert(0, "= " + '1')
            elif math.tan(math.radians(float(current))) == 16331239353195370.0:
                entered_value.insert(0, "= " + '∞')
            else:
                entered_value.insert(0, "= " + str(math.tan(math.radians(float(current)))))
        except ValueError:
            entered_value.insert(0, "Error")
    elif buttontan['text'] == 'tan⁻¹':
        try:
            current = entered_value.get()
            current = current.lstrip("= ")
            entered_value.delete(0, END)
            entered_value.insert(0, "= " + str(int(math.degrees(math.atan(float(current))))))
        except ValueError:
            entered_value.insert(0, "Error")
    else:
        try:
            current = entered_value.get()
            current = current.lstrip("= ")
            entered_value.delete(0, END)
            entered_value.insert(0, "= " + str(math.tan((float(current)))))
        except ValueError:
            entered_value.insert(0, "Error")


def button_root():
    
    try:
        current = entered_value.get()
        current = current.lstrip("= ")
        entered_value.delete(0, END)
        entered_value.insert(0, "= " + str(math.sqrt(float(current))))
    except ValueError:
        entered_value.insert(0, "Error")

        
def button_e():
    
    current = entered_value.get()
    if "+"  not in current and "–"not in current and\
        "×" not in current and "÷" not in current and\
        "(" not in current and ")" not in current and "^" not in current\
        and current != '':
        entered_value.delete(0, END)
        entered_value.insert(0, "Error")
    else:
        current = current.lstrip("= ")
        entered_value.delete(0, END)
        entered_value.insert(0, "= " + str(current) + str(math.e))


def button_pi():
    
    current = entered_value.get()
    if  "+"  not in current and "–"not in current and\
        "×" not in current and "÷" not in current and\
        "(" not in current and ")" not in current and "^" not in current\
        and current != '':
        entered_value.delete(0, END)
        entered_value.insert(0, "Error")
    else:
        current = current.lstrip("= ")
        entered_value.delete(0, END)
        entered_value.insert(0, "= " + str(current) + str(math.pi))


def button_inverse():
    
    try:
        current = entered_value.get()
        current = current.lstrip("= ")
        entered_value.delete(0, END)
        value = 1 / float(current)
        if str(value).endswith(".0"):
            entered_value.insert(0, "= " + str(int(value)))
        else:
            entered_value.insert(0, "= " + str(value))
    except ZeroDivisionError:
        entered_value.insert(0, "Error")
    except ValueError:
        entered_value.insert(0, "Error")


def button_log():
    
    try:
        current = entered_value.get()
        current = current.lstrip("= ")
        entered_value.delete(0, END)
        value = math.log10(float(current))
        if str(value).endswith(".0"):
            entered_value.insert(0, "= " + str(int(value)))
        else:
            entered_value.insert(0, "= " + str(value))
    except ValueError:
        entered_value.insert(0, "Error")


def button_ln():
    
    try:
        current = entered_value.get()
        current = current.lstrip("= ")
        entered_value.delete(0, END)
        value = math.log(float(current))
        if str(value).endswith(".0"):
            entered_value.insert(0, "= " + str(int(value)))
        else:
            entered_value.insert(0, "= " + str(value))
    except ValueError:
        entered_value.insert(0, "Error")


def button_pow():
    
    try:
        current = entered_value.get()
        current = entered_value.get()
        if current.endswith(" – "):
            current = current.rstrip(" – ")
            entered_value.delete(0, END)
            entered_value.insert(0, str(current) + " ^ ")
        elif current.endswith(" × "):
            current = current.rstrip(" × ")
            entered_value.delete(0, END)
            entered_value.insert(0, str(current) + " ^ ")
        elif current.endswith(" ÷ "):
            current = current.rstrip(" ÷ ")
            entered_value.delete(0, END)
            entered_value.insert(0, str(current) + " ^ ")
        elif current.endswith(" + "):
            current = current.rstrip(" + ")
            entered_value.delete(0, END)
            entered_value.insert(0, str(current) + " ^ ")
        elif current.endswith(" ^ "):
            current = current.rstrip(" ^ ")
            entered_value.delete(0, END)
            entered_value.insert(0, str(current) + " ^ ")
        else:
            entered_value.delete(0, END)
            entered_value.insert(0, str(current) + " ^ ")
    except ValueError:
        entered_value.insert(0, "Error")


def button_pow2():
    
    try:
        current = entered_value.get()
        current = current.lstrip("= ")
        entered_value.delete(0, END)
        value = float(str(current)) ** 2
        if str(value).endswith(".0"):
            entered_value.insert(0, "= " + str(int(value)))
        else:
            entered_value.insert(0, "= " + str(value))
    except ValueError:
        entered_value.insert(0, "Error")


def button_2nd(buttondeg, buttonsin, buttoncos, buttontan):

    if buttondeg["state"] == "normal":
        buttonsin["text"] = "sin⁻¹"
        buttoncos["text"] = "cos⁻¹"
        buttontan["text"] = "tan⁻¹"
        buttondeg.config(state = DISABLED)
    elif buttondeg["state"] == "disabled":
        buttonsin["text"] = "sin"
        buttoncos["text"] = "cos"
        buttontan["text"] = "tan"
        buttondeg.config(state = NORMAL)


def button_deg():

    if buttondeg["text"] == "deg":
        buttondeg["text"] = "rad"
    else:
        buttondeg["text"] = "deg"
        

button2nd = Button(root, text = "→", padx = 10, pady = 15, command = lambda : button_2nd(buttondeg, buttonsin, buttoncos, buttontan), bg = "#ffffff")
buttondeg = Button(root, text = "deg", padx = 10, pady = 15, command = lambda : button_deg(), bg = "#ffffff")
buttonsin = Button(root, text = "sin", padx = 10, pady = 15, command = lambda : button_sin(buttonsin, buttondeg), bg = "#ffffff")
buttoncos = Button(root, text = "cos", padx = 10, pady = 15, command = lambda : button_cos(buttoncos, buttondeg), bg = "#ffffff")
buttontan = Button(root, text = "tan", padx = 10, pady = 15, command = lambda : button_tan(buttontan, buttondeg), bg = "#ffffff")

buttonpow2 = Button(root, text = "x²", padx = 10, pady = 15, command = lambda : button_pow2(), bg = "#ffffff")
buttonlog = Button(root, text = "log", padx = 10, pady = 15, command = lambda : button_log(), bg = "#ffffff")
buttonln = Button(root, text = "ln", padx = 10, pady = 15, command = lambda : button_ln(), bg = "#ffffff")
buttonleftbrk = Button(root, text = "(", padx = 10, pady = 15, command = lambda : button_leftbrk(), bg = "#ffffff")
buttonrightbrk = Button(root, text = ")", padx = 10, pady = 15, command = lambda : button_rightbrk(), bg = "#ffffff")

buttonpow = Button(root, text = "xʸ", padx = 10, pady = 15, command = lambda : button_pow(), bg = "#ffffff")
buttonallclear = Button(root, text = "AC", padx = 10, pady = 15, command = lambda : button_allclear(), fg = "#ec7600", bg = "#ffffff")
buttonclear = Button(root, text = "C", padx = 10, pady = 15, command = lambda : button_clear(), fg = "#ec7600", bg = "#ffffff")
buttonpercent = Button(root, text = r"%", padx = 10, pady = 15, command = lambda : button_percent(), fg = "#ec7600", bg = "#ffffff")
buttondivide = Button(root, text = "÷", padx = 10, pady = 15, command = lambda : button_divide(), fg = "#ec7600", bg = "#ffffff")

buttonroot = Button(root, text = r"√x", padx = 10, pady = 15, command = lambda : button_root(), bg = "#ffffff")
button7 = Button(root, text = "7", padx = 10, pady = 15, command = lambda : button_click(7), bg = "#ffffff")
button8 = Button(root, text = "8", padx = 10, pady = 15, command = lambda : button_click(8), bg = "#ffffff")
button9 = Button(root, text = "9", padx = 10, pady = 15, command = lambda : button_click(9), bg = "#ffffff")
buttonmultiply = Button(root, text = r"⛌", padx = 10, pady = 15, command = lambda : button_multiply(), fg = "#ec7600", bg = "#ffffff")

buttonfact = Button(root, text = r"x!", padx = 10, pady = 15, command = lambda : button_fact(), bg = "#ffffff")
button4 = Button(root, text = "4", padx = 10, pady = 15, command = lambda : button_click(4), bg = "#ffffff")
button5 = Button(root, text = "5", padx = 10, pady = 15, command = lambda : button_click(5), bg = "#ffffff")
button6 = Button(root, text = "6", padx = 10, pady = 15, command = lambda : button_click(6), bg = "#ffffff")
buttonminus = Button(root, text = r"–", padx = 10, pady = 15, command = lambda : button_minus(), fg = "#ec7600", bg = "#ffffff")

buttoninverse = Button(root, text = r"1/x", padx = 10, pady = 15, command = lambda : button_inverse(), bg = "#ffffff")
button1 = Button(root, text = "1", padx = 10, pady = 15, command = lambda : button_click(1), bg = "#ffffff")
button2 = Button(root, text = "2", padx = 10, pady = 15, command = lambda : button_click(2), bg = "#ffffff")
button3 = Button(root, text = "3", padx = 10, pady = 15, command = lambda : button_click(3), bg = "#ffffff")
buttonplus = Button(root, text = "+", padx = 10, pady = 15, command = lambda : button_plus(), fg = "#ec7600", bg = "#ffffff")

buttonpi = Button(root, text = "π", padx = 10, pady = 15, command = lambda : button_pi(), bg = "#ffffff")
buttone = Button(root, text = "e", padx = 10, pady = 15, command = lambda : button_e(), bg = "#ffffff")
button0 = Button(root, text = "0", padx = 10, pady = 15, command = lambda : button_click(0), bg = "#ffffff")
buttondot = Button(root, text = r"•", padx = 10, pady = 15, command = lambda : button_dot(), bg = "#ffffff")
buttonequal = Button(root, text = "=", padx = 10, pady = 15, command =  lambda : button_equal(), bg = "#ec7600", fg = "#ffffff")


myFont1 = font.Font(family = "Helvetica", weight = "bold", size = 15)
myFont2 = font.Font(family = "Helvetica", weight = "bold", size = 15)

list_buttons = [button2nd, buttondeg, buttonsin, buttoncos, buttontan, buttonpow2, buttonlog, buttonln, buttonleftbrk, buttonrightbrk,
buttonpow, buttonallclear, buttonclear, buttonpercent, buttondivide, buttonroot, button7, button8, button9, buttonmultiply, buttonfact,
button4, button5, button6, buttonminus, buttoninverse, button1, button2, button3, buttonplus, buttonpi, buttone, button0, buttondot, buttonequal]

list_numbers = [button7, button8, button9, button4, button5, button6, buttonminus, button1, button2, button3, buttone, button0, buttondot]

list_operators = [buttonallclear, buttonclear, buttonpercent, buttondivide, buttonmultiply, buttonminus, buttonplus, buttonequal]
    
for item in list_numbers:
    item["font"] = myFont1

for item in list_operators:
    item["font"] = myFont2

button2nd.grid(row = 1, column = 0, columnspan = 1)
buttondeg.grid(row = 1, column = 1, columnspan = 1)
buttonsin.grid(row = 1, column = 2, columnspan = 1)
buttoncos.grid(row = 1, column = 3, columnspan = 1)
buttontan.grid(row = 1, column = 4, columnspan = 1)

buttonpow2.grid(row = 2, column = 0, columnspan = 1)
buttonlog.grid(row = 2, column = 1, columnspan = 1)
buttonln.grid(row = 2, column = 2, columnspan = 1)
buttonleftbrk.grid(row = 2, column = 3, columnspan = 1)
buttonrightbrk.grid(row = 2, column = 4, columnspan = 1)

buttonpow.grid(row = 3, column = 0, columnspan = 1)
buttonallclear.grid(row = 3, column = 1, columnspan = 1)
buttonclear.grid(row = 3, column = 2, columnspan = 1)
buttonpercent.grid(row = 3, column = 3, columnspan = 1)
buttondivide.grid(row = 3, column = 4, columnspan = 1)

buttonroot.grid(row = 4, column = 0, columnspan = 1)
button7.grid(row = 4, column = 1, columnspan = 1)
button8.grid(row = 4, column = 2, columnspan = 1)
button9.grid(row = 4, column = 3, columnspan = 1)
buttonmultiply.grid(row = 4, column = 4, columnspan = 1)

buttonfact.grid(row = 5, column = 0, columnspan = 1)
button4.grid(row = 5, column = 1, columnspan = 1)
button5.grid(row = 5, column = 2, columnspan = 1)
button6.grid(row = 5, column = 3, columnspan = 1)
buttonminus.grid(row = 5, column = 4, columnspan = 1)

buttoninverse.grid(row = 6, column = 0, columnspan = 1)
button1.grid(row = 6, column = 1, columnspan = 1)
button2.grid(row = 6, column = 2, columnspan = 1)
button3.grid(row = 6, column = 3, columnspan = 1)
buttonplus.grid(row = 6, column = 4, columnspan = 1)

buttonpi.grid(row = 7, column = 0, columnspan = 1)
buttone.grid(row = 7, column = 1, columnspan = 1)
button0.grid(row = 7, column = 2, columnspan = 1)
buttondot.grid(row = 7, column = 3, columnspan = 1)
buttonequal.grid(row = 7, column = 4, columnspan = 1)

root.mainloop()
