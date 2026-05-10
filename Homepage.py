import tkinter as tk
import customtkinter as ctk  # Import the modern library
from PIL import Image, ImageTk


class Homescreen:
    def __init__(self):
        # Setup modern window
        self.root = tk.Tk()
        self.root.title("My flags quiz")
        self.root.geometry("800x600")

        # 1. Background Image (same as before)
        img = Image.open("images/evenevenevenevenevenbetterhomepagesharp.png").resize((2050, 1200))
        self.tk_image = ImageTk.PhotoImage(img)
        self.background_label = tk.Label(self.root, image=self.tk_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # 2. THE CURVED BUTTON (CustomTkinter)
        self.start_button = ctk.CTkButton(
            master=self.root,
            text="Start Quiz",
            command=self.start_quiz,
            corner_radius=32,  # High number = more curved/rounded
            width=140,  # Smaller width
            height=40,  # Smaller height
            fg_color="dark green",  # Button color
            hover_color="#ffffff",  # Darker green when hovering
            font=("Arial", 18)
        )

        # Place it on top of the image
        self.start_button.place(relx=0.5, rely=0.52, anchor="center")

        self.root.mainloop()

    def start_quiz(self):
        print("Quiz Started!")


if __name__ == "__main__":
    Homescreen()
