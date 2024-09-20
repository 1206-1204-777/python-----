import calendar as cal
import tkinter as tk
#from tkinter import messagebox

def show_calendar():
    # カレンダーウィンドウを作成
    calendar_window = tk.Toplevel(root)
    calendar_window.title("カレンダー")
    calendar_text = tk.Text(calendar_window)
    calendar_text.pack()
    
    # 現在の月と年を取得
    year = 2024
    month = 8
    
    # カレンダーを生成
    cal_str = cal.month(year, month)
    calendar_text.insert(tk.END, cal_str)
    
    # カレンダーウィンドウのサイズを調整
    calendar_window.geometry("350x350")
    
root = tk.Tk()
root.geometry("200x200")

lbl = tk.Label(root, text="カレンダー表示アプリ")
btn = tk.Button(root, text="カレンダーを表示", command=show_calendar)

lbl.pack()
btn.pack()

root.mainloop()
