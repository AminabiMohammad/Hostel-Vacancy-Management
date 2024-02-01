from tkinter import Tk, Frame, Label, Entry, Button, Listbox, Scrollbar, messagebox
fonts = ('Calibri', 25, 'bold')
font1 = ('Calibri', 20, 'bold')
user1 = '22B01A0577'
passw = 'svecw'
user2 = '22B01A05A7'
passw = 'svecw'

class Login:
    def __init__(self, root):
        self.root = root
        self.login_frame = Frame(self.root, width=700, height=500, bg='Light yellow')
        self.login_frame.place(x=0, y=0)

        title_label = Label(self.login_frame, text='STUDENT LOGIN', font=font1, bg='Dark Orange', fg='White')
        title_label.place(x=(self.login_frame.winfo_reqwidth() - title_label.winfo_reqwidth()) / 2.5, y=70)

        self.user_name = Label(self.login_frame, text='USER NAME    : ', font=fonts, bg='white', fg='Orange', width=12)
        self.user_name.place(x=100, y=150)
        self.user_name_entry = Entry(self.login_frame, width=13, font=font1, bg='white')
        self.user_name_entry.place(x=350, y=150)

        self.user_pass = Label(self.login_frame, text='PASSWORD    : ', font=fonts, bg='white', fg='Orange', width=12)
        self.user_pass.place(x=100, y=200)
        self.user_pass_entry = Entry(self.login_frame, width=13, font=font1, bg='white', show=".")
        self.user_pass_entry.place(x=350, y=200)

        self.submit_btn = Button(self.login_frame, text='LOGIN', fg='White', bg='Dark Orange', font=font1, command=self.check_login, cursor='hand2', activebackground='Light Yellow')
        self.submit_btn.place(x=250, y=300)

    def check_login(self):
        self.name1 = self.user_name_entry.get()
        self.password1 = self.user_pass_entry.get()
        self.name2 = self.user_name_entry.get()
        self.password2 = self.user_pass_entry.get()
        if self.name1 == user1:
            if self.password1 == passw:
                messagebox.showinfo('WELCOME', 'WELCOME USER')
                self.login_frame.destroy()
                dashboard = Dashboard(self.root)
            else:
                messagebox.showerror('WRONG PASSWORD', 'CHECK YOUR PASSWORD')

        elif self.name2 == user2:
            if self.password2 == passw:
                messagebox.showinfo('WELCOME', 'WELCOME USER')
                self.login_frame.destroy()
                dashboard = Dashboard(self.root)
            else:
                messagebox.showerror('WRONG PASSWORD', 'CHECK YOUR PASSWORD')
        else:
            messagebox.showerror('WRONG ID', 'INVALID USERNAME')

class Dashboard:
    def __init__(self, root):
        self.root = root
        self.root.title('CHECK VACANIES')
        self.d_frame = Frame(self.root, width=700, height=500, bg='Light Green')
        self.d_frame.place(x=0, y=0)

        self.search_button = Button(self.d_frame, text='Search', fg='Black', bg='White', font=font1, cursor='hand2', activebackground='Light Yellow', command=self.search)
        self.search_button.place(x=180, y=50, height=40)

        self.search_entry = Entry(self.d_frame, font=font1, bg='white', width=20)
        self.search_entry.place(x=275, y=50)

        self.hostel_listbox = Listbox(self.d_frame, font=font1, bg='White', selectbackground='Pink', width=15, height=5)
        self.hostel_listbox.place(x=220, y=130)

        self.hostel_listbox.insert(1, ' Sarada')
        self.hostel_listbox.insert(2, ' Medha')
        self.hostel_listbox.insert(3, ' Vaishnavi')

        self.vacant_rooms_label = Label(self.d_frame, text='', font=font1, bg='Light Green')
        self.vacant_rooms_label.place(x=450, y=150)
        self.vacant_rooms_data = {
            ' Sarada': ['101', '102', '103'],
            ' Medha': ['201'],
            ' Vaishnavi': ['117','220']
        }

    def search(self):
        self.hostel_listbox.selection_clear(0, 'end')
        search_query = self.search_entry.get()

        for index, hostel_name in enumerate(self.hostel_listbox.get(0, 'end')):
            if search_query.lower() in hostel_name.lower():
                self.hostel_listbox.selection_set(index)
                selected_hostel = self.hostel_listbox.get(index)
                vacant_rooms = self.vacant_rooms_data[selected_hostel]
                self.vacant_rooms_label.config(text=f'Vacant Rooms:\n {vacant_rooms}\nFor Any Queries\ncontact : 9381614739')

if __name__ == "__main__":
    root = Tk()
    root.title('STUDENT LOGIN')
    root.geometry('700x500+350+140')
    root.resizable(False, False)
    login = Login(root)
    root.mainloop()
