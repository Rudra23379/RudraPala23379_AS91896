# the import statement
import tkinter as tk
root = tk.Tk()

root.title('My flages quiz')

label = tk.Label(root, text='Welcome To My Flag Quiz', font=("Arial", 40))
label.pack(pady=20)

try:
photo = tk.PhotoImage(file='./images/Title_forest.jpg.png')

image_label = tk.Label(root, image=photo)
image_label.pack()

root.mainloop()