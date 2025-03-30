import tkinter as tk
import pyautogui
import keyboard
from PIL import ImageGrab

def get_color():
    x, y = pyautogui.position()
    screen = ImageGrab.grab()
    color = screen.getpixel((x, y))
    color_hex = f'#{color[0]:02x}{color[1]:02x}{color[2]:02x}'
    label.config(text=f"Color: {color_hex}", bg=color_hex, fg="white" if sum(color) < 384 else "black")

root = tk.Tk()
root.title("Color Picker")
root.geometry("400x300")

label = tk.Label(root, text="Press 'Enter' to get color", font=("Arial", 14))
label.pack(expand=True, fill=tk.BOTH)
keyboard.add_hotkey('enter', get_color)

root.mainloop()
