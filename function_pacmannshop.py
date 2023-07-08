class Transaction_id():
    transaction_id = (input("Masukkan Nomor ID Anda: "))
    
class Belanja():    
    def __init__(self):
        self.nama_buah = list()
        self.harga_buah = list()
        self.jumlah_buah = list()
        
    def add_item(self, nama, harga, jumlah):
        self.nama_buah.append(nama)
        self.harga_buah.append(harga)
        self.jumlah_buah.append(jumlah)

    def remove_item(self, nama, harga, jumlah):
        self.nama_buah.remove(nama)
        self.harga_buah.remove(harga)
        self.jumlah_buah.remove(jumlah)

    def delete_item(self):
        self.nama_buah.clear()
        self.harga_buah.clear()
        self.jumlah_buah.clear()

    def check_keranjang(self):
        print('----------YOUR CART-----------')
        for i in range(len(self.nama_buah)):
            print(f'{self.nama_buah[i]}\t{self.jumlah_buah[i]} kg \t {self.harga_buah[i]}')   
    
    def checkout(self):
        total_harga = 0
        for i in range(len(self.nama_buah)):
            total_harga += int(self.harga_buah[i]) * int(self.jumlah_buah[i])
            if total_harga >= 150000:
                print("You Get Discount 10%")
                discount = 0.1 * total_harga
                total_harga -= discount
                print(f"Total Bayar: Rp. {total_harga}")
                


