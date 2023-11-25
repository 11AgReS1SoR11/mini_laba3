from PIL import Image
from io import BytesIO
import tkinter as tk
from tkinter import messagebox
import requests

def handle_fox_search(endpoint_number):
    try:
        image_url = 'https://github.com/xinitrc-dev/randomfox.ca/blob/master/images/{}.jpg'.format(endpoint_number)
        # Заменяем URL для просмотра сырого файла на GitHub
        raw_url = image_url.replace('github.com', 'raw.githubusercontent.com').replace('/blob/', '/')
        response = requests.get(raw_url)
        if response.status_code == 200:
            image = Image.open(BytesIO(response.content))
            image.show()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def handle_random_fox_search():
    try:
        url = 'https://randomfox.ca/floof/'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            response2 = requests.get(data["image"])
            image = Image.open(BytesIO(response2.content))
            image.show()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def exit_application():
    root.destroy()

def main():
    global root
    root = tk.Tk()
    root.title("HTTP Requests Example")
    root.geometry("500x450")

    bg_color = "#5E64FF"
    button_bg_color = "#4CAF50"

    root.configure(bg=bg_color)

    button1 = tk.Button(root, text="FOX 1", command=lambda: handle_fox_search(1), bg=button_bg_color, height=5, width=40)
    button2 = tk.Button(root, text="FOX 2", command=lambda: handle_fox_search(2), bg=button_bg_color, height=5, width=40)
    button3 = tk.Button(root, text="FOX Random", command=lambda: handle_random_fox_search(), bg=button_bg_color, height=5, width=40)
    exit_button = tk.Button(root, text="Exit", command=exit_application, bg="red", fg="white", height=5, width=40)

    button1.pack(pady=10)
    button2.pack(pady=10)
    button3.pack(pady=10)
    exit_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
