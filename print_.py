import customtkinter
import os

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("Theme/lavender.json")

print_ = customtkinter.CTk()
print_.geometry("800x600")
print_.resizable(False,False)
print_.title("Print_")
print_.iconbitmap("Image/icon.ico")

print_.mainloop()