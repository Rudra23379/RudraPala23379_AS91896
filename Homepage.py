import customtkinter as ctk
from PIL import Image, ImageTk


# --------Starter page-------------------------
class Flagquiz:
    def __init__(self, root):

        self.diff_image = None
        self.diff_page = None
        self.root = root
        self.root.after(0, lambda: root.state('zoomed'))

        # Track which page the user is currently on ("starter" or "diff")
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
        quit_button = ctk.CTkButton(self.bg_label, text="Quit", command=root.quit,
                                    text_color="#ffffff", corner_radius=27, width=160,
                                    height=40, bg_color="#c8e690", border_width=0,
                                    font=("CanvaSans", 22, "bold"), fg_color="#2d6349")
        quit_button.place(relx=0.06, rely=0.16, anchor="center")

        # Quiz button icon
        quit_icon = ctk.CTkButton(self.bg_label, text="⏻", width=64, height=64, corner_radius=32,
                                  command=root.quit, font=("CanvaSans", 36, "bold"),
                                  bg_color="#c8e690", hover_color="#ffffff", fg_color="#2d6349")
        quit_icon.place(relx=0.06, rely=0.08, anchor="center")

        # Help button icon
        help_icon = ctk.CTkButton(self.bg_label, text=" ? ", width=64, height=64, corner_radius=32,
                                  font=("CanvaSans", 36, "bold"), bg_color="#c8e690", hover_color="#ffffff",
                                  fg_color="#2d6349", command=self.help_page)
        help_icon.place(relx=0.94, rely=0.08, anchor="center")

        # Help button
        help_button = ctk.CTkButton(self.bg_label, text="Help", bg_color="#c8e690", hover_color="#ffffff",
                                    fg_color="#2d6349", font=("CanvaSans", 22, "bold"), corner_radius=32, width=160,
                                    height=40,
                                    command=self.help_page)
        help_button.place(relx=0.94, rely=0.16, anchor="center")

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

        # Update our current page tracker
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

    # METHOD FOR HELP SCREEN
    def help_page(self):
        # Hide whichever page layout elements are currently active
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
        self.help_title.place(relx=0.5, rely=0.15, anchor="center")

        # Text rules layout blocks
        rules_text = (
            "• Identify the Flag: Look at the image in the center and choose the correct\n"
            "country from the four options.\n\n"
            "• Watch the Timer: Depending on your difficulty, you will have unlimited time,\n"
            "10 seconds or 5 seconds to answer.\n\n"
            "• Navigation: Use the Next button to move forward.\n\n"
            "• Quit Anytime: If you need to stop, just hit the Power icon in the top left."
        )

        self.help_rules = ctk.CTkLabel(self.bg_label, text=rules_text, font=("CanvaSans", 20),
                                       text_color="#ffffff", justify="center")
        self.help_rules.place(relx=0.5, rely=0.5, anchor="center")

        # Go Back layout switch button
        self.back_button = ctk.CTkButton(self.bg_label, text="Go Back", corner_radius=32,
                                         width=200, height=60, fg_color="#475d5b", hover_color="#ffffff",
                                         text_color="#ffffff", font=("CanvaSans", 22, "bold"),
                                         command=self.close_help)
        self.back_button.place(relx=0.5, rely=0.85, anchor="center")

    # RETURN METHOD FROM HELP SCREEN
    def close_help(self):
        # Clean up rules page components
        self.help_title.place_forget()
        self.help_rules.place_forget()
        self.back_button.place_forget()

        # Restore the exact layout the user came from
        if self.current_page == "starter":
            self.bg_image = Image.open("images/firewatch.jpg")
            self.bg_image = ctk.CTkImage(light_image=self.bg_image, dark_image=self.bg_image,
                                         size=(self.screen_width, self.screen_height))
            self.bg_label.configure(image=self.bg_image)

            self.title_text.place(relx=0.46, rely=0.15, anchor="center")
            self.username.place(relx=0.5, rely=0.7, anchor="center")
            self.start_button.place(relx=0.49, rely=0.5, anchor="center")

        elif self.current_page == "diff":
            rice_bg = Image.open("images/Rice.jpg")
            self.diff_image = ctk.CTkImage(light_image=rice_bg, dark_image=rice_bg,
                                           size=(self.screen_width, self.screen_height))
            self.bg_label.configure(image=self.diff_image)

            self.easy_button.place(relx=0.25, rely=0.5, anchor="center")
            self.medium_button.place(relx=0.5, rely=0.5, anchor="center")
            self.hard_button.place(relx=0.75, rely=0.5, anchor="center")


if __name__ == "__main__":
    main_window = ctk.CTk()
    app = Flagquiz(main_window)
    main_window.mainloop()