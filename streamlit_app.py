import datetime
import os

# Database produk sederhana (Kode: [Nama Barang, Harga])
PRODUK_DB: dict[str, tuple[str, int]] = {
    "001": ("Beras Ramos 5kg", 72000),
    "002": ("Minyak Goreng 2L", 35000),
    "003": ("Gula Pasir 1kg", 17500),
    "004": ("Indomie Goreng", 3200),
    "005": ("Susu UHT Full Cream 1L", 19000),
    "006": ("Kopi Kapal Api 165g", 15500),
    "007": ("Telur Ayam 1kg", 28000),
    "008": ("Sabun Mandi Cair 450ml", 24000),
}
