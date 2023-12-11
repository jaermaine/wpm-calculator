import customtkinter as customtkinter
import subprocess
from generate_phrase import generate_random_paragraph
from wpm_calculator import Calculate
from datetime import datetime
from PIL import Image, ImageTk
import time


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # global variables
        self.typed = None
        self.list_for_words_in_phrase = None
        self.return_button = None
        self.my_frame = None
        self.results_content = None
        self.t0 = 0
        self.t1 = 0
        self.error = 0
        self.j = 0
        self.i = 0
        self.now = datetime.now()

        # generate CTk window dimensions
        self.title("Currently typing...")
        self.resizable(False, False)
        self.configure(fg_color="#16161A")
        window_height = 500
        window_width = 900
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        self.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        back_icon = ImageTk.PhotoImage(Image.open("back.png").resize((15, 15)))
        reset_icon = ImageTk.PhotoImage(Image.open("reset.png").resize((15, 15)))
        result_icon = ImageTk.PhotoImage(Image.open("result.png").resize((15, 15)))

        # generate a phrase and add to a label
        self.phrase = generate_random_paragraph(1)
        self.label = customtkinter.CTkLabel(self, text=self.phrase, font=('Consolas', 21), fg_color='transparent',
                                            justify="center")
        self.label.place(x=245, y=100)

        # split the phrase and add to a label
        first_phrase = self.phrase.split()
        self.label_reference = customtkinter.CTkLabel(self, text=first_phrase[0], font=('Consolas', 21))
        self.label_reference.place(x=410, y=150)

        # generate a textbox
        self.entry = customtkinter.CTkEntry(self, placeholder_text='Type here (click to start)', bg_color='#52524e')
        self.entry.place(x=370, y=200)

        # create a label to display WPM
        self.label_wpm = customtkinter.CTkLabel(self, text="WPM: ")
        self.label_wpm.place(x=350, y=250)

        # create a label to display ACC
        self.label_accuracy = customtkinter.CTkLabel(self, text="ACC: ")
        self.label_accuracy.place(x=450, y=250)

        # create a reset button
        self.reset_button = customtkinter.CTkButton(self, text="Reset", border_width=1, border_color="white",
                                                    image=reset_icon, compound="right", font=("arial", 20),
                                                    fg_color="#7f5af0", text_color="#fffffe", command=self.reset)
        self.reset_button.place(x=370, y=300)

        # creates a button for result
        self.results_button = customtkinter.CTkButton(self, text="Results", border_width=1, border_color="white",
                                                      image=result_icon, compound='right',
                                                      fg_color="#7f5af0", text_color="#fffffe", command=self.results)
        self.results_button.place(x=735, y=20)

        # to return to main menu
        def main_menu():
            self.withdraw()  # Hide the main menu
            subprocess.run(["python", "menu.py"])  # Back to Main Menu

        self.main_menu_button = customtkinter.CTkButton(self, text="Return to Main Menu", border_width=1,
                                                        border_color="white",
                                                        image=back_icon, compound="left", font=("arial", 20),
                                                        fg_color="#7f5af0", text_color="#fffffe", command=main_menu)
        self.main_menu_button.place(x=330, y=350)

        # binds for each function
        self.entry.bind("<Button-1>", self.start)
        self.bind("<space>", self.next_thing)
        self.entry.bind("<KeyRelease>", self.to_stop)
        self.entry.bind("<KeyPress>", self.get_accuracy)

    # add methods to app
    def start(self, event):
        self.t0 = time.time()
        return

    def end(self, event):
        self.t1 = time.time()
        return

    def results(self):
        contents = open("WPM Records", "r")
        records = contents.read()
        self.my_frame = customtkinter.CTkScrollableFrame(self, height=750, width=400, label_text="Previous Results",
                                                         fg_color="#16161A", label_fg_color="#7f5af0",
                                                         label_text_color="white",
                                                         border_width=3, border_color="white")
        self.my_frame.pack(anchor='e', padx=10, pady=10)

        self.results_content = customtkinter.CTkLabel(self.my_frame, text=records)
        self.results_content.pack()

        self.return_button = customtkinter.CTkButton(self.my_frame, text="Return", border_width=1, border_color="white",
                                                     fg_color="#7f5af0", text_color="#fffffe",
                                                     command=self.return_to_main)
        self.return_button.pack()

    def return_to_main(self):
        self.my_frame.pack_forget()

    def reset(self):
        self.phrase = generate_random_paragraph(1)
        self.list_for_words_in_phrase = self.phrase.split()
        self.label.configure(text=self.phrase)
        self.label_reference.configure(text=self.list_for_words_in_phrase[0])
        self.entry.configure(state='normal')
        self.typed = None
        self.j = 0
        self.i = 0
        self.t0 = time.time()
        self.t1 = 0
        self.error = 0
        self.label_wpm.configure(text="WPM: ")
        self.label_accuracy.configure(text="ACC: ")
        self.entry.delete(0, len(self.entry.get()))

    def get_accuracy(self, event):
        press = event.keysym
        list_for_words_in_phrase = self.phrase.split()
        characters = [x for x in list_for_words_in_phrase[self.j]]
        self.entry.configure(border_color="#52524e")

        # checks whether the press is in the alphabet and is len == 1 to ensure it's a character not every function
        # button like space and backspace
        if len(press) == 1:
            if self.i < len(list_for_words_in_phrase[self.j]):  # to limit the i

                if press == characters[self.i]:
                    self.i += 1  # move to the next character if it's correct
                else:
                    self.error += 1  # add to errors
            else:
                self.error += 1

    def next_thing(self, event):
        list_for_words_in_phrase = self.phrase.split()
        typed = self.entry.get().strip()
        if self.j < len(list_for_words_in_phrase):
            if list_for_words_in_phrase[self.j] == typed:
                self.i = 0
                self.j += 1
                self.label_reference.configure(text=list_for_words_in_phrase[self.j])
                self.entry.delete(0, len(typed) + 1)
                self.entry.configure(border_color="green")
            else:
                self.entry.configure(border_color="red")

    def to_stop(self, event):
        typed = self.entry.get().strip()
        list_for_words_in_phrase = self.phrase.split()
        last_word_in_phrase = list_for_words_in_phrase[-1]

        last_char_in_word = last_word_in_phrase[len(last_word_in_phrase) - 1]
        if typed == last_word_in_phrase:
            last_char_user_input = typed[len(typed) - 1]
            if last_char_user_input == last_char_in_word:
                self.entry.delete(0, len(typed) + 1)
                self.label_reference.configure(text="")
                self.entry.configure(state="disabled", bg_color="#000000", fg_color="#000000")
                self.end(event)
                word_count = len(self.phrase.replace(" ", ""))
                calculate = Calculate(self.t0, self.t1, word_count, self.error, len(self.phrase.strip()))
                wpm = calculate.get_wpm()
                acc = calculate.get_acc()
                text = open('WPM Records', 'a+')
                text.write(self.now.strftime("\n%m/%d/%Y, %H:%M:%S"))
                text.write("\tWpm: " + str(wpm))
                text.write("\tAcc: " + str(acc))
                self.label_wpm.configure(text="WPM = " + str(wpm))
                self.label_accuracy.configure(text="Accuracy = " + str(acc))
