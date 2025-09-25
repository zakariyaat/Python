import tkinter as tk
from time import strftime

def time():
    string = strftime("%H:%M:%S %p")  # 24-hour format with AM/PM
    label.config(text=string)
    label.after(1000, time)  # update every 1 second

# GUI setup
root = tk.Tk()
root.title("Digital Clock")

label = tk.Label(root, font=("Helvetica", 60, "bold"), background="black", foreground="cyan")
label.pack(anchor="center")

time()
root.mainloop()
