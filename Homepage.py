import tkinter as tk
from PIL import Image, ImageTk


class Homescreen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("My flags quiz")
        self.root.geometry("800x600")

        # 1. Background Image
        img = Image.open("images/evenevenevenevenevenbetterhomepagesharp.png")
        img = img.resize((800, 600))
        self.tk_image = ImageTk.PhotoImage(img)

        # Use place to make it a true background
        self.background_label = tk.Label(self.root, image=self.tk_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)


        # 3. The Start Button (Placed on top of the image)
        self.start_button = tk.Button(
            self.root,
            text="Start Quiz",
            command=self.start_quiz,
            font=("Arial", 20),
            bg="green",
            fg="white",
            padx=20,
            pady=10

        )

        # Use .place() to put it exactly where you want it on the image
        # relx and rely use 0.0 to 1.0 (0.5 is exactly the middle)
        self.start_button.place(relx=0.5, rely=0.5, anchor="center")

        self.root.mainloop()

    def start_quiz(self):
        print("Quiz is starting!")


if __name__ == "__main__":
    Homescreen()
