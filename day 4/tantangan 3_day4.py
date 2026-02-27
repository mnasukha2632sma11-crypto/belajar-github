import tkinter as tk

root = tk.Tk()
root.title("Data Siswa Baru")
root.geometry("400x600")

# Header
header = tk.Label(root, text="DATA SISWA BARU", bg="cyan", font=("Arial", 14, "bold"), pady=10)
header.pack(fill=tk.X)

# Container frame
form_frame = tk.Frame(root, padx=20, pady=10)
form_frame.pack(fill=tk.BOTH)

fields = ["Nama Lengkap", "Tanggal Lahir", "Asal Sekolah", "NISN", "Nama Ayah", "Nama Ibu", "Nomor Telepon / HP"]
entries = {}

for field in fields:
    tk.Label(form_frame, text=field, anchor="w").pack(fill=tk.X)
    e = tk.Entry(form_frame)
    e.pack(fill=tk.X, pady=(0, 10))
    entries[field] = e

tk.Label(form_frame, text="Alamat", anchor="w").pack(fill=tk.X)
text_alamat = tk.Text(form_frame, height=4)
text_alamat.pack(fill=tk.X, pady=(0, 10))

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(side=tk.BOTTOM, pady=20)

tk.Button(btn_frame, text="Simpan", bg="brown", fg="white", width=10).pack(side=tk.RIGHT, padx=5)
tk.Button(btn_frame, text="Hapus", bg="orange", width=10, command=lambda: [e.delete(0, tk.END) for e in entries.values()]).pack(side=tk.RIGHT, padx=5)

root.mainloop()