# project_cashier_pacmann
#
# Requirements/Objectives
1. Membuat function 'input_item()' untuk melakukan proses memasukkan produk ke keranjang belanja.
2. Membuat function 'remove_item()' untuk melakukan proses menghapus salah satu produk yang ada di keranjang belanja.
3. Membuat function 'delete_item()' untuk menghapus seluruh produk yang ada di dalam keranjang belanja.
4. Membuat functin 'check_keranjang()' untuk melihat produk yang ada di keranjang belanja.
5. Membuat function 'checkout()' untuk melakukan proses pembayaran.

# Alur Program/ Flowchart
1. Langkah pertama yang akan dilakukan ialah mengisi 'transaksi_id' berupa nama customer.
2. Selanjutnya akan diberikan option proses belanja dan customer mengisi nomor yang ada pada menu.
3. Jika customer memilih nomor 1(add item) maka akan melakukan proses di dalam function 'add_item()'yang akan memuncul daftar menu/ produk yang dijual beserta harga. kemudian customer diminta untuk mengisi produk, jumlah, dan harga. setelah itu akan kembali muncul option proses belanja. Jika customer mengisi nomor 1 maka akan mengulang proses sebelumnya.
4. jika customer memilih nomor 2 (remove item) maka akan melakukan proses di dalam function 'remove_item()'. Customer diminta untuk mengisi produk, harga, dan jumlah produk yang ingin dihapus sesuai dengan yang sebelumnya sudah diisi (baik produk, harga, dan jumlah). setelah itu akan kembali muncul option proses belanja. Jika customer mengisi nomor 2 maka akan mengulang proses sebelumnya.
5. Jika customer memilih nomor 3 (delete all item) maka akan melakukan proses pada function 'delete_item()' yang akan menghapus keseluruhan produk yang ada dikeranjang belanja.
6. Jika customer memilih nomor 4 (check keranjang) akan melakukan proses pada function 'check_keranjang()' untuk menampilkan keranjang belanja customer.
7. Jika customer memilih nomor 5 (checkout) maka akan melakukan proses pada function 'checkout()' yang akan menampilkan total bayar beserta apakah customer mendapat diskon atau tidak.
8. jika customer memilih nomor 0 maka akan menghentikan proses belanja
9. Untuk mengecek setiap feature berhasil atau tidak dengan melakukan proses 'check_keranjang()'

# Penjelasan Code
1. Script 'main.py' berfungsi untuk menjalankan code yang ada di dalam 'function_pacmannshop.py'
2. Di dalam modul 'function_pacmannshop.py' 'class Belanja()' untuk memasukkan produk ke dalam keranjang belanja. terdiri dari beberapa function, yaitu:
   #
   ![image.png](https://github.com/srihayaati21/project_cashier_pacmann/blob/main/class%202.png)
   #
   a. 'add_item()' berfungsi untuk memasukkan produk ke dalam keranjang belanja
   #
   ![image.png](https://github.com/srihayaati21/project_cashier_pacmann/blob/main/F.1.C.2.png)
   #
   b. 'remove_item()' berfungsi untuk menghapus salah satu produk dalam keranjang belanja
   #
   ![image.png](https://github.com/srihayaati21/project_cashier_pacmann/blob/main/F.2.C.2.png)
   #
   c. 'delete_item()' berfungsi untuk menghapus keseluruhan produk dalam keranjang belanja
   #
   ![image.png](https://github.com/srihayaati21/project_cashier_pacmann/blob/main/F.3.C.2.png)
   #
   d. 'check_keranjang()' berfungsi untuk mengecek produk apa saja yang ada dalam keranjang belanja
   #
   ![image.png](https://github.com/srihayaati21/project_cashier_pacmann/blob/main/F.4.C.2.png)
   #
   e. 'check_out()' berfungsi untuk mentotalkan keseluruhan belanja
   #
   ![image.png](https://github.com/srihayaati21/project_cashier_pacmann/blob/main/F.5.C.2.png)

# Test Case
1. Customer ingin menambahkan item dengan menggunakan method add_item().  Item yang ditambahkan adalah sebagai berikut:
   Nama item: Pisang, qty: 2, harga: 25000.
   Nama item: Mangga, qty: 3, harga: 30000.
   Output:
   #
   ![image.png](https://github.com/srihayaati21/project_cashier_pacmann/blob/main/Screenshot%202023-07-08%20190542.png)
   #
2. Ternyata customer salah membeli salah satu item dan ingin menghapusnya dengan menggunakan method remove_item() untuk menghapus item. Item yang ingin dihapus adalah Mangga. Output:
#
   ![image.png](https://github.com/srihayaati21/project_cashier_pacmann/blob/main/Screenshot%202023-07-08%20190612.png)
#
3. Customer ingin menghapus seluruh item dengan menggunakan method delete_item(). Output:
# 
   ![image.png](https://github.com/srihayaati21/project_cashier_pacmann/blob/main/Screenshot%202023-07-08%20190637.png)
#
4. Setelah customer selesai berbelanja kemudian ingin menghitung seluruh total belanja dengan menggunakan method checkout(). Output:
#
   ![image.png](https://github.com/srihayaati21/project_cashier_pacmann/blob/main/Screenshot%202023-07-08%20190753.png)
#

