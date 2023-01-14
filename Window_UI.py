import tkinter as tk
from tkinter import ttk
import customtkinter


class UI(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        # Initialize Window size
        self.window_width = 1000
        self.window_height = 700

        # Create basic window parameters

        self.geometry(f"{self.window_width}x{self.window_height}+200+50")

        self.title("Language Lab")
        self.wm_iconbitmap("../Resources/culture-307910.ico")
        # Cursor settings
        self.config(cursor="@../Resources/kolba.cur")

        self.Background()
        self.Widgets()
        self.Widgets_cordinates()
        self.Widgets_placing()


    # Set background
    def Background(self):
        self.background = tk.PhotoImage(file="../Resources/sky-2483934_1920.png")
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
        self.btnCL = tk.Button(self, text="Change Language")
        self.btnSubmit = tk.Button(self, text="Submit")
        self.btnAddWord = tk.Button(self, text="Add Word", bd="5", bg="#f0f0f0")

        #Define LineEdit
        self.le_translte = tk.Entry(self)



    def Widgets_cordinates(self):
        #First Language Label cordinates
        self.lbl_one_x = self.window_width - 800
        self.lbl_one_y = 100

        #Second Language Label cordinates
        self.lbl_two_x = self.window_width - 300
        self.lbl_two_y = 100

        #Change Language Button cordinates
        self.btnCL_x = (self.window_width / 2) - (self.buttons_width / 2)
        self.btnCL_y = self.window_height / 4

        #Submit Answer Button cordinates
        self.btnSubmit_x = (self.window_width / 2) - (self.buttons_width / 2)
        self.btnSubmit_y = self.window_height - 200

        #Add Words Button cordinates
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


if __name__ == "__main__":
    app = UI()
    app.mainloop()
