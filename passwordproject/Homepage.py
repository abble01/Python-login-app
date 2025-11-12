
'''
import tkinter as tk
import json
from main import CREDENTIALS_FILE as crds
from main import current_user as u
CREDENTIALS_M = {}


if not crds:
    credential_file = "credentials.json"
    with open(credential_file) as f:
        CREDENTIALS_M = json.load(f)



def open_hp():
    root = tk.Tk()
    root.geometry("700x700")
    root.title("Homepage")

    welcome_title = tk.Label(root, text=f"Welcome {u}")
'''





