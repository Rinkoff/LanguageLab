import tkinter as tk



class UI(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Initialize Window size
        self.window_width = 1000
        self.window_height = 700

        # Create basic window parameters

        self.geometry(
            f"{self.window_width}x{self.window_height}+200+50"
        )

        self.title("Language Lab")
        self.wm_iconbitmap("../Resources/culture-307910.ico")

        self.Background()

    # Set background
    def Background(self):
        self.background=tk.PhotoImage(file="../Resources/sky-2483934_1920.png")
        self.background_label=tk.Label(self,image=self.background)
        self.background_label.place(x=0,y=0,relwidth=1,relheight=1)

    # def LanguageTab(self):
    #




if __name__ == "__main__":
    app = UI()
    app.mainloop()
