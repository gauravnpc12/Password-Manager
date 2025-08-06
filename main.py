from tkinter import *
from tkinter import messagebox
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="OOPS", message="Please don't leave any fields empty.")
    else:
       is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\nDo you want to save?")
       if is_ok:        
          with open("data.txt", "a") as data_file:
            data_file.write(f"{website}  {email}  {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file=r"C:\Users\anand\OneDrive\Desktop\web development\web d\project\Password_Manager_GUI\logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.pack()
canvas.grid(column=1, row=0)
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="email/username:")
email_label.grid(column=0,row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "anandgaurav23@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)
password_entry.focus()
add_button = Button(text="Add",command=save)
add_button.grid(column=0, row=4, columnspan=2)




window.mainloop()
