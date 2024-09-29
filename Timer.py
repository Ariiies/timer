from tkinter import *
from tkinter import messagebox as mb
window = Tk()
window.title("Timer")
window.geometry("300x200")
window.resizable(0,0)
# Entry's and buttons
data_h, data_m, data_s = IntVar(), IntVar(), IntVar()
entry_h = Entry(window, textvariable=data_h)
entry_m = Entry(window, textvariable=data_m)
entry_s = Entry(window, textvariable=data_s)
entry_h.config(width=5)
entry_m.config(width=5)
entry_s.config(width=5)
hrs_label = Label(window, text="Hrs.") 
min_label = Label(window, text="Min.") 
seg_label = Label(window, text="Seg.") 
timer_label = Label(window, text="00:00:00")
##### function to show's entry's 
def ShowEntry(flag = True):
    if flag:
        entry_h.place(x=55, y=70)
        entry_m.place(x=130, y=70)
        entry_s.place(x=205, y=70)
        hrs_label.place(x=87, y = 70)
        min_label.place(x=162, y = 70)
        seg_label.place(x=237, y = 70)
        timer_label.place_forget()
    else:
        entry_h.place_forget()
        entry_m.place_forget()
        entry_s.place_forget()
        hrs_label.place_forget()
        min_label.place_forget()
        seg_label.place_forget()
        timer_label.place(x=127, y=70)
#### yimer functionality
procesTimer= None
def StartTimer(h=0, m=0, s=0):
    global procesTimer, hour, min, sec
    # Some verifications
    if h == 0 and m == 0 and s ==0:
        timer_label['text'] = ("00")+":"+("00")+":"+("00")
        try:
            procesTimer=timer_label.after_cancel(procesTimer)
        except:
            mb.showinfo("Alert!", "Introduce some valor, can't initializing in 0")
            return None
        mb.showinfo("Alert!", "Time Over!")
        ShowEntry()
        return None
    if s == 0:
        s=59
        if m!=0:
            m=m-1
        if m == 0:
            if h!=0:
                h=h-1
                m=59
            if h == 0:
                h=0
    # Stilyzing 
    if (len(str(h))<2):
        sh="0"
    else:
        sh=""
    if (len(str(m))<2):
        sm="0"
    else:
        sm=""
    if (len(str(s))<2):
        ss="0"
    else:
        ss=""
    # Tag for show the timer in the screen
    timer_label['text'] = (sh+str(h))+":"+(sm+str(m))+":"+(ss+str(int(s)))
    ShowEntry(False)
     # initialicing the count down
    procesTimer=timer_label.after(1000, StartTimer, (h), (m), (s-1))
# function to stop the timer
def CancelTimer():
    global procesTimer
    try:
        timer_label.after_cancel(procesTimer)
        ShowEntry()
    except:
        mb.showerror("Error", "Imposible Cancel")
ShowEntry()
fun = lambda: StartTimer(int(data_h.get()), int(data_m.get()), int(data_s.get()))
btn_start = Button(window, text="Start", command=fun).place(x=130, y = 120)
btn_cnacel = Button(window, text="Cancel", command=CancelTimer).place(x=124, y=150)
window.mainloop()