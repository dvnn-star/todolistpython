import tkinter 
from tkinter import *
from tkinter import ttk
task = ["haklaskoa","NASI","PADANG"]
def show_task():
    if not task:
        isi.set(f" \n belum ada tugas")
        isi2.set(f" \n belum ada tugas")
    else:
        isi.set(f"\n".join(f"{i}.{tasks}"for i,tasks in enumerate(task ,1)))
        isi2.set(f"\n".join(f"{i}.{tasks}"for i,tasks in enumerate(task ,1)))
def nambah_task():
    task.append(inputan.get())
    print(task)


def remove_task():
    print(task)
    try:
        
        task_terhapus = task.pop(i-1)
        print(f"sudah terhapus {task_terhapus} silahkan lanjutkan")
    except (IndexError,ValueError):
        print("invalid brow")

root =Tk()
root.title("MENU TO DO ")
mainframe = ttk.Frame(root,padding="10 10 12 12")
mainframe.grid(column=0,row=0,sticky=(N,W,E,S))
root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)

#main frame
ttk.Label(mainframe,text="MENU ").grid(column=2 , row=1 ,sticky=(W,E))
ttk.Label(mainframe,text="1.lihat to-do list").grid(column=2 ,row=2,sticky=(W,E))
ttk.Label(mainframe,text="2.Nambah Task").grid(column=2 ,row=3,sticky=(W,E))
ttk.Label(mainframe,text="3.Remove Task").grid(column=2 ,row=4,sticky=(W,E))
ttk.Button(mainframe,text="1",command=lambda:(Frame2.tkraise(),show_task())).grid(row=6 ,column=1,sticky=W)
ttk.Button(mainframe,text="2",command=lambda:frame3.tkraise()).grid(row=6,column=2,sticky=(W,E))
ttk.Button(mainframe,text="3",command=lambda:(frame4.tkraise(),show_task())).grid(row=6,column=3,sticky=(W,E))


#frame 2

Frame2 = ttk.Frame(root,padding="10 10 12 12")
Frame2.grid(column=0,row=0,sticky=(N,W,E,S))
ttk.Label(Frame2,text="TO DO LIST HARI INI").grid(row=1,column=2,sticky=(W,E))
isi = StringVar()
ttk.Label(Frame2,textvariable=isi).grid(row=2,column=2,sticky=W)
ttk.Button(Frame2,text="BACK",command=lambda:mainframe.tkraise()).grid(row=4,column=1,sticky=(W,E))
 
#frame 3
frame3 = ttk.Frame(root,padding="14 14 14 14")
frame3.grid(column=0,row=0,sticky=(N,W,E,S))
ttk.Label(frame3,text="nambah task apaa?").grid(row=1,column=2,sticky=(W,E))
inputan = StringVar()
inputan_handle = ttk.Entry(frame3,width=10,textvariable=inputan)
inputan_handle.grid(row=2,column=2,sticky=(W,E))
ttk.Button(frame3,text='MASUKKAN',command=lambda:(nambah_task(),inputan_handle.delete(0,"end"))).grid(row=3,column=2,sticky=(W,E))
ttk.Button(frame3,text="BACK",command=lambda:mainframe.tkraise()).grid(row=5,column=1,sticky=(W,E))


#frame4
def update_button():
    for widget in frame4.winfo_children():
        if isinstance(widget, ttk.Button) and widget.cget("text") not in ["BACK",'UPDATE']:
            widget.destroy()
    for i in range(1,len(task) + 1):
        ttk.Button(frame4,text=str(i),command=lambda index=i:button_clicked(index)).grid(row=3 ,column=i,padx=10)

def button_clicked(index):
     task.pop(index - 1)
     print(f"Tombol {index} ditekan!")
     show_task()
     update_button()
    
    

frame4 = ttk.Frame(root,padding="14 14 14 14")
frame4.grid(column=0,row=0,sticky=(N,W,E,S))
ttk.Label(frame4,text="MAU REMOVE TASK APAA?").grid(row=1,column=2,sticky=(W,E))
isi2 = StringVar()
ttk.Label(frame4,textvariable=isi2).grid(row=2,column=2,sticky=W)
for i in range(1,len(task)+1):
    ttk.Button(frame4,text=str(i),command=lambda index=i : button_clicked(index)).grid(row=3 ,column=i)
    
ttk.Button(frame4,text="BACK",command=lambda:mainframe.tkraise()).grid(row=4,column=1,sticky=(W,E))
ttk.Button(frame4,text="UPDATE",command=lambda:update_button()).grid(row=4,column=3,sticky=(W,E))







frames=[mainframe,Frame2,frame3,frame4]
for child in frames:
    for frame in child.winfo_children():
        frame.grid_configure(padx=5, pady=5)
mainframe.tkraise()
root.mainloop()
