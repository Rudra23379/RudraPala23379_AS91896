import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title('My flags quiz')
root.geometry("800x600")

parent = tk.Tk()
parent.title("Application Title")

label = tk.Label(root, text='Welcome To My Flag Quiz', font=("Arial", 40))
label.pack(pady=20)

# Load and convert image
Homescreen_image = Image.open("images/Title_forest.jpg")
Homescreen_image=Homescreen_image.resize(800,600)
tk_image = ImageTk.PhotoImage(Homescreen_image)

background_label = tk.Label(root, image=tk_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Display image
image_label = tk.Label(root, image=tk_image)
image_label.image = tk_image
image_label.pack()

Label= tk.Label(root, text='My Flag Quiz', font=("Arial", 40))

parent.mainloop()

root.mainloop()