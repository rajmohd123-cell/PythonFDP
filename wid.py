from tkinter import *

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
root = Tk()
canvas = Canvas(width=200, height=200, bg='white')
button_frame = Frame()
buttons = [0]*26
for i in range(26):
    buttons[i] = Button(button_frame, font=('Verdana', 18),text=alphabet[i])
    buttons[i].grid(row=0, column=i)

ok_button = Button(text='OK', font=('Verdana', 24))
reset_button = Button(text='Reset', font=('Verdana', 24))
canvas.grid()
button_frame.grid(row=0, column=0)
ok_button.grid(row=1, column=0)
reset_button.grid(row=1, column=1)

mainloop()