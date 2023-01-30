import tkinter as tk
from tkinter import ttk


class Main_window(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.main_window_parameters()


    def main_window_parameters(self):
        # Initialize Window size
        self.window_width = 1000
        self.window_height = 700

        # Center app parameters
        # Center app
        self.window_x = (self.winfo_screenwidth() // 2) - (self.window_width // 2)
        self.window_y = int(self.winfo_screenheight() * 0.1)

        # Add Main window chief geometrics
        self.geometry(
            f"{self.window_width}x{self.window_height}+{str(self.window_x)}+{str(self.window_y)}"
        )

        # Add title and title icon
        self.title("Language Lab")
        self.wm_iconbitmap("./Resources/culture-307910.ico")

        # Add coursor
        self.config(cursor="@./Resources/kolba.cur")

        # Add Modules
        self.main_window_widget_parameters()
        self.define_main_frame()

    def main_colors(self):

        self.frame_bg_color="#1e1e1e"
        self.font_color="#007acc"
        self.btn_color="#3e3e42"
        self.le_color="#2d2d30"

    def define_main_frame(self):
        #Add colors
        self.main_colors()
        # Add Frame
        self.main_frame = tk.Frame(
            self, width=self.window_width, height=self.window_height, bg=self.frame_bg_color
        )
        self.main_frame.grid(row=0, column=0)

        # Add Left language label
        self.left_language = "English"

        self.left_language_label = tk.Label(
            self.main_frame,
            text=self.left_language,
            bg=self.frame_bg_color,
            fg=self.font_color,
            font=("TkheadingFont", 15),
        ).place(
            x=self.lbl_ll_x,
            y=self.lbl_ll_y,
            width=self.lbl_width,
            height=self.lbl_height,
        )

        # Add Right language label
        self.right_language = "Bulgarian"

        self.right_language_label = tk.Label(
            self.main_frame,
            text=self.right_language,
            bg=self.frame_bg_color,
            fg=self.font_color,
            font=("TkheadingFont", 15),
        ).place(
            x=self.lbl_rl_x,
            y=self.lbl_rl_y,
            width=self.lbl_width,
            height=self.lbl_height,
        )

        # Add Button Change Language
        self.btn_change_language = tk.Button(
            self.main_frame,
            text="Change Language",
            bg=self.btn_color,
            fg=self.font_color,
            font=("TkheadingFont", 12),
            activebackground=self.le_color,
            command=self.define_option_frame,
            bd="10"
        ).place(
            x=self.btnCL_x,
            y=self.btnCL_y,
            width=self.buttons_width,
            height=self.buttons_height,
        )

        # Add Random Word Label
        self.random_word = "word"

        self.lbl_random_word = tk.Label(
            self.main_frame,
            text=self.random_word,
            bg=self.frame_bg_color,
            fg=self.font_color,
            font=("TkheadingFont", 15),
        ).place(x=100,
                y=300,
                width=800,
                height=50
        )

        # Add LineEdit
        self.le_translate = tk.Entry(
            self.main_frame,
            justify="center",
            bg=self.le_color,
            fg=self.font_color,
            font=("TkheadingFont", 15),
        ).place(x=100, y=400, width=800, height=50)

        # Add Submit Button
        self.btn_submit = tk.Button(
            self.main_frame,
            text="Submit",
            bg=self.btn_color,
            fg=self.font_color,
            font=("TkheadingFont", 12),
            activebackground=self.le_color,
            bd="10"
        ).place(
            x=self.btn_submit_x,
            y=self.btn_submit_y,
            width=self.buttons_width,
            height=self.buttons_height,
        )

        # Add Button Add Word
        self.btn_add_word = tk.Button(
            self.main_frame,
            text="Add Words",
            bg=self.btn_color,
            fg=self.font_color,
            font=("TkheadingFont", 12),
            activebackground=self.le_color,
            command=self.define_add_word_window_frame,
            bd="10"
        ).place(
            x=self.btn_add_words_x,
            y=self.btn_add_words_y,
            width=self.buttons_width,
            height=self.buttons_height,
        )

        # Load Theme Images
        self.theme_light = tk.PhotoImage(file="./Resources/light_theme_resized.png")
        self.theme_dark = tk.PhotoImage(file="./Resources/dark_theme_resized.png")


    def main_window_widget_parameters(self):
        # Define Main Widget parameters
        self.lbl_width = 100
        self.lbl_height = 50
        self.buttons_width = 150
        self.buttons_height = 50

        # Left Language Label coordinates
        self.lbl_ll_x = self.window_width - 800
        self.lbl_ll_y = 100

        # Right Language Label coordinates
        self.lbl_rl_x = self.window_width - 300
        self.lbl_rl_y = 100

        # Button Change Language coordinates
        self.btnCL_x = (self.window_width / 2) - (self.buttons_width / 2)
        self.btnCL_y = self.window_height / 4

        # Button Submit coordinates
        self.btn_submit_x = (self.window_width / 2) - (self.buttons_width / 2)
        self.btn_submit_y = self.window_height - 200

        # Add Words Button coordinates
        self.btn_add_words_x = (self.window_width / 2) - (self.buttons_width / 2)
        self.btn_add_words_y = self.window_height - 100

    def define_option_frame(self):
        #Add colors
        self.main_colors()

        # Add Frame
        self.option_frame = tk.Frame(
            self, width=self.window_width, height=self.window_height, bg=self.frame_bg_color
        )
        self.option_frame.grid(row=0, column=0)

        # Taka parameters
        self.option_window_widget_parameters()

        # Add Top Language Bar
        self.lbl_top_language_change = tk.Label(
            self.option_frame,
            text="Choose your first language",
            bg=self.frame_bg_color,
            fg=self.font_color,
            font=("TkheadingFont", 15),
        ).place(
            x=self.lbl_change_lang_top_x,
            y=self.lbl_change_lang_top_y,
            width=self.lc_width,
            height=self.lc_height,
        )

        # Add Bottom Language Bar
        self.lbl_bottom_language_change = tk.Label(
            self.option_frame,
            text="Choose your second language",
            bg=self.frame_bg_color,
            fg=self.font_color,
            font=("TkheadingFont", 15),
        ).place(
            x=self.lbl_change_lang_bottom_x,
            y=self.lbl_change_lang_bottom_y,
            width=self.lc_width,
            height=self.lc_height,
        )

        # Make style for radio buttons
        self.style = ttk.Style(self)
        self.style.configure(
            "TRadiobutton",
            background=self.frame_bg_color,
            font=("TkheadingFont", 15),
            foreground=self.font_color,
        )
        # Add Radio buttons
        self.choose_top_lang = tk.StringVar()
        self.choose_bottom_lang = tk.StringVar()

        self.Bulgarian = ttk.Radiobutton(
            self.option_frame,
            text="Bulgarian",
            variable=self.choose_top_lang,
            value="Bulgarian",
        ).place(x=self.radio_bg_x, y=self.radio_top_y)

        self.English = ttk.Radiobutton(
            self.option_frame,
            text="English",
            variable=self.choose_top_lang,
            value="English",
        ).place(x=self.radio_en_x, y=self.radio_top_y)

        self.Bulgarian2 = ttk.Radiobutton(
            self.option_frame,
            text="Bulgarian",
            variable=self.choose_bottom_lang,
            value="Bulgarian",
        ).place(x=self.radio_bg_x, y=self.radio_bottom_button_y)

        self.English2 = ttk.Radiobutton(
            self.option_frame,
            text="English",
            variable=self.choose_bottom_lang,
            value="English",
        ).place(x=self.radio_en_x, y=self.radio_bottom_button_y)

        # Define Button Back
        self.btn_back = tk.Button(
            self.option_frame,
            text="Back",
            command=self.define_main_frame,
            activebackground=self.le_color,
            bg=self.btn_color,
            fg=self.font_color,
            font=("TkheadingFont", 12),
            bd="10"
        ).place(
            x=self.btn_back_x,
            y=self.btn_back_y,
            width=self.buttons_width,
            height=self.buttons_height,
        )

    def option_window_widget_parameters(self):
        # Labels sizes
        self.lc_width = 310
        self.lc_height = 80

        # Choose language top Label coordinates
        self.lbl_change_lang_top_x = (self.window_width / 2) - (self.lc_width / 2)
        self.lbl_change_lang_top_y = 100

        # Choose language botoom Label coordinates
        self.lbl_change_lang_bottom_x = (self.window_width / 2) - (self.lc_width / 2)
        self.lbl_change_lang_bottom_y = 350

        # Radio Buttons coordinates
        self.radio_bg_x = self.window_width / 4
        self.radio_en_x = self.radio_bg_x + 400
        self.radio_top_y = 250
        self.radio_bottom_button_y = 500

        # Back Button coordinates
        self.btn_back_x = (self.window_width / 2) - (self.buttons_width / 2)
        self.btn_back_y = self.window_height - 100

    def define_add_word_window_frame(self):
        #Add colors
        self.main_colors()

        # Add Frame
        self.add_word_frame = tk.Frame(
            self, width=self.window_width, height=self.window_height, bg=self.frame_bg_color
        )
        self.add_word_frame.grid(row=0, column=0)

        # Taka parameters
        self.add_words_window_parameters()

        # Add Top Label Bar
        self.first_language = "English"

        self.lbl_word_top = tk.Label(
            self.add_word_frame,
            text=f"Add {self.first_language} word here",
            bg=self.frame_bg_color,
            fg=self.font_color,
            font=("TkheadingFont", 15),
        ).place(
            x=self.top_lbl_x,
            y=self.top_lbl_y,
            width=self.lbl_word_width,
            height=self.lbl_word_height,
        )

        # Add bottom Label Bar
        self.second_language = "Bulgarian"
        self.lbl_word_bottom = tk.Label(
            self.add_word_frame,
            text=f"Add {self.second_language} word here",
            bg=self.frame_bg_color,
            fg=self.font_color,
            font=("TkheadingFont", 15),
        ).place(
            x=self.bottom_lbl_x,
            y=self.bottom_lbl_y,
            width=self.lbl_word_width,
            height=self.lbl_word_height,
        )

        # Add LineEdits
        self.le_word_english = tk.Entry(
            self.add_word_frame,
            justify="center",
            bg=self.le_color,
            fg=self.font_color,
            font=("TkheadingFont", 15),
        ).place(x=100, y=200, width=800, height=50)

        self.le_word_bulgarian = tk.Entry(
            self.add_word_frame,
            justify="center",
            bg=self.le_color,
            fg=self.font_color,
            font=("TkheadingFont", 15),
        ).place(x=100, y=400, width=800, height=50)

        # Add buttons
        self.add_word_back_button = tk.Button(
            self.add_word_frame,
            text="Back",
            bg=self.btn_color,
            fg=self.font_color,
            font=("TkheadingFont", 12),
            activebackground=self.le_color,
            command=self.define_main_frame,
            bd="10"
        ).place(
            x=self.add_word_buttons_x,
            y=self.add_word_back_button_y,
            width=self.buttons_width,
            height=self.buttons_height,
        )

        self.save_button = tk.Button(
            self.add_word_frame,
            bg=self.btn_color,
            fg=self.font_color,
            font=("TkheadingFont", 12),
            activebackground=self.le_color,
            text="Save",
            bd="10"
        ).place(
            x=self.add_word_buttons_x,
            y=self.add_word_save_button_y,
            width=self.buttons_width,
            height=self.buttons_height,
        )

    def add_words_window_parameters(self):
        # Add Label size
        self.lbl_word_width = 350
        self.lbl_word_height = 50

        # Add Labels coordinates
        self.top_lbl_x = (self.window_width / 2) - (self.lbl_word_width / 2)
        self.top_lbl_y = 100

        self.bottom_lbl_x = (self.window_width / 2) - (self.lbl_word_width / 2)
        self.bottom_lbl_y = 300

        # Buttons coordinates
        self.add_word_buttons_x = (self.window_width / 2) - (self.buttons_width / 2)
        self.add_word_back_button_y = self.window_height - 100
        self.add_word_save_button_y = self.window_height - 200


