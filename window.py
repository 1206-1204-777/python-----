import tkinter
root = tkinter.Tk()
root.title("初めてのGUI")
root.geometry("800x600")
label = tkinter.Label(root,text="こんにちは",font=("System",24))
label.place(x=200, y=100)
root.mainloop()