import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import messagebox


# --------Starter page-------------------------
class Flagquiz:
    def __init__(self, root):

        # page tracker
        self.current_page = "starter"

        self.current_question_index = 0
        self.score = 0
        self.selected_answer = None

        # timer tracking values
        self.time_left = 0
        self.timer_id = None
        self.difficulty = None
        self.timer_label = None

        self.questions = [
            {"image": "images/Flag_of_Canada.png", "options": ["Canada", "Red Cross", "Peru", "Japan"],
             "correct": "Canada"},
            {"image": "images/japan.jpg", "options": ["South Korea", "Palau", "Japan", "China"], "correct": "Japan"},
            {"image": "images/Flag_of_France.png", "options": ["Italy", "France", "Russia", "Netherlands"],
             "correct": "France"},
            {"image": "images/Flag_of_France.png", "options": ["Italy", "France", "Russia", "Netherlands"],
             "correct": "France"},
        ]

        self.diff_image = None
        self.diff_page = None
        self.root = root
        self.root.after(0, lambda: root.state('zoomed'))

        # Display dimensions
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()

        # Background image
        self.bg_image = Image.open("images/firewatch.jpg")
        self.bg_image = ctk.CTkImage(light_image=self.bg_image, dark_image=self.bg_image,
                                     size=(self.screen_width, self.screen_height))
        self.bg_label = ctk.CTkLabel(root, image=self.bg_image, text="")
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Background image text
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
                                       bg_color="#c8e690", hover_color="#ffffff", fg_color="#1a3b2c")
        self.quit_icon.place(relx=0.06, rely=0.08, anchor="center")

        # Help button icon
        self.help_icon = ctk.CTkButton(self.bg_label, text=" ? ", width=64, height=64, corner_radius=32,
                                       font=("CanvaSans", 36, "bold"), bg_color="#c8e690", hover_color="#ffffff",
                                       fg_color="#1a3b2c", command=self.help_page)
        self.help_icon.place(relx=0.94, rely=0.08, anchor="center")

        # Help button
        self.help_button = ctk.CTkButton(self.bg_label, text="Help", bg_color="#c8e690", hover_color="#ffffff",
                                         fg_color="#2d6349", font=("CanvaSans", 22, "bold"), corner_radius=32,
                                         width=160,
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
            messagebox.showerror("Required", "Please enter your name to start the quiz!")
            return
        elif any(char in "!@#$%^&*()_-=+[]{};':?./\\|''" for char in player_name):
            messagebox.showerror("Invalid Name", "Your name cannot contain symbols!")
            return
        elif any(digit in '0123456789' for digit in player_name):
            messagebox.showerror("Invalid Name", "Your name cannot contain numbers!")
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
        self.current_page = "quiz"
        self.current_question_index = 0
        self.score = 0

        self.easy_button.place_forget()
        self.medium_button.place_forget()
        self.hard_button.place_forget()

        self.quiz_title = ctk.CTkLabel(self.bg_label, text="Which Country's Flag Is This?",
                                       font=("CanvaSans", 42, "bold"), text_color="#1a5156",
                                       fg_color="transparent")
        self.quiz_title.place(relx=0.5, rely=0.15, anchor="center")

        self.question_tracker = ctk.CTkLabel(self.bg_label, text="", font=("CanvaSans", 26, "bold"),
                                             text_color="#ffffff", fg_color="#1a5156", corner_radius=20,
                                             width=220, height=50)
        self.question_tracker.place(relx=0.1, rely=0.92, anchor="center")

        self.flag_display = ctk.CTkLabel(self.bg_label, text="", width=480, height=300,
                                         fg_color="#475d5b", corner_radius=0)
        self.flag_display.place(relx=0.28, rely=0.5, anchor="center")

        # Hourglass image
        self.hourglass_original = Image.open("images/hourglass.png")
        self.hourglass_angle = 0

        # hourglass label
        self.hourglass_label = ctk.CTkLabel(
            self.bg_label,
            text="",
            fg_color="#1a3b2c",
            bg_color="#06464f",
            width=150,
            height=150,
            corner_radius=60
        )


        self.hourglass_label.place(relx=0.9, rely=0.5, anchor="center")

        # hourglass label
        self.hourglass_label = ctk.CTkLabel(
            self.bg_label,
            text="",
            fg_color="#1a3b2c",
            bg_color="#06464f",
            width=120,
            height=120,
            corner_radius=35
        )

        self.hourglass_label = ctk.CTkLabel(self.bg_label, text="")
        self.hourglass_label.place(relx=0.9, rely=0.5, anchor="center")

        self.option_buttons = []
        for i in range(4):
            btn = ctk.CTkButton(self.bg_label, text="", width=380, height=60, corner_radius=32,
                                font=("CanvaSans", 20, "bold"), fg_color="#1a5156", text_color="#ffffff",
                                hover_color="#2d6349")
            btn.place(relx=0.65, rely=0.35 + (i * 0.12), anchor="center")
            self.option_buttons.append(btn)

        self.next_button = ctk.CTkButton(self.bg_label, text="Next", width=160, height=50, corner_radius=25,
                                         font=("CanvaSans", 22, "bold"), fg_color="#1a5156", state="disabled",
                                         command=self.next_question)
        self.next_button.place(relx=0.65, rely=0.88, anchor="center")

        # Track chosen difficulty
        self.difficulty = difficulty

        # Timer circle display
        self.timer_label = ctk.CTkLabel(self.bg_label, text="", font=("CanvaSans", 32, "bold"),
                                        text_color="#ffffff", fg_color="#1a3b2c", corner_radius=35,
                                        width=70, height=70, bg_color="#e1c814")
        self.load_question()

    def load_question(self):
        self.selected_answer = None
        self.next_button.configure(state="disabled", fg_color="#1a5156")

        q_data = self.questions[self.current_question_index]

        self.question_tracker.configure(text=f"Question {self.current_question_index + 1}/{len(self.questions)}")

        # Text incase the image doesn't load
        try:
            flag_img = Image.open(q_data["image"])
            ctk_flag = ctk.CTkImage(light_image=flag_img, dark_image=flag_img, size=(480, 300))
            self.flag_display.configure(image=ctk_flag, text="")
            self.flag_display._image = ctk_flag
        except FileNotFoundError:
            self.flag_display.configure(image="", text=f"[ Flag Asset Missing:\n{q_data['image']} ]",
                                        font=("CanvaSans", 18, "bold"), text_color="#ffffff")

        # Question label
        for i, option in enumerate(q_data["options"]):
            self.option_buttons[i].configure(
                text=option,
                fg_color="#1a5156",
                text_color="#ffffff",
                command=lambda opt=option, btn=self.option_buttons[i]: self.select_option(opt, btn)
            )

            # Reset and manage active timer loop strings
            if self.timer_id:
                self.root.after_cancel(self.timer_id)
                self.timer_id = None

            # Add countdown limits based on difficulty choice
            if self.difficulty in ("Medium", "Hard"):
                self.time_left = 10 if self.difficulty == "Medium" else 5
                self.timer_label.configure(text=str(self.time_left))
                self.timer_label.place(relx=0.9, rely=0.7, anchor="center")
                self.start_timer_countdown()
            else:
                self.timer_label.place_forget()

    def start_timer_countdown(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.configure(text=str(self.time_left))

            # change the timer rotation
            self.hourglass_angle = (self.hourglass_angle + 180) % 360

            #  Rotate the original clean image and convert it to a CTkImage
            rotated_img = self.hourglass_original.rotate(-self.hourglass_angle, resample=Image.BICUBIC)
            ctk_hourglass = ctk.CTkImage(light_image=rotated_img, dark_image=rotated_img, size=(100, 100))

            #  Display the newly rotated image
            self.hourglass_label.configure(image=ctk_hourglass)
            self.hourglass_label._image = ctk_hourglass

            #  Loop again after 1 second
            self.timer_id = self.root.after(1000, self.start_timer_countdown)
        else:
            messagebox.showinfo("Time's Up!", "You ran out of time for this question!")
            self.next_question()

    def select_option(self, chosen_text, clicked_button):
        self.selected_answer = chosen_text

        for btn in self.option_buttons:
            btn.configure(fg_color="#1a5156", text_color="#ffffff")

        clicked_button.configure(fg_color="#ffffff", text_color="#1a5156")

        self.next_button.configure(state="normal")

    def next_question(self):
        q_data = self.questions[self.current_question_index]

        if self.selected_answer == q_data["correct"]:
            self.score += 1

        self.current_question_index += 1

        if self.current_question_index < len(self.questions):
            self.load_question()
        else:
            self.show_results()

    def show_results(self):
        self.quiz_title.place_forget()
        self.question_tracker.place_forget()
        self.flag_display.place_forget()
        self.next_button.place_forget()
        for btn in self.option_buttons:
            btn.place_forget()
        self.timer_label.place_forget()

        if self.timer_id:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None

        self.current_page = "results"

        percentage = int((self.score / len(self.questions)) * 100)

        if percentage >= 50:
            title_text = "You passed!"
            title_color = "#ffffff"
            bg_results = "images/win.jpg"
        else:
            title_text = "You failed!"
            title_color = "#e17055"
            bg_results = "images/lose.jpg"

        self.bg_image = Image.open(bg_results)
        self.result_image = ctk.CTkImage(light_image=self.bg_image, dark_image=self.bg_image,
                                         size=(self.screen_width, self.screen_height))
        self.bg_label.configure(image=self.result_image)

        self.results_title = ctk.CTkLabel(self.bg_label, text=title_text,
                                          font=("CanvaSans", 64, "bold"),
                                          text_color=title_color,
                                          fg_color="transparent")
        self.results_title.place(relx=0.5, rely=0.18, anchor="center")

        score_text = f"Your Score: {self.score} / {len(self.questions)}\n\nAccuracy: {percentage}%"

        self.score_display = ctk.CTkLabel(self.bg_label, text=score_text, font=("CanvaSans", 26, "bold"),
                                          text_color="#ffffff", fg_color="#134e4a", width=500, height=180,
                                          corner_radius=32)
        self.score_display.place(relx=0.5, rely=0.52, anchor="center")

    # Go back to the Title screen
    def return_to_menu(self):
        self.results_title.place_forget()
        self.score_display.place_forget()


        self.current_page = "starter"

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

    # help page
    def help_page(self):
        if self.current_page == "starter":
            self.title_text.place_forget()
            self.username.place_forget()
            self.start_button.place_forget()
        elif self.current_page == "diff":
            self.easy_button.place_forget()
            self.medium_button.place_forget()
            self.hard_button.place_forget()
        elif self.current_page == "quiz":
            self.quiz_title.place_forget()
            self.question_tracker.place_forget()
            self.flag_display.place_forget()
            self.next_button.place_forget()
            for btn in self.option_buttons:
                btn.place_forget()

        self.bg_label.configure(image="", fg_color="#1d4d4f")

        # Add "How to play" title
        self.help_title = ctk.CTkLabel(self.bg_label, text="How To Play",
                                       font=("CanvaSans", 56, "bold"), text_color="#ffffff")
        self.help_title.place(relx=0.5, rely=0.15, anchor="center")

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
        self.rule6_body = ctk.CTkLabel(self.bg_label,
                                       text="When you click an option, the button will change colour to show your selection has been registered.",
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

        # Restore the layout the user came from
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

        elif self.current_page == "quiz":
            rice_bg = Image.open("images/Rice.jpg")
            self.diff_image = ctk.CTkImage(light_image=rice_bg, dark_image=rice_bg,
                                           size=(self.screen_width, self.screen_height))
            self.bg_label.configure(image=self.diff_image)

            self.quiz_title.place(relx=0.5, rely=0.15, anchor="center")
            self.question_tracker.place(relx=0.1, rely=0.92, anchor="center")
            self.flag_display.place(relx=0.28, rely=0.5, anchor="center")
            self.next_button.place(relx=0.65, rely=0.88, anchor="center")

            for i, btn in enumerate(self.option_buttons):
                btn.place(relx=0.65, rely=0.35 + (i * 0.12), anchor="center")


if __name__ == "__main__":
    main_window = ctk.CTk()
    app = Flagquiz(main_window)
    main_window.mainloop()