from tkinter import *

root = Tk()
root.title("Calulator")
root.geometry("400x600")
root.configure(bg="white")
root.resizable(False, False)
l1 = Label(root, text="Calculator", font=("Comic Sans MS", 24, "bold"), bg="black", fg="white")
l1.pack(pady=20)
l2 = Label(root, text="Enter the Numbers:", font=("Comic Sans MS", 24, "bold"), bg="black", fg="white")
l2.pack(pady=20)
num1 = Label(root, font=("Comic Sans MS", 24), bg="black", fg="white", bd=2, relief=SUNKEN)
num1.pack(pady=10)
num2 = Label(root, font=("Comic Sans MS", 24), bg="black", fg="white", bd=2, relief=SUNKEN)
num2.pack(pady=10)

root.mainloop()