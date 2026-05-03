from tkinter import Tk, messagebox

root = Tk()
root.withdraw()

device = "active"
temperatue = 31

if device == "active":
    if temperatue < 35:
        messagebox.showwarning("Warning", "High Temperature Alert!")
    else:
        messagebox.showinfo("Info", "Temperature Normal")
else:
    print("Device is Offline!")