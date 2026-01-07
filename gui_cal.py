import tkinter as tk

# 1. Main Window එක හදනවා
root = tk.Tk()
root.title("My First App")
root.geometry("300x200")

# 2. Text එකක් පෙන්වන්න Label එකක්
label = tk.Label(root, text="Hello, Welcome to my App!")
label.pack(pady=20)

# 3. Button එකක් ක්ලික් කළාම වෙන දේ
def click_me():
    label.config(text="Button Clicked! Success!")

button = tk.Button(root, text="Click Here", command=click_me)
button.pack()

# 4. Window එක දිගටම පෙන්වන්න (Loop)
root.mainloop()