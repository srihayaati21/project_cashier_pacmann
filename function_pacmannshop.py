class Belanja():
    # Fanction untuk memasukkan produk, harga, jumlah ke dalam keranjang belanja
    # Berisi parameter berupa nama, harga, dan jumlah 
    def __init__(self):
        self.nama_buah = list()
        self.harga_buah = list()
        self.jumlah_buah = list()
        
    def add_item(self, nama, harga, jumlah):
        # Function untuk melakukan proses memasukkan produk ke dalam keranjang belanja
        # Berisi parameters nama, harga, dan jumlah
        self.nama_buah.append(nama)
        self.harga_buah.append(harga)
        self.jumlah_buah.append(jumlah)

    def remove_item(self, nama, harga, jumlah):
        # Function untuk menghapus salah satu produk yang ada dalam keranjang belanja
        # Berisi parameters nama, harga, dan jumlah
        self.nama_buah.remove(nama)
        self.harga_buah.remove(harga)
        self.jumlah_buah.remove(jumlah)

    def delete_item(self):
        # Function untuk menghapus keseluruhan produk yang ada dalam list keranjang belanja
        self.nama_buah.clear()
        self.harga_buah.clear()
        self.jumlah_buah.clear()

    def check_keranjang(self):
        # Function untuk melakukan proses mengecek keranjang belanja
        print('----------YOUR CART-----------')
        for i in range(len(self.nama_buah)):
            print(f'{self.nama_buah[i]}\t{self.jumlah_buah[i]} kg \t {self.harga_buah[i]}')   
    
    def checkout(self):
        # Function untuk melakukan proses pentotalan harga bayar beserta discount    
        total_harga = 0
        for i in range(len(self.nama_buah)):
            total_harga += int(self.harga_buah[i]) * int(self.jumlah_buah[i])
            if total_harga >= 150000:
                print("You Get Discount 10%")
                discount = 0.1 * total_harga
                total_harga -= discount
                print(f"Total Bayar: Rp. {total_harga}") 
                


