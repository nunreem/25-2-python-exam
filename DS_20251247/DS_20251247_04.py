import tkinter as tk

root=tk.Tk()
root.title("중간고사 4번")

canvas = tk.Canvas(root, width=400, height = 400)
canvas.pack()

Radiobutton(root,text="사각형",padx=20,variable=choice,value=1).pack(anchor=W)
Radiobutton(root,text="원",padx=20,variable=choice,value=2).pack(anchor=W)
Radiobutton(root,text="텍스트",padx=20,variable=choice,value=3).pack(anchor=W)




root.mainloop()