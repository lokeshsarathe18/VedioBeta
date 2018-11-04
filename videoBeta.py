from tkinter import *
import os
 
window = Tk()
 
window.title("Welcome to LikeGeeks app")
 
window.geometry('350x200')
 
lbl = Label(window, text="Hello")
 
lbl.grid(column=0, row=0)
 
def clicked():
 
	os.system('python final.py')    
	os.system('googleimagesdownload --keywords "Polar bears" --limit 2')
 
btn = Button(window, text="Click Me", command=clicked)
 
btn.grid(column=1, row=0)
 
window.mainloop()
