import tkinter as tk
from tkinter import ttk, messagebox
import qrcode
from PIL import ImageTk, Image
import io

def generate_qr():
    """Generates a QR code from the input text and displays it."""
    data = entry_data.get()
    if not data:
        messagebox.showerror("Error", "Please enter data to generate QR code.")
        return

    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img_qr = qr.make_image(fill_color="black", back_color="white")
        img_bytes = io.BytesIO()
        img_qr.save(img_bytes, format="PNG")
        img_bytes.seek(0)
        img_tk = ImageTk.PhotoImage(Image.open(img_bytes))

        qr_label.config(image=img_tk)
        qr_label.image = img_tk  # Keep a reference!
        save_button.config(state=tk.NORMAL) #enable save button

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def save_qr():
    """Saves the generated QR code as a PNG file."""
    data = entry_data.get()
    if not data:
        messagebox.showerror("Error", "No QR code to save.")
        return

    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img_qr = qr.make_image(fill_color="black", back_color="white")
        img_qr.save("qrcode.png")
        messagebox.showinfo("Success", "QR code saved as qrcode.png")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during saving: {e}")

# Create the main window
root = tk.Tk()
root.title("QR Code Generator")

# Create and place widgets
label_data = ttk.Label(root, text="Enter Data:")
label_data.pack(pady=10)

entry_data = ttk.Entry(root, width=40)
entry_data.pack(pady=5)

generate_button = ttk.Button(root, text="Generate QR Code", command=generate_qr)
generate_button.pack(pady=10)

qr_label = ttk.Label(root)
qr_label.pack(pady=10)

save_button = ttk.Button(root, text="Save QR Code", command=save_qr, state=tk.DISABLED) #disabled until generated
save_button.pack(pady=10)


# Start the main loop
root.mainloop()