import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Service Selection")
root.geometry("1000x350")
root.configure(bg="white")

services = ["Safety Lockers", "Other Matters"]
all_options = ["Pawning", "Personal Banking", "Cash Deposit"]
selected_index = tk.IntVar(value=-1)

row_frames = []
green_check_vars = []
yellow_check_vars = []

# --- Scrollable left container ---
def create_scrollable_container(parent):
    container = tk.Frame(parent, bg="white", bd=1, relief="solid")
    canvas = tk.Canvas(container, bg="#c0c0c0", highlightthickness=0)
    scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scroll_frame = tk.Frame(canvas, bg="#c0c0c0")

    scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    container.grid(row=0, column=0, sticky="nsew")
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    return container, scroll_frame

# --- Layout ---
root.grid_columnconfigure(0, weight=2)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)

# Left: Services Panel
left_frame = tk.Frame(root, bg="white")
left_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
container, service_list_frame = create_scrollable_container(left_frame)

# Right: Controls Panel
right_frame = tk.Frame(root, bg="white")
right_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)



# --- Render Service Rows ---
def render_services():
    for frame in row_frames:
        frame.destroy()
    row_frames.clear()
    green_check_vars.clear()
    yellow_check_vars.clear()

    for idx, service in enumerate(services):
        bg_color = "#aaaaaa" if idx == selected_index.get() else "#e0e0e0"

        row = tk.Frame(service_list_frame, bg=bg_color, pady=4)
        row.grid(row=idx, column=0, sticky="ew", padx=0, pady=2)

        row.grid_columnconfigure(1, weight=1)

        circle = tk.Canvas(row, width=28, height=28, bg=bg_color, highlightthickness=0)
        circle.grid(row=0, column=0)
        circle.create_oval(2, 2, 26, 26, fill="gold", outline="black")
        circle.create_text(14, 14, text=str(idx + 1), font=("Arial", 10, "bold"))

        label = tk.Label(row, text=service, font=("Arial", 12), bg=bg_color, anchor="w")
        label.grid(row=0, column=1, padx=10, sticky="w")

        green_var = tk.BooleanVar()
        yellow_var = tk.BooleanVar()
        green_check_vars.append(green_var)
        yellow_check_vars.append(yellow_var)

        green_cb = tk.Checkbutton(row, variable=green_var, bg=bg_color)
        yellow_cb = tk.Checkbutton(row, variable=yellow_var, bg=bg_color)
        green_cb.grid(row=0, column=2, padx=10)
        yellow_cb.grid(row=0, column=3, padx=10)

        def select_row(event, index=idx):
            selected_index.set(index)
            render_services()

        # Make full row selectable
        # Make row, circle, and label selectable
        for widget in [row, circle, label]:
            widget.bind("<Button-1>", select_row)

        # Prevent checkbox clicks from triggering row selection
        green_cb.bind("<Button-1>", lambda e: None)
        yellow_cb.bind("<Button-1>", lambda e: None)


        row_frames.append(row)

# --- Service Controls ---
def add_service(new_item):
    if new_item != "Select Service" and new_item not in services:
        services.append(new_item)
        selected_index.set(len(services) - 1)
        render_services()

def remove_service():
    idx = selected_index.get()
    if 0 <= idx < len(services):
        services.pop(idx)
        selected_index.set(-1)
        render_services()

def reorder_service(direction):
    idx = selected_index.get()
    if direction == "up" and idx > 0:
        services[idx], services[idx - 1] = services[idx - 1], services[idx]
        selected_index.set(idx - 1)
    elif direction == "down" and idx < len(services) - 1:
        services[idx], services[idx + 1] = services[idx + 1], services[idx]
        selected_index.set(idx + 1)
    render_services()

# --- Right Panel Buttons ---
style = ttk.Style()
style.configure("Custom.TCombobox", padding=(10, 8))  # (horizontal, vertical)

dropdown = ttk.Combobox(
    right_frame,
    values=all_options,
    state="readonly",
    width=20,
    font=("Arial", 12),
    style="Custom.TCombobox"
)
dropdown.set("Select Service")
dropdown.grid(row=0, column=0, columnspan=2, sticky="ew", padx=(0, 5), pady=5, ipady=5)


tk.Button(
    right_frame, text="Add New Service", bg="green", fg="white",
    command=lambda: add_service(dropdown.get()),
    width=20, height=2, font=("Arial", 12),
    relief="solid", bd=2, highlightbackground="black", highlightcolor="black", highlightthickness=1
).grid(row=0, column=2, sticky="ew", padx=5)

arrow_frame = tk.Frame(right_frame, bg="white")
arrow_frame.grid(row=1, column=0, columnspan=3, pady=5, sticky="ew")

tk.Button(
    arrow_frame, text="↑", bg="#fddd00", font=("Arial", 12), width=10, height=2,
    command=lambda: reorder_service("up"),
    relief="solid", bd=2, highlightbackground="black", highlightcolor="black", highlightthickness=1
).pack(side="left", expand=True, fill="x", padx=(0, 5))

tk.Button(
    arrow_frame, text="↓", bg="#fddd00", font=("Arial", 12), width=10, height=2,
    command=lambda: reorder_service("down"),
    relief="solid", bd=2, highlightbackground="black", highlightcolor="black", highlightthickness=1
).pack(side="left", expand=True, fill="x")

tk.Button(
    right_frame, text="Remove Service", bg="darkred", fg="white",
    command=remove_service, width=20, height=2, font=("Arial", 12),
    relief="solid", bd=2, highlightbackground="black", highlightcolor="black", highlightthickness=1
).grid(row=2, column=0, columnspan=3, sticky="ew", pady=5)

tk.Button(
    right_frame, text="Proceed", bg="blue", fg="white",
    width=20, height=2, font=("Arial", 12),
    relief="solid", bd=2, highlightbackground="black", highlightcolor="black", highlightthickness=1
).grid(row=3, column=0, columnspan=3, sticky="ew", pady=5)

tk.Button(
    right_frame, text="Close", bg="gray", fg="white",
    width=20, height=2, font=("Arial", 12), command=root.destroy,
    relief="solid", bd=2, highlightbackground="black", highlightcolor="black", highlightthickness=1
).grid(row=4, column=0, columnspan=3, sticky="ew", pady=5)

# --- Start App ---
render_services()
root.mainloop()
