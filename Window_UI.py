import tkinter as tk
from tkinter import ttk


class UI(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.style = ttk.Style()

        # Initialize Window size
        self.window_width = 1000
        self.window_height = 700

        # Create basic window parameters

        self.geometry(f"{self.window_width}x{self.window_height}+200+50")

        self.title("Language Lab")
        self.wm_iconbitmap("../Resources/culture-307910.ico")

        self.Background()
        self.LanguageTab()

    # Set background
    def Background(self):
        self.background = tk.PhotoImage(file="../Resources/sky-2483934_1920.png")
        self.background_label = tk.Label(self, image=self.background)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

    def LanguageTab(self):
        # Add widgets
        # Label stilizate
        self.lbl_one = tk.Label(self, text="English")
        self.lbl_two = tk.Label(self, text="Bulgarian")
        self.lbl_width = 100
        self.lbl_height = 50
        self.lbl_one_x = 200
        self.lbl_one_y = 100
        self.lbl_two_x = 700
        self.lbl_two_y = 100
        self.lbl_one.place(
            x=self.lbl_one_x,
            y=self.lbl_one_y,
            width=self.lbl_width,
            height=self.lbl_height,
        )
        self.lbl_two.place(
            x=self.lbl_two_x,
            y=self.lbl_two_y,
            width=self.lbl_width,
            height=self.lbl_height,
        )

        # Button styles and cordinates
        self.btnCL_width = 150
        self.btnCL_height = 50
        self.btnCL_x = (self.window_width / 2) - (self.btnCL_width / 2)
        self.btnCL_y = self.window_height / 4
        # self.style.configure(
        #     "Round.TButton", background="#737CA1", foreground="#0C090A", font="KUVAS"
        # )
        self.btnCL = tk.Button(self, text="Change Language")
        self.btnCL.pack()

        self.btnCL.place(
            x=self.btnCL_x,
            y=self.btnCL_y,
            width=self.btnCL_width,
            height=self.btnCL_height,
        )


    # def Translate(self):



if __name__ == "__main__":
    app = UI()
    app.mainloop()
