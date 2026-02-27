import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Init
window = tk.Tk()
window.configure(bg="white")
window.geometry("300x200")
window.resizable(False, False)
window.title("Sapa")

# Variabel
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

# Fungsi
def tombol_click():
    pesan = f"Hello {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}, Have nice day"
    showinfo(title="Hi", message=pesan)

# frame input
input_frame = ttk.Frame(window)
input_frame.pack(padx=10, pady=10, fill="x", expand=True)

# komponen
# 1. Label nama depan
nama_depan_label = ttk.Label(input_frame, text="Nama Depan:")
nama_depan_label.pack(padx=10, fill="x", expand=True)

# 2. entry nama depan
nama_depan_entry = ttk.Entry(input_frame, textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10, fill="x", expand=True)

# 3. Label nama belakang
nama_belakang_label = ttk.Label(input_frame, text="Nama Belakang:")
nama_belakang_label.pack(padx=10, fill="x", expand=True)

# 4. entry nama belakang
nama_belakang_entry = ttk.Entry(input_frame, textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10, fill="x", expand=True)

# 5. tombol
tombol = ttk.Button(input_frame, text="Sapa!", command=tombol_click)
tombol.pack(fill='x', expand=True, padx=10, pady=10)

window.mainloop()