from tkinter import *
import time
from PIL import Image, ImageTk
root = Tk()
root.geometry("666x444")
root.title("Digital Clock")
root.config(bg="midnightblue")

def Time():
    curr_time = time.localtime()
    hr = curr_time.tm_hour
    min = curr_time.tm_min
    sec = curr_time.tm_sec
    label_hr.config(text=f"{hr:02d}", bg="black", fg="Lawngreen")
    label_min.config(text=f"{min:02d}", bg="black", fg="Lawngreen")
    label_sec.config(text=f"{sec:02d}", bg="black", fg="Lawngreen")
    root.after(1000, Time)


frame = Frame(root, bg="black")
frame.pack(padx=20, pady=100)

label_hr = Label(frame, text="12", bg="black", fg="Lawngreen", padx=10, pady=10, font=("Arial", 80, "bold"))
label_hr.grid(row=0, column=0, padx=10, pady=10)
label_colon1 = Label(frame, text=":", bg="black", fg="Lawngreen", padx=5, pady=5, font=("Arial", 80, "bold"))
label_colon1.grid(row=0, column=1)
label_min = Label(frame, text="12", bg="black", fg="Lawngreen", padx=10, pady=10, font=("Arial", 80, "bold"))
label_min.grid(row=0, column=2, padx=6, pady=10)
label_colon2 = Label(frame, text=":", bg="black", fg="Lawngreen", padx=5, pady=5, font=("Arial", 80, "bold"))
label_colon2.grid(row=0, column=3)
label_sec = Label(frame, text="12", bg="black", fg="Lawngreen", padx=10, pady=10, font=("Arial", 80, "bold"))
label_sec.grid(row=0, column=4, padx=10, pady=10)

Time()

root.mainloop()
