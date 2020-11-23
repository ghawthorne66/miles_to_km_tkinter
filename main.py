from tkinter import *

window = Tk()
window.title("GUI")
window.minsize(500, 300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="Label", font=("Arial", 18, "bold"))
my_label.config(text="My Text")
my_label.grid(column=0, row=0)
my_label.config(padx=40, pady=40)

_input = Entry(width=10)
_input.grid(column=3, row=2)


def button_clicked():
    new_text = _input.get()
    my_label.config(text=new_text)
    print("I got clicked")


button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)
button.config(padx=5, pady=5)

new_button = Button(text="New Button", command=button_clicked)
new_button.grid(column=2, row=0)
new_button.config(padx=5, pady=5)


def add(*args):
    print(args[1])
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(3, 5, 6, 7))


def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="infinity", model="G30")
print(my_car.model)

window.mainloop()
