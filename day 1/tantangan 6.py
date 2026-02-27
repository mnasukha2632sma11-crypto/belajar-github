while True:
    nilai_siswa = float(input("input nilai_siswa: "))
    
    if nilai_siswa >= 75:
        print("Tuntas")
        break
    else:
        mengulang = input("input mengulang (Ya/Tidak): ")
        if mengulang.lower() != "ya":
            print("Tidak Tuntas")
            break