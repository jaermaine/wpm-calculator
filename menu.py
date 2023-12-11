import customtkinter as ctk
from PIL import Image, ImageTk
import subprocess


def info(mainmenu):
    mainmenu.withdraw()  # Hide the main menu

    info_window = ctk.CTkToplevel(mainmenu)
    info_window.title("Info Page")
    info_window.resizable(False, False)
    info_window.configure(fg_color="#16161A")

    # Center
    window_height = 500
    window_width = 900
    screen_width = info_window.winfo_screenwidth()
    screen_height = info_window.winfo_screenheight()
    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))
    info_window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    # For Info
    info_label = ctk.CTkLabel(info_window,
                              text="\nWe made this App/Project to calculate the speed of your Typing. "
                                   "Typing faster has a lot of benefits to us.\n"
                                   "Here are the examples:\n\n"
                                   "1. Typing speed is crucial in the workplace because it directly impacts "
                                   "productivity and efficiency.\n\n"
                                   "2. A skilled typist is able to finish a writing task within a specific "
                                   "length of time and is not hindered \nby their slower typing speed.\n\n"
                                   "3. Candidates who learn to type faster are more favorable to employers.\n\n"
                                   "4. It guarantees that they can produce more text for the company (and in less "
                                   "time).\n\n"
                                   "5. Makes it Easier to Take Notes\n\n"
                                   "6. Typing helps activate new memory muscles and build more active and strong "
                                   "cognitive"
                                   "\nconnections that in turn will enhance your overall brain capacity and "
                                   "function.\n",
                              justify='left', font=("Nunito", 19), text_color="#fffffe")
    info_label.pack()

    def main_menu():
        info_window.withdraw()  # Hide the info window then go back to main menu
        mainmenu.deiconify()

    back_button = ctk.CTkButton(info_window, 50, 50, border_width=1, border_color="white",
                                text='<<Back to Main Menu>>', command=main_menu, fg_color="#7f5af0",
                                text_color="#fffffe", font=("Nunito", 15))
    back_button.pack()


def create_main_menu():
    mainmenu = ctk.CTk()
    mainmenu.title("Words Per Minute")
    mainmenu.resizable(False, False)

    # Center
    window_height = 500
    window_width = 900
    screen_width = mainmenu.winfo_screenwidth()
    screen_height = mainmenu.winfo_screenheight()
    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))
    mainmenu.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    def start_wpm():
        mainmenu.withdraw()  # Hide the main menu
        subprocess.run(["python", "launch_game_menu.py"])  # Run the launch_game_menu.py which is the wpm

    # Image for the Main Menu
    image = Image.open("menu.png")  # Path of the image
    image = image.resize((1000, 500), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(image)

    # Display the image using a CTkLabel
    image_label = ctk.CTkLabel(mainmenu, image=photo, text="")
    image_label.image = photo  # Keep a reference to the image
    image_label.place(x=0, y=0)  # Adjust the position as needed

    play_icon = ImageTk.PhotoImage(Image.open("play.png").resize((40, 40)))  # Play button icon
    info_icon = ImageTk.PhotoImage(Image.open("info.png").resize((40, 40)))  # Icon button icon

    start_button = ctk.CTkButton(mainmenu, image=play_icon, compound="right",
                                 width=250, height=70,
                                 border_width=1, border_color="white",
                                 text="START", fg_color="#7f5af0", text_color="#fffffe", font=("arial", 40),
                                 command=start_wpm)
    start_button.place(x=60, y=100)

    info_button = ctk.CTkButton(mainmenu, image=info_icon, compound="right",
                                width=250, height=70,
                                border_width=1, border_color="white",
                                text="INFO", fg_color="#7f5af0", text_color="#fffffe", font=("arial", 40),
                                command=lambda: info(mainmenu))
    info_button.place(x=60, y=310)

    mainmenu.mainloop()


if __name__ == "__main__":
    create_main_menu()
