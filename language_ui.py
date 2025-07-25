import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# --- Rounded rectangle helper ---
def round_rectangle(obj, x1, y1, x2, y2, r=25, **kwargs):
    points = [
        x1 + r, y1,
        x2 - r, y1,
        x2, y1,
        x2, y1 + r,
        x2, y2 - r,
        x2, y2,
        x2 - r, y2,
        x1 + r, y2,
        x1, y2,
        x1, y2 - r,
        x1, y1 + r,
        x1, y1
    ]
    return obj.create_polygon(points, **kwargs, smooth=True)



# --- Canvas-based rounded button ---
def create_rounded_button(parent, text, command):
    canvas_width = 350
    canvas_height = 140
    canvas = tk.Canvas(parent, width=canvas_width, height=canvas_height, bg='white', highlightthickness=0)

    button_shape = round_rectangle(
        canvas,
        5, 5,
        canvas_width - 5, canvas_height - 5,
        r=30,
        fill="#fddd01",
        outline="#000000",
        width=2
    )

    button_text = canvas.create_text(
        canvas_width // 2, canvas_height // 2,
        text=text,
        font=("Arial", 32, "bold"),
        fill="black"
    )

    def on_click(event):
        command()

    canvas.tag_bind(button_shape, "<Button-1>", on_click)
    canvas.tag_bind(button_text, "<Button-1>", on_click)
    return canvas

# --- Language selection actions ---
def select_sinhala():
    messagebox.showinfo("Selected", "ඔබ සිංහල තෝ  රා  ඇත")

def select_tamil():
    messagebox.showinfo("Selected", "நீங்கள் தமிழ் தேர்ந்தெடுத்துள்ளீர்கள்")

def select_english():
    messagebox.showinfo("Selected", "You selected English")

# --- Main window ---
root = tk.Tk()
root.title("BOC Language Selector")
root.geometry("1080x800")
root.configure(bg="white")

# --- Header ---
header_frame = tk.Frame(root, bg="white")
header_frame.pack(side="top", fill="x")
header_frame.columnconfigure(0, weight=1)
header_frame.columnconfigure(1, weight=1)
header_frame.columnconfigure(2, weight=1)

logo_img = Image.open("E:/BOC-/assets/bank_of_Ceylon_logo.png")
logo_img = logo_img.resize((120, 60))
logo_photo = ImageTk.PhotoImage(logo_img)

center_content = tk.Frame(header_frame, bg="white")
center_content.pack()
tk.Label(center_content, image=logo_photo, bg="white").pack(side="left", padx=(0, 10), pady=10)
tk.Label(center_content, text="Kadawatha - West", font=("Arial", 22, "bold"), bg="white", fg="black").pack(side="left")

# Bars
tk.Frame(root, bg="#231f20", height=8).pack(fill="x")
tk.Frame(root, bg="#fddd00", height=10).pack(fill="x")

# --- Body layout ---
main_frame = tk.Frame(root, bg="white")
main_frame.pack(expand=True, fill="both")

left_right_container = tk.Frame(main_frame, bg="white")
left_right_container.pack(expand=True, fill="both")

# Left Panel
left_frame_container = tk.Frame(left_right_container, bg="white")
left_frame_container.pack(side="left", expand=True, fill="both")

left_frame = tk.Frame(left_frame_container, bg="white")
left_frame.pack(expand=True, fill="both")

# Add equal spacers above and below buttons
tk.Frame(left_frame, height=60, bg="white").pack()

buttons_wrapper = tk.Frame(left_frame, bg="white")
buttons_wrapper.pack(expand=True)

create_rounded_button(buttons_wrapper, "සිංහල", select_sinhala).pack(pady=(10, 40))
create_rounded_button(buttons_wrapper, "English", select_english).pack(pady=(10, 40))
create_rounded_button(buttons_wrapper, "தமிழ்", select_tamil).pack(pady=(10, 10))

tk.Frame(left_frame, height=60, bg="white").pack()

# Separator
separator = tk.Frame(left_right_container, bg="#808285", width=2, height=700)
separator.pack(side="left", padx=20, pady=20)

# Right Panel
right_frame_container = tk.Frame(left_right_container, bg="white")
right_frame_container.pack(side="right", expand=True, fill="both")

right_frame = tk.Frame(right_frame_container, bg="white")
right_frame.pack(expand=True, fill="both")

# Top spacer to balance vertical alignment
tk.Frame(right_frame, height=60, bg="white").pack()

# Wrapper for centered welcome texts
welcome_wrapper = tk.Frame(right_frame, bg="white")
welcome_wrapper.pack(expand=True)

# Welcome texts (aligned with buttons)
tk.Label(welcome_wrapper, text="ආයුබෝ  වන්", font=("Arial", 30, "bold"), fg="#808285", bg="white").pack(pady=(10,5))
tk.Label(welcome_wrapper, text="කරුණා  කර ඔබට සේවා  ලබා  ගත\nයුතු භා  ෂා  ව තෝ  රන්න", font=("Arial", 15), fg="#808285", bg="white").pack(pady=(0, 40))

tk.Label(welcome_wrapper, text="Welcome", font=("Arial", 30, "bold"), fg="#808285", bg="white").pack(pady=(50, 5))
tk.Label(welcome_wrapper, text="Please select your language\nthat need to get service", font=("Arial", 15), fg="#808285", bg="white").pack(pady=(0, 40))

tk.Label(welcome_wrapper, text="வரவேற்பு", font=("Arial", 30, "bold"), fg="#808285", bg="white").pack(pady=(60, 5))
tk.Label(welcome_wrapper, text="உங்கள் மொழியைத்\nதேர்ந்தெடுக்கவும்", font=("Arial", 15), fg="#808285", bg="white").pack(pady=(0, 40))

# Bottom spacer
tk.Frame(right_frame, height=60, bg="white").pack()


# --- Start the application ---
root.mainloop()
