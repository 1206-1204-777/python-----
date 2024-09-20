import tkinter
import random

FNT = ("Time New Roman", 20, "bold")
key = ""
keyfn = False
idx = 0
tmr = 0
stage = 0
score = 0
bar_x = 400  # 初期位置
bar_y = 540
ball_x = 0
ball_y = 0
ball_xp = 0
ball_yp = 0
is_clr = False

block = []
for i in range(5):
    block.append([1] * 10)  # ブロックの初期配置
for i in range(10):
    block.append([0] * 10)  # 空の行

def key_down(e):
    global key
    key = e.keys

def key_up(e):
    global keyfn
    keyfn = True

def draw_block():
    global is_clr
    is_clr = True
    csv.delete("BG")
    for y in range(15):
        for x in range(10):
            gx = x * 80
            gy = y * 40
            if block[y][x] == 1:
                csv.create_rectangle(gx + 1, gy + 4, gx + 79, gy + 32, fill=block_color(x, y), width=0, tag="BG")
                is_clr = False

    csv.create_text(200, 20, text="STAGE " + str(stage), fill="white", font=FNT, tag="BG")
    csv.create_text(600, 20, text="SCORE " + str(score), fill="white", font=FNT, tag="BG")

def block_color(x, y):
    col = "#{:02x}{:02x}{:02x}".format(15 - x - int(y / 3), x + 1, y * 3 + 3)
    return col

def draw_bar():
    csv.delete("BAR")
    csv.create_rectangle(bar_x - 80, bar_y - 12, bar_x + 80, bar_y + 12, fill="silver", width=0, tag="BAR")

def bar_move():
    global bar_x
    if key == "Left" and bar_x > 80:
        bar_x -= 40
    if key == "Right" and bar_x < 720:
        bar_x += 40

def draw_ball():
    csv.delete("BALL")
    csv.create_oval(ball_x - 20, ball_y - 20, ball_x + 20, ball_y + 20, fill="gold", outline="orange", width=2, tag="BALL")

def move_ball():
    global idx, tmr, score, ball_x, ball_y, ball_xp, ball_yp
    ball_x += ball_xp
    if ball_x < 20:
        ball_x = 20
        ball_xp = -ball_xp
    if ball_x > 780:
        ball_x = 780
        ball_xp = -ball_xp

    x = int(ball_x / 80)
    y = int(ball_y / 40)
    if 0 <= y < len(block) and 0 <= x < len(block[y]) and block[y][x] == 1:
        block[y][x] = 0  # ブロックを消す
        ball_yp = -ball_yp  # Y方向の反射
        score += 10
        draw_block()  # ブロックを再描画

    ball_y += ball_yp
    if ball_y >= 600:
        idx = 2
        tmr = 0
        return
    if ball_y < 20:
        ball_y = 20
        ball_yp = -ball_yp
    if bar_y - 40 <= ball_y <= bar_y:
        if bar_x - 80 <= ball_x <= bar_x + 80:
            ball_yp = -ball_yp
            score += 1
        elif bar_x - 100 <= ball_x < bar_x - 80:
            ball_yp = -ball_yp
            ball_xp = random.randint(-20, -10)
        elif bar_x + 80 < ball_x <= bar_x + 100:
            ball_yp = -ball_yp
            ball_xp = random.randint(10, 20)
            score += 2

def main_proc():
    global ball_x, ball_xp, ball_y, ball_yp, idx, tmr, stage, score, key, keyfn
    if idx == 0:
        tmr += 1
        if tmr == 1:
            stage = 1
            score = 0
        if tmr == 2:
            ball_x = 160
            ball_y = 240
            ball_xp = 10
            ball_yp = 10
            bar_x = 400
            draw_block()
        draw_ball()
        draw_bar()
        bar_move()
        move_ball()
        if is_clr:
            idx = 3
            tmr = 0
        if keyfn:
            keyfn = False
            key = ""

    elif idx == 2:
        tmr += 1
        if tmr == 1:
            csv.create_text(400, 260, text="GAME SET", fill="red", font=FNT, tag="TXT")
        if tmr == 15:
            csv.create_text(300, 340, text="[R]eplay", fill="cyan", font=FNT, tag="TXT")
            csv.create_text(500, 340, text="[N]ew game", fill="yellow", font=FNT, tag="TXT")
        if key == "r":
            csv.delete("TXT")
            idx = 0
            tmr = 1
        if key == "n":
            csv.delete("TXT")
            for y in range(5):
                for x in range(10):
                    block[y][x] = 1
            idx = 0
            tmr = 0

    elif idx == 3:
        tmr += 1
        if tmr == 1:
            csv.create_text(400, 260, text="CLEAR", fill="lime", font=FNT, tag="TXT")
        if tmr == 15:
            csv.create_text(400, 340, text="NEXT [SPACE]", fill="cyan", font=FNT, tag="TXT")
        if key == "space":
            csv.delete("TXT")
            for y in range(5):
                for x in range(10):
                    block[y][x] = 1
            idx = 0
            tmr = 1
            stage += 1

    if keyfn:
        keyfn = False
        key = ""
    root.after(50, main_proc)

root = tkinter.Tk()
root.title("ブロックゲーム")
root.resizable(False, False)
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)
csv = tkinter.Canvas(root, width=800, height=600, bg="black")
csv.pack()
main_proc()
root.mainloop()