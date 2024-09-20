import tkinter
root = tkinter.Tk()
root.title("迷路")
canvace = tkinter.Canvas(width=800,height=560, bg="white")
canvace.pack()
maze = [[1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,1,0,0,1],
        [1,0,1,1,0,0,1,0,0,1],
        [1,0,0,1,0,0,0,0,0,1],
        [1,0,0,1,1,1,1,1,0,1],
        [1,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1]
        ]
for y in range(7):
    for x in range(10):
        if maze[y][x] == 1:
            canvace.create_rectangle(x*80,y*80,x*80+80,y*80+80, fill="gray")
        

root.mainloop()