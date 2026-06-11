import customtkinter as ctk
from PIL import Image, ImageTk


# --------Starter page-------------------------
class Flagquiz:
    def __init__(self, root):

        self.diff_image = None
        self.diff_page = None
        self.root = root
        self.root.after(0, lambda: root.state('zoomed'))

        # page tracker
        self.current_page = "starter"

        # Display dimensions
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()

        # Background image
        self.bg_image = Image.open("images/firewatch.jpg")
        self.bg_image = ctk.CTkImage(light_image=self.bg_image, dark_image=self.bg_image,
                                     size=(self.screen_width, self.screen_height))
        self.bg_label = ctk.CTkLabel(root, image=self.bg_image, text="")
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Title
        root.title("My Flag Quiz")
        self.title_text = ctk.CTkLabel(self.bg_label, text="Welcome To My Flag Quiz",
                                       font=("CanvaSans", 56, "bold"), text_color="#1a5c3a", fg_color="transparent",
                                       bg_color="#c8e690")
        self.title_text.place(relx=0.46, rely=0.15, anchor="center")

        # Quit button
        self.quit_button = ctk.CTkButton(self.bg_label, text="Quit", command=root.quit,
                                    text_color="#ffffff", corner_radius=27, width=160,
                                    height=40, bg_color="#c8e690", border_width=0,
                                    font=("CanvaSans", 22, "bold"), fg_color="#2d6349")
        self.quit_button.place(relx=0.06, rely=0.16, anchor="center")

        # Quiz button icon
        self.quit_icon = ctk.CTkButton(self.bg_label, text="⏻", width=64, height=64, corner_radius=32,
                                  command=root.quit, font=("CanvaSans", 36, "bold"),
                                  bg_color="#c8e690", hover_color="#ffffff", fg_color="#2d6349")
        self.quit_icon.place(relx=0.06, rely=0.08, anchor="center")

        # Help button icon
        self.help_icon = ctk.CTkButton(self.bg_label, text=" ? ", width=64, height=64, corner_radius=32,
                                  font=("CanvaSans", 36, "bold"), bg_color="#c8e690", hover_color="#ffffff",
                                  fg_color="#2d6349", command=self.help_page)
        self.help_icon.place(relx=0.94, rely=0.08, anchor="center")

        # Help button
        self.help_button = ctk.CTkButton(self.bg_label, text="Help", bg_color="#c8e690", hover_color="#ffffff",
                                    fg_color="#2d6349", font=("CanvaSans", 22, "bold"), corner_radius=32, width=160,
                                    height=40,
                                    command=self.help_page)
        self.help_button.place(relx=0.94, rely=0.16, anchor="center")

        # Username Input
        self.username = ctk.CTkEntry(self.bg_label, placeholder_text="please enter your name here",
                                     width=320, height=50, justify="center", corner_radius=32, text_color="#ffffff",
                                     placeholder_text_color="#ffffff", fg_color="#2d6349", bg_color="#0b3835")
        self.username.place(relx=0.5, rely=0.7, anchor="center")

        # Start button
        self.start_button = ctk.CTkButton(self.bg_label, text="start", corner_radius=32, width=220, height=70,
                                          bg_color="#2d6349",
                                          border_width=0, fg_color="#1a5156", font=("Canvasans", 22, "bold"),
                                          command=self.diff)
        self.start_button.place(relx=0.49, rely=0.5, anchor="center")

    def diff(self):
        # Username return
        player_name = self.username.get().strip()
        if player_name in ("", "please enter your name here"):
            print("please enter a vaild name")
            return

        # Update page tracker
        self.current_page = "diff"

        # Unpacking starter page widgets
        self.title_text.place_forget()
        self.username.place_forget()
        self.start_button.place_forget()

        # New background image
        rice_bg = Image.open("images/Rice.jpg")
        self.diff_image = ctk.CTkImage(light_image=rice_bg, dark_image=rice_bg,
                                       size=(self.screen_width, self.screen_height))
        self.bg_label.configure(image=self.diff_image)

        # Show difficulty options
        self.easy_button = ctk.CTkButton(self.bg_label, text="Easy", width=180, height=250, corner_radius=32,
                                         font=("CanvaSans", 28, "bold"), fg_color="#1a5156",
                                         command=lambda: self.start_quiz("Easy"))
        self.easy_button.place(relx=0.25, rely=0.5, anchor="center")

        self.medium_button = ctk.CTkButton(self.bg_label, text="Medium", width=180, height=250, corner_radius=32,
                                           font=("CanvaSans", 28, "bold"), fg_color="#1a5156",
                                           command=lambda: self.start_quiz("Medium"))
        self.medium_button.place(relx=0.5, rely=0.5, anchor="center")

        self.hard_button = ctk.CTkButton(self.bg_label, text="Hard", width=180, height=250, corner_radius=32,
                                         font=("CanvaSans", 28, "bold"), fg_color="#1a7556",
                                         command=lambda: self.start_quiz("Hard"))
        self.hard_button.place(relx=0.75, rely=0.5, anchor="center")

    def start_quiz(self, difficulty):
        print(f"Starting quiz on {difficulty} mode")
        self.easy_button.place_forget()
        self.medium_button.place_forget()
        self.hard_button.place_forget()

    #  help page
    def help_page(self):
        # Hide whichever page layout elements are currently active

        # Hide Help/Quit buttons
        self.help_button.place_forget()
        self.help_icon.place_forget()
        self.quit_button.place_forget()
        self.quit_icon.place_forget()

        if self.current_page == "starter":
            self.title_text.place_forget()
            self.username.place_forget()
            self.start_button.place_forget()
        elif self.current_page == "diff":
            self.easy_button.place_forget()
            self.medium_button.place_forget()
            self.hard_button.place_forget()

        # Change background configuration to match the dark color mockup
        self.bg_label.configure(image="", fg_color="#134e4a")

        # Add "How to play" title
        self.help_title = ctk.CTkLabel(self.bg_label, text="How to play",
                                       font=("CanvaSans", 56, "bold"), text_color="#ffffff")
        self.help_title.place(relx=0.5, rely=0.13, anchor="center")

        # Help page text

        # Bullet 1
        self.rule1_header = ctk.CTkLabel(self.bg_label, text="• Identify the Flag:", font=("CanvaSans", 24, "bold"),
                                         text_color="#ffffff")
        self.rule1_header.place(relx=0.5, rely=0.21, anchor="center")
        self.rule1_body = ctk.CTkLabel(self.bg_label,
                                       text="Look at the image in the center and choose the correct country from the four options.",
                                       font=("CanvaSans", 20), text_color="#ffffff")
        self.rule1_body.place(relx=0.5, rely=0.25, anchor="center")

        # Bullet 3
        self.rule2_header = ctk.CTkLabel(self.bg_label, text="• Watch the Timer:", font=("CanvaSans", 24, "bold"),
                                         text_color="#ffffff")
        self.rule2_header.place(relx=0.5, rely=0.43, anchor="center")
        self.rule2_body = ctk.CTkLabel(self.bg_label,
                                       text="Depending on your difficulty, you will have unlimited time, 10 seconds or 5 seconds to answer.",
                                       font=("CanvaSans", 20), text_color="#ffffff")
        self.rule2_body.place(relx=0.5, rely=0.47, anchor="center")

        # Bullet 4
        self.rule3_header = ctk.CTkLabel(self.bg_label, text="• Navigation:", font=("CanvaSans", 24, "bold"),
                                         text_color="#ffffff")
        self.rule3_header.place(relx=0.5, rely=0.54, anchor="center")
        self.rule3_body = ctk.CTkLabel(self.bg_label, text="Use the Next button to move forward.",
                                       font=("CanvaSans", 20), text_color="#ffffff")
        self.rule3_body.place(relx=0.5, rely=0.58, anchor="center")

        # Bullet 5
        self.rule4_header = ctk.CTkLabel(self.bg_label, text="• Quit Anytime:", font=("CanvaSans", 24, "bold"),
                                         text_color="#ffffff")
        self.rule4_header.place(relx=0.5, rely=0.65, anchor="center")
        self.rule4_body = ctk.CTkLabel(self.bg_label,
                                       text="If you need to stop, just hit the Power icon in the top left.",
                                       font=("CanvaSans", 20), text_color="#ffffff")
        self.rule4_body.place(relx=0.5, rely=0.69, anchor="center")

        # Bullet 6
        self.rule5_header = ctk.CTkLabel(self.bg_label, text="• Score System:", font=("CanvaSans", 24, "bold"),
                                         text_color="#ffffff")
        self.rule5_header.place(relx=0.5, rely=0.75, anchor="center")
        self.rule5_body = ctk.CTkLabel(self.bg_label,
                                       text="Your score will be shown at the end of the quiz.",
                                       font=("CanvaSans", 20), text_color="#ffffff")
        self.rule5_body.place(relx=0.5, rely=0.8, anchor="center")
        # Bullet 2

        self.rule6_header = ctk.CTkLabel(self.bg_label, text="• Selecting an Answer:", font=("CanvaSans", 24, "bold"),
                                         text_color="#ffffff")
        self.rule6_header.place(relx=0.5, rely=0.32, anchor="center")
        self.rule6_body = ctk.CTkLabel(self.bg_label, text="When you click an option, the button will change colour to show your selection has been registered.",
                                       font=("CanvaSans", 20), text_color="#ffffff")
        self.rule6_body.place(relx=0.5, rely=0.36, anchor="center")

        # Go Back layout switch button
        self.back_button = ctk.CTkButton(self.bg_label, text="Go Back", corner_radius=32,
                                         width=200, height=60, fg_color="#475d5b", hover_color="#ffffff",
                                         text_color="#ffffff", font=("CanvaSans", 22, "bold"),
                                         command=self.close_help)
        self.back_button.place(relx=0.5, rely=0.9, anchor="center")



    # return from help screen
    def close_help(self):
        # Clean up rules page components
        self.help_title.place_forget()
        self.back_button.place_forget()

        # Clear all text from active memory
        self.rule1_header.place_forget()
        self.rule1_body.place_forget()
        self.rule2_header.place_forget()
        self.rule2_body.place_forget()
        self.rule3_header.place_forget()
        self.rule3_body.place_forget()
        self.rule4_header.place_forget()
        self.rule4_body.place_forget()
        self.rule5_header.place_forget()
        self.rule5_body.place_forget()
        self.rule6_header.place_forget()
        self.rule6_body.place_forget()


        # Restore the exact layout the user came from
        if self.current_page == "starter":
            self.bg_image = Image.open("images/firewatch.jpg")
            self.bg_image = ctk.CTkImage(light_image=self.bg_image, dark_image=self.bg_image,
                                         size=(self.screen_width, self.screen_height))
            self.bg_label.configure(image=self.bg_image)

            self.title_text.place(relx=0.46, rely=0.15, anchor="center")
            self.username.place(relx=0.5, rely=0.7, anchor="center")
            self.start_button.place(relx=0.49, rely=0.5, anchor="center")
            self.quit_button.place(relx=0.06, rely=0.16, anchor="center")
            self.quit_icon.place(relx=0.06, rely=0.08, anchor="center")

            self.help_button.place(relx=0.94, rely=0.16, anchor="center")
            self.help_icon.place(relx=0.94, rely=0.08, anchor="center")

        elif self.current_page == "diff":
            rice_bg = Image.open("images/Rice.jpg")
            self.diff_image = ctk.CTkImage(light_image=rice_bg, dark_image=rice_bg,
                                           size=(self.screen_width, self.screen_height))
            self.bg_label.configure(image=self.diff_image)

            self.easy_button.place(relx=0.25, rely=0.5, anchor="center")
            self.medium_button.place(relx=0.5, rely=0.5, anchor="center")
            self.hard_button.place(relx=0.75, rely=0.5, anchor="center")
            self.quit_button.place(relx=0.06, rely=0.16, anchor="center")
            self.quit_icon.place(relx=0.06, rely=0.08, anchor="center")

            self.help_button.place(relx=0.94, rely=0.16, anchor="center")
            self.help_icon.place(relx=0.94, rely=0.08, anchor="center")


if __name__ == "__main__":
    main_window = ctk.CTk()
    app = Flagquiz(main_window)
    main_window.mainloop()
