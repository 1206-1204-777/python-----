import tkinter
root = tkinter.Tk()
root.title( "初めてのキャンバス")
canvas = tkinter.Canvas(root, width=600, height=750, bg= "skyblue")
canvas.pack()
gazou = tkinter.PhotoImage(file="7p89.png")
canvas.create_image(500, 500, image = gazou)
root.mainloop()