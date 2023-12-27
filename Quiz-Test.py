import os
import json
import datetime
from PIL import Image, ImageTk
from tkinter import Tk, Label, Entry, Button, StringVar, ttk, Canvas

class Main(Tk):
    def __init__(self, company:str):
        super().__init__()
        self.total = 0
        self.setter = {}
        self.company = company
        self.iconbitmap("logo.ico")
        self.get_userN = StringVar()
        self.get_courseN = StringVar()
        self.time = datetime.datetime.now()
        self.json_path = f"{os.environ["userprofile"]}\\qz-data\\{company.lower()}.{self.time.strftime("%H_%h-%Y")}.rdf"
        self.question = self.genJson()["set-a"]
        self.result = self.genJson()["answer-a"]

    def genJson(self):
        with open(r'data.json', "r+") as reading:
            return json.load(reading)

    def intro(self):
        self.title(f'Introduction Yourself - {self.company} Exam')
        self.config(bg='#fff')
        self.bind('<Escape>', lambda e: e.widget.quit())

        # Heading
        self.Header = Label(self, text=f'Welcome to the {self.company}.', font='arial-round-mt 16', bg=self['bg'], justify='center')
        self.Header.pack(side='top', padx=5, pady=5, ipadx=10, ipady=10)

        # User Name
        user = Label(master=self, text="Student Name", font='times-new-roman 16 italic', bg=self['bg'], fg='#000')
        user.pack(anchor='nw', padx=5, pady=5, ipadx=10, ipady=5)

        self.user_name = Entry(master=self, textvariable=self.get_userN, font='times-new-roman 14 italic', bg='#fff', fg='#000')
        self.user_name.pack(anchor='ne', padx=5, pady=5, ipadx=10, ipady=5)
        self.user_name.focus()

        # Course Name
        course = Label(master=self, text="Student Course", font='times-new-roman 16 italic', bg=self['bg'], fg='#000')
        course.pack(anchor='nw', padx=5, pady=5, ipadx=10, ipady=5)

        self.course_name = Entry(master=self, textvariable=self.get_courseN, font='times-new-roman 14 italic', bg='#fff', fg='#000')
        self.course_name.pack(anchor='ne', padx=5, pady=5, ipadx=10, ipady=5)

        # Action Button
        self.action = Button(master=self, text='Start Test', font='arial 16 bold', command=self.freeze, bd=0, foreground='#fff', background='red', activebackground='green', activeforeground='blue')
        self.action.pack(side='bottom', padx=5, pady=5, ipadx=5, ipady=5)

        self.geometry("500x300")
        self.resizable(False, False)
        self.mainloop()

    def freeze(self):
        if not len(self.get_userN.get()) < 3:
            self.user_name.config(state="disabled")
            if len(self.get_courseN.get()) < 3:
                self.course_name.config(bg="#f55")
            else:
                self.course_name.config(state="disabled")
                self.action.destroy()
                return self.main()
        else:
            self.user_name.config(bg="#f55")

    def JsonSave(self):
        if os.path.exists(self.json_path):
            with open(self.json_path, 'r') as file:
                existing_data = json.load(file)

            new_data = {self.get_userN.get()+"_"+self.time.strftime("%d-%m-%y-%H-%M_%p"): {"Total": self.total, "Result": self.setter}}
            existing_data.update(new_data)

            with open(self.json_path, 'w') as file:
                json.dump(existing_data, file, indent=4)
        else:
            directory = os.path.dirname(self.json_path)
            if not os.path.exists(directory):
                os.makedirs(directory)
            new_data = {self.get_userN.get()+"_"+self.time.strftime("%d-%m-%y-%H-%M_%p"): {"Total": self.total, "Result": self.setter}}
            with open(self.json_path, 'w') as file:
                json.dump(new_data, file, indent=4)
        return self.Header.config(text=f"You will get your result\non {self.time.strftime(f'%d-%m-%y')}", pady=500)

    def correction(self):
        for n, a in enumerate(self.setter.values()):
            if self.result[n].upper() == a.upper():
                self.total += 1
        else:
            return self.JsonSave()

    def destroy_question_widgets(self):
        for widget in ['Q', 'a', 'b', 'c', 'd', 'pre', 'nxt', 'gapping']:
            if hasattr(self, widget):
                getattr(self, widget).destroy()
        return self.main()

    def main(self):
        self.num = 0
        self.title(f"{self.company} Question Paper")
        self.bind("<Escape>", lambda e: e.widget.quit())
        self.config(bg='#fff')
        self.var = StringVar()
        self.Header.config(text=f'Welcome to {self.company} Exam, {self.get_userN.get()}')
        self.custom_style = ttk.Style()
        self.custom_style.configure("Custom.TRadiobutton", background=self['bg'], foreground="#333", font=("Helvetica", 12), padding=10)

        # Load the image
        image = Image.open(r"logo.jpg")  # Replace with the actual path to your image
        image = image.resize((100, 100), Image.ADAPTIVE)
        self.background_image = ImageTk.PhotoImage(image)
        self.canvas = Canvas(self, width=100, height=100, bg=self['bg'])
        self.canvas.place(x=700, y=5)
        self.canvas.create_image(0, 0, anchor="nw", image=self.background_image)

        def next_question():
            self.setter.update({self.num: self.var.get()})
            self.var.set('')
            self.num += 1
            try:
                que = self.question[self.num]
            except IndexError:
                return self.correction()
            else:
                return display_question(que)

        def prev_question():
            if self.num > 0:
                self.num -= 1
                que = self.question[self.num]
                return display_question(que)

        def display_question(que):
            self.Q.config(text=f"Qn.{self.num + 1}) {que[0]}")
            self.a.config(text=f'{que[1]}')
            self.b.config(text=f'{que[2]}')
            self.c.config(text=f'{que[3]}')
            self.c.config(text=f'{que[4]}')

        self.gapping = Label(self, bg=self['bg'])
        self.gapping.pack(side='top', anchor='center', pady=10)
        self.Q = Label(self, text=f"Qn.{self.num + 1}) {self.question[self.num][0]}", bg=self['bg'], fg='#000', font='arial 16 bold', wraplength=self.winfo_screenwidth() - 1000)
        self.Q.pack(side='top', anchor='center')

        self.a = ttk.Radiobutton(self, padding=5, variable=self.var, value='A', text=self.question[0][1], style="Custom.TRadiobutton")
        self.a.pack(fill='x', anchor='center', padx=10, pady=5)

        self.b = ttk.Radiobutton(self, padding=5, variable=self.var, value='B', text=self.question[0][2], style="Custom.TRadiobutton")
        self.b.pack(fill='x', anchor='center', padx=10, pady=5)

        self.c = ttk.Radiobutton(self, padding=5, variable=self.var, value='C', text=self.question[0][3], style="Custom.TRadiobutton")
        self.c.pack(fill='x', anchor='center', padx=10, pady=5)

        self.d = ttk.Radiobutton(self, padding=5, variable=self.var, value='D', text=self.question[0][4], style="Custom.TRadiobutton")
        self.d.pack(fill='x', anchor='center', padx=10, pady=5)

        self.pre = Button(self, text="< Preview", font="times 16", bg="#fff", fg="#f0f", command=prev_question)
        self.pre.pack(anchor="s", side='left', padx=15, ipadx=10, ipady=5)

        self.nxt = Button(self, text="Next >", font="times 16", bg="#fff", fg="#f0f", command=next_question)
        self.nxt.pack(anchor="s", side='right', padx=15, ipadx=10, ipady=5)

        self.geometry("800x650")
        self.mainloop()


screen = Main("Company Name")
screen.intro()
