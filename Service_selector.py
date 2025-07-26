import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Service Selection")
root.geometry("1000x400")
root.configure(bg="white")

services = ["Safety Lockers", "Other Matters"]
all_options = ["Pawning", "Personal Banking", "Cash Deposit"]
selected_index = tk.IntVar(value=-1)  # No selection initially

row_frames = []
checkbox_states = []  # Stores checkbox states as list of dicts [{'green': False, 'yellow': False}]

# --- Left Panel (Service Rows) ---
left_frame = tk.Frame(root, bg="white")
left_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

# --- Right Panel (Buttons + Dropdown) ---
right_frame = tk.Frame(root, bg="white")
right_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

root.grid_columnconfigure(0, weight=2)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)


def toggle_checkbox(service_idx, color):
    """Toggle fill color on green or yellow checkbox."""
    canvas = checkbox_states[service_idx][f"{color}_canvas"]
    state = checkbox_states[service_idx][color]
    new_state = not state
    checkbox_states[service_idx][color] = new_state
    canvas.itemconfig("fill", fill=color if new_state else "")  # fill green/yellow or empty


def select_row(idx):
    """Update selected row and re-render highlighting."""
    selected_index.set(idx)
    render_services()


def render_services():
    for frame in row_frames:
        frame.destroy()
    row_frames.clear()

    for idx, service in enumerate(services):
        row = tk.Frame(left_frame, bg="#e0e0e0", pady=5)
        row.grid(row=idx, column=0, sticky="ew", padx=1, pady=1)
        row.bind("<Button-1>", lambda e, i=idx: select_row(i))

        circle = tk.Canvas(row, width=28, height=28, bg="#e0e0e0", highlightthickness=0)
        circle.grid(row=0, column=0)
        circle.create_oval(2, 2, 26, 26, fill="gold", outline="black")
        circle.create_text(14, 14, text=str(idx + 1), font=("Arial", 10, "bold"))

        label = tk.Label(row, text=service, font=("Arial", 12), bg="#e0e0e0")
        label.grid(row=0, column=1, padx=10, sticky="w")
        label.bind("<Button-1>", lambda e, i=idx: select_row(i))

        # Standard Green Checkbutton
        green_var = tk.BooleanVar()
        green_check = tk.Checkbutton(row, variable=green_var, bg="#e0e0e0",
                                     highlightbackground="green", highlightthickness=2,
                                     activebackground="#e0e0e0")
        green_check.grid(row=0, column=2, padx=10)
        
        # Standard Yellow Checkbutton
        yellow_var = tk.BooleanVar()
        yellow_check = tk.Checkbutton(row, variable=yellow_var, bg="#e0e0e0",
                                      highlightbackground="orange", highlightthickness=2,
                                      activebackground="#e0e0e0")
        yellow_check.grid(row=0, column=3, padx=10)

        row_frames.append(row)

        # Highlight selected row
        if idx == selected_index.get():
            row.configure(bg="#c0c0c0")
            label.configure(bg="#c0c0c0")
            green_check.configure(bg="#c0c0c0", activebackground="#c0c0c0")
            yellow_check.configure(bg="#c0c0c0", activebackground="#c0c0c0")
            circle.configure(bg="#c0c0c0")


# --- Dropdown + Buttons ---
dropdown = ttk.Combobox(right_frame, values=all_options, state="readonly")
dropdown.set("Select Service")
dropdown.grid(row=0, column=0, columnspan=2, sticky="ew", pady=5)

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

tk.Button(right_frame, text="Add New Service", bg="green", fg="white",
          command=lambda: add_service(dropdown.get())).grid(row=0, column=2, sticky="ew", padx=5)

tk.Button(right_frame, text="↑", bg="#fddd00", command=lambda: reorder_service("up")).grid(row=1, column=0, pady=5, sticky="ew")
tk.Button(right_frame, text="↓", bg="#fddd00", command=lambda: reorder_service("down")).grid(row=1, column=1, pady=5, sticky="ew")

tk.Button(right_frame, text="Remove Service", bg="darkred", fg="white", command=remove_service)\
    .grid(row=2, column=0, columnspan=3, sticky="ew", pady=5)

tk.Button(right_frame, text="Proceed", bg="blue", fg="white").grid(row=3, column=0, columnspan=3, sticky="ew", pady=5)
tk.Button(right_frame, text="Close", bg="gray", fg="white", command=root.destroy)\
    .grid(row=4, column=0, columnspan=3, sticky="ew", pady=5)

render_services()
root.mainloop()
