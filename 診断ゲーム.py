import tkinter  

KEKKA = ["  ","あなた誰ですか？","興味ありません","つまらない人","普通ですねw","目標を持ちなさい","大変生きずらいでしょう","あなたは変人です"]
def click_btn():
    pts = 0
    for i in range(7):
        if bvar[i].get() == True:
            pts = pts +1
            omosiroi = int(100*pts/7)
    text.delete("1.0", tkinter.END)
    text.insert("1.0", "＜診断結果＞\nあなたの変人度は" + str(omosiroi) + "%です\n" + KEKKA[pts])
    
root = tkinter.Tk()
root.title("診断ゲーム")
root.resizable(False,False)
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()

gazou = tkinter.PhotoImage(file="7p89.png")
canvas.create_image(400, 500, image=gazou)

button = tkinter.Button(text="診断する", font=("TIme Nwe Roman", 32), bg="lightgreen", command=click_btn)
button.place(x=400, y=480)
text = tkinter.Text(width=40, height=5, font=("Time Nwe Roman", 16))
text.place(x=320, y=30)

bvar = [None]*7
cbtn = [None]*7
ITEM = ["高いところが好き", "挑戦が好き", "強いトラウマがある", "遊びたい", "矛盾に敏感に気づく", "夜元気になる", "マイペースと言われる、思う"]
for i in range(7):
    bvar[i] = tkinter.BooleanVar()
    bvar[i].set(False)
    cbtn[i] = tkinter.Checkbutton(text=ITEM[i], font=("Time Nwe Roman", 12), variable=bvar[i], bg="#dfe")
    cbtn[i].place(x=400, y=160+40*i)
root.mainloop()