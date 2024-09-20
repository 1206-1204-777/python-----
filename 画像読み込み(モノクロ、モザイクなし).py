import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

def dipPhot(path):
    newImage = PIL.Image.open(path).resize((500,300))
    
    imageDate = PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image = imageDate)
    imageLabel.image = imageDate

def openFile():
    fpath = fd.askopenfilename()
    
    if fpath:
        dipPhot(fpath)

root = tk.Tk()
root.geometry("400x350")

btn = tk.Button(root, text="ファイルを開く", command=openFile)
imageLabel = tk.Label(root)
btn.pack()
imageLabel.pack()

tk.mainloop()