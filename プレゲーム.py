import tkinter
import random

index = 0
timer = 0
score = 0
next = 0

cursor_x = 0
cursor_y = 0
mouse_x = 0
mouse_y = 0
mouse_c = 0

def mouse_move(e):
    global mouse_x, mouse_y
    mouse_x = e.x
    mouse_y = e.y

def mouse_press(e):
    global mouse_c
    mouse_c = 1

cat = []
check = []
for i in range(10):
    cat.append([0, 0, 0, 0, 0, 0, 0, 0])
    check.append([0, 0, 0, 0, 0, 0, 0, 0])

def draw_cat():
    canvas.delete("cat")
    for y in range(10):
        for x in range(8):
            if cat[y][x] != 0:
                canvas.create_image(x*72+60, y*72+60, image=img_cat[cat[y][x]], tag="cat")

def check_cat():
    for y in range(10):
        for x in range(8):
            check[y][x] = cat[y][x]
    
    for y in range(1, 9):
        for x in range(8):
            if check[y][x] > 0 and check[y-1][x] == check[y+1][x] == check[y][x]:
                cat[y-1][x] = 7
                cat[y][x] = 7
                cat[y+1][x] = 7

    for y in range(10):
        for x in range(1, 7):
            if check[y][x] > 0 and check[y][x-1] == check[y][x] == check[y][x+1]:
                cat[y][x-1] = 7
                cat[y][x] = 7
                cat[y][x+1] = 7

    for y in range(1, 9):
        for x in range(1, 7):
            if check[y][x] > 0 and check[y-1][x-1] == check[y+1][x+1] == check[y][x] == check[y+1][x-1] == check[y-1][x+1]:
                cat[y-1][x-1] = 7
                cat[y][x] = 7
                cat[y+1][x+1] = 7
                cat[y-1][x+1] = 7
                cat[y+1][x-1] = 7

def sweep_cat():
    num = 0
    for y in range(10):
        for x in range(8):
            if cat[y][x] == 7:
                cat[y][x] = 0
                num += 1
    return num

def drop_cat():
    flag = False
    for y in range(8, -1, -1):
        for x in range(8):
            if cat[y][x] != 0 and cat[y+1][x] == 0:
                cat[y+1][x] = cat[y][x]
                cat[y][x] = 0
                flag = True
    return flag

def over_cat():
    for x in range(8):
        if cat[0][x] > 0:
            return True
    return False

def set_cat():
    for x in range(8):
        if cat[0][x] == 0:  # 空のスロットにのみ新しい猫を配置
            cat[0][x] = random.randint(1, 6)

def draw_txt(txt, x, y, siz, col, tg):
    font = ("Time New Roman", siz, "bold")
    canvas.create_text(x+2, y+2, text=txt, fill="black", font=font, tag=tg)
    canvas.create_text(x, y, text=txt, fill=col, font=font, tag=tg)

def game_main():
    global index, timer, score, next, cursor_x, cursor_y, mouse_x, mouse_y, mouse_c
    if index == 0:
        draw_txt("ねこねこ", 312, 240, 100, "violet", "TITLE")
        draw_txt("Click to start!", 312, 560, 50, "orange", "TITLE")
        index = 1
        mouse_c = 0
    elif index == 1:
        if mouse_c == 1:
            for y in range(10):
                for x in range(8):
                    cat[y][x] = 0
                    mouse_c = 0
                    score = 0
                    next = 0
                    cursor_x = 0
                    cursor_y = 0
                    set_cat()
                    draw_cat()
                    canvas.delete("TITLE")
                    index = 2
    elif index == 2:
        if not drop_cat():
            index = 3
        draw_cat()
    elif index == 3:
        check_cat()
        draw_cat()
        index = 4
    elif index == 4:
        sc = sweep_cat()
        score += sc * 10
        if sc > 0:
            index = 2
        else:
            if not over_cat():
                next = random.randint(1, 6)
                index = 5
            else:
                index = 6
                timer = 0
        draw_cat()
    elif index == 5:
        if 24 <= mouse_x < 24+72*8 and 24 <= mouse_y < 24+72*10:
            cursor_x = int((mouse_x-24)/72)
            cursor_y = int((mouse_y-24)/72)
            if mouse_c == 1:
                mouse_c = 0
                if cat[cursor_y][cursor_x] == 0:  # 画像がない場所のみ選択
                    cat[cursor_y][cursor_x] = next
                    next = 0
                    index = 2
        canvas.delete("CURSOR")
        canvas.create_image(cursor_x*72+60, cursor_y*72+60, image=cursor, tag="CURSOR")
        draw_cat()
    elif index == 6:
        timer += 1
        if timer == 1:
            draw_txt("GAME OVER", 312, 348, 60, "red", "OVER")
        if timer == 50:
            canvas.delete("OVER")
            index = 0
    canvas.delete("INFO")
    draw_txt("SCORE: " + str(score), 160, 60, 32, "blue", "INFO")
    if next > 0:
        canvas.create_image(752, 128, image=img_cat[next], tag="INFO")
    root.after(100, game_main)

root = tkinter.Tk()
root.title("CAT GAME")
root.resizable(False, False)
root.bind("<Motion>", mouse_move)
root.bind("<ButtonPress>", mouse_press)
canvas = tkinter.Canvas(root, width=912, height=768)
canvas.pack()

bg = tkinter.PhotoImage(file="image\\Neko_bg.png")
cursor = tkinter.PhotoImage(file="image\\Neko_cursor.png")
img_cat = [
    None,
    tkinter.PhotoImage(file="image\\neko1.png"),
    tkinter.PhotoImage(file="image\\neko2.png"),
    tkinter.PhotoImage(file="image\\neko3.png"),
    tkinter.PhotoImage(file="image\\neko4.png"),
    tkinter.PhotoImage(file="image\\neko5.png"),
    tkinter.PhotoImage(file="image\\neko6.png"),
    tkinter.PhotoImage(file="image\\neko_niku.png")
]

canvas.create_image(456, 384, image=bg)
game_main()
root.mainloop()
