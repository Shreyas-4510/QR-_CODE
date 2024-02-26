import tkinter as tk
import pyqrcode 
from pyqrcode import create
import png
from PIL import Image,ImageTk

my_w=tk.Tk()
my_w.geometry("410x360")
my_w.title("www.cricheroes.com")
e1=tk.Entry(my_w,font=22,bg='yellow',width=15)
e1.grid(row=0,column=0,padx=10,pady=4)
b1=tk.Button(my_w,font=22,text='Generate QR code',command=lambda:my_generate())
b1.grid(row=0,column=1,padx=5,pady=4)
l1=tk.Label(my_w,text='QR code ')
l1.grid(row=1,column=0,columnspan=2)
def my_generate():
    global my_image
    my_qr=pyqrcode.create(e1.get())
    my_qr.svg('C:/Users/SHREYAS M/OneDrive/pictures/my_qr.svg',scale=8)
    my_qr.png('C:/Users/SHREYAS M/OneDrive/pictures/my_qr1.png',scale=6,module_color=[0,0,0,128],background=[0xff,0xcc,0xcc])
    my_qr.show()
    my_qr=my_qr.xbm(scale=10)
    my_image=tk.BitmapImage(data=my_qr)
    l1.config(image=my_image)
my_w.mainloop()