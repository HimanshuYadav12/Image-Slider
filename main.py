from tkinter import*
from PIL import ImageTk,Image
import time
class Slider:
    def __init__(self,root):
        self.root=root
        self.root.title("Slider")
        self.root.geometry("1350x700+0+0")

        #=========Open image===========
        self.my_pic1=Image.open("1.jpg")
        self.my_pic2=Image.open("2.jpg")
        #resize
        self.resized=self.my_pic1.resize((1100,600),Image.ANTIALIAS)
        self.image1=ImageTk.PhotoImage(self.resized)

        self.resized=self.my_pic2.resize((1100,600), Image.ANTIALIAS)
        self.image2=ImageTk.PhotoImage(self.resized)

        #=============Images======
        Frame_slider=Frame(self.root)
        Frame_slider.place(x=150,y=50,width=1100,height=600)
        self.lbl1=Label(Frame_slider,image=self.image1,bd=0)
        self.lbl1.place(x=0,y=0)

        self.lbl2=Label(Frame_slider,image=self.image2,bd=0)
        self.lbl2.place(x=1100,y=0)
        self.x=1100
        self.slider_func()

    def slider_func(self):
        self.x-=1
        if self.x==0:
            self.x=1100
            time.sleep(1)
            #============Swap============
            self.new_im=self.image1
            self.image1=self.image2
            self.image2=self.new_im
            self.lbl1.config(image=self.image1)
            self.lbl2.config(image=self.image2)
        self.lbl2.place(x=self.x,y=0)
        self.lbl2.after(1,self.slider_func)

root=Tk()
obj=Slider(root)
root.mainloop()