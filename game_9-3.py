import tkinter

neko = [
    [1, 0, 0, 0, 0, 0, 0, 7],
    [1, 0, 0, 0, 0, 0, 0, 7],
    [1, 0, 0, 0, 0, 0, 7, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 2, 3, 4, 5, 6]
]

def draw():
    for y in range(10):
        for x in range(8):
            if neko[y][x] > 0:
                canvas.create_image(x*72 + 60, y*72 + 60, image = imgneko[neko[y][x]], tag = "neneko")

def drop():
    for y in range(8, -1, -1):
        for x in range(8):
            


root = tkinter.Tk()
root.title("貓貓")
root.resizable(False,False)
root.bind("<Motion>", mmove)

canvas = tkinter.Canvas(root, width = 912, height = 768)
canvas.pack()

bg = tkinter.PhotoImage(file = "neko_bg.png")
#cor = tkinter.PhotoImage(file = "neko_cursor.png")
canvas.create_image(456, 384, image = bg)

imgneko = [
    None,
    tkinter.PhotoImage(file = "neko1.png"),
    tkinter.PhotoImage(file = "neko2.png"),
    tkinter.PhotoImage(file = "neko3.png"),
    tkinter.PhotoImage(file = "neko4.png"),
    tkinter.PhotoImage(file = "neko5.png"),
    tkinter.PhotoImage(file = "neko6.png"),
    tkinter.PhotoImage(file = "neko_niku.png"),
]

draw()

root.mainloop()