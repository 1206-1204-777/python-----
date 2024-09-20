import tkinter
import random

cursor_x = 0
cursor_y = 0
mouse_x = 0
mouse_y = 0
mouse_c = 0

def mouse_move(e):
    global mouse_x, mouse_y
    mouse_x = e.x
    mouse_y = e.y
    cursor_x = (mouse_x // 72) * 72
    cursor_y = (mouse_y // 72) * 72
    print(f"Mouse moved to ({cursor_x}, {cursor_y})")  # デバッグ用

def mouse_click(e):
    global mouse_c
    mouse_c = 1
    print("Mouse clicked")  # デバッグ用
    print(f"Mouse moved to ({mouse_x}, {mouse_y})")  # デバッグ用


neko = []
for i in range(10):
    neko.append([0, 0, 0, 0, 0, 0, 0, 0])

def draw_neko():
    for y in range(10):
        for x in range(8):
            if neko[y][x] > 0:
                csv.create_image(x*72+60, y*72+60, image=img_neko[neko[y][x]], tag="NEKO")
                
def yoko_neko():
    for y in range(10):
        for x in range(1, 7):
            if neko[y][x] > 0:
                if neko[y][x-1] == neko[y][x] and neko[y][x+1] == neko[y][x]:
                    neko[y][x-1] = 7  # Neko_niku.png に置き換え
                    neko[y][x] = 7    # Neko_niku.png に置き換え
                    neko[y][x+1] = 7  # Neko_niku.png に置き換え

def game_main():
    global cursor_x, cursor_y, mouse_c
    if 660 <= mouse_x and mouse_x < 840 and 100 <= mouse_y < 160 and mouse_c == 1:  # 修正
        mouse_c = 0
        yoko_neko()
    if 24 <= mouse_x and mouse_x < 24+72*8 and 24 <= mouse_y and mouse_y < 24+72*10:
        cursor_x = int((mouse_x-24)/72)
        cursor_y = int((mouse_y-24)/72)
        if mouse_c == 1:
            mouse_c = 0
            neko[cursor_y][cursor_x] = random.randint(1, 6)
            
    csv.delete("CURSOR")
    csv.create_image(cursor_x*72+60, cursor_y*72+60, image=cursor, tag="CURSOR")
    csv.delete("NEKO")
    draw_neko()
    root.after(100, game_main)
    
root = tkinter.Tk()
root.title("TEST")
root.resizable(False, False)
root.bind("<Motion>", mouse_move)
root.bind("<Button-1>", mouse_click)  # 修正
csv = tkinter.Canvas(root, width=912, height=768)
csv.pack()

bg = tkinter.PhotoImage(file="python\\image\\Neko_bg.png")
cursor = tkinter.PhotoImage(file="python\\image\\Neko_cursor.png")
img_neko = [
    None,
    tkinter.PhotoImage(file="python\\image\\neko1.png"),
    tkinter.PhotoImage(file="python\\image\\neko2.png"),
    tkinter.PhotoImage(file="python\\image\\neko3.png"),
    tkinter.PhotoImage(file="python\\image\\neko4.png"),
    tkinter.PhotoImage(file="python\\image\\neko5.png"),
    tkinter.PhotoImage(file="python\\image\\neko6.png"),
    tkinter.PhotoImage(file="python\\image\\Neko_niku.png")
]
csv.create_image(456, 384, image=bg)
csv.create_rectangle(660, 100, 840, 160, fill="white")
csv.create_text(750, 130, text="test", fill="red", font=("Times New Roman", 30))
game_main()
root.mainloop()
