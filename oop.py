class Menu:
    def __init__(self, nama, jenis, harga):
        self.nama = nama
        self.jenis = jenis
        self.harga = harga



menu_a = Menu("Bakso", "makanan", 13000)
menu_b = Menu("Es Cendol", "minuman", 5000)

print(f"nama {menu_a.nama} jenis {menu_a.jenis} harganya {menu_a.harga}")
print(f"nama {menu_b.nama} jenis {menu_b.jenis} harganya {menu_b.harga}")

