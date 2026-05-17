import tkinter as tk
import PIL.ImageTk

root = tk.Tk()
root.title("Homepage")
root.attributes("-fullscreen", True)
quitButton = tk.Button(root, text="Quit", command=root.destroy, padx=35, pady=25)
quitButton.place(x=85, y=100)

Helpbutton = tk.Button(root, text="Help", padx=35, pady=25)
Helpbutton.place(x=400, y=150)
root.mainloop()