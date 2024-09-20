import random
import tkinter as tk
#root = cl.CL()

def calendar():
    kuji = [1,2,3,4,5]
    lbl.configure(text=random.choice(kuji))
    
root = tk.Tk()
root.geometry("200x100")

lbl = tk.Label(text="LABEL")
btn = tk.Button(text="PUSH", command=calendar)     

#cl.pack()
lbl.pack()
btn.pack()
tk.mainloop()


