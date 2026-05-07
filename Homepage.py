import tkinter as tk
from PIL import Image, ImageTk





class Homescreen:
    root = tk.Tk()
    root.title("My flags quiz")
    root.geometry("800x600")

    # Load and convert image
    homescreen_image = Image.open("images/evenevenevenevenevenbetterhomepagesharp.png")
    homescreen_image = homescreen_image.resize((1950, 1200))
    tk_image = ImageTk.PhotoImage(homescreen_image)

    background_label = tk.Label(root, image=tk_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Display image
    image_label = tk.Label(root, image=tk_image)
    image_label.image = tk_image
    image_label.pack()

    canvas = tk.Canvas(root, width=800, height=600, highlightthickness=0)
    canvas.pack()
    canvas.create_image(0, 0, image=tk_image, anchor="nw")

    label = tk.Label(root, text="Welcome To My Flag Quiz", font=("Arial", 40))
    label.pack(pady=20)

    Label = tk.Label(root, text="My Flag Quiz", font=("Arial", 40))





    root.mainloop()
