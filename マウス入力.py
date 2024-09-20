import tkinter

mouse_x = 0
mouse_y = 0
mouse_c = 0

def mouse_move(e):
    global mouse_x,mouse_y
    mouse_x = e.x
    mouse_y = e.y
    
def mouse_press(e):
    global mouse_c
    mouse_c = 1

def mouse_release(e):
    global mouse_c
    mouse_c = 0

def game_main():
    fnt = ("Time New Roman",30)
    txt = "mouse({},{}){}".format(mouse_x,mouse_y,mouse_c)
    csv.delete("TEST")
    csv.create_text(456,384,text=txt, fill="black", font=fnt, tag="TEST")
    root.after(100,game_main)
    
root =tkinter.Tk()
root.title("マウス入力")
root.resizable(False,False)
root.bind("<Motion>",mouse_move)
root.bind("<ButtonPress>",mouse_press)
root.bind("<ButtonRelease>", mouse_release)
csv = tkinter.Canvas(root, width=912,height=768)
csv.pack()
game_main()
root.mainloop()