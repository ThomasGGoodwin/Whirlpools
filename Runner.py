from Whirl_Funcs import *
import tkinter as tk
#Type function down below then run (refer to README.txt for use)
color = False
lamp = False
prev = False
def check_color():
    global color
    color = not color
def check_lamp():
    global lamp
    lamp = not lamp
def check_prev():
    global prev
    prev = not prev

def go(event):
    update_txt()
    n = int(Ent_n.get())
    rho = float(Ent_rho.get())
    phi = float(Ent_phi.get())
    base = float(Ent_base.get())
    iters = int(Ent_iters.get())
    colors = Ent_colors.get().split(",")
    backcol=""
    if(Ent_back.get()==""):
        backcol="#cccccc"
    else:
        backcol=Ent_back.get()
    startx=0
    if color:
        startx=540
        if Ent_startx.get()!="":
            startx=int(Ent_startx.get())
    else:
        startx=600
        if Ent_startx.get()!="":
            startx=int(Ent_startx.get())
    starty=0
    if color:
        starty=315
        if Ent_starty.get()!="":
            startx=int(Ent_starty.get())
    else:
        starty=-300
        if Ent_starty.get()!="":
            startx=int(Ent_starty.get())
    rad=350
    if Ent_rad.get()!="":
        rad=float(Ent_rad.get())
    if color:
        if prev:
            preview(n,rho,phi,iters,colors,lamp=lamp,rad=rad)
        else:
            colored(n,rho,phi,base,iters,colors,backcol,startx,starty,lamp)
    else:
        if prev:
            colorless_preview(n,rho,phi,iters,lamp=lamp,rad=rad)
        else:
            colorless(n,rho,phi,base,iters,startx,starty,lamp)
    #stuff

def update_txt():
    file = open("save.txt","w")
    file.write(Ent_n.get()+"\n")
    file.write(Ent_rho.get()+"\n")
    file.write(Ent_phi.get()+"\n")
    file.write(Ent_base.get()+"\n")
    file.write(Ent_iters.get()+"\n")
    file.write(Ent_colors.get()+"\n")
    file.write(Ent_back.get()+"\n")
    file.write(Ent_startx.get()+"\n")
    file.write(Ent_starty.get()+"\n")
    file.write(Ent_rad.get())

def fill_save():
    file = open("save.txt","r")
    data = list(file)
    for i in range(0,len(data)):
        data[i] = data[i][0:len(data[i])-1]
    Ent_n.insert(0,data[0])
    Ent_rho.insert(0,data[1])
    Ent_phi.insert(0,data[2])
    Ent_base.insert(0,data[3])
    Ent_iters.insert(0,data[4])
    Ent_colors.insert(0,data[5])
    Ent_back.insert(0,data[6])
    Ent_startx.insert(0,data[7])
    Ent_starty.insert(0,data[8])

gui = tk.Tk()
label1 = tk.Label(text="Main options")
label1.pack()
frame1 = tk.Frame(master = gui)
frame1['borderwidth'] = (5)
Lab_n = tk.Label(master= frame1, text = "n", width = 3,height=1)
Lab_n.grid(row=0,column=0)
Ent_n = tk.Entry(master=frame1,width = 3)
Ent_n.grid(row=1,column=0)
Lab_rho = tk.Label(master = frame1, text = "rho",height=1)
Lab_rho.grid(row=0,column=1)
Ent_rho = tk.Entry(master=frame1,width = 3)
Ent_rho.grid(row=1,column=1)
Lab_phi = tk.Label(master=frame1, text = "phi",width=3,height=1)
Lab_phi.grid(row=0,column=2)
Ent_phi = tk.Entry(master=frame1,width=3)
Ent_phi.grid(row=1,column=2)
Fill_Label = tk.Label(master=frame1,width=1,height=1)
Fill_Label.grid(row=0,column=3)
Fill_Label.grid(row=1,column=3)
Lab_base = tk.Label(master=frame1,text="base",height=1)
Lab_base.grid(row=0,column=4)
Ent_base = tk.Entry(master=frame1,width=4)
Ent_base.grid(row=1,column=4)
Lab_iters = tk.Label(master=frame1,text="iters",height=1,padx=5)
Lab_iters.grid(row=0,column=5)
Ent_iters = tk.Entry(master=frame1,width=4)
Ent_iters.grid(row=1,column=5)
frame1.pack()

label2 = tk.Label(text="Coloring options")
label2.pack()
frame2 = tk.Frame(master = gui)
frame2['borderwidth'] = (5)
Lab_col = tk.Label(master=frame2,text="colors?",height=1)
Lab_col.grid(row=0,column=0)
Check_col = tk.Checkbutton(master=frame2,command=check_color)
Check_col.grid(row=1,column=0)
Lab_back = tk.Label(master=frame2,text="background color",height=1)
Lab_back.grid(row=0,column=1)
Ent_back = tk.Entry(master=frame2,width=7)
Ent_back.grid(row=1,column=1)
Lab_colors = tk.Label(master=frame2,text="color list",height=1)
Lab_colors.grid(row=0,column=2)
Ent_colors = tk.Entry(master=frame2,width=35)
Ent_colors.grid(row=1,column=2)
frame2.pack()

label3 = tk.Label(text="Other options")
label3.pack()
frame3 = tk.Frame(master=gui)
frame3['borderwidth'] = (5)
Lab_lamp = tk.Label(master=frame3,text="Lampshade",height=1)
Lab_lamp.grid(row=0,column=0)
var=0
Check_lamp = tk.Checkbutton(master=frame3,command=check_lamp,variable=var)
Check_lamp.grid(row=1,column=0)
Lab_startx = tk.Label(master=frame3,text="startx",height=1)
Lab_startx.grid(row=0,column=2)
Ent_startx = tk.Entry(master=frame3,width=5)
Ent_startx.grid(row=1,column=2)
Lab_starty = tk.Label(master=frame3,text="starty",height=1,padx=5)
Lab_starty.grid(row=0,column=3)
Ent_starty = tk.Entry(master=frame3,width=5)
Ent_starty.grid(row=1,column=3)
Lab_prev = tk.Label(master=frame3,text="Preview?",height=1)
Lab_prev.grid(row=0,column=1)
Check_prev= tk.Checkbutton(master=frame3,command=check_prev)
Check_prev.grid(row=1,column=1)
Lab_rad = tk.Label(master=frame3,text="rad",height=1)
Lab_rad.grid(row=0,column=4)
Ent_rad = tk.Entry(master=frame3,width=4)
Ent_rad.grid(row=1,column=4)
frame3.pack()

button = tk.Button(master=gui,text="Go!",width=5,height=2,bg="yellow")
button.bind("<Button-1>",go)
button.pack()
fill_save()
gui.mainloop()