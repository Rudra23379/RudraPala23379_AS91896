import customtkinter as ctk
from PIL import Image, ImageTk

#--------Starter page-------------------------
class Flagquiz:
    def __init__(self,root):

        self.diff_image = None
        self.diff_page = None
        self.root = root
        self.root.after(0, lambda: root.state('zoomed'))

        #display dimensions
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()


        #background image
        self.bg_image = Image.open("images/firewatch.jpg")
        self.bg_image = ctk.CTkImage(light_image=self.bg_image, dark_image=self.bg_image, size=(self.screen_width, self.screen_height))
        self.bg_label = ctk.CTkLabel(root, image=self.bg_image, text="")
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Title
        root.title("My Flag Quiz")
        self.title_text = ctk.CTkLabel(self.bg_label, text="Welcome To My Flag Quiz",
                                  font=("CanvaSans", 56, "bold"), text_color="#1a5c3a", fg_color="transparent",
                                  bg_color="#c8e690")
        self.title_text.place(relx=0.46, rely=0.15, anchor="center")

        #Quit button
        quit_button = ctk.CTkButton(self.bg_label, text="Quit", command=root.quit,
                                    text_color="#ffffff", corner_radius=27, width=160,
                                    height=40, bg_color="#c8e690", border_width=0,
                                    font=("CanvaSans", 22, "bold"), fg_color="#2d6349")
        quit_button.place(relx=0.06, rely=0.16, anchor="center")


        #Quiz button icon
        quit_icon = ctk.CTkButton(self.bg_label, text="⏻", width=64, height=64, corner_radius=32,
                                  command=root.quit, font=("CanvaSans", 36, "bold"),
                                  bg_color="#c8e690", hover_color="#ffffff", fg_color="#2d6349")
        quit_icon.place(relx=0.06, rely=0.08, anchor="center")
        #help button
        help_icon = ctk.CTkButton(self.bg_label, text=" ? ", width=64, height=64, corner_radius=32,
                                  font=("CanvaSans", 36, "bold"), bg_color="#c8e690", hover_color="#ffffff",
                                  fg_color="#2d6349")
        help_icon.place(relx=0.94, rely=0.08, anchor="center")
        #Help button icon
        help_button = ctk.CTkButton(self.bg_label, text="Help", bg_color="#c8e690", hover_color="#ffffff",
                                    fg_color="#2d6349", font=("CanvaSans", 22, "bold"),corner_radius= 32, width=160,height=40,
                                    )
        help_button.place(relx=0.94, rely=0.16, anchor="center")

        # Username Input
        self.username = ctk.CTkEntry(self.bg_label, placeholder_text="please enter your name here",
                                width=320, height=50, justify="center", corner_radius=32, text_color="#ffffff",
                                placeholder_text_color="#ffffff", fg_color="#2d6349", bg_color="#0b3835")
        self.username.place(relx=0.5, rely=0.7, anchor="center")
        #start button
        self.start_button = ctk.CTkButton(self.bg_label, text="start", corner_radius=32, width=220, height=70, bg_color="#2d6349",
         border_width=0,fg_color="#1a5156", font=("Canvasans", 22, "bold", ),command=self.diff)
        self.start_button.place(relx=0.49, rely=0.5, anchor="center")

    def diff(self):
            # Username return
            player_name = self.username.get().strip()
            if player_name in("","please enter your name here",):
                print("please enter a vaild name")
                return

            #Unpacking widgets
            self.title_text.place_forget()
            self.username.place_forget()
            self.start_button.place_forget()

            #New background image
            self.diff_image = ImageTk.PhotoImage(image=Image.open("images/Rice.jpg"))
            self.bg_label.configure(image=self.diff_image)

            easy_button = ctk.CTkButton(self.bg_label, text="Easy", width=120, height=250, corner_radius=32,)
            easy_button.place(relx=0.3, rely=0.15, anchor="center")




if __name__ == "__main__":
    main_window = ctk.CTk()
    app = Flagquiz(main_window)
    main_window.mainloop()