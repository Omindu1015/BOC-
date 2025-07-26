import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox

root = tk.Tk()
root.title("BOC Queue Management")
root.geometry("1280x800")
root.configure(bg="white")

# Screen scaling factor based on resolution
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

font_scale = screen_width / 1920  # assuming base design was for 1920px width
font_large = int(64 * font_scale)
font_medium = int(20 * font_scale)
font_small = int(12 * font_scale)


def on_icon_click(event):
    messagebox.showinfo("Profile", "Profile icon clicked!")

# --- Grid Configuration ---
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(0, weight=1)

# --- Header Frame ---
header_frame = tk.Frame(root, bg="white")
header_frame.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=20, pady=10)
header_frame.grid_columnconfigure(0, weight=1)
header_frame.grid_columnconfigure(1, weight=1)
header_frame.grid_columnconfigure(2, weight=1)

# Left Section (Logo + Branch Name)
logo_img = Image.open("E:/BOC-/assets/bank_of_Ceylon_logo.png")
logo_img = logo_img.resize((int(80 * font_scale), int(40 * font_scale)))
logo_photo = ImageTk.PhotoImage(logo_img)

left_section = tk.Frame(header_frame, bg="white")
left_section.grid(row=0, column=0, sticky="w")

logo_label = tk.Label(left_section, image=logo_photo, bg="white")
logo_label.grid(row=0, column=0, padx=(0, 10))
tk.Label(left_section, text="Kadawatha - West", font=("Arial", font_medium, "bold"), bg="white", fg="black").grid(row=0, column=1)

# Right Section (User Info + Icon)
right_section = tk.Frame(header_frame, bg="white")
right_section.grid(row=0, column=2, sticky="e")

user_label = tk.Label(right_section, text="Sachinthani", font=("Arial", font_small, "bold"), bg="white", fg="black")
user_label.grid(row=0, column=0, padx=(10, 5))

separator = tk.Frame(right_section, bg="gray", width=2, height=20)
separator.grid(row=0, column=1, padx=5)

nic_label = tk.Label(right_section, text="9012345678V", font=("Arial", font_small), bg="white", fg="black")
nic_label.grid(row=0, column=2, padx=(0, 10))

canvas = tk.Canvas(right_section, width=40, height=40, bg="white", highlightthickness=0, cursor="hand2")
canvas.grid(row=0, column=3)
circle = canvas.create_oval(5, 5, 35, 35, fill="#fddd01", outline="black")
canvas.tag_bind(circle, "<Button-1>", on_icon_click)

# --- Bottom Bars ---
tk.Frame(root, bg="#231f20", height=4).grid(row=1, column=0, columnspan=3, sticky="ew")
tk.Frame(root, bg="#fddd00", height=6).grid(row=2, column=0, columnspan=3, sticky="ew")

# --- Main Content ---
main_frame = tk.Frame(root, bg="white")
main_frame.grid(row=3, column=0, columnspan=3, sticky="nsew", padx=20, pady=20)
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)
main_frame.grid_columnconfigure(2, weight=1)

# Token Box
token_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid")
token_frame.grid(row=0, column=0, sticky="nsew", padx=10)
token_frame.grid_rowconfigure(1, weight=1)
token_frame.grid_columnconfigure(0, weight=1)

top = tk.Frame(token_frame, bg="#fddd00", height=120)
top.grid(row=0, column=0, sticky="ew")
tk.Label(top, text="1002", font=("Arial", font_large, "bold"), bg="#fddd00").pack(expand=True)

bottom = tk.Frame(token_frame, bg="#d3d3d3")
bottom.grid(row=1, column=0, sticky="nsew")
bottom.grid_columnconfigure(0, weight=1)

services = ["Pawning", "Personal Banking", "Cash Deposit"]
checkbox_vars = []

for i, service in enumerate(services):
    var = tk.BooleanVar()
    checkbox_vars.append(var)
    row = tk.Frame(bottom, bg="#d3d3d3")
    row.grid(row=i, column=0, padx=10, pady=5, sticky="ew")
    row.grid_columnconfigure(1, weight=1)

    circle = tk.Canvas(row, width=28, height=28, bg="#d3d3d3", highlightthickness=0)
    circle.grid(row=0, column=0)
    circle.create_oval(2, 2, 26, 26, fill="gold", outline="")
    circle.create_text(14, 14, text=str(i+1), font=("Arial", int(10 * font_scale), "bold"))

    tk.Label(row, text=service, font=("Arial", font_small, "bold"), bg="#d3d3d3").grid(row=0, column=1, padx=10, sticky="w")
    tk.Checkbutton(row, variable=var, bg="#d3d3d3").grid(row=0, column=2, padx=5, sticky="e")

tk.Button(bottom, text="Add / Reorder", font=("Arial", font_small), bg="black", fg="white").grid(row=3, column=0, pady=10)
tk.Frame(bottom, bg="black", height=2).grid(row=4, column=0, sticky="ew", pady=(10, 0))

footer = tk.Frame(bottom, bg="#d3d3d3")
footer.grid(row=5, column=0, sticky="ew", pady=5)
tk.Label(footer, text="Customer Waiting Time", font=("Arial", font_small), bg="#d3d3d3").grid(row=0, column=0, padx=10, sticky="w")
tk.Label(footer, text="5mnts", font=("Arial", font_small, "bold"), bg="#d3d3d3").grid(row=0, column=1, padx=10, sticky="e")

# Middle Panel Buttons
middle_panel = tk.Frame(main_frame, bg="white")
middle_panel.grid(row=0, column=1, sticky="nsew")
for i in range(3):
    middle_panel.grid_columnconfigure(i, weight=1)

# Button labels and colors
btn_style = [
    ("CALL", "#444"), ("SKIP", "red"),
    ("HOLD", "#fddd00"), ("RECALL", "orange"),
    ("PROCEED", "#2c57a3")
]

# Buttons: 3 in first row
for i, (text, color) in enumerate(btn_style[:3]):
    tk.Button(middle_panel, text=text, bg=color, fg="white",
              font=("Arial", font_small, "bold"), width=12, height=2)\
        .grid(row=0, column=i, padx=10, pady=10, sticky="nsew")

# Buttons: 2 in second row (centered under columns 1 and 2)
for i, (text, color) in enumerate(btn_style[3:]):
    tk.Button(middle_panel, text=text, bg=color, fg="white",
              font=("Arial", font_small, "bold"), width=12, height=2)\
        .grid(row=1, column=i+0, padx=10, pady=10, sticky="nsew")



# --- Right Panel (Stats + Display/Settings + Dropdown) ---
right_panel = tk.Frame(main_frame, bg="white")
right_panel.grid(row=0, column=2, sticky="nsew", padx=(10, 0))
right_panel.grid_columnconfigure(0, weight=1)

# Styled Stats Rows
stats_data = [
    ("✔", "Total Completed Tokens", "20"),
    ("⏰", "Total Pending Tokens", "33"),
    ("⏱", "Turn Around Time", "2m")
]

for i, (icon, label, value) in enumerate(stats_data):
    row = tk.Frame(right_panel, bg="#d3d3d3", pady=5)
    row.grid(row=i, column=0, sticky="ew", padx=(0, 5))
    row.grid_columnconfigure(1, weight=1)

    tk.Label(row, text=icon, font=("Arial", font_small), bg="#d3d3d3").grid(row=0, column=0, padx=5)
    tk.Label(row, text=label, font=("Arial", font_small, "bold"), bg="#d3d3d3").grid(row=0, column=1, sticky="w")
    tk.Label(row, text=f"-  {value}", font=("Arial", font_small, "bold"), bg="#d3d3d3").grid(row=0, column=2, sticky="e", padx=5)

# Display and Settings Buttons with Unicode
btn_style = [
    ("Display", "🖥️"),
    ("Settings", "⚙")
]

for i, (text, icon) in enumerate(btn_style):
    full_text = f"{text}  {icon}"
    btn = tk.Button(right_panel, text=full_text, font=("Arial", font_small, "bold"),
                    bg="#2b2b2b", fg="#fddd00", relief="groove", anchor="w", padx=10)
    btn.grid(row=i, column=1, sticky="ew", padx=(10, 0), pady=5)

# Yellow Border Box for Dropdown & Break
yellow_border = tk.Frame(right_panel, bg="#fddd00", padx=2, pady=2)
yellow_border.grid(row=4, column=0, columnspan=2, pady=(20, 0), sticky="ew")

dropdown_row = tk.Frame(yellow_border, bg="#d3d3d3")
dropdown_row.pack(fill="x")

dropdown = ttk.Combobox(dropdown_row, values=["Administrative", "Technical", "Customer Service"], width=20)
dropdown.set("Administrative")
dropdown.pack(side="left", padx=10, pady=10, fill="x", expand=True)

break_btn = tk.Button(dropdown_row, text="Break", bg="black", fg="white", font=("Arial", font_small, "bold"))
break_btn.pack(side="right", padx=10, pady=10)

# Start the app
root.mainloop()
