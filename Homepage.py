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
title_text = ctk.CTkLabel(bg_label, text="Welcome to my flag quiz",
font=("Arial", 56, "bold"), text_color="#1a5c3a",fg_color="transparent",bg_color="transparent")
title_text.place(relx=0.5, rely=0.15, anchor="center")


quit_button = ctk.CTkButton(bg_label, text="Quit", command=root.quit, text_color="#ffffff", corner_radius=27, width=160, height=40,bg_color="transparent", border_width = 0)
quit_button.place(relx=0.06, rely=0.16, anchor="center")


quit_icon = ctk.CTkButton(bg_label,text="⏻", width=64, height=64,corner_radius=32, command=root.quit,font=("CanvaSans", 32, "bold"),bg_color="transparent", hover_color="#ffffff")
quit_icon.place(relx=0.06, rely=0.08, anchor="center")


help_icon = ctk.CTkButton(bg_label, text="?", width=64,height=64,corner_radius=32,font=("CanvaSans", 32, "bold"),bg_color="transparent",hover_color="#ffffff")
help_icon.place(relx=0.94, rely=0.08, anchor="center")



help_button = ctk.CTkButton(bg_label, text="Help",bg_color="transparent",hover_color="#ffffff" )
help_button.place(relx=0.94, rely=0.16, anchor="center")

username = ctk.CTkEntry(bg_label, placeholder_text="please enter your name here", width=320,height=50)
username.place(relx=0.5, rely=0.7, anchor="center")

start_button =ctk.CTkButton(bg_label, text="start", corner_radius= 27, width= 180 , height=50,bg_color="transparent",border_width = 0,)
start_button.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()