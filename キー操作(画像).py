import tkinter
key = 0
def key_down(e):
    global key
    key = e.keysym
def key_UP(e):
    global key
    key = " "
    
cx = 400
cy = 300 
def main_proc():
    global cx,cy
    if key == "Up":
        cy = cy-20
    if key == "Down":
        cy = cy+20
    if key == "Right":
        cx = cx+20
    if key == "Left":
        cx = cx-20
    canvas.coords("NYCHR", cx, cy)
    root.after(100, main_proc)
root = tkinter.Tk()
root.title("画像操作")
root.bind("<KeyPress>", key_down)
root.bind("KeyRelease", key_UP)
canvas = tkinter.Canvas(width=800, height=600, bg="lightgreen")
canvas.pack()
img = tkinter.PhotoImage(file="mimi.png")
canvas.create_image(cx,cy,image=img, tag= "NYCHR")
main_proc()
root.mainloop()

