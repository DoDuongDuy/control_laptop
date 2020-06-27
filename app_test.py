import tkinter as tk
import requests
from main import run
HEIGHT = 400
WIDTH = 400

root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#42c2f4', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.3, relheight=0.1, anchor='n')

button = tk.Button(frame, text = "voice", font=40, command=run)
button.place(relx=0, relheight=1, relwidth=1)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.5, anchor='n')

label = tk.Label(lower_frame,text ="INTPUT:\n\n Khoá màn hình\n24h\n Mở trình duyệt\n Excel \n Tắt nguồn ")
label.place(relwidth=1, relheight=1)


root.mainloop()