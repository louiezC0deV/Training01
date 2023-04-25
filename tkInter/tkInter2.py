from tkinter import *
import random

counter = 0
w2 = None
root1 = Tk()

def cmd():
    root2 = Tk()

def cnt():
    global counter
    counter += 1
    root1.after(1000, cnt)
    w2.config(text=str(counter))
    print(counter)


img1 = PhotoImage(file="dw.gif")
txt1 = """At present, only GIF and PPM/PGM
formats are supported, but an interface 
exists to allow additional image file
formats to be added easily."""

f0=Frame(root1, relief="raised", bd=2, padx=10, pady=10)
f0.pack(side="left")

wx = []
for i in range(0, 5):
    w1 = Label(f0, fg="red", justify=CENTER, compound=CENTER, text=txt1, image=img1)
    wx.append(w1)


for s in wx:
    s.pack()

f1 = LabelFrame(root1, relief="sunken", bd=1, text="hello")
f1.pack(side="left")

img2 = PhotoImage(file="gifgaff.gif")
txt2 = txt1
w2 = Label(f1, font="Helvetica", bg="blue", compound=LEFT, text=txt2, image=img2)
w2.pack()

f2 = LabelFrame(root1, relief="sunken", bd=1, text="Second Frame")
f2.pack(side="right")

wx = []
for i in range(0, 5):
    w3 = Button(f2, text="Hello-{}".format(i), command=cmd)
    wx.append(w3)

for s in wx:
    s.pack()


root1.after(0, cnt)
root1.mainloop()
