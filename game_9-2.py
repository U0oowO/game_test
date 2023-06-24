import tkinter

cx = 0
cy = 0

mx = 0
my = 0
mc = 0

def mmove(e):
    global mx, my
    mx = e.x
    my = e.y

#def mpress(e):
    global mc
    mc = 1

#def mrelease(e):
    global mc
    mc = 0

def gamemain():
    global cx, cy
    if 24 <= mx and mx < 24 + 72*8 and 24 <= my and my < 24 + 72*10:
        cx = int((mx - 24) / 72) #int = 計算
        cy = int((my - 24) / 72)
    
    canvas.delete("cursor")
    canvas.create_image(cx*72 + 60, cy*72 + 60, image = cor, tag = "cursor")

    #fnt = ("Times New Roman", 30)
    #txt = "mouse({},{}){}".format(mx, my, mc)
    #canvas.delete("test")
    #canvas.create_text(456, 384, text = txt, fill = "black", font = fnt, tag = "test")
    root.after(100,gamemain)

root = tkinter.Tk()
root.title("貓貓")
root.resizable(False,False)
root.bind("<Motion>", mmove)
#root.bind("<ButtonPress>", mpress)
#root.bind("<ButtonRelease>", mrelease)

canvas = tkinter.Canvas(root, width = 912, height = 768)
canvas.pack()

bg = tkinter.PhotoImage(file = "neko_bg.png")
cor = tkinter.PhotoImage(file = "neko_cursor.png")
canvas.create_image(456, 384, image = bg)

gamemain()

root.mainloop()
