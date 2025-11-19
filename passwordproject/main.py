# Richard mesioye

#attempt 2 make a password checker login page


import json
import tkinter as tk
from os import remove
from os.path import exists



# USER CLASS
class User:
    def __init__(self, username, password, age, education):
        self.username = username
        self.password = password
        self.age = age
        self.education = education

        #self.status = status

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "age": self.age,
            "education": self.education
            #"status": self.status
        }

    @classmethod
    def from_dict(cls, cdata):
        return cls(
            username=cdata["username"],
            password=cdata["password"],
            age=cdata["age"],
            education=cdata["education"]
        )


from encrypt import encrypt, check_validity


CREDENTIALS_FILE = "credentials.json"
current_user = ""
# load saved login things
if exists(CREDENTIALS_FILE):
    with open(CREDENTIALS_FILE, "r") as f:
        data = json.load(f)
        CREDENTIALS = {user: User.from_dict(info) for user, info in data.items()}
else:
    CREDENTIALS = {}

# GUI
root = tk.Tk()
root.geometry("500x500")
root.title("Login Page Project")

def clear_save():
    try:
        if exists(CREDENTIALS_FILE):
            remove(CREDENTIALS_FILE)
        CREDENTIALS.clear()
        print("all credentials cleared successfully.")
    except Exception as e:
        print(f"Error clearing creds: {e}")


def clear_entry(event):
    event.widget.delete(0, tk.END)

    event.widget.config(fg="black")

# feedback
message = tk.Label(root, text="", fg="red", font=("Arial", 12))
message.pack()

# FUNC

def check_conditions(temp_pass):
    pass

def login():
    user = username_box.get()
    password = password_box.get()

    if user in CREDENTIALS and encrypt(password) == CREDENTIALS[user].password:
        message.config(text="✅ Access Granted", fg="green")
        username_box.delete(0, tk.END)
        password_box.delete(0, tk.END)
        global current_user
        current_user = user
        root.after(3000, root.destroy)
    else:
        username_box.delete(0, tk.END)
        username_box.insert(0, "Access Denied")
        username_box.config(fg="red")
        password_box.delete(0, tk.END)
        age_box.delete(0, tk.END)
        edu_box.delete(0, tk.END)
        message.config(text="❌ Access Denied", fg="red")

def signup():
    user = username_box.get()
    password = password_box.get()
    age = age_box.get()
    edu = edu_box.get()

    if user in CREDENTIALS:
        message.config(text="❌ Username already exists", fg="red")
    else:
        val = check_validity(password)
        if not val == True:
            message.config(text=val, fg="red")
        else:
            c_user = User(username=user, password=encrypt(password), age=age, education=edu)
            CREDENTIALS[user] = c_user
            with open(CREDENTIALS_FILE, "w") as g:
                json.dump({u: CREDENTIALS[u].to_dict() for u in CREDENTIALS}, g, indent=4)
            message.config(text="✅ User signed up", fg="green")

            username_box.delete(0, tk.END)
            username_box.insert(0, "Enter Username")

            password_box.delete(0, tk.END)
            password_box.insert(0, "Enter Password")

            age_box.delete(0, tk.END)
            age_box.insert(0, "Enter Age")

            edu_box.delete(0, tk.END)
            edu_box.insert(0, "Place of Education")


#laayout

label = tk.Label(root, height=3, font=("Arial", 25), text="Welcome.")
label.pack(padx=5, pady=10)

username_box = tk.Entry(root, font=("Arial", 15), fg="grey")
username_box.insert(0, "Enter Username")
username_box.bind("<FocusIn>", clear_entry)
username_box.pack(pady=5)

age_box = tk.Entry(root, font=("Arial", 15), fg="grey")
age_box.insert(0, "Enter Age")
age_box.bind("<FocusIn>", clear_entry)
age_box.pack(pady=5)

edu_box = tk.Entry(root, font=("Arial", 15), fg="grey")
edu_box.insert(0, "Place of Education")
edu_box.bind("<FocusIn>", clear_entry)
edu_box.pack(pady=5)


# pframe
password_frame = tk.Frame(root)
password_frame.pack(pady=10)

password_box = tk.Entry(password_frame, font=("Arial", 15), fg="grey", show="*")
password_box.insert(0, "Enter Password")
password_box.bind("<FocusIn>", clear_entry)
password_box.pack(side="left")

def reveal_pass():
    if not password_box.cget("show") == "*":
        password_box.config(show="*")
    else:
        password_box.config(show="")


toggle_btn = tk.Button(password_frame, text="👁", command=reveal_pass)
toggle_btn.pack(side="left", padx=5)


login_button = tk.Button(root, text="Login", font=("Arial", 14), command=login)
login_button.pack(pady=10)

signup_button = tk.Button(root, text="Sign Up", font=("Arial", 14), command=signup)
signup_button.pack(pady=10)

wipe_button = tk.Button(root, text="Wipe saved", font=("Arial", 10), command=clear_save)
wipe_button.place(x=10,y=460)


root.mainloop()

