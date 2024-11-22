from tkinter import Tk, ttk, messagebox, Frame, Label, StringVar, Entry, Button
from Relishionshib import Repository


class App(Frame):
    def __init__(self, screen):
        super().__init__(screen)
        self.screen = screen
        self.repository = Repository()
        self.create_widgets()

    def create_widgets(self):
        # Labels
        self.lblName = Label(self.screen, text="نام", justify="right")
        self.lblName.place(x=900, y=40)

        self.lblFamili = Label(self.screen, text="نام خانوادگی",
                               justify="right")
        self.lblFamili.place(x=900, y=80)

        self.lblAge = Label(self.screen, text="سن", justify="right")
        self.lblAge.place(x=900, y=120)

        self.lblPaye = Label(self.screen, text="پایه",
                             justify="right")
        self.lblPaye.place(x=900, y=160)

        # Inputs
        self.Name = StringVar()
        self.Famili = StringVar()
        self.Age = StringVar()
        self.Id = StringVar()
        self.Paye = StringVar()

        # Entry Widgets
        self.TxtName = Entry(self.screen, justify="right",
                             textvariable=self.Name)
        self.TxtName.place(x=760, y=40)

        self.TxtFamili = Entry(self.screen, justify="right",
                               textvariable=self.Famili)
        self.TxtFamili.place(x=760, y=80)

        self.TxtAge = Entry(self.screen, justify="right",
                            textvariable=self.Age)
        self.TxtAge.place(x=760, y=120)

        self.TxtPaye = Entry(self.screen, justify="right",
                             textvariable=self.Paye)
        self.TxtPaye.place(x=760, y=160)

        # Buttons
        self.BtnRegister = Button(self.screen, text="ثبت نام", bg="green",
                                  command=self.on_click_register)
        self.BtnRegister.place(x=760, y=190)

        self.BtnDelete = Button(self.screen, text="حذف", bg="red",
                                command=self.on_click_delete)
        self.BtnDelete.place_forget()

        self.BtnEdit = Button(self.screen, text="ویرایش", bg="orange",
                              command=self.on_click_edit)
        self.BtnEdit.place_forget()

        # Table
        self.tbl = ttk.Treeview(self.screen,
                                columns=("c1", "c2", "c3", "c4", "c5"),
                                show="headings", height=10)
        self.tbl.heading("c1", text="پایه")
        self.tbl.heading("c2", text="سن")
        self.tbl.heading("c3", text="نام خانوادگی")
        self.tbl.heading("c4", text="نام")
        self.tbl.heading("c5", text="شناسه")
        self.tbl.column("c5", width=50)
        self.tbl.bind("<ButtonRelease-1>", self.get_selection)
        self.tbl.place(x=650, y=250)

        self.load_data()

    def on_click_register(self):
        user = {
            "Name": self.Name.get(),
            "Famili": self.Famili.get(),
            "Age": self.Age.get(),
            "Paye": self.Paye.get(),
        }
        if int(user["Age"]) >= 7:
            col_names = ("""student_name, student_famili,
                         student_age, student_paye""")
            values = f"""'{user['Name']}', '{user['Famili']}',
            {user['Age']}, '{user['Paye']}'"""
            if self.repository.create("student", col_names, values):
                messagebox.showinfo("موفقیت", "ثبت با موفقیت انجام شد")
                self.clear_inputs()
                self.load_data()
            else:
                messagebox.showerror("خطا", "خطایی در ثبت رخ داده است")
        else:
            messagebox.showerror("خطا", "سن باید بیشتر از 7 سال باشد")

    def clear_inputs(self):
        self.Name.set("")
        self.Famili.set("")
        self.Age.set("")
        self.Paye.set("")
        self.TxtName.focus_set()

    def load_data(self):
        for row in self.tbl.get_children():
            self.tbl.delete(row)
        records = self.repository.read("student")
        for record in records:
            self.tbl.insert("", "end", values=(record[4], record[3],
                                               record[2], record[1],
                                               record[0]))

    def get_selection(self, event):
        selected_item = self.tbl.focus()
        if selected_item:
            values = self.tbl.item(selected_item, "values")
            self.Id.set(values[4])
            self.Name.set(values[3])
            self.Famili.set(values[2])
            self.Age.set(values[1])
            self.Paye.set(values[0])
            self.BtnEdit.place(x=760, y=190)
            self.BtnDelete.place(x=860, y=190)

    def on_click_edit(self):
        set_clause = (
            f"student_name = '{self.Name.get()}', "
            f"student_famili = '{self.Famili.get()}', "
            f"student_age = {self.Age.get()}, "
            f"student_paye = '{self.Paye.get()}'"
        )
        where_clause = f"student_id = {self.Id.get()}"
        if self.repository.update("student", set_clause, where_clause):
            messagebox.showinfo("موفقیت", "ویرایش با موفقیت انجام شد")
            self.clear_inputs()
            self.load_data()
        else:
            messagebox.showerror("خطا", "ویرایش ناموفق بود")

    def on_click_delete(self):
        where_clause = f"student_id = {self.Id.get()}"
        if self.repository.delete("student", where_clause):
            messagebox.showinfo("موفقیت", "حذف با موفقیت انجام شد")
            self.clear_inputs()
            self.load_data()
        else:
            messagebox.showerror("خطا", "حذف ناموفق بود")


if __name__ == "__main__":
    screen = Tk()
    screen.title("مدرسه")
    screen.geometry("1000x500")
    app = App(screen)
    screen.mainloop()
