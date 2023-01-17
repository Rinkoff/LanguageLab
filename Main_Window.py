import tkinter as tk
from tkinter import ttk
import pyglet



class Main_window(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.Main_window_parameters()

    def Main_window_parameters(self):
        # Initialize Window size
        self.window_width = 1000
        self.window_height = 700

        #Center app
        self.app_x=(self.winfo_screenwidth()//2)-(self.window_width//2)
        self.app_y=int(self.winfo_screenheight()*0.1)


        # Create basic window parameters

        self.geometry(f"{self.window_width}x{self.window_height}+{str(self.app_x)}+{str(self.app_y)}")

        self.title("Language Lab")
        self.wm_iconbitmap("./Resources/culture-307910.ico")
        # Cursor settings
        self.config(cursor="@./Resources/kolba.cur")

        pyglet.font.add_file("./Resources/KUVAS.otf")

        self.Background()
        self.Widgets()
        self.Widgets_coordinates()
        self.Widgets_placing()

    def Background(self):
        self.background_image = tk.PhotoImage(file="./Resources/sky-2483934_1920.png")
        self.background = tk.Label(self, image=self.background_image)
        self.background.place(x=0, y=0, relwidth=1, relheight=1)
    def Widgets(self):
        # Define labels
        self.lbl_one = tk.Label(self,text="English",font=("KUVAS",15))
        self.lbl_two = tk.Label(self, text="Bulgarian",font=("KUVAS",15))
        self.lbl_translate = tk.Label(self, text="Word")

        # Define buttons
        self.btnCL = tk.Button(
            self, text="Change Language", command=self.Option_window_main_parameters
        )
        self.btnSubmit = tk.Button(self, text="Submit")
        self.btnAddWord = tk.Button(
            self,
            text="Add Word",
            bd="5",
            bg="#f0f0f0",
            command=self.Add_word_window_parameters,
        )

        # Define LineEdit
        self.le_translte = tk.Entry(self)

    def Widgets_coordinates(self):
        # Define Main Widget parameters
        self.lbl_width = 100
        self.lbl_height = 50
        self.buttons_width = 150
        self.buttons_height = 50

        # First Language Label coordinates
        self.lbl_one_x = self.window_width - 800
        self.lbl_one_y = 100

        # Second Language Label coordinates
        self.lbl_two_x = self.window_width - 300
        self.lbl_two_y = 100

        # Change Language Button coordinates
        self.btnCL_x = (self.window_width / 2) - (self.buttons_width / 2)
        self.btnCL_y = self.window_height / 4

        # Submit Answer Button coordinates
        self.btnSubmit_x = (self.window_width / 2) - (self.buttons_width / 2)
        self.btnSubmit_y = self.window_height - 200

        # Add Words Button coordinates
        self.btnAddWord_x = (self.window_width / 2) - (self.buttons_width / 2)
        self.btnAddWord_y = self.window_height - 100

    def Widgets_placing(self):
        # Place First Language Label
        self.lbl_one.place(
            x=self.lbl_one_x,
            y=self.lbl_one_y,
            width=self.lbl_width,
            height=self.lbl_height,
        )

        # Place Second Language Label
        self.lbl_two.place(
            x=self.lbl_two_x,
            y=self.lbl_two_y,
            width=self.lbl_width,
            height=self.lbl_height,
        )

        # Place Change Language Button
        self.btnCL.place(
            x=self.btnCL_x,
            y=self.btnCL_y,
            width=self.buttons_width,
            height=self.buttons_height,
        )

        # Place Word for Translate
        self.lbl_translate.place(x=100, y=300, width=800, height=50)

        # Place Answer LineEdit
        self.le_translte.place(x=100, y=400, width=800, height=50)

        # Place Submit Answer Button
        self.btnSubmit.place(
            x=self.btnSubmit_x,
            y=self.btnSubmit_y,
            width=self.buttons_width,
            height=self.buttons_height,
        )

        # Place Add Word Button
        self.btnAddWord.place(
            x=self.btnAddWord_x,
            y=self.btnAddWord_y,
            width=self.buttons_width,
            height=self.buttons_height,
        )

    def Option_window_main_parameters(self):

        # Initialize Window size
        self.window_width = 1000
        self.window_height = 700

        self.app_x = (self.winfo_screenwidth() // 2) - (self.window_width // 2)
        self.app_y = int(self.winfo_screenheight() * 0.1)

        # Create basic window parameters

        self.geometry(f"{self.window_width}x{self.window_height}+{str(self.app_x)}+{str(self.app_y)}")

        self.title("Options")
        self.wm_iconbitmap("./Resources/culture-307910.ico")
        # Cursor settings
        self.config(cursor="@./Resources/kolba.cur")

        self.Background()
        self.Option_widgets()
        self.Option_widget_parameters()
        self.Option_placing_widgets()

    # Define Widgets
    def Option_widgets(self):

        # Language Labels
        self.top_lang_change = tk.Label(self, text="Choose your first language")
        self.bottom_language_change = tk.Label(self, text="Choose you second language")

        # Define Radio Buttons
        self.choose_top_lang = tk.StringVar()
        self.choose_bottom_lang = tk.StringVar()
        self.Bulgarian = ttk.Radiobutton(
            self,
            text="Bulgarian",
            variable=self.choose_top_lang,
            value="Bulgarian",
        )
        self.English = ttk.Radiobutton(
            self,
            text="English",
            variable=self.choose_top_lang,
            value="English",
        )
        self.Bulgarian2 = ttk.Radiobutton(
            self, text="Bulgarian", variable=self.choose_bottom_lang, value="Bulgarian"
        )
        self.English2 = ttk.Radiobutton(
            self, text="English", variable=self.choose_bottom_lang, value="English"
        )

        # Define Button Back
        self.btnBack = tk.Button(self, text="Back", command=self.Main_window_parameters)

    def Option_widget_parameters(self):

        # Choose Languages Label sizes
        self.lc_width = 310
        self.lc_height = 80

        # First Language text choose coordinates
        self.first_lc_x = (self.window_width / 2) - (self.lc_width / 2)
        self.first_lc_y = 100

        # Second Language text choose coordinates
        self.second_lc_x = (self.window_width / 2) - (self.lc_width / 2)
        self.second_lc_y = 350

        # Radio Buttons coordinates
        self.radio_bg_x = self.window_width / 4
        self.radio_en_x = self.radio_bg_x + 400
        self.radio_1_y = 250
        self.radio_2_y = 500

        # Back Button coordinates
        self.btnBack_x = (self.window_width / 2) - (self.buttons_width / 2)
        self.btnBack_y = self.window_height - 100

    def Option_placing_widgets(self):
        # Placing First Choose language text
        self.top_lang_change.place(
            x=self.first_lc_x,
            y=self.first_lc_y,
            width=self.lc_width,
            height=self.lc_height,
        )

        # Placing Second Choose language text
        self.bottom_language_change.place(
            x=self.second_lc_x,
            y=self.second_lc_y,
            width=self.lc_width,
            height=self.lc_height,
        )

        # Placing Radio Buttons
        self.Bulgarian.place(x=self.radio_bg_x, y=self.radio_1_y)
        self.English.place(x=self.radio_en_x, y=self.radio_1_y)
        self.Bulgarian2.place(x=self.radio_bg_x, y=self.radio_2_y)
        self.English2.place(x=self.radio_en_x, y=self.radio_2_y)

        # Placing Back button
        self.btnBack.place(
            x=self.btnBack_x,
            y=self.btnBack_y,
            width=self.buttons_width,
            height=self.buttons_height,
        )

    def Add_word_window_parameters(self):
        # Initialize Window size
        self.window_width = 1000
        self.window_height = 700

        self.app_x = (self.winfo_screenwidth() // 2) - (self.window_width // 2)
        self.app_y = int(self.winfo_screenheight()*0.1)

        # Create basic window parameters

        self.geometry(f"{self.window_width}x{self.window_height}+{str(self.app_x)}+{str(self.app_y)}")

        self.title("Add Word")
        self.wm_iconbitmap("./Resources/culture-307910.ico")
        # Cursor settings
        self.config(cursor="@./Resources/kolba.cur")

        self.Background()
        self.Add_words_widgets()
        self.Add_words_parameters()
        self.Placing_word_elements()

    def Add_words_widgets(self):
        # Add Labels
        self.lbl_word_english = tk.Label(self, text="Add English word here")
        self.lbl_word_bulgarian = tk.Label(self, text="Add Bulgarian word here")

        # Add LineEdits
        self.le_word_english = tk.Entry(self)
        self.le_word_bulgarian = tk.Entry(self)

        # Add buttons
        self.add_word_back_button = tk.Button(
            self, text="Back", command=self.Main_window_parameters
        )

        self.save_button=tk.Button(self,text="Save")


    def Add_words_parameters(self):

        # Add Label size
        self.lbl_word_width = 350
        self.lbl_word_height = 50

        # Add Labels coordinates
        self.top_lbl_x = (self.window_width / 2) - (self.lbl_word_width / 2)
        self.top_lbl_y = 100

        self.bot_lbl_x = (self.window_width / 2) - (self.lbl_word_width / 2)
        self.bot_lbl_y = 300

        # Back button coordinates
        self.add_word_buttons_x = (self.window_width / 2) - (self.buttons_width / 2)
        self.add_word_back_button_y = self.window_height - 100
        self.add_word_save_button_y= self.window_height - 200


    def Placing_word_elements(self):
        # Placing Labels
        self.lbl_word_english.place(
            x=self.top_lbl_x,
            y=self.top_lbl_y,
            width=self.lbl_word_width,
            height=self.lbl_word_height,
        )
        self.lbl_word_bulgarian.place(
            x=self.bot_lbl_x,
            y=self.bot_lbl_y,
            width=self.lbl_word_width,
            height=self.lbl_word_height,
        )

        self.le_word_english.place(x=100, y=200, width=800, height=50)
        self.le_word_bulgarian.place(x=100, y=400, width=800, height=50)

        # Placing back button
        self.add_word_back_button.place(
            x=self.add_word_buttons_x,
            y=self.add_word_back_button_y,
            width=self.buttons_width,
            height=self.buttons_height,
        )

        self.save_button.place(
            x=self.add_word_buttons_x,
            y=self.add_word_save_button_y,
            width=self.buttons_width,
            height=self.buttons_height

        )