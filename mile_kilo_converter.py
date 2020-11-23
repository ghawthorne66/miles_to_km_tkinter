from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_result_label.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

# window.minsize(500, 300)
# window.config(padx=20, pady=20)
#
# my_label = Label(text="Label", font=("Arial", 18, "bold"))
# my_label.config(text="0")
# my_label.grid(column=2, row=2)
# my_label.config(padx=0, pady=20)
#
# is_equal = Label(text="Label", font=("Arial", 18, "bold"))
# is_equal.config(text="is equal to")
# is_equal.grid(column=0, row=2)
# is_equal.config(padx=0, pady=0)
#
# miles_text = Label(text="Label", font=("Arial", 18, "bold"))
# miles_text.config(text="Miles")
# miles_text.grid(column=3, row=0)
# miles_text.config(padx=0, pady=40)

# km_text = Label(text="Label", font=("Arial", 18, "bold"))
# km_text.config(text="km")
# km_text.grid(column=3, row=2)
# km_text.config(padx=0, pady=0)
#
# input = Entry(width=10)
# input.grid(column=2, row=0)
# input.config(padx=0, pady=0)


# def button_clicked():
#     new_text = input.get()
#     my_label.config(text=new_text)
#     print("I got clicked")
#
#
# button = Button(text="Calculate", command=button_clicked)
# button.grid(column=2, row=3)
# button.config(padx=60, pady=5)

window.mainloop()
