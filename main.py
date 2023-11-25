from PIL import Image
from io import BytesIO
import tkinter as tk
from tkinter import messagebox
import requests

def get_image(url):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    image.show()

def handle_random_search(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if "image" in data:
                get_image(data["image"])
            elif "url" in data:
                # ignore gif and mp4
                if (data["url"][-3:] == "mp4" or data["url"][-3:] == "gif" or data["url"][-3:] == "GIF"):
                    handle_random_search(url)
                    return
                get_image(data["url"])
            else:
               raise ValueError("Broke url")

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

    button1 = tk.Button(root, text="CAT", command=lambda: get_image('https://cataas.com/cat'), bg=button_bg_color, height=5, width=40)
    button2 = tk.Button(root, text="DOG", command=lambda: handle_random_search('https://random.dog/woof.json'), bg=button_bg_color, height=5, width=40)
    button3 = tk.Button(root, text="FOX", command=lambda: handle_random_search('https://randomfox.ca/floof/'), bg=button_bg_color, height=5, width=40)
    exit_button = tk.Button(root, text="Exit", command=exit_application, bg="red", fg="white", height=5, width=40)

    button1.pack(pady=10)
    button2.pack(pady=10)
    button3.pack(pady=10)
    exit_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
