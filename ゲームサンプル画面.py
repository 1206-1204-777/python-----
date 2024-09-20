import tkinter

neko = [
    [1,0,0,0,0,0,7,7],
    [0,2,0,0,0,0,7,7],
    [0,0,3,0,0,0,0,0],
    [0,0,0,4,0,0,0,0],
    [0,0,0,0,5,0,0,0],
    [0,0,0,0,0,6,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,1,2,3,4,5,6]
]

def draw_neko():
    for y in range(10):
        for x in range(8):
            if neko[y][x] > 0:
                csv.create_image(x*72+60,y*72+60,image=img_neko[neko[y][x]])
                
def drop_neko():
    for y in range(8, -1, -1):
        for x in range(8):
            if neko[y][x] > 0:
                if neko[y][x] != 0 and neko[y+1][x] == 0:
                    neko[y+1][x] = neko[y][x]
                    neko[y][x] = 0
root = tkinter.Tk()
root.title('GAME')
root.resizable(False,False)
csv = tkinter.Canvas(root, width=912,height=768)
csv.pack()

bg = tkinter.PhotoImage(file="image\\Neko_bg.png")
img_neko = [
    None,
    tkinter.PhotoImage(file="image\\neko1.png"),
    tkinter.PhotoImage(file="image\\neko2.png"),
    tkinter.PhotoImage(file="image\\neko3.png"),
    tkinter.PhotoImage(file="image\\neko4.png"),
    tkinter.PhotoImage(file="image\\neko5.png"),
    tkinter.PhotoImage(file="image\\neko6.png"),
    tkinter.PhotoImage(file="image\\Neko_niku.png")
]

csv.create_image(456, 384, image=bg)
draw_neko()
root.mainloop()