import tkinter

def click_btn():
    txt = entry.get()
    button["text"] = txt
    
root = tkinter.Tk()
root.title("テキスト入力")
root.geometry("400x200")
entry = tkinter.Entry(width=20)
entry.place(x=20, y=20)
button = tkinter.Button(text="pythonゲーム開発", command=click_btn)
button.place(x=20, y=100)
root.mainloop()