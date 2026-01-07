import tkinter as tk
import operator

# --- Backend Logic (ඔයාගේ සම්පූර්ණ Dictionary එක) ---
ops = {
    "+": operator.add, "-": operator.sub, "*": operator.mul,
    "/": operator.truediv, "^": operator.pow, "%": operator.mod,
    "//": operator.floordiv, "**": operator.pow, ">>": operator.rshift,
    "<<": operator.lshift, "&": operator.and_, "|": operator.or_,
    "^": operator.xor
}

def calculate():
    try:
        n1 = float(entry_n1.get()) 
        n2 = float(entry_n2.get())
        mark = entry_mark.get()
        
        # Validation and Calculation
        if mark in ops:
            # Zero division check
            if mark in ["/", "//", "%"] and n2 == 0:
                result_label.config(text="Error: Divide by 0", fg="red")
            else:
                # දශම සංඛ්‍යා Bitwise කරන්න බැරි නිසා integer වලට හරවනවා
                if mark in [">>", "<<", "&", "|", "^"]:
                    res = ops[mark](int(n1), int(n2))
                else:
                    res = ops[mark](n1, n2)
                
                result_label.config(text=f"Answer: {round(res, 2)}", fg="#00FF00") # කොළ පාටින් උත්තරය
        else:
            result_label.config(text="Invalid Operation!", fg="red")
            
    except ValueError:
        result_label.config(text="Please enter valid numbers!", fg="orange")

# --- UI Setup ---
root = tk.Tk()
root.title("Google Bound - Advanced Calc")
root.geometry("350x450")
root.configure(bg="#2c5035") # ලස්සන තද පාටක් (Dark theme)

# Styles
label_style = {"bg": "#2c3e50", "fg": "white", "font": ("Arial", 10)}

tk.Label(root, text="ENTER 1st NUMBER:", **label_style).pack(pady=5)
entry_n1 = tk.Entry(root, font=("Arial", 12), justify='center')
entry_n1.pack(ipady=5)

tk.Label(root, text="MARK (+, -, *, /, **, %, >>, <<, &):", **label_style).pack(pady=5)
entry_mark = tk.Entry(root, font=("Arial", 12), justify='center')
entry_mark.pack(ipady=5)

tk.Label(root, text="ENTER 2nd NUMBER:", **label_style).pack(pady=5)
entry_n2 = tk.Entry(root, font=("Arial", 12), justify='center')
entry_n2.pack(ipady=5)

# Calculate Button
btn = tk.Button(root, text="CALCULATE", command=calculate, bg="#27ae60", fg="white", font=("Arial", 10, "bold"), width=15)
btn.pack(pady=30)

# Result Area
result_label = tk.Label(root, text="READY", font=("Arial", 14, "bold"), bg="#2c3e50", fg="#ecf0f1")
result_label.pack()

root.mainloop()