from tkinter import *


expression = ""


class Node:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value


def get_priority(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0


def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)


def is_operator(expresie):
    if expresie in ('+', '-', '*', '/'):
        return 1
    return 0


def evaluate(node: Node):
    if node == None:
        return 0
    if is_operator(node.value) == 0:
        return float(node.value)
   
    stanga = evaluate(node.left)
    dreapta = evaluate(node.right)
   
    if node.value == '+': return stanga + dreapta
    if node.value == '-': return stanga - dreapta
    if node.value == '*': return stanga * dreapta
    if node.value == '/':
        if dreapta == 0: raise ZeroDivisionError("Diviziune la zero")
        return stanga / dreapta


def prelucrare_sir(expresie):
    for op in "+-*/()":
        expresie = expresie.replace(op, f" {op} ")
    return expresie.split()


def build_tree(nod):
    if nod == None or len(nod) == 0:
        return None
   
    if len(nod) == 1:
        return Node(nod[0])
   
    index_pivot = -1
    paranteze = 0
    prioritate_minima = 10
   
    for i in range(len(nod) - 1, -1, -1):
        caracter_curent = nod[i]


        if caracter_curent == ')':
            paranteze += 1
        elif caracter_curent == '(':
            paranteze -= 1


        if paranteze == 0 and is_operator(caracter_curent):
            prioritate = get_priority(caracter_curent)
            if prioritate < prioritate_minima:
                prioritate_minima = prioritate
                index_pivot = i
   
    if index_pivot == -1:
        if nod[0] == '(' and nod[-1] == ')':
            return build_tree(nod[1:-1])
        return None


    radacina = Node(nod[index_pivot])
    radacina.left = build_tree(nod[0:index_pivot])
    radacina.right = build_tree(nod[index_pivot + 1:])
    return radacina


def equalpress():
    global expression
    try:
        sir_pe_care_il_prelucrez = prelucrare_sir(expression)
        arbore = build_tree(sir_pe_care_il_prelucrez)
        rezultat = evaluate(arbore)
       
           
        equation.set(str(rezultat))
        expression = str(rezultat)
    except:
        equation.set(" error ")
        expression = ""


def clear():
    global expression
    expression = ""
    equation.set("")


if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="gray")
    gui.title("Simple Tree Calculator")
    gui.geometry("340x180")


    equation = StringVar()
    expression_field = Entry(gui, textvariable=equation)
    expression_field.grid(columnspan=4, ipadx=70)


   
    button1 = Button(gui, text=' 1 ', fg='white', bg='blue', command=lambda: press(1), height=1, width=7)
    button1.grid(row=2, column=0)
    button2 = Button(gui, text=' 2 ', fg='white', bg='blue', command=lambda: press(2), height=1, width=7)
    button2.grid(row=2, column=1)
    button3 = Button(gui, text=' 3 ', fg='white', bg='blue', command=lambda: press(3), height=1, width=7)
    button3.grid(row=2, column=2)
    button4 = Button(gui, text=' 4 ', fg='white', bg='blue', command=lambda: press(4), height=1, width=7)
    button4.grid(row=3, column=0)
    button5 = Button(gui, text=' 5 ', fg='white', bg='blue', command=lambda: press(5), height=1, width=7)
    button5.grid(row=3, column=1)
    button6 = Button(gui, text=' 6 ', fg='white', bg='blue', command=lambda: press(6), height=1, width=7)
    button6.grid(row=3, column=2)
    button7 = Button(gui, text=' 7 ', fg='white', bg='blue', command=lambda: press(7), height=1, width=7)
    button7.grid(row=4, column=0)
    button8 = Button(gui, text=' 8 ', fg='white', bg='blue', command=lambda: press(8), height=1, width=7)
    button8.grid(row=4, column=1)
    button9 = Button(gui, text=' 9 ', fg='white', bg='blue', command=lambda: press(9), height=1, width=7)
    button9.grid(row=4, column=2)
    button0 = Button(gui, text=' 0 ', fg='white', bg='blue', command=lambda: press(0), height=1, width=7)
    button0.grid(row=5, column=0)


    plus = Button(gui, text=' + ', fg='white', bg='blue', command=lambda: press("+"), height=1, width=7)
    plus.grid(row=2, column=3)
    minus = Button(gui, text=' - ', fg='white', bg='blue', command=lambda: press("-"), height=1, width=7)
    minus.grid(row=3, column=3)
    multiply = Button(gui, text=' * ', fg='white', bg='blue', command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=4, column=3)
    divide = Button(gui, text=' / ', fg='white', bg='blue', command=lambda: press("/"), height=1, width=7)
    divide.grid(row=5, column=3)
    equal = Button(gui, text=' = ', fg='white', bg='blue', command=equalpress, height=1, width=7)
    equal.grid(row=5, column=2)
    clear_btn = Button(gui, text='Clear', fg='white', bg='blue', command=clear, height=1, width=7)
    clear_btn.grid(row=5, column=1)
    p_d = Button(gui, text=' ( ', fg='white', bg='blue', command=lambda: press("("), height=1, width=7)
    p_d.grid(row=6, column=2)
    p_i = Button(gui, text=' ) ', fg='white', bg='blue', command=lambda: press(")"), height=1, width=7)
    p_i.grid(row=6, column=3)


    gui.mainloop()

