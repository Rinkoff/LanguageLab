import tkinter as tk
from tkinter import ttk



class UI(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        # Initialize Window size
        self.window_width = 1000
        self.window_height = 700

        # Create basic window parameters

        self.geometry(f"{self.window_width}x{self.window_height}+200+50")

        self.title("Language Lab")
        self.wm_iconbitmap("./Resources/culture-307910.ico")
        # Cursor settings
        self.config(cursor="@./Resources/kolba.cur")

        self.Background()
        self.Widgets()
        self.Widgets_coordinates()
        self.Widgets_placing()


    # Set background
    def Background(self):
        self.background = tk.PhotoImage(file="./Resources/sky-2483934_1920.png")
        self.background_label = tk.Label(self, image=self.background)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)


    def Widgets(self):
        # Define Main Widget parameters
        self.lbl_width = 100
        self.lbl_height = 50
        self.buttons_width = 150
        self.buttons_height = 50

        # Define labels
        self.lbl_one = tk.Label(self, text="English")
        self.lbl_two = tk.Label(self, text="Bulgarian")
        self.lbl_translate = tk.Label(self, text="Word")

        #Define buttons
        self.btnCL = tk.Button(self, text="Change Language", command=self.change_language)
        self.btnSubmit = tk.Button(self, text="Submit")
        self.btnAddWord = tk.Button(self, text="Add Word", bd="5", bg="#f0f0f0")

        #Define LineEdit
        self.le_translte = tk.Entry(self)



    def Widgets_coordinates(self):
        #First Language Label coordinates
        self.lbl_one_x = self.window_width - 800
        self.lbl_one_y = 100

        #Second Language Label coordinates
        self.lbl_two_x = self.window_width - 300
        self.lbl_two_y = 100

        #Change Language Button coordinates
        self.btnCL_x = (self.window_width / 2) - (self.buttons_width / 2)
        self.btnCL_y = self.window_height / 4

        #Submit Answer Button coordinates
        self.btnSubmit_x = (self.window_width / 2) - (self.buttons_width / 2)
        self.btnSubmit_y = self.window_height - 200

        #Add Words Button coordinates
        self.btnAddWord_x = (self.window_width / 2) - (self.buttons_width / 2)
        self.btnAddWord_y = self.window_height - 100


    def Widgets_placing(self):
        #Place First Language Label
        self.lbl_one.place(
            x=self.lbl_one_x,
            y=self.lbl_one_y,
            width=self.lbl_width,
            height=self.lbl_height,
        )

        #Place Second Language Label
        self.lbl_two.place(
            x=self.lbl_two_x,
            y=self.lbl_two_y,
            width=self.lbl_width,
            height=self.lbl_height,
        )

        #Place Change Language Button
        self.btnCL.place(
            x=self.btnCL_x,
            y=self.btnCL_y,
            width=self.buttons_width,
            height=self.buttons_height,
        )

        #Place Word for Translate
        self.lbl_translate.place(x=100, y=300, width=800, height=50)

        #Place Answer LineEdit
        self.le_translte.place(x=100, y=400, width=800, height=50)

        #Place Submit Answer Button
        self.btnSubmit.place(
            x=self.btnSubmit_x,
            y=self.btnSubmit_y,
            width=self.buttons_width,
            height=self.buttons_height,
        )

        #Place Add Word Button
        self.btnAddWord.place(
            x=self.btnAddWord_x,
            y=self.btnAddWord_y,
            width=self.buttons_width,
            height=self.buttons_height,
        )



    def change_language(self):

        self.active=True

        # Initialize Window size
        self.window_width = 1000
        self.window_height = 700

        # Create basic window parameters

        self.geometry(f"{self.window_width}x{self.window_height}+200+50")

        self.title("Options")
        self.wm_iconbitmap("./Resources/culture-307910.ico")
        # Cursor settings
        self.config(cursor="@./Resources/kolba.cur")

        self.Background()
        self.Option_widgets()
        self.Option_widget_parameters()
        self.Option_placing_widgets()

        while True:
            if self.active==True:
                self.mainloop()
            else:
                break




        #Define Widgets
    def Option_widgets(self):


        #Language Labels
        self.first_lang_change=tk.Label(self,text="Choose your first language")
        self.second_language_change=tk.Label(self,text="Choose you second language")

        #Languages Ratios
        self.language=""         #Chosen Language

        #Define Radio Buttons
        self.choose_first_lang=tk.StringVar()
        self.choose_second_lang=tk.StringVar()
        self.Bulgarian = ttk.Radiobutton(self, text="Bulgarian",variable=self.choose_first_lang, value="Bulgarian")
        self.English = ttk.Radiobutton(self,text="English",variable=self.choose_first_lang,value="English")
        self.Bulgarian2 = ttk.Radiobutton(self, text="Bulgarian",variable=self.choose_second_lang, value="Bulgarian")
        self.English2 = ttk.Radiobutton(self, text="English",variable=self.choose_second_lang, value="English")

        #Define Button Back
        self.btnBack=tk.Button(self,text="Back",command=self.Back_button_pressed)




    def Option_widget_parameters(self):

        #Choose Languages Label sizes
        self.lc_width=310
        self.lc_height=80

        #Language label sizes
        self.l_width=150
        self.l_height=50

        #First Language text choose coordinates
        self.first_lc_x = (self.window_width / 2) - (self.lc_width / 2)
        self.first_lc_y = 100

        #Second Language text choose coordinates
        self.second_lc_x = (self.window_width / 2) - (self.lc_width / 2)
        self.second_lc_y = 350

        #Radio Buttons coordinates
        self.radio_bg_x=self.window_width/4
        self.radio_en_x=self.radio_bg_x + 400
        self.radio_1_y=250
        self.radio_2_y=500

        #Back Button coordinates
        self.btnBack_x = (self.window_width / 2) - (self.buttons_width / 2)
        self.btnBack_y = self.window_height - 100








    def Option_placing_widgets(self):
        #Placing First Choose language text
        self.first_lang_change.place(x=self.first_lc_x,y=self.first_lc_y,width=self.lc_width,height=self.lc_height)

        # Placing Second Choose language text
        self.second_language_change.place(x=self.second_lc_x,y=self.second_lc_y,width=self.lc_width,height=self.lc_height)

        #Placing Radio Buttons
        self.Bulgarian.place(x=self.radio_bg_x,y=self.radio_1_y)
        self.English.place(x=self.radio_en_x,y=self.radio_1_y)
        self.Bulgarian2.place(x=self.radio_bg_x,y=self.radio_2_y)
        self.English2.place(x=self.radio_en_x,y=self.radio_2_y)

        #Placing Back button
        self.btnBack.place(x=self.btnBack_x,y=self.btnBack_y,width=self.buttons_width,height=self.buttons_height)




    def Back_button_pressed(self):
        if self.active:
            self.active = False
        else:
            self.active = True





