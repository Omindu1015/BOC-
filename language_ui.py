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
    canvas_height = 80
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
        font=("Arial", 22, "bold"),
        fill="black"
    )

    def on_click(event):
        command()

    canvas.tag_bind(button_shape, "<Button-1>", on_click)
    canvas.tag_bind(button_text, "<Button-1>", on_click)
    return canvas

# --- Language selection actions ---
def select_sinhala():
    messagebox.showinfo("Selected", "ඔබ සිංහල තෝ  රා   ඇත")

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
left_frame.pack(expand=True)

# Add buttons with spaced padding
create_rounded_button(left_frame, "සිංහල", select_sinhala).pack(pady=(60, 10))
create_rounded_button(left_frame, "English", select_english).pack(pady=(60, 10))
create_rounded_button(left_frame, "தமிழ்", select_tamil).pack(pady=(60, 10))

# Separator
separator = tk.Frame(left_right_container, bg="#808285", width=2, height=700)
separator.pack(side="left", padx=20, pady=20)

# Right Panel
right_frame_container = tk.Frame(left_right_container, bg="white")
right_frame_container.pack(side="right", expand=True, fill="both")

right_frame = tk.Frame(right_frame_container, bg="white")
right_frame.pack(expand=True)

# Add welcome texts with matching vertical padding
tk.Label(right_frame, text="ආයුබෝ  වන්", font=("Arial", 28, "bold"), fg="#808285", bg="white").pack(pady=(60, 5))
tk.Label(right_frame, text="කරුණා  කර ඔබට සේවා  ව ලබා  ගත\n යුතු භා  ෂා  ව තෝ  රන්න", font=("Arial", 14), fg="#808285", bg="white").pack()

tk.Label(right_frame, text="Welcome", font=("Arial", 28, "bold"), fg="#808285", bg="white").pack(pady=(60, 5))
tk.Label(right_frame, text="Please select your language\nthat need to get service", font=("Arial", 14), fg="#808285", bg="white").pack()

tk.Label(right_frame, text="வரவேற்பு", font=("Arial", 28, "bold"), fg="#808285", bg="white").pack(pady=(60, 5))
tk.Label(right_frame, text="உங்கள் மொழியைத்\n தேர்ந்தெடுக்கவும்", font=("Arial", 14), fg="#808285", bg="white").pack()

# --- Start the application ---
root.mainloop()
