import tkinter
import random

def click_btn():
    label["text"]=random.choice(["大吉", "中吉", "小吉", "末吉", "凶", "大凶"])
    label.update()
    
root = tkinter.Tk()
root.title("おみくじアプリ")
root.resizable(False, False)
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()
gazou = tkinter.PhotoImage(file="7p89.png")
canvas.create_image(400, 500, image=gazou)
label = tkinter.Label(root, text=" ? ? ", font=("Time New Roman", 120), bg="white")
label.place(x=380, y=60)
button = tkinter.Button(root, text="おみくじを引く", font=("Time New Roman", 36), command=click_btn, fg="skyblue")
button.place(x=360, y=400)
root.mainloop()