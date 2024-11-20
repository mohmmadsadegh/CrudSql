from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Relishionshib import * 

class App(Frame):
    def __init__(self, screen):
        super().__init__(screen)
        self.screen = screen
        self.repository = Repository()
        self.cratewidget()
    
    
    def cratewidget(self):
        #  lable
        self.lblName = Label(self.screen, text="نام", justify="right")
        self.lblName.place(x=900, y=40)
        self.lblFamili = Label(self.screen, text="نام خانوادگی", justify="right")
        self.lblFamili.place(x=900, y=80)
        self.lblAge = Label(self.screen, text="سن", justify="right")
        self.lblAge.place(x=900, y=120)
        self.lblPaye = Label(self.screen, text="پایه", justify="right")
        self.lblPaye.place(x=900, y=160)
        #  input
        self.Name = StringVar()
        self.Famili = StringVar()
        self.Age = StringVar()
        self.Id = StringVar()
        self.Paye = StringVar()
        # Entry
        self.TxtName = Entry(self.screen, justify="right", textvariable=self.Name).place(x=760, y=40)
        self.TxtFamili = Entry(self.screen, justify="right", textvariable=self.Famili).place(x=760, y=80)
        self.TxtAge = Entry(self.screen, justify="right", textvariable=self.Age).place(x=760, y=120)
        self.Txtpaye = Entry(self.screen, justify="right", textvariable=self.Paye).place(x=760, y=160)
        self.TxId = Entry(self.screen, justify="right", textvariable=self.Id).place_forget()
        #  Button
        self.BtnRigester = Button(self.screen, text="ثبت نام", bg="green", fg="black", command=self.OnClickRigester)
        self.BtnRigester.place(x=760, y=190)
        self.UserAll = []
    
    
    def OnClickRigester(self):
        name = self.Name.get()
        famili = self.Famili.get()
        age = self.Age.get()
        paye = self.Paye.get()
        us = {"NAME": name, "Famili": famili, "Age": age, "Paye": paye}
        result = self.Rigester(us)
        if result:
            return True
    
    
    def Rigester(self, user):
        if int(user["Age"]) >= 7:
            self.UserAll.append(user)
            col1 = "student_name,student_famili,student_age,student_paye"
            val1 = " '"+user["Name"]+"', '"+user["Famili"]+"', '"+user["Age"]+"', '"+user["Paye"]+"' "
            #val1 = "'asghar','farhadi','25'"
            self.repository.crate("student", col1, val1)
            messagebox.showinfo("تبریک", "ثبت نام شما در این مدرسه انجام شد")
        else:
            messagebox.showerror("انجام نشد", "شما باید به پیش دبستانی بروید")

if __name__ == "__main__":
    screen = Tk()
    screen.resizable(True, True)
    screen.title("مدرسه")
    screen.geometry("%dx%d+%d+%d" % (1000, 500, 200, 200))
    repository = Repository()
    PageMe = App(screen)
    screen.mainloop()
