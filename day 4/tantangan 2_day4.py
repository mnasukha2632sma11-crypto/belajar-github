import tkinter as tk
from tkinter import ttk

def hitung_parkir():
    plat = entry_plat.get()
    masuk = entry_masuk.get()
    keluar = entry_keluar.get()
    biaya = "2.000"
    
    # Menambah ke tabel
    tree.insert("", "end", values=(plat, masuk, keluar, biaya))
    entry_biaya.delete(0, tk.END)
    entry_biaya.insert(0, biaya)

root = tk.Tk()
root.title("Aplikasi Parkir Kelompok 6")

# Input Section
frame_input = tk.Frame(root)
frame_input.pack(pady=10, padx=10)

tk.Label(frame_input, text="No Plat Polisi").grid(row=0, column=0, sticky="w")
entry_plat = tk.Entry(frame_input)
entry_plat.grid(row=0, column=1)

tk.Label(frame_input, text="Waktu Masuk").grid(row=1, column=0, sticky="w")
entry_masuk = tk.Entry(frame_input)
entry_masuk.grid(row=1, column=1)

tk.Label(frame_input, text="Waktu Keluar").grid(row=2, column=0, sticky="w")
entry_keluar = tk.Entry(frame_input)
entry_keluar.grid(row=2, column=1)

tk.Label(frame_input, text="Biaya").grid(row=3, column=0, sticky="w")
entry_biaya = tk.Entry(frame_input)
entry_biaya.grid(row=3, column=1)

tk.Button(frame_input, text="Hitung", command=hitung_parkir).grid(row=3, column=2, padx=5)

tk.Label(root, text="Biaya Per Jam\nRp. 2.000", fg="red", font=("Arial", 16, "bold")).pack()

# Table Section
columns = ("No Plat Polisi", "Masuk", "Keluar", "Biaya")
tree = ttk.Treeview(root, columns=columns, show='headings', height=5)
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)
tree.pack(pady=10, padx=10)

root.mainloop()