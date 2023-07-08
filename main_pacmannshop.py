from tabulate import tabulate
from function_pacmannshop import Belanja

#Daftar Menu PacmannShop
produk = [
    ['Buah', 'Harga(dalam kg)'],
    ['pisang', 25000],
    ['Mangga', 30000],
    ['Jeruk', 45000],
    ['Nanas', 25000],
    ['Lemon', 36000]
]

#Membuat Id Transaksi
transaksi_id = input('Masukan ID Anda: ')
message = (f'Welcome to PacmannShop {transaksi_id}')

print('*' * len(message))
print(message)
print('*' * len(message))


#Option belanja di PacmannShop
main_menu = ("""
Selamat datang di PacmannShop
=============================
1: add item
2: remove item
3: delete all item
4: check keranjang
5: checkout
0: exit program
""")
print(main_menu)

#Proses Belanja
belanja = Belanja()
while True:
    option = int(input("Pilih Menu: "))
    if option == 1: 
        print(tabulate(produk, headers= "firstrow"))
        buah = input("Masukkan Buah: ").lower()
        harga = input("Masukkan Harga(dalam kg): ")
        jumlah = input("Masukkan Jumlah(dalam kg): ")
        belanja.add_item(buah, harga, jumlah)
        print(main_menu)
    elif option == 2:
        buah = input("Masukkan Buah: ").lower()
        harga = input("Masukkan Harga(dalam kg): ")
        jumlah = input("Masukkan Jumlah(dalam kg): ")
        belanja.remove_item(buah, harga, jumlah)
        print(main_menu)
    elif option == 3:
        belanja.delete_item()
        print("Keranjang belanja anda kosong")
        print(main_menu)
    elif option == 4:
        belanja.check_keranjang()
        print(main_menu)
    elif option == 5:
        belanja.check_keranjang()
        belanja.checkout()
    else:
        print("Terima kasih sampai bertemu kembali!")
        break