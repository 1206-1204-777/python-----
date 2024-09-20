import tkinter
tmr = 0
def count_UP():
    global tmr
    tmr = tmr + 1
    label["text"] = tmr
    root.after(100, count_UP)

root = tkinter.Tk()
label = tkinter.Label(font=("Time New Roman", 100))
label.pack()
root.after(100,count_UP)
root.mainloop()