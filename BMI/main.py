from tkinter import * 
import tkinter as tk 
from tkinter import ttk
from PIL import Image,ImageTk


root=Tk()
root.title("BMI Calculator")
root.geometry("470x580+300+200")
#root.resizable(False,False)
root.configure(bg="#f0f1f5")

def BMI():
    h=float(Height.get())
    w=float(Weight.get())

    #convert height into meter
    m=h/100
    bmi=round(float(w/m**2),1) 
    #print(bmi)
    Label1.config(text=bmi)

    if bmi<18.5:
        Label2.config(text="Underweight!")
        Label3.config(text="you have lower weight than normal body")
    
    elif bmi>18.5 and bmi<25:
        Label2.config(text="Normal!")
        Label3.config(text="you have healthy body ")

    elif bmi>25 and bmi<30:
        Label2.config(text="overweight!")
        Label3.config(text="slightly overweight")

    else:
        Label2.config(text="obes!")
        Label3.config(text="health at risk if you not lose weight")



#icon
image_icon=PhotoImage(file="icon.png")
root.iconphoto(False,image_icon)


#top
top=PhotoImage(file="top.png")
top_image=Label(root,image=top,background='#f0f1f5')
top_image.place(x=-10,y=-10)

#bottom box
Label(root,width=72,height=18,bg="lightblue").pack(side=BOTTOM)

#two boxes 
box=PhotoImage(file="box.png")
Label(root,image=box).place(x=20,y=100)
Label(root,image=box).place(x=240,y=100)

#scale
scale=PhotoImage(file="scale.png")
Label(root,image=scale,bg="lightblue").place(x=20,y=310)

#slider
current_value=tk.DoubleVar()

def get_current_value():
    return '{: .2f}'.format(current_value.get())

def slider_changed(event):
    Height.set(get_current_value())

    size=int(float(get_current_value()))
    img=(Image.open("man.png"))
    resized_img=img.resize((50,10+size))
    photo2=ImageTk.PhotoImage(resized_img)
    man_img.config(image=photo2)
    man_img.place(x=70,y=550-size)
    man_img.image=photo2

#command to change bg color of scale 
style=ttk.Style()
style.configure("TScale",background="Black")
slider=ttk.Scale(root,from_=0,to=220,orient='horizontal',style="TScale",command=slider_changed,variable=current_value)
slider.place(x=80,y=250)


#slider2
current_value2 = tk.DoubleVar()

def get_current_value2():
    return '{: .2f}'.format(current_value2.get())

def slider_changed2(event):
    Weight.set(get_current_value2())

#command to change bg color of scale 
style2=ttk.Style()
style2.configure("TScale",background="Black")
slider2=ttk.Scale(root,from_=0,to=220,orient='horizontal',style="TScale",command=slider_changed2,variable=current_value2)
slider2.place(x=300,y=250)



#Entrybox
Height=StringVar()
Weight=StringVar()
height=Entry(root,textvariable=Height,width=5,font="arial 50",bg="#fff",fg='#000',bd=0,justify=CENTER)
height.place(x=35,y=160)
Height.set(get_current_value())

weight=Entry(root,textvariable=Weight,width=5,font="arial 50",bg="#fff",fg='#000',bd=0,justify=CENTER)
weight.place(x=255,y=160)
Weight.set(get_current_value2())

#maniamge
man_img=Label(root,bg="lightblue")
man_img.place(x=70,y=530)


Button(root,text="View Report",width=15,height=2,font="arial 10 bold",bg="#1f6e68",fg="white",command=BMI).place(x=280,y=340)

Label1=Label(root,font="arial 60 bold",bg="lightblue",fg="#fff")
Label1.place(x=125,y=305)

Label2=Label(root,font="arial 10 bold",bg="lightblue",fg="#3b3a3a")
Label2.place(x=280,y=430)

Label3=Label(root,font="arial 10 bold",bg="lightblue")
Label3.place(x=200,y=500)

root.mainloop()