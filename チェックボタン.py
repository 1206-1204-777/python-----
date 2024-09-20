import tkinter

def check():
    if cval.get() == True:
        print("チェックされています")
    else:
        print("チェックされていません")
root = tkinter.Tk()
root.title("チェックボタン")
root.geometry("400x200")
cval = tkinter.BooleanVar()
cval.set(True)
cbtn = tkinter.Checkbutton(text="チェックボタン", variable=cval, command=check)
cbtn.pack()
root.mainloop()