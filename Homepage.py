import customtkinter as ctk
from PIL import Image, ImageTk

root= ctk.CTk()
root.after(0, lambda: root.state('zoomed'))

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

bg_image = Image.open("images/firewatch.jpg")
bg_image = ctk.CTkImage(light_image=bg_image, dark_image=bg_image, size=(screen_width, screen_height))
bg_label = ctk.CTkLabel(root, image=bg_image, text="")
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

root.title("My Flag Quiz")
title_text = ctk.CTkLabel(root, text="Welcome to my flag quiz",
font=("Arial", 56, "bold"), text_color="#1a5c3a",fg_color="transparent")
title_text.place(x=600, y=90)


quit_button = ctk.CTkButton(root, text="Quit", command=root.quit, text_color="#ffffff", corner_radius=27, width=160, height=40,)
quit_button.place(x=15, y=35)


quit_icon = ctk.CTkButton(root,text="⏻", width=64, height=64,corner_radius=32, command=root.quit,font=("CanvaSans", 32, "bold"))
quit_icon.place(x=300, y=400)

help_icon = ctk.CTkButton(root, text="?", width=64,height=64,corner_radius=32,font=("CanvaSans", 32, "bold"),)
help_icon.place(x=200, y=200)



help_button = ctk.CTkButton(root, text="Help" )
help_button.place(x=1400, y=35)

username = ctk.CTkEntry(root, placeholder_text="please enter your name here", width=320,height=50)
username.place(x=400, y=450)


root.mainloop()