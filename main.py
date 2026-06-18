import customtkinter as ctk
from tkinter import messagebox

from generator import generate_password
from strength_checker import check_strength
from history_manager import save_password, load_passwords


# ---------------- Appearance ----------------

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

dark_mode = True


# ---------------- Window ----------------

root = ctk.CTk()

root.title("Secure Password Generator")

root.geometry("700x780")

root.resizable(False, False)


# ---------------- Variables ----------------

upper_var = ctk.BooleanVar(value=True)
lower_var = ctk.BooleanVar(value=True)
number_var = ctk.BooleanVar(value=True)
symbol_var = ctk.BooleanVar(value=True)


# ---------------- Title ----------------

title = ctk.CTkLabel(

    root,

    text="🔐 Secure Password Generator",

    font=("Helvetica", 34, "bold")

)

title.pack(pady=25)


# ---------------- Length ----------------

length_label = ctk.CTkLabel(

    root,

    text="Password Length",

    font=("Helvetica", 18)

)

length_label.pack()


def update_length(value):

    length_value.configure(

        text=str(int(value))

    )


length_slider = ctk.CTkSlider(

    root,

    from_=6,

    to=30,

    number_of_steps=24,

    width=320,

    command=update_length

)

length_slider.set(12)

length_slider.pack(pady=10)


length_value = ctk.CTkLabel(

    root,

    text="12",

    font=("Helvetica", 16, "bold")

)

length_value.pack(pady=5)
# ---------------- Checkboxes ----------------

upper_check = ctk.CTkCheckBox(
    root,
    text="Uppercase Letters",
    variable=upper_var
)
upper_check.pack(pady=5)


lower_check = ctk.CTkCheckBox(
    root,
    text="Lowercase Letters",
    variable=lower_var
)
lower_check.pack(pady=5)


number_check = ctk.CTkCheckBox(
    root,
    text="Numbers",
    variable=number_var
)
number_check.pack(pady=5)


symbol_check = ctk.CTkCheckBox(
    root,
    text="Symbols",
    variable=symbol_var
)
symbol_check.pack(pady=5)


# ---------------- Password Entry ----------------

password_entry = ctk.CTkEntry(

    root,

    width=420,

    height=50,

    font=("Consolas", 20),

    justify="center",

    placeholder_text="Your password will appear here"

)

password_entry.pack(pady=30)


# ---------------- Strength ----------------

strength_label = ctk.CTkLabel(

    root,

    text="Strength: -",

    font=("Helvetica", 18, "bold")

)

strength_label.pack(pady=10)
# ---------------- FUNCTIONS ----------------

def create_password():

    password = generate_password(

        int(length_slider.get()),

        upper_var.get(),

        lower_var.get(),

        number_var.get(),

        symbol_var.get()

    )

    if password == "":

        messagebox.showwarning(

            "Warning",

            "Please select at least one option!"

        )

        return

    password_entry.delete(0, "end")

    password_entry.insert(0, password)

    strength, reasons = check_strength(password)

    if "Strong" in strength:

        strength_label.configure(

            text=f"🟢 Strength: {strength}",

            text_color="#22C55E"

        )

    elif "Medium" in strength:

        strength_label.configure(

            text=f"🟡 Strength: {strength}",

            text_color="#FACC15"

        )

    else:

        strength_label.configure(

            text=f"🔴 Strength: {strength}",

            text_color="#EF4444"

        )

    save_password(password)



def copy_password():

    password = password_entry.get()

    if password:

        root.clipboard_clear()

        root.clipboard_append(password)

        root.update()

        messagebox.showinfo(

            "Copied",

            "✅ Password copied successfully!"

        )



def show_history():

    history_window = ctk.CTkToplevel(root)

    history_window.geometry("450x350")

    history_window.title("Password History")

    title = ctk.CTkLabel(

        history_window,

        text="📜 Password History",

        font=("Helvetica", 22, "bold")

    )

    title.pack(pady=20)

    passwords = load_passwords()

    for password in passwords:

        label = ctk.CTkLabel(

            history_window,

            text=password,

            font=("Consolas", 14)

        )

        label.pack(pady=3)



def clear_history():

    with open("password_history.json", "w") as file:

        file.write("[]")

    messagebox.showinfo(

        "History",

        "Password history cleared!"

    )



def toggle_theme():

    global dark_mode

    dark_mode = not dark_mode

    if dark_mode:

        ctk.set_appearance_mode("dark")

        theme_btn.configure(

            text="☀ Light Mode"

        )

    else:

        ctk.set_appearance_mode("light")

        theme_btn.configure(

            text="🌙 Dark Mode"

        )
        # ---------------- BUTTONS ----------------

generate_btn = ctk.CTkButton(

    root,

    text="Generate Password",

    width=260,

    height=50,

    corner_radius=18,

    font=("Helvetica", 18, "bold"),

    fg_color="#4F46E5",

    hover_color="#4338CA",

    command=create_password

)

generate_btn.pack(pady=20)


copy_btn = ctk.CTkButton(

    root,

    text="📋 Copy Password",

    width=260,

    height=45,

    corner_radius=15,

    command=copy_password

)

copy_btn.pack(pady=8)


history_btn = ctk.CTkButton(

    root,

    text="📜 Password History",

    width=260,

    height=45,

    corner_radius=15,

    command=show_history

)

history_btn.pack(pady=8)


clear_btn = ctk.CTkButton(

    root,

    text="🗑 Clear History",

    width=260,

    height=45,

    corner_radius=15,

    fg_color="#DC2626",

    hover_color="#B91C1C",

    command=clear_history

)

clear_btn.pack(pady=8)


theme_btn = ctk.CTkButton(

    root,

    text="☀ Light Mode",

    width=260,

    height=45,

    corner_radius=15,

    command=toggle_theme

)

theme_btn.pack(pady=8)


# ---------------- Footer ----------------

footer = ctk.CTkLabel(

    root,

    text="Created by Nada Mohammad",

    font=("Helvetica", 13)

)

footer.pack(side="bottom", pady=25)


# ---------------- Run ----------------

root.mainloop()